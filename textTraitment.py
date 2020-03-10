import paho.mqtt.client as mqtt


class textTraitment():
    def __init__(self, mqttClient):
        #orderTreatment init
        self.sentence = ""
        self.order=""

        # mqtt init
        self.mqtt = mqttClient

    def testEtage(self, floor, text):
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
        if not flag and "stop" in text:
            self.sentence = "arreter " + self.sentence
            self.order = "arreter " + prefix

    def textTreatment(self, text):
        print("you just said : " + text)
        if "floor" in text:
            print("oh my god you said floor")
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
        print("sentence :")
        print(self.sentence)
        print("order :")
        print(self.order)
        if (self.order != ""):
            self.mqtt.publish(self.order)
        self.order = ""
        self.sentence = ""



            # aide
            # accueil
            # allumer tout
            # allumer 1
            # allumer 2
            # allumer 3
            # afficher 1
            # afficher 2
            # afficher 3
            # arroser tout
            # arroser 1
            # arroser 2
            # arroser 3
            # arreter arrosage
            # arreter eclairage
            # historique humidite
            # historique temperature
            # historique acidite 1
            # historique acidite 2
            # historique acidite 3
            # historique luminosite 1
            # historique luminosite 2
            # historique luminosite 3
            # historique eau 1
            # historique eau 2
            # historique eau 3
