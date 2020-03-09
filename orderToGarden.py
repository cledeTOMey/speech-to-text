import paho.mqtt.client as mqtt

class order():
    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect("localhost",1883,60)
        self.topic = "speech"

    def publish(self, orderToGive):
        self.client.publish(self.topic,orderToGive)

    def close(self):
        self.client.disconnect();
