class Vector():
    def __init__(self, *args):
        self.coords = [x for x in args]

    def __len__(self):
        return len(self.coords)

    def __repr__(self):
        args = ", ".join(repr(x) for x in self.coords)
        return "{}({})".format(self.__class__.__name__, args)

    def __add__(self, other):
        tmp = []
        for x in range(len(self)):
            tmp.append(self.coords[x] + other.coords[x])
        return Vector(*tmp)

    def __iadd__(self, other):
        for i in range(len(self)):
            self.coords[i] += other.coords[i]
        return self

    def __eq__(self, other):
        for i in range(len(self)):
            if self.coords[i] != other.coords[i]:
                return False
        return True

    def __mul__(self, other):
        tmp = []
        for x in self.coords:
            tmp.append(other * x)
        return tmp

    def __rmul__(self, other):
        tmp = []
        for x in self.coords:
            tmp.append(other * x)
        return tmp

a = Vector(5) # tworzy wektor jednowymiarowy o długości 5 (n = 1)
b = Vector(1, 2, 3) # tworzy wektor trójwymiarowy (n = 3)
print(a.__dict__)
print(b.coords)

print(len(Vector(1, 2, 3)))
print(len(Vector(4, 5)))

v = Vector(1, 2)
print('v: ', v)
v1 = Vector(2, 4, 5.6, 7,8)
print('v1: ', v1)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v1)
print(v2)
print(v3)
print(id(v1))
print(id(v2))
print(id(v3))



v1 = Vector(1, 2)
v2 = Vector(3, 4)
print('id(v1): ', id(v1))
print('id(v2): ', id(v2))
v1 += v2
print(v1)
print(v2)
print('id(v1): ', id(v1))
print('id(v2): ', id(v2))




v1 = Vector(1, 2, 3)
v2 = Vector(1, 2, 3)
print('id(v1): ', id(v1))
print('id(v2): ', id(v2))
print('v1 is v2: ', v1 is v2)
print('v1 == v2: ', v1 == v2)  # dwa wektory powinny być uznane za równe tylko jeśli mają te same "współrzędne"
v3 = Vector(1, 2, 4)
print('v1 == v3: ', v1 == v3)  # dwa wektory z różnymi "współrzędnymi" powinny być uznane za nierówne
print('id(v3): ', id(v3))



print(80*"-")

v1 = Vector(1.1, 2.2, 3, 4)
v2 = v1 * 6
print(v1)
print(v2)
print('id(v1): ', id(v1))
print('id(v2): ', id(v2))



v1 = Vector(1.1, 2.2, 3, 4)
v2 = v * 6
print(v1)
print(v2)
v1 = Vector(1.1, 2.2, 3, 4)
v2 = v1 * 6
v3 = 6 * v1
print(v1)
print(v2)
print(v3)
print(v2 == v3)
print('id(v1): ', id(v1))
print('id(v2): ', id(v2))
print('id(v3): ', id(v3))