# classes/lien.py
class Lien:
    def __init__(self, parent, enfant, type_lien="relation"):
        
        self.parent = parent
        self.enfant = enfant
        self.type_lien = type_lien
        self.id = (parent.id, enfant.id)

    def __repr__(self):
        return f"<Lien {self.type_lien} parent={self.parent.nom} enfant={self.enfant.nom} id={self.id}>"
