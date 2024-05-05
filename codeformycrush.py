import turtle
import json

def for_you_my_beloved_crush(coordinates):
    screen = turtle.Screen()
    screen.bgcolor("black")  
    t = turtle.Turtle()
    t.speed(1)  
    screen_width = screen.window_width()
    screen_height = screen.window_height()
    t.pensize(2)  
    t.pencolor("lime")  
    x_start, y_start = coordinates[-1]
    t.penup()
    t.goto(x_start - screen_width / 2, screen_height / 2 - y_start)
    t.pendown()
    for i in range(len(coordinates) - 1, 0, -1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i - 1]
        t.goto(x1 - screen_width / 2, screen_height / 2 - y1)
        t.goto(x2 - screen_width / 2, screen_height / 2 - y2)
    turtle.done()

with open("mycrush.json", "r") as mycrush:
    me = json.load(mycrush)
    for_you_my_beloved_crush(me)
