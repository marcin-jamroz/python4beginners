class Vector():
    def __init__(self, *args):
        #print(args)
        self.coords = list(args)

    def __len__(self):
        return len(self.coords)

    def __repr__(self):
        template = "{}({})"
        name = self.__class__.__name__
        args = ", ".join(repr(x) for x in self.coords)
       # print(name, args)
        return template.format(name, args)
    
    def __add__(self, other):
        tmp = []
        for i in range(len(self)):
            tmp.append(self.coords[i] + other.coords[i])
        return Vector(*tmp)
    
    def __iadd__(self, other):
        for i in range(len(self)):
            self.coords[i] += other.coords[i]
        return self

    def __eq__(self, other):
        for i in range(len(self)):
            if not self.coords[i] == other.coords[i]:
                return False
            return True

Vector(5)
Vector(1, 2, 3)

#print("len(Vector(1,2,3)): ", len(Vector(1,2,3)))
#print("len(Vector(4, 5)): ", len(Vector(4, 5)))

v = Vector(1, 2)
v1 = Vector(2, 3)
v2 = v + v1
v3 = Vector(3, 5)
#print(v2)

v1 += v
print(v1)
print(v2 == v3)