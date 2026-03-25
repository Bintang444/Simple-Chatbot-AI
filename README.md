# Simple AI Chatbot (Gemini 2.5)

Chatbot ini adalah prototipe aplikasi percakapan berbasis Streamlit dan Google Gemini (cloud AI model). Cocok untuk eksperimen conversational AI, termasuk prompt style bahasa gaul.

## Fitur

- UI web interaktif via Streamlit
- History chat tersimpan di `st.session_state`
- Reset chat sekali klik
- Memanggil model Google Gemini 2.5 (gemini-2.5-flash)
- System prompt memaksa jawaban: bahasa gaul anak Jakarta, singkat, pake emoji

## Persyaratan

- Python 3.10+
- `streamlit`
- `google-generativeai`

## Setup

1. Clone repo:
   ```bash
   git clone https://github.com/<username>/<repo>.git
   cd project-ai
   ```
2. Aktifkan virtual env dan install dependencies:
   ```bash
   source venv/bin/activate
   pip install streamlit google-generativeai
   ```
3. Atur API key:
   - Ubah `YOUR_API_KEY` di `chatbot.py` ke API key kamu, atau gunakan `os.environ` agar lebih aman.
   - Contoh (Linux/macOS):
     ```bash
     export GEMINI_API_KEY="your_key_here"
     ```
4. Jalankan:
   ```bash
   streamlit run chatbot.py
   ```

## Cara kerja cepat

- `chatbot.py` menampilkan UI Streamlit dengan `st.chat_input`.
- Setiap pesan user ditambahkan ke history, lalu kirim ke Gemini dengan `model.start_chat`.
- Balasan model ditampilkan di layar dan disimpan di session.