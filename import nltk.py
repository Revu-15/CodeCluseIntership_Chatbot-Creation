import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']],
    ['how are you?', ['I am doing well, thank you.', 'I am good, thanks for asking.']],
    ['what is your name?', ['My name is Chatbot.', 'You can call me Chatbot.']],
    ['bye|goodbye', ['Goodbye!', 'See you later!', 'Take care!']],
    ['tell me a joke', ['Why don\'t scientists trust atoms? Because they make up everything!', 'What do you call a fish wearing a crown? A kingfish!', 'Why did the scarecrow win an award? Because he was outstanding in his field!']],
    ['how old are you?', ['I am just a program, so I don\'t have an age.']],
    ['what can you do?', ['I can chat with you, tell jokes, answer questions, and more!']],
    ['do you like cats?', ['I am a program, so I don\'t have feelings like humans do.']],
    ['who created you?', ['I was created by a team of developers.', 'My creators are amazing programmers.']],
]

pairs.extend([
    ['what is your favorite color?', ['I don\'t have a favorite color since I am just a program.', 'I don\'t perceive colors like humans do.']],
    ['can you help me with Python programming?', ['Yes, I can help you with Python programming questions.', 'Of course! What do you need help with?']],
    ['tell me about yourself', ['I am a chatbot designed to interact with users and provide assistance.', 'I am an AI program created to chat and answer questions.']],
    ['what is the meaning of life?', ['The meaning of life is a philosophical question that humans have pondered for centuries.']],
    ['do you dream?', ['As an AI, I don\'t experience dreams or consciousness like humans do.']],
    ['can you sing a song?', ['I can\'t sing, but I can share song lyrics if you\'d like.']],
    ['what is the weather like today?', ['I don\'t have access to real-time data, so I can\'t provide current weather information.']],
    ['tell me a fun fact', ['Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!']],
])

chatbot = Chat(pairs, reflections)

def chat_with_bot():
    print("Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot:", response)
        if user_input.lower() in ['bye', 'goodbye']:
            break

chat_with_bot()