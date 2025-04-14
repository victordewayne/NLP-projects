def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can i help you today?"
    elif "your name" in user_input:
        return "I'm a simple chatbot built using Python."
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."
    else:
        return "I'm not sure how to respond to that. Can you rephrase?"
    

print("Chatbot: Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break 
    response = chatbot_response(user_input)
    print("Chatbot: ", response)