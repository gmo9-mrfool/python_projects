import random
import turtle as t
tim=t.Turtle()
colors = ["DarkOrchid","CornflowerBlue",'IndianRed','LightSeaGreen','wheat','SlateGray']
tim.pensize(5)
directions= [0,90,180,270]
t.colormode(255)
def random_colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r, g, b)
tim.speed(6)
tim.shape('turtle')
for _ in range(5000):
    tim.color(random_colors())
    tim.forward(30)
    tim.setheading(random.choice(directions))
