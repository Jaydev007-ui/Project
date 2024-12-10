# knowledge_base.py
import json

# Load knowledge base (you can replace this with a database or external API)
def load_knowledge():
    with open('data/knowledge.json', 'r') as f:
        return json.load(f)

knowledge = load_knowledge()

def get_answer(intent):
    return knowledge.get(intent, "I'm sorry, I don't understand.")
