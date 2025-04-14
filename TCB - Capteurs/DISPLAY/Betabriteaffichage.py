import socket
import time

def send_to_betabrite_ip(ip_address, port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            s.sendall(message.encode('ascii'))
            print("Message envoyé : ", message)
    except Exception as e:
        print("Erreur lors de l'envoi :", e)

# Exemple de message Betabrite
def create_message():
    # Message brut, selon le protocole Alpha (à adapter si besoin)
    return "\x02Z00\x1bAHello World!\x04"

if __name__ == '__main__':
    ip = "192.168.1.100"   #  À remplacer par l’IP de ton panneau Betabrite
    port = 3001            #  À adapter selon ton modèle (parfois 23, parfois 3001)
    
    message = create_message()
    send_to_betabrite_ip(ip, port, message)

