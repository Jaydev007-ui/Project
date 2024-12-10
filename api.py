import openai
import streamlit as st

# Initialize the OpenAI API key
openai.api_key = "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"

# Define Streamlit interface
st.title("OpenAI GPT Chatbot")
st.write("Ask anything, and the chatbot will respond.")

# Get user input
user_input = st.text_input("You:", placeholder="Type your message here...")

# When the user provides input
if user_input:
    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can use "gpt-4" instead of "gpt-4o-mini"
        messages=[{"role": "user", "content": user_input}]
    )

    # Display the response from the AI
    ai_response = response['choices'][0]['message']['content']
    st.write(f"Bot: {ai_response}")
