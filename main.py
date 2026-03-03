import os
import sys
import time
import hashlib
import requests

# Styles et Couleurs (Style GRAS)
BOLD = "\033[1m"
P = "\033[1;35m" ; G = "\033[1;32m" ; Y = "\033[1;33m" 
C = "\033[1;36m" ; R = "\033[1;31m" ; W = "\033[1;37m"
B = "\033[1;34m" # Bleu SMM
V = "\033[1;32m" # Vert clair

DB_URL = "https://raw.githubusercontent.com/elinoj89-dotcom/INSTALL/refs/heads/main/database.txt"

def get_hwid():
    id_str = os.popen('getprop ro.serialno').read().strip()
    if not id_str:
        id_str = os.popen('getprop ro.product.model').read().strip()
    return hashlib.md5(id_str.encode()).hexdigest().upper()[:15]

def show_menu():
    os.system('clear')
    # Logo SMM Bleu et Gras
    print(f"{BOLD}{B}  ██████  ███    ███ ███    ███ ")
    print(" ██       ████  ████ ████  ████ ")
    print("   ████   ██ ████ ██ ██ ████ ██ ")
    print("       ██ ██  ██  ██ ██  ██  ██ ")
    print(f"  ██████  ██      ██ ██      ██{W}")
    
    print(f"{BOLD}{P}┌───────────────────────────────────────────┐")
    print(f"│ {Y}[*] TOOL NAME   >> {B}SMM PRO{P}               │")
    print(f"│ {Y}[*] DEVELOPPER  >> {G}ELINO{P}                 │")
    print(f"│ {Y}[*] INTERFACE   >> {C}Web Scraping{P}          │")
    print(f"│ {Y}[*] VERSION     >> {G}5.5{P}                   │")
    print(f"└───────────────────────────────────────────┘{W}")
    
    print(f"{BOLD}{P}╔═══════════════════════════════════════════╗")
    print(f"║       {G}Un Telegram autorisé(s)             {P}║")
    print(f"╚═══════════════════════════════════════════╝{W}")

    print(f"{BOLD}{P}┌───────────────────────────────────────────┐")
    print(f"│ {V}[1] Démarrer le Bot                       {P}│")
    print(f"│ {V}[2] Se connecter aux comptes              {P}│")
    print(f"│ {V}[3] Déconnexion T/G                       {P}│")
    print(f"│ {V}[4] Listes des comptes                    {P}│")
    print(f"│ {V}[5] Supprimer un compte                   {P}│")
    print(f"│ {V}[6] Corbeille                             {P}│")
    print(f"│ {V}[7] Récupérer ma clé                      {P}│")
    print(f"│ {V}[8] Mettre à jour                         {P}│")
    print(f"│ {V}[9] Autres                                {P}│")
    print(f"│ {R}[0] Quitter                               {P}│")
    print(f"└───────────────────────────────────────────┘{W}")

    choice = input(f"\n{BOLD}{B}[➤] Choix : {W}{BOLD}")
    if choice == "1" or choice == "8":
        os.system('python ~/insta-manager-pro/update.py')
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
    
