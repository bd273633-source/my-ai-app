import streamlit as st
import requests
import warnings
from duckduckgo_search import DDGS

warnings.filterwarnings('ignore')

API_KEY = "AQ.Ab8RN6L5BQyXbCbWwQKEpYJ2ykaTMUZ5yuKfRx2wICKs3XnPPw"

def search_net(query):
    results_text = ""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
            for r in results:
                results_text += f"\nTitle: {r['title']}\nSnippet: {r['body']}\n"
        return results_text
    except Exception as e:
        return f"Error during web search: {e}"

def ask_blackbox(prompt, search_needed=True):
    if search_needed:
        search_results = search_net(prompt)
        full_prompt = f"Live Search Results:\n{search_results}\n\nUser Question: {prompt}"
    else:
        full_prompt = prompt

    api_url = "https://www.blackbox.ai/api/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "messages": [{"role": "user", "content": full_prompt}],
        "id": API_KEY
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.text
        else:
            return f"API Failed ({response.status_code}): {response.text}"
    except Exception as e:
        return f"Request Error: {e}"

st.set_page_config(page_title="My Personal AI", page_icon="🤖")
st.title("My Personal AI")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for msg in st.session_state['messages']:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

user_input = st.chat_input("Your message:")

if user_input:
    st.session_state['messages'].append({'role': 'user', 'content': user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ask_blackbox(user_input, search_needed=True)
            st.markdown(response)
            
    st.session_state['messages'].append({'role': 'assistant', 'content': response})
