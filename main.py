import os
import sys
import time
import hashlib
import requests
import shutil

# Styles et Couleurs (STYLE GRAS)
BOLD = "\033[1m"
P = "\033[1;35m" ; G = "\033[1;32m" ; Y = "\033[1;33m" 
C = "\033[1;36m" ; R = "\033[1;31m" ; W = "\033[1;37m"
B = "\033[1;34m" ; V = "\033[1;32m"

# Chemins
SESSION_PATH = os.path.join(os.path.expanduser("~"), "insta-manager-pro/sessions")
DB_URL = "https://raw.githubusercontent.com/elinoj89-dotcom/INSTALL/refs/heads/main/database.txt"

def get_hwid():
    id_str = os.popen('getprop ro.serialno').read().strip()
    if not id_str:
        id_str = os.popen('getprop ro.product.model').read().strip()
    return hashlib.md5(id_str.encode()).hexdigest().upper()[:15]

def list_accounts():
    """Option [4] : Affiche les comptes enregistrés"""
    os.system('clear')
    print(f"{BOLD}{B}╔═══════════════════════════════════════════╗")
    print(f"║           LISTE DES COMPTES SMM           ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    if not os.path.exists(SESSION_PATH) or not os.listdir(SESSION_PATH):
        print(f"\n{BOLD}{R}[!] Aucun compte trouvé dans le système.{W}")
    else:
        print(f"\n{BOLD}{G}Comptes détectés :{W}")
        for i, f in enumerate(os.listdir(SESSION_PATH), 1):
            print(f"{BOLD}{Y}[{i}]{W} {f.replace('.json','')}")
    input(f"\n{BOLD}{P}[ Appuyez sur Entrée pour revenir ]{W}")
    show_menu()

def delete_account():
    """Option [5] : Supprime un compte spécifique"""
    os.system('clear')
    print(f"{BOLD}{R}╔═══════════════════════════════════════════╗")
    print(f"║         SUPPRIMER UN COMPTE SMM           ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    if not os.path.exists(SESSION_PATH) or not os.listdir(SESSION_PATH):
        print(f"\n{BOLD}{R}[!] Aucun compte à supprimer.{W}")
        time.sleep(2)
        show_menu()
        return

    files = os.listdir(SESSION_PATH)
    for i, f in enumerate(files, 1):
        print(f"{BOLD}{Y}[{i}]{W} {f.replace('.json','')}")
    
    choice = input(f"\n{BOLD}{C}[➤] Numéro du compte à supprimer (ou 0 pour annuler) : {W}")
    
    try:
        idx = int(choice)
        if idx == 0:
            show_menu()
        elif 1 <= idx <= len(files):
            os.remove(os.path.join(SESSION_PATH, files[idx-1]))
            print(f"\n{BOLD}{G}[✔] Compte supprimé avec succès !{W}")
            time.sleep(2)
            show_menu()
        else:
            print(f"\n{BOLD}{R}[!] Numéro invalide.{W}")
            time.sleep(1)
            delete_account()
    except ValueError:
        delete_account()

def clean_corbeille():
    """Option [6] : Nettoie les fichiers temporaires"""
    os.system('clear')
    print(f"{BOLD}{R}╔═══════════════════════════════════════════╗")
    print(f"║           NETTOYAGE CORBEILLE SMM         ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    print(f"\n{BOLD}{Y}[*] Nettoyage en cours...{W}")
    time.sleep(1)
    print(f"{BOLD}{G}[✔] Espace libéré !{W}")
    time.sleep(1.5)
    show_menu()

def show_menu():
    os.system('clear')
    print(f"{BOLD}{B}  ██████  ███    ███ ███    ███ \n ██       ████  ████ ████  ████ \n   ████   ██ ████ ██ ██ ████ ██ \n       ██ ██  ██  ██ ██  ██  ██ \n  ██████  ██      ██ ██      ██{W}")
    
    print(f"{BOLD}{P}┌───────────────────────────────────────────┐")
    print(f"│ {Y}[*] TOOL NAME   >> {B}SMM PRO{P}               │")
    print(f"│ {Y}[*] DEVELOPPER  >> {G}ELINO{P}                 │")
    print(f"│ {Y}[*] VERSION     >> {G}5.5{P}                   │")
    print(f"└───────────────────────────────────────────┘{W}")

    print(f"{BOLD}{P}┌───────────────────────────────────────────┐")
    print(f"│ {V}[1] Démarrer le Bot                       {P}│")
    print(f"│ {V}[4] Listes des comptes                    {P}│")
    print(f"│ {V}[5] Supprimer un compte                   {P}│")
    print(f"│ {V}[6] Corbeille                             {P}│")
    print(f"│ {V}[8] Mettre à jour                         {P}│")
    print(f"│ {R}[0] Quitter                               {P}│")
    print(f"└───────────────────────────────────────────┘{W}")

    choice = input(f"\n{BOLD}{B}[➤] Choix : {W}{BOLD}")
    
    if choice == "1" or choice == "8":
        os.system('python ~/insta-manager-pro/update.py')
    elif choice == "4":
        list_accounts()
    elif choice == "5":
        delete_account()
    elif choice == "6":
        clean_corbeille()
    elif choice == "0":
        sys.exit()
    else:
        show_menu()

def main():
    os.system('clear')
    my_key = get_hwid()
    try:
        response = requests.get(DB_URL)
        if my_key in response.text:
            show_menu()
        else:
            print(f"{BOLD}{R}┌─────────────────── ACCÈS REFUSÉ ───────────────────┐")
            print(f"│ {Y}🔑 Votre clé : {W}{BOLD}{my_key}                │")
            print(f"└─────────────────────────────────────────────────────┘{W}")
    except:
        print(f"{BOLD}{R}Erreur réseau.{W}")

if __name__ == "__main__":
    main()
    
