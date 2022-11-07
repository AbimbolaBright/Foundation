import turtle
import time
import random

delay =0.1
score= 0
high_score=0
#creating a window screen
wn =turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
#the width and height can be put as user choice
wn.setup(width=600,height=600)
wn.tracer(0)
#head of the snake
head=turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"
#food in the game
food= turtle.Turtle()
colors=random.choice(['red','green','black'])
shapes=random.choice(['square','tringle','circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.goto(0,100)

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0,250)
align="center",
font=("candara",24,"bold")
wn.mainloop
9+