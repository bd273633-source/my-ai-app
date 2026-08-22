import streamlit as st
import requests
import urllib.parse

st.title("My Personal AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Kuch bhi pucho...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                encoded_prompt = urllib.parse.quote(user_input)
                url = f"https://text.pollinations.ai/{encoded_prompt}"
                
                res = requests.get(url)
                if res.status_code == 200:
                    bot_reply = res.text
                else:
                    bot_reply = "Aapka message mil gaya! Phir se try karein."
            except Exception as e:
                bot_reply = f"Error: {e}"
            
            st.markdown(bot_reply)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                
