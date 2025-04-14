import paho.mqtt.client as mqtt

# Paramètres du broker MQTT
BROKER = "test.mosquitto.org"
TOPIC = "capteur/etat"

# Callback quand on reçoit un message
def on_message(client, userdata, msg):
    print(f"📩 Message reçu - Topic: {msg.topic} | Donnée: {msg.payload.decode()}")

# Configuration du client MQTT
client = mqtt.Client()
client.on_message = on_message

# Connexion au broker
print("📡 Connexion au broker MQTT...")
client.connect(BROKER, 1883, 60)

# S'abonner au topic
client.subscribe(TOPIC)

# Boucle pour écouter en continu
print(f"🟢 En attente de messages sur le topic: {TOPIC}")
client.loop_forever()
