import streamlit as st
import requests

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
        with st.spinner("Soch raha hoon..."):
            try:
                api_key = st.secrets["GEMINI_API_KEY"]
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={api_key}"

                system_instruction = (
                    "Tum ek friendly AI ho jo Hinglish (Hindi + English mix) mein "
                    "baat karta hai, jaise ek dost karta hai. Casual, helpful aur "
                    "seedha jawab do."
                )

                payload = {
                    "system_instruction": {"parts": [{"text": system_instruction}]},
                    "contents": [
                        {"role": "user", "parts": [{"text": user_input}]}
                    ]
                }

                res = requests.post(url, json=payload, timeout=30)

                if res.status_code == 200:
                    data = res.json()
                    bot_reply = data["candidates"][0]["content"]["parts"][0]["text"]
                else:
                    bot_reply = f"Error {res.status_code}: {res.text[:200]}"
            except Exception as e:
                bot_reply = f"Error: {e}"

            st.markdown(bot_reply)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
