# nlp_model.py
from transformers import pipeline

# Initialize transformer-based model for zero-shot classification
nlp_model = pipeline("zero-shot-classification")

# Function to classify user intent
def get_intent(user_input):
    candidate_labels = ['greeting', 'information', 'farewell', 'default']
    result = nlp_model(user_input, candidate_labels)
    return result['labels'][0]  # Return the top intent
