class MyAbc():
    def __init__(self, a, b, c):
        print("Jestem w __init__")
        print("Type: ", type(self))
        self.a = a
        self.b = b
        self.c = c

    def someMethod(self):
        print("Jestem w someMethod")
        for k, v in self.__dict__.items():
            print("Key: {}, Value: {}".format(k, v))
    
    @classmethod
    def fromString(cls, strIn):
        print("Jestem w classMethod")
        print("Type: ", type(cls))
        a, b, c = strIn.split(".")
        return cls(a, b, c)

tmpInit = MyAbc(1, 2, 3)
tmpInit.someMethod()
tmpString = MyAbc.fromString("Ala.ma.kota")
tmpString.someMethod()