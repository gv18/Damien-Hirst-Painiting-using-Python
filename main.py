import turtle

from colorgram import extract
from turtle import Turtle,Screen
import random
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")
my_turtle.speed("fastest")
turtle.colormode(255)
colors = extract('pic.jpeg', 15)
rgb_colors = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    color = (r, g, b)
    rgb_colors.append(color)
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
number_of_dots = 100
for dot_count in range(1,number_of_dots+1):
    my_turtle.dot(20, random.choice(rgb_colors))
    my_turtle.forward(50)
    if(dot_count % 10 == 0):
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)
screen = Screen()
screen.exitonclick()