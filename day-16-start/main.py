from turtle import Turtle, Screen

# import another_module
# print(another_module.another_variable)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("brown")
timmy.forward(100)

screen = Screen()
print(screen.canvheight)
screen.exitonclick()

# from prettytable.colortable import PrettyTable, ColorTable,Themes

# table = PrettyTable()
# colorTable = ColorTable(theme= Themes.OCEAN)
# table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
# table.add_column("Type",["Electric","Water","Fire"])
# table.align = "l"
# print(table)
