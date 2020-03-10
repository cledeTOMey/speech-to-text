from orderToGarden import order
from speechRecognition import speechRecognition
from textTraitment import textTraitment


if __name__ == "__main__":
    # initialisation des objets
    stt = speechRecognition() #objet gerant la reconaissance vocale
    tt = textTraitment() # objet qui analyse le texte
    mqtt = order() # objet d'envoi des ordres au programme principal

    # initialisation des variables du programme
    phrase = "" # recupere la string renvoyee la reconaissance vocale
    order = "" # recupere l'ordre deduit du traitement du texte
    while(1):
        # recuperations des valeurs des variables
        phrase = stt.reconnaissance()
        order = tt.textTreatment(phrase)
        # si un ordre a ete deduit il est envoye au programme principal et on reinitialise la valeur
        if (order != ""):
            mqtt.publish(order)
        order = ""
    #quand le programme termine on ferme de canal de discution
    mqtt.close()
