# fonctions/links_utils.py
from classes.lien import Lien

def create_link(parent, child, type_lien="relation"):
    """
    Crée un lien entre un parent et un enfant.

    Args:
        parent: objet parent (Axiome, Definition, Proposition...)
        child: objet enfant
        link_type: type de lien (par défaut 'base')
    """
    # Crée le lien
    link = Lien(parent=parent, enfant=child, type_lien=type_lien)
    
    # Ajoute le lien aux listes de liens des deux objets
    parent.liens.append(link)
    child.liens.append(link)
    
    # Ajoute l'enfant à la liste des enfants du parent
    parent.enfants.append(child)
    
    return link
