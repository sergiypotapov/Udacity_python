__author__ = 'spotapov'

import turtle

def draw_body(body):
    for k in range(1, 40):
        for i in range(1,5):
            body.forward(100)
            body.right(90)
        body.right(10)
def draw_line(line):
        line.pensize(5)
        line.right(90)
        line.forward(800)
def draw_flower():
    window = turtle.Screen()
    window.bgcolor("grey")
    body = turtle.Turtle()
    line = turtle.Turtle()
    draw_body(body)
    draw_line(line)
    window.exitonclick()
draw_flower()

