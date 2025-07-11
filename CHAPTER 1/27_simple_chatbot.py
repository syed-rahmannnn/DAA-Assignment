while True:
    msg = input("You: ")
    if "hi" in msg.lower():
        print("Bot: Hello!")
    elif "bye" in msg.lower():
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I didn't understand.")