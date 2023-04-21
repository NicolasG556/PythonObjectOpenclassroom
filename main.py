from BoiteAOutils import BoiteAOutils
from Clou import Clou
from Marteau import Marteau
from Tournevis import Tournevis
from Vis import Vis


class Cake:

    def __init__(self, flavor):
        self.flavor = flavor

    def cut_in_part(self):
        print("Le gâteau est coupé en parts")


boite_a_outils = BoiteAOutils()

tournevis = Tournevis()

marteau = Marteau()

boite_a_outils.ajouterOutil(tournevis)
boite_a_outils.ajouterOutil(marteau)

vis1 = Vis()
print(vis1)
tournevis.serrerVis(vis1)
print(vis1)

clou1 = Clou()
print(clou1)
marteau.enfoncerClou(clou1)
print(clou1)
