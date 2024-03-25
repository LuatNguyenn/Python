from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fordward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_left():
    tim.setheading(tim.heading() + 10)  # same with tim.left(10)


def move_right():
    tim.right(10)


def clear():
    tim.reset()


# key pressed will envoke this
screen.listen()


screen.onkey(
    key="w", fun=move_fordward
)  # DOESN'T MATTER THE POSITION OF THE ARGUMENT BECAUSE IT PASSED THE KEY NAME (key and fun)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
