# main.py
from model import simple_ai

def main():
    print("Welcome to Abhay's AI!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = simple_ai(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
