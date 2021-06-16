import turtle as turtle_module
tom=turtle_module.Turtle()
turtle_module.colormode(255)
import random
color_list = [
  (222, 163, 67), (19, 45, 85),
 (134, 62, 86), (172, 62, 46), (230, 240, 236),
 (127, 40, 61), (23, 84, 61), (59, 48, 37),
 (247, 195, 49), (17, 115, 143), (57, 140, 73),
 (228, 86, 38), (193, 131, 153), (231, 173, 190),
 (155, 190, 184), (195, 102, 133),
 (30, 65, 55), (57, 71, 39),
 (166, 204, 201), (152, 169, 181),
 (35, 46, 101), (60, 30, 46)]
tom.speed(0)
tom.penup()
tom.hideturtle()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    tom.dot(20,random.choice(color_list))
    tom.forward(50)

    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)




for _ in range(10):
    tom.dot(20, random.choice(color_list))
    tom.forward(50)
screen = turtle_module.Screen()
screen.exitonclick()