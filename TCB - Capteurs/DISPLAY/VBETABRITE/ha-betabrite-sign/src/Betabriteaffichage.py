import paho.mqtt.client as mqtt

MQTT_BROKER = "192.168.4.1"
MQTT_PORT = 1883
MQTT_TOPIC = "capteur/donnees"

def on_message(client, userdata, message):
    print(f"Message reçu sur {message.topic}: {message.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

print(f"Connexion au broker MQTT {MQTT_BROKER}:{MQTT_PORT}...")
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)

print(f"Abonné au topic {MQTT_TOPIC}, en attente de messages...")
client.loop_forever()

