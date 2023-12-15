class Tiere:
    typ="amazing"
    def __init__(self,herkunft, durchschnittsalter, name, hauptnahrung, ist_bedroht, ist_vegetarisch):
        self.herkunft=herkunft
        self.durchschnittsalter=durchschnittsalter
        self.name=name
        self.hauptnahrung=hauptnahrung
        self.ist_bedroht=ist_bedroht
        self.ist_vegetarisch=ist_vegetarisch
    
    def zeige_info(self):
        print(f"Herkunft: {self.herkunft}, durchschnittsalter: {self.durchschnittsalter}, name: {self.name}, hauptnahrung: {self.hauptnahrung}, ist_bedroht: {self.ist_bedroht}, ist_vegetarisch: {self.ist_vegetarisch}")

    def zeige_essen(self):
        print(f"hauptnahrung: {self.hauptnahrung}, ist_vegetarisch: {self.ist_vegetarisch}")

Panda=Tiere("asien", "10", "Panda", "Bambus", "nein", "ja")

#print(f"mein Tier: {Panda}, {Panda.typ}")
Panda.zeige_essen()
Panda.zeige_info()

