
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Inisialisasi Model LLM
# Model Gemini-2.5-flash adalah pilihan yang baik untuk kecepatan.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt = ChatPromptTemplate.from_template("Anda adalah asisten kafe. Jawab: {pertanyaan}")

chain = prompt | model

# Antarmuka Streamlit
st.title("🤖 Chatbot Kafe Siap Deploy")
st.caption("Aplikasi di-host di Streamlit Cloud")

# Inisialisasi riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan riwayat chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input dari user dan mendapatkan respons
if user_input := st.chat_input("Tanyakan sesuatu..."):
    # Tampilkan input user
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Dapatkan respons dari model AI
    with st.chat_message("assistant"):
        with st.spinner("Berpikir..."):
            response = chain.invoke({"pertanyaan": user_input})
            st.markdown(response.content)

    # Simpan respons AI
    st.session_state.messages.append({"role": "assistant", "content": response.content})
