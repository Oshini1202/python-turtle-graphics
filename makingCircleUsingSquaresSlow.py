import turtle

my_turtle = turtle.Turtle()
def square():
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(15)
    
for i in range(28):
    square()
