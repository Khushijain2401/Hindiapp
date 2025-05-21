import streamlit as st
import openai
import os

# Page config
st.set_page_config(page_title="Hindi Learning Chatbot", layout="centered")
st.title("🗣️ Hindi Learning Chatbot")
st.markdown("Ask me anything, and I'll help you learn Hindi!")

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEY not found in environment variables.")
    st.stop()

openai.api_key = api_key

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful and friendly tutor that teaches Hindi to beginners. Explain Hindi concepts clearly with examples and English translations. Be encouraging and use simple language."}
    ]

# User input
user_input = st.text_input("Type your question or message:")

# Generate response
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        st.error(f"Error: {e}")

# Show conversation
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Tutor:** {msg['content']}")
