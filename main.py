import os
import sys
import time
import hashlib
import requests
import shutil

# Couleurs
P = "\033[35m" ; G = "\033[32m" ; Y = "\033[33m" 
C = "\033[36m" ; R = "\033[31m" ; W = "\033[0m"
BLINK = "\033[5m"

DB_URL = "https://raw.githubusercontent.com/elinoj89-dotcom/INSTALL/refs/heads/main/database.txt"
SESSION_PATH = os.path.join(os.path.expanduser("~"), "insta-manager-pro/sessions")

def get_hwid():
    """Génère l'identifiant unique du téléphone"""
    id_str = os.popen('getprop ro.serialno').read().strip()
    if not id_str:
        id_str = os.popen('getprop ro.product.model').read().strip()
    return hashlib.md5(id_str.encode()).hexdigest().upper()[:15]

def show_others():
    """Affiche les tarifs et les infos de contact (Option 9)"""
    os.system('clear')
    print(f"{P}╔═══════════════════════════════════════════╗")
    print(f"║            INFOS & TARIFS {Y}SMM{P}             ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    print(f"\n{Y}[💳] NOS TARIFS D'ACTIVATION :{W}")
    print(f" ├─ Hebdomadaire : {G}5,000 Ar{W}")
    print(f" ├─ Mensuel      : {G}15,000 Ar{W}")
    print(f" └─ À vie (VIP)  : {G}50,000 Ar{W}")
    
    print(f"\n{C}[👤] CONTACT DÉVELOPPEUR :{W}")
    print(f" ├─ Facebook : {C}Randriamihary Jean Elino{W}")
    print(f" └─ WhatsApp : {G}+261 XX XX XXX XX{W}") # Remplace par ton vrai numéro
    
    print(f"\n{R}[⚠️] RÈGLES :{W}")
    print(f" └─ Pas de remboursement après activation.")
    
    input(f"\n{P}[ Appuyez sur Entrée pour revenir ]{W}")
    show_menu()

def list_accounts():
    """Affiche les comptes enregistrés (Option 4)"""
    os.system('clear')
    print(f"{P}╔═══════════════════════════════════════════╗\n║           LISTE DES COMPTES SMM           ║\n╚═══════════════════════════════════════════╝{W}\n")
    if not os.path.exists(SESSION_PATH) or not os.listdir(SESSION_PATH):
        print(f"{R}[!] Aucun compte trouvé.{W}")
    else:
        for i, f in enumerate(os.listdir(SESSION_PATH), 1):
            print(f"{Y}[{i}]{W} {f.replace('.json','')}")
    input(f"\n{G}[ Entrée pour revenir ]{W}")
    show_menu()

def delete_account():
    """Supprime un compte (Option 5)"""
    os.system('clear')
    print(f"{R}╔═══════════════════════════════════════════╗\n║         SUPPRIMER UN COMPTE SMM           ║\n╚═══════════════════════════════════════════╝{W}\n")
    if os.path.exists(SESSION_PATH) and os.listdir(SESSION_PATH):
        files = os.listdir(SESSION_PATH)
        for i, f in enumerate(files, 1):
            print(f"{Y}[{i}]{W} {f}")
        c = input(f"\n{C}[➤] Numéro à supprimer : {W}")
        try:
            os.remove(os.path.join(SESSION_PATH, files[int(c)-1]))
            print(f"{G}[✔] Compte supprimé avec succès !{W}")
        except: print(f"{R}[✘] Erreur.{W}")
    else: print(f"{R}[!] Liste vide.{W}")
    time.sleep(2)
    show_menu()

def show_menu():
    """Menu principal après activation"""
    os.system('clear')
    print(f"{P}╔═══════════════════════════════════════════╗")
    print(f"║   {Y}[*] TOOL NAME   >> {BLINK}SMM{W}{P}               ║")
    print(f"║   {Y}[*] DEVELOPPER  >> ELINO{P}             ║")
    print(f"║   {Y}[*] VERSION     >> 5.5{P}               ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    print(f"\n{G}[1] Démarrer le Bot")
    print(f"{G}[4] Listes des comptes")
    print(f"{G}[5] Supprimer un compte")
    print(f"{G}[9] Autres (Tarifs & Contact)")
    print(f"{R}[0] Quitter{W}")
    
    choice = input(f"\n{C}[➤] Choix : {W}")
    
    if choice == "1": 
        os.system('python ~/insta-manager-pro/update.py')
    elif choice == "4": 
        list_accounts()
    elif choice == "5": 
        delete_account()
    elif choice == "9":
        show_others()
    elif choice == "0": 
        sys.exit()
    else: 
        show_menu()

def main():
    """Point d'entrée : Vérification de la licence"""
    os.system('clear')
    my_key = get_hwid()
    try:
        response = requests.get(DB_URL)
        if my_key in response.text:
            show_menu()
        else:
            print(f"{R}┌─────────────────── ACCÈS REFUSÉ ───────────────────┐")
            print(f"│ {R}🚫 APPAREIL NON ENREGISTRÉ                        │")
            print(f"│                                                   │")
            print(f"│ {Y}🔑 Votre clé : {W}{my_key}                │")
            print(f"│ {C}💬 Contactez Randriamihary Jean Elino            │")
            print(f"└─────────────────────────────────────────────────────┘{W}")
    except: 
        print(f"{R}Erreur réseau. Vérifiez votre connexion.{W}")

if __name__ == "__main__":
    main()
    
