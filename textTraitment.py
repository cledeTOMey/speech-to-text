import paho.mqtt.client as mqtt


class textTraitment():
    def __init__(self):
        #orderTreatment init
        self.sentence = "" #phrase deduite
        self.order="" # ordre deduit


    def testEtage(self, floor, text):
        # fonction qui regarde quel etage est demande (3 valeurs differentes par etage en fonction de la reconnaissance vocale et de la tournure de phrase)
        # la fonction renvoie faux si aucun numero d'etage a ete soumis.
        if floor == 1:
            if ("1" in text) or ("one" in text) or ("first" in text):
                return True
        if floor == 2:
            if ("2" in text) or ("two" in text) or ("second" in text):
                return True
        if floor == 3:
            if ("3" in text) or ("three" in text) or ("third" in text):
                return True
        return False

    def floors(self, text, prefix):
        # drapeau pour verifier la derniere condition
        flag = False
        if self.testEtage(1, text):
            self.sentence = self.sentence + " a l'etage 1"
            self.order = prefix + " 1"
            flag = True
        if self.testEtage(2, text):
            self.sentence = text + " a l'etage 2"
            self.order = prefix + " 2"
            flag = True
        if self.testEtage(3, text):
            self.sentence = text + " a l'etage 3"
            self.order = prefix + " 3"
            flag = True
        if "all" in text:
            self.sentence = text + " a tous les etage"
            self.order = prefix + " tout"
            flag = True
            # si aucn etage a ete cite et qu'il y a un stop on doit arreter
        if not flag and "stop" in text:
            self.sentence = "arreter " + self.sentence
            self.order = "arreter " + prefix

    def textTreatment(self, text):
        # initialisationd es attributs
        self.order = ""
        self.sentence = ""
        # debut du traitement de texte. il fonctionne par mot cle. ainsi si on donne des ordres direct ou si on fait des phrases le programme comprendre
        # ex : "help" et "I need some help" seront compris de la meme maniere
        if "help" in text:
            self.sentence = "demande d'aide detecte"
            self.order = "aide"
        if "home" in text:
            self.sentence = "retour accueil"
            self.order = "accueil"
        if "turn on light" in text or "turn on lights" in text:
            self.sentence = "allumage de la lumiere"
            self.floors(text, "allumer")
        if "turn off light" in text or "turn off lights" in text:
            self.sentence="arreter eclairage"
            self.order= "arreter eclairage"
        if "spray" in text:
            self.sentence = "arroser"
            self.floors(text, "arroser")
        if "display" in text:
            if "stat" in text:
                self.order = "afficher statistiques"
            else:
                self.floors(text, "afficher")
        if "history" in text:
            if "temperature" in text:
                self.sentence = "historique temperature"
                self.order = "historique temperature"
            if "humidity" in text:
                self.sentence = "historique humidite"
                self.order = "historique humidite"
            if "light" in text:
                self.sentence = "historique luminosite"
                self.floors(text, "historique luminosite")
            if "water" in text:
                self.sentence = "historique eau"
                self.floors(text, "historique eau")
            if "acidity" in text:
                self.sentence = "historique acidite"
                self.floors(text, "historique acidite")
        # affichage des valeurs deduites et on retourne l'ordre deduit.
        print("sentence :")
        print(self.sentence)
        print("order :")
        print(self.order)
        # retourne l'ordre deduit
        return self.order
