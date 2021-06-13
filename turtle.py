import random
import turtle
from turtle import Turtle, Screen
from random import choice
tom = Turtle()
tom.shape('turtle')
tom.color("red")

colours=["medium aquamarine","navy","honeydew"]
def fn(n):
    for i in range(n):
        tom.right(360 / n)
        tom.forward(100)



for i in range(3, 11):
    tom.color(random.choice(colours))
    fn(i)

screen = Screen()
screen.exitonclick()
