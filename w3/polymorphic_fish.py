class Shark():
    def swim(self):
        print("The shark is swimming")

    def swim_backwards(self):
        print("the shark cannot swim backwards, but can sink backwards")
    
    def skeleton(self):
        print("The shark's skeleton is made of carilage")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming")
    
    def swim_backwards(self):
        print("The clownfish can swim backwards")

    def skeleton(self):
        print("The clownfish skeleton is made of bone")


        
        
sammy = Shark()
#sammy.skeleton()

casey = Clownfish()
#casey.skeleton()


for fish in (sammy, casey):
    #fish.swim()
    #fish.swim_backwards()
    fish.skeleton()


def in_the_pacific(fish):
    fish.swim()


in_the_pacific(sammy)
in_the_pacific(casey)