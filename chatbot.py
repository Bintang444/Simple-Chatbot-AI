import streamlit as st
import google.generativeai as genai
import os 
from dotenv import load_dotenv

# Load API key dari .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API key tidak ditemukan! Isi GEMINI_API_KEY di .env")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Simple Chatbot AI")

# Reset chat
if st.button("Reset Chat"):
    st.session_state.messages = []
    st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input user
user_input = st.chat_input("Ketik pesan kamu...")

if user_input:
    # Simpan pesan user
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # System prompt
    system_prompt = "Kamu adalah asisten yang selalu jawab dengan bahasa gaul anak Jakarta, singkat, dan pakai emoji."
    
    # Buat history untuk model
    history = [
        {"role": "user", "parts": [system_prompt]},
        {"role": "model", "parts": ["Sip bro, siap!"]}
    ]

    # Loop pesan
    for msg in st.session_state.messages:
        history.append({
            "role": msg["role"],
            "parts": [msg["content"]]
        })

    # Kirim ke model
    chat = model.start_chat(history=history[:-1])
    response = chat.send_message(user_input)
    reply = response.text

    # Simpan dan tampilkan balasan
    st.session_state.messages.append({"role": "model", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)