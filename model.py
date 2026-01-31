# model.py
def simple_ai(text):
    """
    This is a very basic AI response function.
    You can replace this with your AI model code later.
    """
    text = text.lower()
    if "hello" in text:
        return "Hi there! How can I help you?"
    elif "how are you" in text:
        return "I'm doing great! You?"
    else:
        return "Sorry, I don't understand that yet."
