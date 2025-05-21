import streamlit as st
import openai

# Page config
st.set_page_config(page_title="Hindi Learning Chatbot", layout="centered")

# Title
st.title("🗣️ Hindi Learning Chatbot")
st.markdown("Ask me anything, and I'll help you learn Hindi!")

# API key input
api_key = st.text_input("Enter your OpenAI API Key:", type="password")
if api_key:
    openai.api_key = api_key

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful and friendly tutor that teaches Hindi to beginners. Explain Hindi concepts clearly with examples and English translations. Be encouraging and use simple language."}
    ]

# User input
user_input = st.text_input("Type your question or message:")

# Submit and get response
if user_input and api_key:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" if you don't have GPT-4 access
            messages=st.session_state.messages
        )
        reply = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        st.error(f"Error: {e}")

# Display chat history
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Tutor:** {msg['content']}")
