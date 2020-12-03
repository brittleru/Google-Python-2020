class Coordonate(object):
    """ O coordonata este compusa din valorile x si y """

    def __init__(self, x, y):
        """ Setam valorile pentru x si y """
        print("Constructor is called...")
        self.x = x
        self.y = y

    def __str__(self):
        """ Afisam coordonatele x si y """
        return f"<{self.x}, {self.y}>"

    def distance(self, other):
        """ Returneaza distanta euclidiana dintre doua coordonate """
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2

        return (x_diff_sq + y_diff_sq) ** 0.5


origin = Coordonate(0, 0)
print((id(origin)))
print(origin.x)
print(origin)

c1 = Coordonate(1, 0)
c2 = Coordonate(0, 2)

print(f"Coordonata 1 -> {c1}")
print(f"Coordonata 2 -> {c2}")

print(f"Distanta euclidiana dintre cele doua coordonate {origin} ---> {origin.distance(origin)}")
print(f"Distanta euclidiana dintre cele doua coordonate {c1} ---> {c1.distance(origin)}")
print(f"Distanta euclidiana dintre cele doua coordonate {c2} ---> {c2.distance(origin)}")
print(f"Distanta euclidiana dintre cele doua coordonate {c2} ---> {c1.distance(c2)}")
