import streamlit as st
import google.generativeai as genai

# Hardcoded Gemini API key
API_KEY = "AQ.Ab8RN6KQONl95-rueM0lMZ3bcr-Dw7Lmi8LwrmwjGf8P7fYVUQ"

# Configure GenAI with the API key and model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def get_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit App
st.title("Gemini AI Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask a question or give a prompt")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get and display assistant response
    response_text = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    with st.chat_message("assistant"):
        st.markdown(response_text)
