import speech_recognition as sr


class speechRecognition():
    def __init__(self):
        # initialisationd es attibuts
        self.r = sr.Recognizer() # objet de reconaissance vocale fournit dans la librairie SpeechRecognition de Python

    def reconnaissance(self):
        # programme basique de reconaissance vocale en python
        with sr.Microphone() as source:
            print("give me orders")
            audio = self.r.listen(source)
        try:
            text = self.r.recognize_google(audio) # appel a l'API Google de reconaissance vocale
            return text
        except sr.UnknownValueError:
            # retourne une erreur si google n'a pas reussis a comprendre
            return "UnknownValueError"
        except sr.RequestError as e:
            # retourne une erreur si google a eu une erreur
            return "RequestError"
