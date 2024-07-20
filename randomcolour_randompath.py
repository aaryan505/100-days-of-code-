import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r,g,b)
    return random_colour
direction = [0, 90, 180, 270]
tim.speed("fastest")
tim.pensize(5)
for _ in range(200):

    tim.color(random_colour())
    tim.forward(30)
    tim.setheading(random.choice(direction))
