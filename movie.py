__author__ = 'spotapov'

import turtle

def draw_cr(cr):
    cr.circle(90)

def draw_tr(tr):
    for i in range(1,5):
        tr.forward(100)
        tr.left(120)

def draw_sq(some_turtle):

    for k in range(1, 500):
        for i in range(1,5):
            some_turtle.forward(100)
            some_turtle.right(90)
        some_turtle.right(8)
        # some_turtle.write(k, True, align = "left" )
def draw():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    brad.shape("turtle")
    draw_sq(brad)
    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("white")
    # tring = turtle.Turtle()
    # draw_cr(angie)
    # draw_tr(tring)

    #bobby = turtle.Turtle()
    #bobby.shape("classic")
    #bobby.color("red")
    #bobby.right(100)
    #bobby.right(45)
    #bobby.right(180)
    window.exitonclick()
draw()