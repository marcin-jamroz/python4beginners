class A():
    def whoAmI(self):
        self.primitiveWhoAmI()
        self.detailedWhoAmI()

    def primitiveWhoAmI(self):
        print("Baza")

    def detailedWhoAmI(self):
        print("self.__class__.__name__: ", self.__class__.__name__)

class B():
    pass

class C(A, B):
    def primitiveWhoAmI(self):
        print("Potomek")
        super().primitiveWhoAmI()
    
a = A()
c = C()

print(type(c))
print("isinstance(c, A): ", isinstance(c, B))
print("issubclass(c, B): ", issubclass(C, A))
print("issubclass(A, B): ", issubclass(C, B))
print("isinstance(c, A): ", isinstance(c, A))
print("isinstance(c, B): ", isinstance(c, B))


a.whoAmI()
c.whoAmI()