from turtle import Turtle, Screen
import random

is_race_on = False
all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which one win ? Enter color:"
)
colors = ["red", "orange", "green", "yellow", "blue", "purple"]

y_position = [-70, -40, -10, 20, 50, 80]

for turtle in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle])
    tim.penup()
    tim.goto(x=-230, y=y_position[turtle])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            print("turtle.xcor(): ", turtle.xcor())
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print("Won")
            else:
                print("lost")
        print("turtle: ", turtle)
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
