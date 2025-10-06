import colorgram
import turtle
import random

### Functions
def draw_dots(d_size: int, f_pace: int, rgb_list: list):
    """Draw dots of size d_size, moving forward f_pace paces, and of a random color
    from rgb_list"""
    for _ in range(10):
        chi.dot(d_size, random.choice(rgb_list))
        chi.penup()
        chi.forward(f_pace)
        chi.pendown()

def go_west(f_pace):
    """Turn the turtle west and move it to the next row"""
    chi.penup()
    chi.setheading(90)
    chi.forward(f_pace)
    chi.setheading(180)
    chi.forward(f_pace)

def go_east(f_pace):
    """Turn the turtle east and move it to the next row"""
    chi.penup()
    chi.setheading(90)
    chi.forward(f_pace)
    chi.setheading(0)
    chi.forward(f_pace)


# Extract 30 colors from the image
colors = colorgram.extract('C:\\Users\\User\\Documents\\100 Days of Code\\100-Days-of-Code-\\Projects-Complete\\Hirst-Painting\\image.jpg', 30)

# Create a list of a tuple of RGB colors
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

# Remove the white colors
color_list = [(237, 222, 85), (231, 170, 98), (193, 227, 243), (252, 53, 12), 
              (239, 49, 85), (156, 84, 28), (172, 59, 112), (59, 179, 227), 
              (85, 204, 147), (110, 216, 248), (22, 127, 214), (24, 183, 216), 
              (237, 130, 161), (43, 112, 38), (36, 84, 43), (131, 234, 211), 
              (252, 136, 142), (87, 29, 37), (250, 235, 239), (68, 162, 33), 
              (99, 43, 22), (253, 221, 1), (105, 47, 27), (98, 37, 45), 
              (38, 69, 44), (169, 132, 21), (234, 162, 157), (76, 130, 187)]

turtle.colormode(255)
chi = turtle.Turtle()
chi.pensize(20)
chi.speed("fastest")
chi.hideturtle()
dot_size = 20
pace = 50

# Set starting position of turtle
chi.setheading(225)
chi.penup()
chi.forward(250)
chi.pendown()
chi.setheading(0)

for _ in range(5):
    draw_dots(dot_size, pace, color_list)
    go_west(pace)
    draw_dots(dot_size, pace, color_list)
    go_east(pace)

screen = turtle.Screen()
screen.exitonclick()