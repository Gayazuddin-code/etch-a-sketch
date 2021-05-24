from turtle import Turtle, Screen

tim = Turtle()
tim.pensize(5)
screen = Screen()


def mov_forward():
    tim.forward(10)


def mov_backward():
    tim.backward(10)


def counter_clock():
    tim.left(10)


def clock():
    tim.right(10)


def clear_screen():
    screen.reset()


screen.listen()
screen.onkey(key="w", fun=mov_forward)
screen.onkey(key="s", fun=mov_backward)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
