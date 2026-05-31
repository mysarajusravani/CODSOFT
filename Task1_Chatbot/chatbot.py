def digital_chat():

    print("=== Digital chat ===")
    print("Enter 'hault' if you want to leave the chat.\n")

    while True:

        chat_query = input("You: ").strip().lower()

        if chat_query in ["hi", "hello", "hey"]:
            print("Helper: Greetings! How may I assist you today?")

        elif "your name" in chat_query:
            print("Helper: I am Digital Helper, a rule-based chatbot.")

        elif "programming" in chat_query:
            print("Helper: Programming is the process of writing instructions for computers.")

        elif "developer" in chat_query:
            print("Helper: Developers design, build, and maintain software applications.")

        elif "computer science" in chat_query:
            print("Helper: Computer Science deals with algorithms, software, and computing systems.")

        elif "database" in chat_query:
            print("Helper: A database is used to store and manage information efficiently.")

        elif "career" in chat_query:
            print("Helper: Building projects and learning new skills can improve your career opportunities.")

        elif "internship" in chat_query:
            print("Helper: Internships provide practical experience and industry exposure.")

        elif "motivate" in chat_query:
            print("Helper: Consistency and dedication are the keys to success.")

        elif "thank you" in chat_query or "thanks" in chat_query:
            print("Helper: Happy to help!")

        elif "good night" in chat_query:
            print("Helper: Good night! Take care and rest well.")

        elif chat_query == "hault":
            print("Helper: Chat session closed. See you again!")
            break

        else:
            print("Helper: I couldn't recognize that query. Please try a different question.")

digital_chat()
