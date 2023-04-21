class Marteau:

    def __init__(self, couleur = "rouge"):
        self.couleur = couleur

    def peindreMarteau(self, couleur):
        self.couleur = couleur

    def enfoncerClou(self, clou):
        clou.enfoncer()

    def retirerClou(self, clou):
        clou.retirer()

    def __repr__(self):
        return f"Marteau de couleur {self.couleur}"

