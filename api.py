import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import git
import os
import spacy

# Correct way to load a model
nlp = spacy.load("en_core_web_sm")

# Load GitHub credentials from environment variables for security
username = os.getenv("GITHUB_USERNAME", "Jaydev007-ui")
token = os.getenv("GITHUB_TOKEN", "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")  # Set this in your environment
repo_name = "Project"
repo_url = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"

# Path to the local repository folder
repo_local_path = "./local_repo"

# Clone the repository if it does not exist locally
if not os.path.exists(repo_local_path):
    st.write("Cloning repository...")
    try:
        git.Repo.clone_from(repo_url, repo_local_path)
        st.success("Repository cloned successfully!")
    except git.exc.GitCommandError as e:
        st.error("Failed to clone repository. Please check your credentials and try again.")
        st.write(f"Error details: {e}")

# Initialize the repo object
repo = git.Repo(repo_local_path)

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Train the chatbot on the English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Streamlit app interface
st.title("ChatBot with GitHub Logging")

# File to store the conversation log
log_file_path = os.path.join(repo_local_path, "conversation_log.txt")

# Input from the user
user_input = st.text_input("You: ")

if st.button("Submit"):
    if user_input:
        # Get bot response
        bot_response = chatbot.get_response(user_input)
        st.write(f"Bot: {bot_response}")

        # Save conversation to log
        with open(log_file_path, "a") as log_file:
            log_file.write(f"You: {user_input}\n")
            log_file.write(f"Bot: {bot_response}\n\n")

        # Add and commit changes to Git
        try:
            repo.git.add(log_file_path)
            repo.index.commit(f"Updated conversation log with user input: {user_input}")

            # Push the changes to GitHub
            origin = repo.remote(name='origin')
            origin.push()
            st.success("Conversation logged and pushed to GitHub!")
        except git.exc.GitCommandError as e:
            st.error("Failed to push changes to GitHub.")
            st.write(f"Error details: {e}")
