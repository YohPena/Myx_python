from fonctions.give_id import give_id  # Génère un ID unique (nombre premier)

class Axiome:
    def __init__(self, nom: str, valeur: str, force: float = 1.0):
         # Vérification de la force
        if not (0 <= force <= 1):
            print(f"Valeur de force invalide ({force}) pour l'axiome '{nom}', elle sera mise à 1.0.")
            force = 1.0
            print(f"Force initialisé à 1.0.")

        self.id = give_id()
        self.nom = nom
        self.valeur = valeur
        self.type = "axiome"
        self.force = 1.0
        self.couleur = "#ffe927"
        self.enfants = []  # les objets qui découleront de cet axiome
        self.liens = []    # liste d'objets Lien

    def ajouter_enfant(self, enfant):
        lien = Lien(parent=self, enfant=enfant)
        self.liens.append(lien)
        enfant.liens.append(lien)
        
    def __repr__(self):
        return (f"<Axiome id={self.id}, nom='{self.nom}', "
                f"valeur='{self.valeur}', couleur={self.couleur}>")