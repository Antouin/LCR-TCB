import RPi.GPIO as GPIO
import time

# Numérotation BCM
GPIO.setmode(GPIO.BCM)

# Définition des broches pour les boutons
BOUTON_LOCAL = 17
BOUTON_VISITEUR = 27

# Configuration des entrées avec résistance pull-up
GPIO.setup(BOUTON_LOCAL, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BOUTON_VISITEUR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Scores initiaux
score_local = 0
score_visiteur = 0

def afficher_scores():
    print(f"Score - Local : {score_local} | Visiteur : {score_visiteur}")

# Callback pour le bouton local
def bouton_local_callback(channel):
    global score_local
    score_local += 5
    afficher_scores()

# Callback pour le bouton visiteur
def bouton_visiteur_callback(channel):
    global score_visiteur
    score_visiteur += 5
    afficher_scores()

# Détection d'événement sur les boutons (front descendant)
GPIO.add_event_detect(BOUTON_LOCAL, GPIO.FALLING, callback=bouton_local_callback, bouncetime=300)
GPIO.add_event_detect(BOUTON_VISITEUR, GPIO.FALLING, callback=bouton_visiteur_callback, bouncetime=300)

# Message de démarrage
print("Appuyez sur un bouton pour ajouter 5 points au score.")
afficher_scores()

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nArrêt du programme.")
finally:
    GPIO.cleanup()

