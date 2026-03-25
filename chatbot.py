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
if st.button("Reset Chat"):
    st.session_state.messages = []
    st.rerun()

# Simpan history chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan history chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input dari user
user_input = st.chat_input("Ketik pesan kamu...")

if user_input:
    # 1. Simpan & tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 2. Susun semua history buat dikirim ke Gemini
    system_prompt = "Kamu adalah asisten yang selalu jawab dengan bahasa gaul anak Jakarta, singkat, dan pakai emoji."
    history = []
    for msg in st.session_state.messages:
        history.append({
            "role": "user",
            "parts": [system_prompt]
                })
        history.append({
            "role": "model", 
            "parts": ["Sip bro, siap!"]
                })

    # 3. Kirim history lengkap ke Gemini
    chat = model.start_chat(history=history[:-1])
    response = chat.send_message(user_input)
    reply = response.text

    # 4. Simpan & tampilkan balasan AI
    st.session_state.messages.append({"role": "model", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)