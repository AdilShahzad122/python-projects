import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()  # Initialize the TTS engine
    print("Welcome to Robospeaker created by Adil")
    while True:
        x = input("Enter what you want me to pronounce: ")
        if x == "exit":
            engine.say("Goodbye!")
            engine.runAndWait()
            break
        engine.say(x)        # Use engine.say() instead of x.say()
        engine.runAndWait()  # Use engine.runAndWait() instead of x.runAndWait()