class Clou:
    def __init__(self):
        self.danslemur = False

    def enfoncer(self):
        if not self.danslemur:
            self.danslemur = True

    def retirer(self):
        if self.danslemur:
            self.danslemur = False

    def __str__(self):
        etat_mur = "dans le mur" if self.danslemur else "hors du mur"
        return f"clou {etat_mur}"