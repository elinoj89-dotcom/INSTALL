import os
import time
import sys
import shutil

# Styles et Couleurs (STYLE GRAS)
BOLD = "\033[1m"
P = "\033[1;35m" ; G = "\033[1;32m" ; Y = "\033[1;33m" 
C = "\033[1;36m" ; B = "\033[1;34m" ; R = "\033[1;31m" ; W = "\033[1;37m"

def banner():
    os.system('clear')
    print(f"{BOLD}{B}╔═══════════════════════════════════════════╗")
    print(f"║       SMM PRO - GESTIONNAIRE SYSTÈME      ║")
    print(f"║           DEVELOPPER BY ELINO             ║")
    print(f"╚═══════════════════════════════════════════╝{W}")

def uninstall_system():
    print(f"\n{BOLD}{R}╔════════════════ ATTENTION ════════════════╗")
    print(f"║      SUPPRESSION DU SYSTÈME EN COURS      ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    path_bot = os.path.join(os.path.expanduser("~"), "insta-manager-pro")
    
    if os.path.exists(path_bot):
        print(f"\n{BOLD}{Y}[*] Nettoyage du moteur de bot...{W}")
        shutil.rmtree(path_bot)
        print(f"{BOLD}{G}[✔] Dossier insta-manager-pro supprimé.{W}")
    
    confirm = input(f"\n{BOLD}{Y}[?] Supprimer aussi l'installeur ? (y/n) : {W}{BOLD}")
    if confirm.lower() == 'y':
        print(f"\n{BOLD}{G}[✔] Nettoyage complet effectué.{W}")
        print(f"{BOLD}{R}[!] Tapez 'rm -rf ~/INSTALL' pour finir.{W}")
        time.sleep(2)
        sys.exit()

def install_process():
    print(f"\n{BOLD}{Y}[*] Préparation de l'environnement...{W}")
    
    # Liste des paquets à installer
    packages = [
        ("Mise à jour système", "pkg update -y && pkg upgrade -y"),
        ("Python & Git", "pkg install python git -y"),
        ("Termux API", "pkg install termux-api -y"),
        ("Instaloader", "pip install instaloader"),
        ("Requests", "pip install requests")
    ]

    for name, cmd in packages:
        print(f"\n{BOLD}{C}───────────────────────────────────────────")
        print(f"{BOLD}{B}[▶] Installation : {W}{BOLD}{name}")
        os.system(cmd)
        print(f"{BOLD}{G}[✔] Terminé.{W}")

    print(f"\n{BOLD}{G}[✔] CONFIGURATION RÉUSSIE !{W}")
    time.sleep(2)
    os.system('python main.py')

def main():
    banner()
    print(f"{BOLD}{P}┌───────────────────────────────────────────┐")
    print(f"│ {V}[1] Installer / Lancer SMM PRO            {P}│")
    print(f"│ {R}[2] Désinstaller (Nettoyage)              {P}│")
    print(f"│ {W}[0] Quitter                               {P}│")
    print(f"└───────────────────────────────────────────┘{W}")
    
    choice = input(f"\n{BOLD}{B}[➤] Choix : {W}{BOLD}")
    
    if choice == "1":
        install_process()
    elif choice == "2":
        uninstall_system()
    elif choice == "0":
        sys.exit()
    else:
        main()

if __
        
