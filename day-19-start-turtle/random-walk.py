from turtle import Turtle as t, Screen as s
import random

tim = t()


colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]
directions = [0, 90, 180, 270]
steps = [5, 15, 20]
# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.right(angle)

DEGREE = 90

# PYTHON TUPLE == IMMUTABLE (CAN'T BE CHANGED)
my_tuple = (1, 3, 8)  # PYTHON TUPLE CAN BE CONVERTED TO LIST

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
    rand_direction = random.choice(directions)
    tim.width(5)
    # tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(random.choice(steps))
    tim.setheading(rand_direction)


screen.exitonclick()
