import speech_recognition as sr


class speechRecognition():
    def __init__(self):
        self.r = sr.Recognizer()
    def corpus(self):
        with sr.Microphone() as source:
            print("give me orders")
            audio = self.r.listen(source)
        try:
            text = self.r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "UnknownValueError"
        except sr.RequestError as e:
            return "RequestError"