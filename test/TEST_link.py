import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.registry import all_axiomes, all_definitions, all_propositions, all_liens
from classes.axiome import Axiome
from classes.definition import Definition
from classes.proposition import Proposition
from fonctions import create_link

#Créer des axiomes
axiome1 = Axiome(nom="Axiome 1", valeur="Tout nombre pair est divisible par 2")
axiome2 = Axiome(nom="Axiome 2", valeur="0 est un nombre pair")

#Créer une définition
definition1 = Definition(nom="Définition 1", valeur="Nombre pair : divisible par 2")

# Créer une proposition à partir des deux axiomes
proposition1 = Proposition(
    nom="Proposition 1",
    texte="0 est divisible par 2",
    parents=[axiome1, axiome2]
)

# Créer une deuxième proposition à partir de proposition1 et axiome1
proposition2 = Proposition(
    nom="Proposition 2",
    texte="Tout multiple de 2 est divisible par 2",
    parents=[proposition1, axiome1]
)

# Créer un lien entre la définition et la dernière proposition
create_link(definition1, proposition2)

# Afficher tous les objets
print(axiome1)
print(axiome2)
print(definition1)
print(proposition1)
print(proposition2)

# Afficher les liens pour vérification
print("\nLiens de Proposition 2 :")
for lien in proposition2.liens:
    print(lien)

print("\nLiens de Définition 1 :")
for lien in definition1.liens:
    print(lien)

print(f"ALL LINK HERE")
print(all_liens)