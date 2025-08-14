from .registry import all_liens
class Lien:
    def __init__(self, parent, enfant, type_lien="relation"):
        
        self.parent = parent
        self.enfant = enfant
        self.type_lien = type_lien
        self.id = (parent.id, enfant.id)

        all_liens.append(self)

    def __repr__(self):
        return f"<Lien {self.type_lien} parent={self.parent.nom} enfant={self.enfant.nom} id={self.id}>"
