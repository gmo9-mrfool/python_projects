import random
import turtle as t

tom = t.Turtle()
t.colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tom.speed(0)


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tom.color(random_colors())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()