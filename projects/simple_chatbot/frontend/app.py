import requests
import streamlit as st

st.title("ChatGPT-like clone")

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

# Field for users to choose model from OpenAI
model_options = ["gpt-4", "gpt-4o-mini"]
st.session_state["openai_model"] = st.selectbox(
    "Choose OpenAI Model:",
    model_options,
    index=model_options.index(st.session_state["openai_model"]),
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = requests.post(
            "http://localhost:8000/chat",
            json={
                "model": st.session_state["openai_model"],
                "messages": [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
            },
            stream=True,
        )
        full_response = ""
        for chunk in response.iter_lines():
            word_list = chunk.decode().split()  # Split the response into words
            for word in word_list:
                full_response += word + " "
                message_placeholder.markdown(full_response + "▌")
        st.session_state.messages.append({"role": "assistant", "content": full_response})
