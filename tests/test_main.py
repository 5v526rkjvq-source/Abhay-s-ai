
# tests/test_main.py
from model import simple_ai

def test_simple_ai_hello():
    assert simple_ai("Hello") == "Hi there! How can I help you?"

def test_simple_ai_unknown():
    assert simple_ai("What's up?") == "Sorry, I don't understand that yet."
