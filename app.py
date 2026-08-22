import streamlit as st
import requests

st.title("My Personal AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                res = requests.post(
                    "https://text.pollinations.ai/",
                    json={"messages": [{"role": "user", "content": user_input}], "model": "openai"}
                )
                bot_reply = res.text
            except Exception as e:
                bot_reply = f"Error: {e}"
            st.markdown(bot_reply)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            
