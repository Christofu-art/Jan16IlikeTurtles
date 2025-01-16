
import turtle
screen = turtle.Screen()
screen.bgcolor("dark blue") 
donatello = turtle.Turtle() #donatello is mo's favorite TMNT

def hexagon(x, y):
    donatello.pensize(5)
    donatello.pencolor("orange")
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    for i in range(6): 
        donatello.forward(50) 
        donatello.right(60)

def star(x, y):
    donatello.pensize(5)
    donatello.pencolor("yellow")
    donatello.fillcolor("yellow")
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    for i in range(5): 
        donatello.forward(90) 
        donatello.right(145)


def triangle(tx, ty):
    donatello.pensize(5)
    donatello.pencolor("blue")
    donatello.penup()
    donatello.goto(tx, ty)
    donatello.pendown()
    for i in range(3): 
        donatello.forward(80) 
        donatello.right(120)

def square(x, y):
    donatello.pensize(5)
    donatello.pencolor("red")
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    for i in range(4): 
        donatello.forward(50) 
        donatello.right(90)

def circle(cx, cy, radius):
    donatello.pensize(8)
    donatello.pencolor("light blue")
    donatello.fillcolor("white")
    donatello.penup()
    donatello.goto(cx, cy)
    donatello.pendown()
    donatello.begin_fill()
    donatello.circle(radius)
    donatello.end_fill()

    


#call functions
square(30, 40)
square(10, 50)
square (100, 200)
circle(-200, 200, 80)
triangle(200, 60)
hexagon(60, 10)
star(-30, 80)

turtle.done() 
