from .registry import all_definitions
from fonctions import give_id  # ta fonction d'ID unique

class Definition:
    def __init__(self, nom: str, valeur: str, force: float = 1.0):
         # Vérification de la force
        if not (0 <= force <= 1):
            print(f"Valeur de force invalide ({force}) pour '{nom}', elle sera mise à 1.0.")
            force = 1.0
            print(f"Force initialisé à 1.0.")

        self.id = give_id()
        self.nom = nom
        self.valeur = valeur
        self.type = "definition"
        self.force = force
        self.couleur = "#dddddd"  # Par défaut blanc
        self.enfants = []  # les objets qui découleront de cet axiome
        self.liens = []    # liste d'objets Lien

        all_definitions.append(self)
        
    def __repr__(self):
        return (f"Definition(id={self.id}, nom='{self.nom}', "
                f"force={self.force}, liens={len(self.liens)})")
