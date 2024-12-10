import openai
import streamlit as st
import git
import os

# Initialize the OpenAI API key
openai.api_key = "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"

# GitHub repository details
username = "Jaydev007-ui"
token = "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"
repo_name = "Project"

# Function to push code to GitHub
def push_to_github():
    try:
        repo_dir = os.getcwd()  # Assuming you're pushing from the current directory
        repo = git.Repo(repo_dir)
        repo.git.add('--all')
        repo.index.commit("Updated chatbot code with new changes")
        origin = repo.remote(name='origin')
        origin.set_url(f"https://{username}:{token}@github.com/{username}/{repo_name}.git")
        origin.push()
        st.success("Code pushed to GitHub successfully!")
    except Exception as e:
        st.error(f"Failed to push to GitHub: {e}")

# Define Streamlit interface
st.title("OpenAI GPT Chatbot with GitHub Integration")
st.write("Ask anything, and the chatbot will respond.")

# Get user input
user_input = st.text_input("You:", placeholder="Type your message here...")

# When the user provides input
if user_input:
    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # You can use "gpt-4" instead of "gpt-4o-mini"
        messages=[{"role": "user", "content": user_input}]
    )

    # Display the response from the AI
    ai_response = response['choices'][0]['message']['content']
    st.write(f"Bot: {ai_response}")

    # Provide a button to push changes to GitHub
    if st.button("Push to GitHub"):
        push_to_github()

