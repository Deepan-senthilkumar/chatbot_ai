import streamlit as st
import os
from groq import Groq

# 1. Initialize the client (Replace with your actual Groq API key)
# Make sure to set your Groq API key in your environment variables
client = Groq(api_key=st.secrets["GROQ_API_KEY"])


# 2. This list acts as the "Memory" of the conversation
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
]

print("--- Groq AI Chatbot ---")
print("Type 'exit' or 'quit' to stop the conversation.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    try:
        # UPDATED: Using Llama 3.3 70B Versatile for 2025
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
        )

        response = completion.choices[0].message.content
        print(f"\nAI: {response}\n")
        messages.append({"role": "assistant", "content": response})

    except Exception as e:
        print(f"Error: {e}")
        break
