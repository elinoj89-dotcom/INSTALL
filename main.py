import os
import sys
import time
import hashlib
import requests

# Définition des couleurs
G = "\033[32m"      # Vert
R = "\033[31m"      # Rouge
W = "\033[0m"       # Blanc (Reset)
Y = "\033[33m"      # Jaune
P = "\033[35m"      # Violet
C = "\033[36m"      # Cyan
BLINK = "\033[5m"   # Clignotement

# Ton lien d'activation validé
DB_URL = "https://raw.githubusercontent.com/elinoj89-dotcom/INSTALL/refs/heads/main/database.txt"

def get_hwid():
    """Génère l'identifiant unique du téléphone"""
    id_str = os.popen('getprop ro.serialno').read().strip()
    if not id_str:
        id_str = os.popen('getprop ro.product.model').read().strip()
    return hashlib.md5(id_str.encode()).hexdigest().upper()[:15]

def install_logic():
    """Installation des composants techniques"""
    print(f"\n{P}[⚙️] PRÉPARATION DU SYSTÈME...{W}")
    
    # Nettoyage et installations
    os.system('pip uninstall instaweb -y --quiet')
    print(f"{Y}[*] Installation des dépendances (Rich, Brotli, Zstd)...{W}")
    os.system('pip install rich brotli zstandard --quiet')
    
    print(f"{Y}[*] Configuration de Libsodium et Pynacl...{W}")
    os.system('pkg install libsodium -y')
    os.system('export SODIUM_INSTALL=system && pip install pynacl --quiet')
    os.system('pip install git+https://github.com/Trade999/curl_requests.git --quiet')
    
    # Clonage du projet principal
    path = os.path.join(os.path.expanduser("~"), "insta-manager-pro")
    if os.path.exists(path):
        os.system(f'cd {path} && git pull')
    else:
        os.system(f'cd $HOME && git clone https://github.com/Lariot08/insta-manager-pro')
    
    print(f"\n{G}[✔] ENVIRONNEMENT PRÊT !{W}")
    time.sleep(1)
    os.system(f'cd {path} && python update.py')

def main():
    os.system('clear')
    
    # --- TITRE STYLISÉ AVEC SMM CLIGNOTANT ---
    print(f"{P}╔═══════════════════════════════════════════╗")
    print(f"║       INTERFACE D'INSTALLATION {BLINK}{Y}SMM{W}{P}       ║") 
    print(f"║            ÉDITION SÉCURISÉE              ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    my_key = get_hwid()
    print(f"\n{C}[*] Connexion au serveur d'activation...{W}")
    
    try:
        response = requests.get(DB_URL)
        authorized_keys = response.text.splitlines()
        
        if my_key in authorized_keys:
            print(f"\n{G}╔═══════════════════════════════════════════╗")
            print(f"║       ACCÈS AUTORISÉ : {my_key}        ║")
            print(f"╚═══════════════════════════════════════════╝{W}")
            time.sleep(1)
            install_logic()
            
        else:
            print(f"\n{R}┌─────────────────── ACCÈS REFUSÉ ───────────────────┐")
            print(f"│ {R}🚫 APPAREIL NON ENREGISTRÉ                        │")
            print(f"│                                                   │")
            print(f"│ {Y}🔑 Votre clé : {W}{my_key}                │")
            print(f"│ {C}💬 Envoyez cette clé à :                          │")
            print(f"│    Randriamihary Jean Elino pour activation.      │")
            print(f"└─────────────────────────────────────────────────────┘{W}")
            sys.exit()
            
    except Exception as e:
        print(f"{R}[!] Erreur de connexion au serveur d'activation.{W}")
        sys.exit()

if __name__ == "__main__":
    main()
    
