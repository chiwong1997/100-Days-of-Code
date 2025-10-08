from turtle import Turtle, Screen

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.left(10)
    tim.forward(10)

def move_right():
    tim.right(10)
    tim.forward(10)

def clear_drawing():
    tim.home()
    tim.clear()

tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()