import random
from nltk.chat.util import Chat, reflections

# Define extended patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you.', 'I\'m good, thanks for asking.', 'All good!']),
    (r'what is your name?', ['I am a chatbot.', 'You can call me a chatbot.', 'I go by the name of chatbot.']),
    (r'quit|bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']),
    (r'(.*) (age|old) are you', ["I'm just a computer program, I don't have an age."]),
    (r'(.*) (love|like) you', ['Aww, that\'s sweet!', 'Thank you!', 'I appreciate that.']),
    (r'what can you do\?', ['I can chat with you, tell jokes, or provide information.']),
    (r'joke|tell me a joke', ['Why don\'t scientists trust atoms? Because they make up everything!', 
                              'Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!', 
                              'What do you call an alligator in a vest? An investigator!']),
    (r'(.*) (weather|forecast) in (.*)', ['I am not equipped to provide real-time weather updates.']),
    (r'how can I contact you\?', ['I am just a chatbot, so I don\'t have personal contact information.']),
    (r'what is your purpose\?', ['I\'m here to assist and chat with you!']),
    (r'(.*) (favorite|favourite) (color|colour)', ['I don\'t have eyes, so I don\'t have a favorite color.']),
    (r'(.*) (hobby|interest) do you have\?', ['I like helping people and learning new things.']),
    (r'(.*) (movie|film) do you like\?', ['I don\'t watch movies, but I\'ve heard "The Matrix" is quite popular among computers.']),
    (r'(.*) (music|song) do you like\?', ['I don\'t listen to music, but I can appreciate different genres.']),
    (r'(.*) (book|novel) do you like\?', ['I don\'t read books, but I store and process a lot of text!']),
    (r'', ["I'm not sure I understand.", "Can you please elaborate?", "Tell me more."]),
]

# Create a Chatbot using the patterns
chatbot = Chat(patterns, reflections)

# Function to start the chat
def start_chat():
    print("Welcome! Let's chat. Type 'quit' to exit.")
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot:", chatbot.respond(user_input))

# Start the chat
start_chat()
