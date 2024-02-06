
import re

def simple_chatbot(user_input, user_profile):
    user_input = user_input.lower()
    user_profile = user_profile.lower()

    # Define rules based on the user's profile
    rules = {}
    if user_profile == 'profile1':
        rules = {
            r'hello|hi|hey': 'Greetings! How can I assist you?',
            r'explain about|define about': 'Please ask in a clear manner, and I will do my best to provide information.',
            # Add more rules specific to profile1
        }
    elif user_profile == 'profile2':
        rules = {
            r'hello|hi|hey': 'Hello there! What can I do for you?',
            r'explain about|define about': 'Certainly, I will explain it in a clear manner.',
            # Add more rules specific to profile2
        }
    
    # Common rules for both profiles
    common_rules = {
        r'how are you|how are you doing': 'I am a chatbot and lack emotions, but thanks for inquiring!',
        r'your name|who are you': 'I am a rule-based chatbot. You can refer to me as ChatBot.',
        r'bye|goodbye|see you': 'Farewell! Feel free to return if you have more questions.',
        r'\b(?:thanks?|thank you)\b': 'You\'re appreciated!',
        r'\b(?:yes|yeah|sure)\b': 'Excellent!',
        r'\b(?:no|nope)\b': 'Alright, let me know if you change your mind.',
        r'\b(?:help|what can you do)\b': 'I can provide information and answer questions. Feel free to ask!',
        r'\b(?:can you provid pdf|can you convert into word document)\b': 'Unfortunately, I cannot provide PDFs or convert to Word. Try using another platform.',
        r'\b(?:give with output|generate code output)\b': 'I encourage you to generate code output yourself for a better learning experience.',
    }

    # Merge the common and user-specific rules
    rules.update(common_rules)

    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
    
    return "Apologies, I didn't quite catch that. Could you please ask something else?"

print("Greetings! Type 'bye' to exit.")
user_profile = input("Enter your profile (profile1 or profile2): ")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Goodbye! Have a wonderful day ahead.")
        break
    response = alternate_chatbot(user_input, user_profile)
    print("Simple Chatbot:", response)
