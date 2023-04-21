class BoiteAOutils:

    def __init__(self):
        self.outils = []

    def ajouterOutil(self, outil):
        self.outils.append(outil)

    def supprimerOutil(self, outil):
        index = self.outils.index(outil)
        del self.outils[index]




