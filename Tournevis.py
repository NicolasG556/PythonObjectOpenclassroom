class Tournevis:

    def __init__(self, taille=3):
        self.taille = taille

    def serrerVis(self, vis):
        vis.visser()

    def dessererVis(self, vis):
        vis.devisser()

    def __repr__(self):
        return f"Tournevis de taille {self.taille}"



