import turtle
t =  turtle.Pen()
t.pencolor("green,red,orange")
for x in range(250):
    t.forward(x*x/2)
    t.left(100)
