import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",150)
text = ("Hi, this is Friday.")
engine.say(text)
engine.runAndWait()