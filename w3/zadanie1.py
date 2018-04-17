class Surprise():
    a = 44
    b = []
    def __init__(self, name):
        self.name = name

sup1 = Surprise('pierwsza')
sup2 = Surprise('druga')

def print_surprise():
    print(Surprise, Surprise.a, Surprise.b)
    print(sup1, sup1.a, sup1.b, sup1.name)
    print(sup2, sup2.a, sup2.b, sup2.name)


print_surprise()

sup1.a = 26
print_surprise()

Surprise.a = 55
print_surprise()

sup1.b.append("niespodzianka")
print_surprise()

sup2.b = ["inna niespodzianka"]
print_surprise()

Surprise.nowy = "Czary mary"
print(sup2.nowy)