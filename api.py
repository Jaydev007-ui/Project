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

