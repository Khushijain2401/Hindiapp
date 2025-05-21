import streamlit as st
import os
import openai

from openai import OpenAI

# Page config
st.set_page_config(page_title="Hindi Learning Chatbot", layout="centered")
st.title("🗣️ Hindi Learning Chatbot")
st.markdown("Ask me anything, and I'll help you learn Hindi!")

# Load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEY not found in environment variables.")
    st.stop()

client = OpenAI(api_key=api_key)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a friendly Hindi tutor. Teach the user Hindi with examples and English translations. Use simple and encouraging language.",
        }
    ]

# User input
user_input = st.text_input("Type your question or message:")

# Handle user input and get response
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" if gpt-4 not available
            messages=st.session_state.messages,
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        st.error(f"Error: {e}")

# Display conversation
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Tutor:** {msg['content']}")

