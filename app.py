import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="Ocean Softwares chatbot", page_icon="d:\Downloads\logo.png")
st.title("OS Chatbot")

# 2. Initialize Groq Client
# Securely replace with your fresh API key
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# 3. Initialize Chat History (Memory)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful Python programming tutor."}
    ]

# 4. Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 5. React to user input
if prompt := st.chat_input("Ask me anything you want to know..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 6. Get response from Groq
    try:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""
            
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages,
            )
            
            full_response = completion.choices[0].message.content
            response_placeholder.markdown(full_response)
            
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error(f"Error: {e}")

