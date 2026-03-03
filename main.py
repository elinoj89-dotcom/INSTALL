import os
import sys
import time
import hashlib
import requests

# Couleurs pour le style
G = "\033[32m" # Vert
R = "\033[31m" # Rouge
W = "\033[0m"  # Blanc
Y = "\033[33m" # Jaune
P = "\033[35m" # Violet
C = "\033[36m" # Cyan

# Ton lien d'activation validé
DB_URL = "https://raw.githubusercontent.com/elinoj89-dotcom/INSTALL/refs/heads/main/database.txt"

def get_hwid():
    """Génère l'identifiant unique du téléphone"""
    id_str = os.popen('getprop ro.serialno').read().strip()
    if not id_str:
        id_str = os.popen('getprop ro.product.model').read().strip()
    return hashlib.md5(id_str.encode()).hexdigest().upper()[:15]

def main():
    os.system('clear')
    my_key = get_hwid()
    
    print(f"{P}[*] Connexion au serveur d'activation...{W}")
    
    try:
        # Lecture de ton fichier GitHub
        response = requests.get(DB_URL)
        authorized_keys = response.text.splitlines()
        
        if my_key in authorized_keys:
            # Message spécial pour toi (Remplace 'TA_CLE' par ta vraie clé après le premier test)
            if my_key == "TA_CLE_PERSO":
                print(f"{G}╔═══════════════════════════════════════════╗")
                print(f"║       BIENVENUE CRÉATEUR : ELINO        ║")
                print(f"╚═══════════════════════════════════════════╝{W}")
            else:
                print(f"{G}[✔] Accès autorisé !{W}")
            
            time.sleep(2)
            # Ici, le script continue vers l'installation d'Instagram
            print(f"{Y}[*] Lancement de la configuration...{W}")
            
        else:
            # Écran d'erreur si la clé n'est pas dans database.txt
            print(f"{R}┌─────────────────── ACCÈS REFUSÉ ───────────────────┐")
            print(f"│ {R}🚫 APPAREIL NON ENREGISTRÉ                        │")
            print(f"│                                                   │")
            print(f"│ {Y}🔑 Votre clé : {W}{my_key}                │")
            print(f"│ {C}💬 Envoyez cette clé à Randriamihary Jean Elino pour activation.     │")
            print(f"└─────────────────────────────────────────────────────┘{W}")
            sys.exit()
            
    except Exception as e:
        print(f"{R}[!] Erreur de connexion au serveur d'activation.{W}")
        sys.exit()

if __name__ == "__main__":
    main()
                
