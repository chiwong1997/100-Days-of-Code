class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.num_fins = 4

    def swim(self):
        print("Moving in water")

    def breathe(self):
        super().breathe()
        # the breathe method from the Animal class is called, and then there will also be 
        # an additional step performed by the breathe method in the Fish class
        print("Doing this underwater")

nemo = Fish()
print(nemo.num_eyes)
nemo.breathe()