import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")

st.title("ChatGPT-like clone")

st.session_state["openai_model"] = st.selectbox(
    "Select OpenAI Model:", options=["gpt-4o-mini", "gpt-4o"], index=0
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = requests.post(
            f"{BACKEND_URL}/api/v1/chat",
            json={
                "message": prompt,
                "history": st.session_state.messages,
                "model": st.session_state["openai_model"],
            },
            stream=True,
        )

        # Display the response as it comes in
        placeholder = st.empty()
        full_response = ""
        for chunk in response.iter_content(chunk_size=8):
            full_response += chunk.decode("utf-8")
            placeholder.markdown(full_response + "▌")

    st.session_state.messages.append({"role": "assistant", "content": full_response})
