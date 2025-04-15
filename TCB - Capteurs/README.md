
Composants de chaque partie
BROKER
Raspberry Pi (hébergeant le broker MQTT – Mosquitto)
Réseau local ou point d’accès WiFi (NETGEAR ou autre)
Configuration sécurisée des topics et clients MQTT

DISPLAY
Raspberry Pi 3B
Afficheur LED Betabrite connecté via port Ethernet
Script Python pour l'abonnement MQTT et affichage des messages reçus

LET DETECTION
ESP32
Capteur vibratoire piézoélectrique avec résistance sur nappe
Batterie Li-ion 3.7V 2000mAh (EEMB)
Programme Arduino pour mesurer les variations de résistance et publier un message MQTT en cas de let

