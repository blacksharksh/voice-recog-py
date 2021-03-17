#imported speech recognition
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)

    voice_data = r.recognize_google(audio, language="en-IN", show_all=True)
    print(voice_data)
