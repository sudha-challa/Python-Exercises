from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you|how are you doing?",
        ["I'm doing great, thank you! How can I assist you today?", "I'm fine, thanks for asking! What about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's all right.", "No problem. Is there anything else I can help with?"]
    ],
    [
        r"I'm (.*) (good|well|okay|ok)",
        ["Nice to hear that. How can I assist you today?", "Glad to hear you're %1! How can I help you today?"]
    ],
    [
        r"quit",
        ["Bye!", "Have a great day!", "Goodbye!"]
    ],
]

def chat():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    chat()
