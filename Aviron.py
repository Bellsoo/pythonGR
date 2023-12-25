#Bateau
class Bateau:
    def __init__(self, nom, vitesse):
        self.nom = nom
        self.vitesse = vitesse
        self.distance_parcourue = 0

    def avancer(self):
        self.distance_parcourue += self.vitesse

    def distance_parcourue(self):
        return self.distance_parcourue
    
    
class Bateau2x(Bateau):
    def __init__(self, nom, vitesse):
        super().__init__(nom, vitesse)

        def type_du_bateau(self):
            self.type_du_bateau = "2x"
            return type_du_bateau


class BateauSkiff(Bateau):
    def __init__(self, nom, vitesse):
        super().__init__(nom, vitesse)

        def type_du_bateau(self):
            self.type_du_bateau = "1x"
            return type_du_bateau
        
class Bateau2moins(Bateau):
    def __init__(self, nom, vitesse):
        super().__init__(nom, vitesse)

        def type_du_bateau(self):
            self.type_du_bateau = "2-"
            return type_du_bateau
        


#Course

class Course:
    def __init__(self, type_bateau, course_fini):
        self.type_bateau = type_bateau
        self.bateaux_ligne_depart = []
        self.course_fini = course_fini

    def ajout_bateau_ligne_depart(self, bateau):
        if isinstance(bateau, Bateau) and isinstance(bateau, self.get_class_from_type()):
            self.bateaux_ligne_depart.append(bateau)
        else:
            print("Ce n'est pas le bon type de bateau.")

    def depart(self):
        print("Début de la course")

    def en_cours(self):
        return not self.course_fini

    def next_loop(self):
        for bateau in self.bateaux_ligne_depart:
            bateau.avancer()

    def affiche_positions(self):
        positions = [f"{bateau.nom},{bateau.get_distance_parcourue()}" for bateau in self.bateaux_ligne_depart]
        return '\n'.join(positions)

    def vainqueur(self):
        winner = max(self.bateaux_ligne_depart, key=lambda x: x.get_distance_parcourue())
        return f"Le vainqueur est {winner.nom} avec une distance de {winner.get_distance_parcourue()} mètres."

    def get_class_from_type(self):
        if self.type_bateau == '2x':
            return Bateau2x
        elif self.type_bateau == '1x':
            return BateauSkiff
        elif self.type_bateau == '2-':
            return Bateau
        else:
            raise ValueError("Type de bateau non pris en charge.")




if __name__ == "__main__":
    course_cadets = Course('2x')
    bateau_1_2x = Bateau2x('mickey', 62)
    bateau_2_2x = Bateau2x('minnie', 70)
    bateau_3_skiff = BateauSkiff('picsou', 15)

    course_cadets.ajout_bateau_ligne_depart(bateau_1_2x)
    course_cadets.ajout_bateau_ligne_depart(bateau_2_2x)
    course_cadets.ajout_bateau_ligne_depart(bateau_3_skiff)

    course_cadets.depart()

    with open("result.txt", "a") as f:
        while course_cadets.en_cours():
            course_cadets.next_loop()
            positions = course_cadets.affiche_positions()
            print(positions, flush=True)
            f.write(positions + "\n")

        print(course_cadets.vainqueur())