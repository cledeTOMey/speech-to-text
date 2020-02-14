
from speechRecognition import speechRecognition
from textTraitment import textTraitment


if __name__ == "__main__":
    stt = speechRecognition()
    tt = textTraitment()
    phrase = ""
    while(phrase != "stop"):
            phrase = stt.corpus()
            tt.textTreatment(phrase)