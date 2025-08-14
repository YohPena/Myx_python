from .registry import all_propositions
from classes.lien import Lien
from fonctions import give_id, create_link

class Proposition:
    def __init__(self, nom, texte, parents):
        if not parents or len(parents) < 2:
            raise ValueError("Une proposition doit avoir au moins 2 parents.")
        
        self.nom = nom
        self.texte = texte
        self.type = "proposition"
        self.couleur = "#64c0f5"  # couleur fixe pour toutes les propositions
        self.parents = parents
        self.enfants = []  # les objets qui découleront de cette proposition
        
        # Calculer l'ID et la force à partir des parents
        self.id = 1
        self.force = 1.0
        for p in parents:
            self.id *= p.id
            self.force *= p.force

        # Créer les liens avec create_link
        self.liens = []
        for p in parents:
            create_link(p, self)  # met à jour parent.liens, self.liens et parent.enfants

        all_propositions.append(self)

    def __repr__(self):
        return f"<Proposition {self.nom} id={self.id} force={self.force:.2f} liens={len(self.liens)}>"
