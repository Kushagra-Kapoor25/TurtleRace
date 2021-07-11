from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.title("Welcome to Turtle Race!")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "purple", "green", "blue"]
all_turtles = []


def create_turtles():
    sep = 125
    for color in colors:
        new_turtle = Turtle("turtle")
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(x=-230, y=sep)
        all_turtles.append(new_turtle)
        sep -= 50


create_turtles()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
