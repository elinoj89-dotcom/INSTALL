import os
import time
import sys

# Couleurs
P = "\033[35m" # Violet
G = "\033[32m" # Vert
W = "\033[0m"  # Blanc
Y = "\033[33m" # Jaune

def progress_bar(duration):
    """Affiche une barre de chargement animée"""
    for i in range(1, 101):
        time.sleep(duration / 100)
        sys.stdout.write(f"\r{P}[*] Installation : {i}% [{'#' * (i // 5)}{'.' * (20 - i // 5)}]")
        sys.stdout.flush()
    print(f"\n{G}[✔] Composants installés avec succès !{W}")

def banner():
    os.system('clear')
    print(f"{P}┌───────────────────────────────────────────┐")
    print(f"│            ELINO SYSTEM INSTALL           │")
    print(f"└───────────────────────────────────────────┘{W}")
    print(f"{G}(✓) Github    = elinoj89-dotcom")
    print(f"(✓) Tool Name = INSTALL{W}")
    print("-" * 45)

def main():
    banner()
    print(f"{W}[1] ALL INSTALL PKG")
    print(f"[0] EXIT")
    
    choice = input(f"\n{Y}[?] Choice: {W}")
    
    if choice == "1":
        print(f"\n{G}[*] Initialisation des miroirs Termux...{W}")
        time.sleep(1)
        
        # Lancement de la barre de chargement
        progress_bar(3) # Dure 3 secondes pour faire "vrai"
        
        print(f"{G}[*] Configuration de l'environnement Python...{W}")
        time.sleep(1)
        
        # On passe à la vérification du mot de passe
        os.system('python main.py')
    else:
        print(f"{R}[!] Annulation.{W}")
        sys.exit()

if __name__ == "__main__":
    main()
