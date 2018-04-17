class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def formalize(self):
        return "Imię: {}, Nazwisko: {}".format(self.name, self.surname)

janek = Person("Jan", "Kos")
print(janek.__dict__)
print(janek.formalize())



for(int i = 0; i < 01)