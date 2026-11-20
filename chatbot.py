
def chatbot():

    print("--------------------------------")
    print("   WELCOME TO PYTHON CHATBOT")
    print("--------------------------------")
    print("Chatbot: Hi! I am your Python chatbot.")
    print("Chatbot: You can talk to me.")
    print("Chatbot: Type 'bye' whenever you want to exit.")
    print("--------------------------------")

    while True:

        user = input("You: ").lower()

        if user in ["hello", "hi", "hey"]:
            print("Chatbot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Chatbot: I am fine, thanks for asking!")
            print("Chatbot: How are you doing today?")

        elif user == "i am fine":
            print("Chatbot: That's great to hear!")
            print("Chatbot: I hope you have a wonderful day.")

        elif user == "what is your name":
            print("Chatbot: My name is Python Bot.")
            print("Chatbot: You can call me your little assistant.")

        elif user == "how old are you":
            print("Chatbot: I don't have a real age.")
            print("Chatbot: I am a computer program.")

        elif user == "what can you do":
            print("Chatbot: I can talk with you and answer simple messages.")
            print("Chatbot: I can also help you with basic greetings.")

        elif user == "are you happy":
            print("Chatbot: I don't have real feelings.")
            print("Chatbot: But I am always ready to chat with you!")

        elif user == "i am sad":
            print("Chatbot: I am sorry you are feeling sad.")
            print("Chatbot: I hope things get better for you.")
            print("Chatbot: Take care of yourself!")

        elif user == "i am bored":
            print("Chatbot: Oh no! Let's make your day interesting.")
            print("Chatbot: You can listen to music or learn something new.")

        elif user == "tell me a joke":
            print("Chatbot: Why did the computer go to the doctor?")
            print("Chatbot: Because it had a virus!")

        elif user == "what is python":
            print("Chatbot: Python is a programming language.")
            print("Chatbot: It is easy to learn and used in AI, ML and web development.")

        elif user == "i want to study":
            print("Chatbot: That's a great decision!")
            print("Chatbot: Study a little every day and never give up.")

        elif user == "thank you":
            print("Chatbot: You're welcome!")
            print("Chatbot: Happy to help you.")

        elif user == "good morning":
            print("Chatbot: Good morning!")
            print("Chatbot: Have a wonderful and productive day.")

        elif user == "good night":
            print("Chatbot: Good night!")
            print("Chatbot: Sleep well and sweet dreams.")

        elif user == "who created you":
            print("Chatbot: I was created using Python programming.")
            print("Chatbot: A programmer gave me rules to respond.")

        elif user == "help":
            print("Chatbot: You can try talking to me using these messages:")
            print("hello, how are you, what is your name,")
            print("tell me a joke, what is python, help, bye")

        elif user == "bye":
            print("Chatbot: It was nice talking to you!")
            print("Chatbot: Have a great day. Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")
            print("Chatbot: Try typing 'help' to see what I can answer.")

chatbot()
