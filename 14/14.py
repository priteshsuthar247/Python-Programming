import turtle 
 
def draw_square(side_length): 
    for _ in range(4): 
        turtle.forward(side_length) 
        turtle.right(90) 
 
def draw_hexagon(side_length): 
    for _ in range(6): 
        turtle.forward(side_length) 
        turtle.right(60) 
 
turtle.speed(10) 
 
turtle.penup() 
turtle.goto(-300, 100) 
turtle.pendown() 
draw_square(100) 
 
turtle.penup() 
turtle.goto(200, 100) 
turtle.pendown() 
draw_hexagon(70)

turtle.hideturtle()
 
turtle.done() 