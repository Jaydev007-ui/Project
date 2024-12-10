# app.py
import os
import streamlit as st
from nlp_model import get_intent
from knowledge_base import get_answer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch GitHub username and token from environment variables
username = os.getenv("GITHUB_USERNAME", "Jaydev007-ui")
token = os.getenv("GITHUB_TOKEN", "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")  # Set this in your environment

# Specify the repository name
repo_name = "Project"

# Construct the repository URL using the fetched credentials
repo_url = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"

# Streamlit app layout
st.title("Professional Chatbot")

# Input text box for the user query
user_input = st.text_input("You: ", "")

# Process the user input
if user_input:
    # Get the intent of the user input using NLP model
    intent = get_intent(user_input)
    
    # Fetch an appropriate answer based on the intent
    response = get_answer(intent)
    
    # Display the bot's response
    st.write(f"Bot: {response}")
    
    # Example: Use GitHub authentication URL for some task (e.g., cloning the repository)
    # Uncomment the line below if you want to use this functionality
    # os.system(f"git clone {repo_url}")
