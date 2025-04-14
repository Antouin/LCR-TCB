#include <ESP8266WiFi.h>
#include <ESP8266MQTTClient.h>

const char* ssid = "VOTRE_SSID";
const char* password = "VOTRE_MOT_DE_PASSE";
const char* mqtt_server = "mqtt://test.mosquitto.org:1883";

MQTTClient mqtt;
const int capteurPin = 4;  // GPIO 4 (D2 sur certaines cartes)

void setup() {
  Serial.begin(115200);
  
  // Connexion WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n✅ WiFi connecté !");
  
  // Configuration MQTT
  mqtt.begin(mqtt_server);
  Serial.println("📡 Connexion au broker MQTT...");

  // Configuration GPIO
  pinMode(capteurPin, INPUT);
}

void loop() {
  mqtt.handle();  // Gestion du client MQTT

  // Lire l'état du capteur
  int valeurCapteur = digitalRead(capteurPin);
  
  // Envoyer la valeur sur MQTT
  String message = String(valeurCapteur);
  mqtt.publish("capteur/etat", message);
  
  Serial.printf("📤 Donnée envoyée : %d\n", valeurCapteur);
  
  delay(3000);  // Attente 3s avant le prochain envoi
}
