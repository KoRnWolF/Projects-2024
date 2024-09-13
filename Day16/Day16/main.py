# from turtle import Turtle, Screen
#
# tessa = Turtle()
# my_screen = Screen()
# print(my_screen.canvwidth)
# print(my_screen.canvheight)
# tessa.color("cyan")
# tessa.shape("turtle")
# tessa.speed(10)
# for x in range(0, 100):
#
#     tessa.forward(100 + x)
#     tessa.left(90 + x)
#     tessa.forward(100 + x)
#     x += 1
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtal"])
table.add_column("Type",["Fire", "Water"])
table.align = "l"
table.padding_width = 10


print(table)


