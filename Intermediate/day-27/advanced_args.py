def add(*args):
    print(args[0])
    total = 0
    for n in args:
        total+=n
    print(total)

add(4,2,4,5)
add(10,2)

# referring to our args by name instead of position

def test(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)

test(add=3, multiply=5) #produces a dictionary

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n*= kwargs['multiply']
    print(n)

    

calculate(2, add=3, multiply=5) #produces a dictionary

class Car: 

    def __init__(self, **kw):
        self.make = kw.get("make") #get function returns make=None if no value set when initializing the class
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)

my_second_car = Car(make="Ferrari", model="Spyder")
print(my_second_car.model)

def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)