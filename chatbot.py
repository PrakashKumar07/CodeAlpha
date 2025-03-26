import nltk
import random
import string
from nltk.chat.util import Chat, reflections

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
# Define the chatbot's conversation patterns
patterns = [
    (r"hi|hello|hey", ["Hello there!", "Hi!", "Hey, how's it going?"]),
    (r"what is your name?", ["I am a chatbot, created to chat with you!"]),
    (r"how are you?", ["I'm doing great, thank you! How about you?"]),
    (r"what can you do?", ["I can have conversations with you! Ask me anything."]),
    (r"greeting?", ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How may I help you?"]),
    (r"goodbye?", ["Goodbye! Have a great day!", "See you later!", "Take care!"]),
    (r"thanks?", ["You're welcome!", "No problem!", "Glad to help!"]),
    (r"what?", ["how!"]),
    (r"default?", ["I'm sorry, I didn't understand that.", "Could you please rephrase?", "I'm not sure how to respond to that."]),
    (r"(.*) your (.*)", ["Sorry, I didn't get that. Can you clarify?"]),
    (r"(.*)", ["Sorry, I don't quite understand what you mean. Can you rephrase?"]),
]

# Create a Chat instance with the patterns
chatbot = Chat(patterns, reflections)
def start_chat():
    print("Hi! I'm your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Exit the chat if the user says 'bye'
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get a response from the chatbot based on the user input
        response = chatbot.respond(user_input)
        
        print(f"Chatbot: {response}")
if __name__ == "__main__":
    start_chat()
