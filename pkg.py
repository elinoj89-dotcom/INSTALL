import os
import time
import sys
import shutil

# Couleurs Style Screenshot
P = "\033[35m" # Violet
G = "\033[32m" # Vert
R = "\033[31m" # Rouge
W = "\033[0m"  # Blanc
Y = "\033[33m" # Jaune

def banner():
    os.system('clear')
    print(f"{P}┌───────────────────────────────────────────┐")
    print(f"│            ELINO SYSTEM MANAGER           │")
    print(f"└───────────────────────────────────────────┘{W}")
    print(f"{G}(✓) Github    = elinoj89-dotcom")
    print(f"(✓) Tool Name = INSTALL{W}")
    print("-" * 45)

def uninstall_system():
    print(f"\n{R}[!] Suppression du système en cours...{W}")
    path_bot = os.path.join(os.path.expanduser("~"), "insta-manager-pro")
    path_install = os.path.join(os.path.expanduser("~"), "INSTALL")
    
    # Supprime le bot
    if os.path.exists(path_bot):
        shutil.rmtree(path_bot)
        print(f"{G}[✔] Dossier insta-manager-pro supprimé.{W}")
    
    print(f"{Y}[?] Voulez-vous aussi supprimer l'installeur ? (y/n) : {W}", end="")
    confirm = input()
    if confirm.lower() == 'y':
        print(f"{G}[✔] Nettoyage complet. Merci d'avoir utilisé Elino System.{W}")
        print(f"{R}[!] Note: Vous devrez supprimer manuellement le dossier INSTALL avec 'rm -rf ~/INSTALL'{W}")
        time.sleep(2)
        sys.exit()

def main():
    banner()
    print(f"{W}[1] {G}Lancer / Installer SMM{W}")
    print(f"{W}[2] {R}Désinstaller SMM (Nettoyage){W}")
    print(f"{W}[0] EXIT")
    
    choice = input(f"\n{Y}[?] Choice: {W}")
    
    if choice == "1":
        print(f"\n{G}[*] Lancement de la procédure...{W}")
        time.sleep(1)
        os.system('python main.py')
    elif choice == "2":
        uninstall_system()
    elif choice == "0":
        sys.exit()
    else:
        print(f"{R}[✘] Choix invalide.{W}")
        time.sleep(1)
        main()

if __name__ == "__main__":
    main()
    
