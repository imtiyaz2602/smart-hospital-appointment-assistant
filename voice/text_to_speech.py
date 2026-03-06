import pyttsx3

# initialize the speech engine
engine = pyttsx3.init()

# optional settings
engine.setProperty("rate", 160)   # speech speed
engine.setProperty("volume", 1.0) # volume (0.0 to 1.0)

# select voice (optional)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # 0 = male, 1 = female (depends on system)

def speak(text):
    """
    Convert text to speech and play it.
    """

    print("Speaking:", text)

    engine.say(text)
    engine.runAndWait() 