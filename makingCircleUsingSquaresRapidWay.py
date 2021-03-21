import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
def makingSquare(lenght,angle):
    for i in range(4):
        my_turtle.forward(lenght)
        my_turtle.right(angle)
    
for i in range(150):
    makingSquare(100,90)
    my_turtle.right(11)
    
