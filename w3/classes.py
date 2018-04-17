#tworzenie obiektu klasy
class First():
    pass


#print(type(First))

#instancjonowanie - instancja jest pusta, pola tworzy dopiero __init__ - inicjalizator, __new__ - konstruktor
pierwszy = First()
#print(type(pierwszy))


class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


janek = Person("Jan", "Kos")
gustlik = Person("Gustaw", "Jeleń")


print(type(Person))
for x in (janek, gustlik):
    print(type(x), x.name, x.surname)
    print(80 * "-")