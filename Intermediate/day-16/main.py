import turtle
import prettytable

timmy = turtle.Turtle()
# object = module.Class()
timmy.shape("turtle")
# object.method
timmy.color('Coral')
# object.method
timmy.forward(100)
# object.method
my_screen = turtle.Screen()
# object = module.Class()
print(my_screen.canvheight)
# object.attribute
my_screen.exitonclick()
# object.method

table = prettytable.PrettyTable()
# object = module.Class()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# object.method
table.add_column("Type", ["Electric", "Water", "Fire"])
# object.method
table.align = "l"

print(table)