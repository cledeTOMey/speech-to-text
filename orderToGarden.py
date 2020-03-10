import paho.mqtt.client as mqtt

class order():
    def __init__(self):
        # initialisationd es attributs du mosquitto
        self.client = mqtt.Client()
        # les deux programmes fonctionnent sur le meme ordinateur mais on peut les faire fonctionner sur deux ordianteurs differents, il faut juste changer le "localhost"
        self.client.connect("localhost",1883,60)
        # definition du topic
        self.topic = "speech"

    def publish(self, orderToGive):
        # ordre de publication sur le topic
        self.client.publish(self.topic,orderToGive)

    def close(self):
        # deconnection du client mosquitto
        self.client.disconnect();
