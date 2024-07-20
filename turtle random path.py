from turtle import Turtle,Screen
import random
tim = Turtle()
tim.shape("turtle")
colours = ["medium blue","dark grey", "black", "red", "violet"]
direction = [0,90,180,270]
#tim.speed(("fastest"))
tim.pensize(5)
for _ in range(200):

    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(direction))
screen = Screen()
screen.exitonclick()
