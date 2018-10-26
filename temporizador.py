import turtle 

wn = turtle.Screen()

wn.title("1999")
wn.bgcolor("lightgreen")
javier = turtle.Turtle()
harry = turtle.Turtle()
harry.color("BLUE")

def j1(): javier.forward(100)
def j2(): javier.left(90)
def j3(): javier.right(90)
def j5(): javier.forward(100)
def j4(): wn.bye()

def h1(): harry.forward(100)
def h2(): harry.left(90)
def h3(): harry.right(90)
def h5(): harry.forward(100)
def h4(): wn.bye()

wn.onkey(j1, "Up")
wn.onkey(j2, "Left")
wn.onkey(j3, "Right")
wn.onkey(j5, "Down")
wn.onkey(j4, "q")

wn.onkey(h1, "w")
wn.onkey(h2, "a")
wn.onkey(h3, "d")
wn.onkey(h5, "s")
wn.onkey(h4, "q")

wn.listen()
wn.mainloop()