class Fraction(object):

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'''The fraction elements are the:
Numerator   --->  {self.numerator}
Denominator --->  {self.denominator}
'''

    def __add__(self, other):
        print("The sum of the fraction elements")
        sum = self.numerator + self.denominator
        return f"{self.numerator} + {self.denominator} = {sum}\n"

    def __sub__(self, other):
        print("The substract of the fraction elements")
        sub = self.numerator - self.denominator
        return f"{self.numerator} - {self.denominator} = {sub}\n"

    def inverse(self):
        print("This returns the inverse faction")
        return Fraction(2, 12)


# Instantierea numaratorului si numitorului
fraction = Fraction(12, 2)

# Afisarea numaratorului si numitorului
print(fraction)

# Afisarea sumei elementelor fractiei
print(fraction + fraction)

# Afisarea scaderii elemetelor fractiei
print(fraction - fraction)

# Afisarea inversei fractiei
print(fraction.inverse())
