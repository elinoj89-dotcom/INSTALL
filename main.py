import os
import sys
import time
import hashlib
import requests

# Couleurs
P = "\033[35m" ; G = "\033[32m" ; Y = "\033[33m" 
C = "\033[36m" ; R = "\033[31m" ; W = "\033[0m"
B = "\033[34m" # Bleu pour le style SMM
V = "\033[0;32m" # Vert clair

DB_URL = "https://raw.githubusercontent.com/elinoj89-dotcom/INSTALL/refs/heads/main/database.txt"

def get_hwid():
    id_str = os.popen('getprop ro.serialno').read().strip()
    if not id_str:
        id_str = os.popen('getprop ro.product.model').read().strip()
    return hashlib.md5(id_str.encode()).hexdigest().upper()[:15]

def show_menu():
    os.system('clear')
    # --- LOGO SMM EN BLEU ---
    print(f"""{B}
  ██████  ███    ███ ███    ███ 
 ██       ████  ████ ████  ████ 
   ████   ██ ████ ██ ██ ████ ██ 
       ██ ██  ██  ██ ██  ██  ██ 
  ██████  ██      ██ ██      ██ 
    {W}""")
    
    # En-tête du Tool
    print(f"{P}┌───────────────────────────────────────────┐")
    print(f"│ {Y}[*] TOOL NAME   >> {B}SMM{P}                 │")
    print(f"│ {Y}[*] DEVELOPPER  >> {G}ELINO{P}               │")
    print(f"│ {Y}[*] INTERFACE   >> {C}Web Scraping{P}        │")
    print(f"│ {Y}[*] VERSION     >> {G}5.5{P}                 │")
    print(f"└───────────────────────────────────────────┘{W}")
    
    # Barre de statut Telegram (Style capture)
    print(f"{P}╔═══════════════════════════════════════════╗")
    print(f"║       {G}Un Telegram autorisé(s)             {P}║")
    print(f"╚═══════════════════════════════════════════╝{W}")

    # Liste complète des options
    print(f"{P}┌───────────────────────────────────────────┐")
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

    choice = input(f"\n{B}[➤] Choix : {W}")

    # Logique des choix
    if choice == "1":
        os.system('python ~/insta-manager-pro/update.py')
    elif choice == "2":
        print(f"\n{Y}[*] Redirection vers connexion...{W}")
        time.sleep(1); show_menu()
    elif choice == "3":
        print(f"\n{R}[*] Déconnexion en cours...{W}")
        time.sleep(1); show_menu()
    elif choice == "8":
        os.system('python ~/insta-manager-pro/update.py')
    elif choice == "0":
        sys.exit()
    else:
        # Relance pour les options non encore codées ou retour menu
        time.sleep(1); show_menu()

def main():
    os.system('clear')
    my_key = get_hwid()
    try:
        response = requests.get(DB_URL)
        if my_key in response.text:
            show_menu()
        else:
            print(f"{R}┌─────────────────── ACCÈS REFUSÉ ───────────────────┐")
            print(f"│ {Y}🔑 Votre clé : {W}{my_key}                │")
            print(f"└─────────────────────────────────────────────────────┘{W}")
    except:
        print(f"{R}Erreur réseau.{W}")

if __name__ == "__main__":
    main()
    
