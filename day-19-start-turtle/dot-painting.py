from turtle import Turtle as t, Screen as s
import random

tim = t()
tim.hideturtle()
tim.penup()

screen = s()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    # random
    return random_color

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 300
tim.speed("fastest")
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random_color())
    tim.forward(50)

    
    if(dot_count % 10 == 0):
        tim.setheading(90) 
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0) 
    # tim.forward(40)
    tim.pendown()




     
screen.exitonclick()
