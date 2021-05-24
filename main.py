from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def set_turtle():
    tim.pensize(5)
    pen_color = screen.textinput("color", "choose red or blue or green")
    pen_color = pen_color.lower()
    if pen_color == "exit":
        exit(0)
    elif pen_color not in ["red", "blue", "green"]:
        tim.pencolor("black")
    else:
        tim.pencolor(pen_color)


def mov_forward():
    tim.forward(10)


def mov_backward():
    tim.backward(10)


def counter_clock():
    tim.left(10)


def clock():
    tim.right(10)


def clear_screen():
    tim.reset()
    set_turtle()


set_turtle()

screen.listen()
screen.onkey(key="w", fun=mov_forward)
screen.onkey(key="s", fun=mov_backward)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
