import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fonctions import *
from classes.definition import Definition

def main():
    print("Bonjour, projet Python bien initialisé ! 🚀")

    d1 = Definition("Gravité", "Force qui attire les corps")
    d2 = Definition("Lumière", "Onde électromagnétique")

    print(d1)
    print(d2)

if __name__ == "__main__":
    main()
