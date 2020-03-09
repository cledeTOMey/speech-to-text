from orderToGarden import order
from speechRecognition import speechRecognition
from textTraitment import textTraitment


if __name__ == "__main__":
    stt = speechRecognition()
    mqtt = order()
    tt = textTraitment(mqtt)
    phrase = ""
    while(phrase != "stop"):
            phrase = stt.corpus()
            tt.textTreatment(phrase)
    mqtt.close()
