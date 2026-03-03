import os
import sys
import time

# Couleurs pour le style
G = "\033[32m" # Vert
R = "\033[31m" # Rouge
W = "\033[0m"  # Blanc
Y = "\033[33m" # Jaune
P = "\033[35m" # Violet

def check_security():
    os.system('clear')
    # Style de ta capture d'écran
    print(f"{Y}(🔑)Mot De Passe: {W}", end="")
    pwd = input()
    
    if pwd == "Elino21#2006":
        print(f"{G}\n[✔] Accès autorisé.{W}")
        time.sleep(1)
        manage_project()
    else:
        print(f"{R}\n[✘] Mot de passe incorrect. Accès refusé.{W}")
        sys.exit()

def manage_project():
    path = os.path.join(os.path.expanduser("~"), "insta-manager-pro")
    
    # Vérification si le projet existe déjà
    if os.path.exists(path):
        print(f"{P}[*] Le projet existe déjà. Vérification des mises à jour...{W}")
        os.system(f'cd {path} && git pull')
    else:
        print(f"{P}[*] Premier lancement : Téléchargement du Manager Pro...{W}")
        os.system(f'cd $HOME && git clone https://github.com/Lariot08/insta-manager-pro')
    
    print(f"{G}[✔] Prêt ! Lancement du système...{W}")
    time.sleep(2)
    
    # Lancement final
    os.system(f'cd {path} && python main.py')

if __name__ == "__main__":
    check_security()
      
