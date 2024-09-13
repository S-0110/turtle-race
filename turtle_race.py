from turtle import Turtle, Screen
import random

is_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt= "Which Turtle will win the race? Guess the colour.")
y_position = [-70, -40, -10, 20, 50, 80]
colors = ["Blue", "Green","Yellow", "Orange", "Red", "Purple"]
all_turtle = []

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230, y=y_position[i])
    all_turtle.append(tim)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        rand_move = random.randint(0,10)
        turtle.forward(rand_move)



screen.exitonclick()