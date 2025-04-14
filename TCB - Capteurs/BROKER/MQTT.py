import paho.mqtt.client as mqtt

# Configuration MQTT
# BROKER = "ESPBROKER"  # Remplacez par l'adresse IP de votre broker MQTT
BROKER = "192.168.95.42"  # Remplacez par l'adresse IP de votre broker MQTT
PORT = 1883
TOPIC = "ESP/LET"
USERNAME = "broker"
PASSWORD = "tcbBROKER"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connexion au broker MQTT réussie")
        client.subscribe(TOPIC)
    else:
        print(f"Échec de connexion, code de retour : {rc}")

def on_message(client, userdata, msg):
    print(f"Message reçu sur {msg.topic}: {msg.payload.decode()}")

# Configuration du client MQTT
client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

# Connexion au broker
client.connect(BROKER, PORT, 60)

# Boucle de maintien de la connexion
client.loop_forever()

