import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(height=400, width=500)
user_choice = screen.textinput(title="Select Turtle", prompt="Which turtle will win the race? Enter the color")
is_game_on = False
turtle_color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = list()
initial_ypos = 100

for index in range(6):
    new_trutle = Turtle(shape="turtle")
    new_trutle.color(turtle_color[index])
    new_trutle.penup()
    new_trutle.goto(x=-230, y=initial_ypos)
    initial_ypos -= 40
    all_turtles.append(new_trutle)

if user_choice:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230.0:
            is_game_on = False
            break

if user_choice != turtle.pencolor():
    print("you lost the bet")
else:
    print("you won the bet")

screen.exitonclick()
