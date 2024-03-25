from turtle import Turtle as t, Screen as s
import random

tim = t()
screen = s()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(0, 110000000):
    tim.speed("fastest")
    tim.color(random_color())
    tim.left(3)
    tim.circle(100)


screen.exitonclick()
