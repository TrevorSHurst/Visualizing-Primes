import math, turtle, time

#Determine if the passed through number is prime
def isprime(x):
    for i in range(2,math.floor(1+x**.5)):
        if x % i == 0:
            return False
    return True

#Setup the canvas
canvas = turtle.Screen()
w,h = (800,800)
canvas.setup(w,h)
#Increase speed by turning tracer off
turtle.tracer(0,0)

#scf = Scale factor
scf = 1
turtle.pensize(scf)

#Moving to top left
#pu and pd ensure there is no line from the center
#to the top left
turtle.pu()
turtle.goto(-400,400)
turtle.pd()
turtle.ht()

#start a timer that updates the screen
st = time.time()

# Ensure the turtle stays on the screen
for i in range(math.floor(w*h/scf)):
    #sets the color of the turtle if the current number is prime
    turtle.color('red' if isprime(i) else 'black')
    turtle.forward(scf)
    #red = prime, black = composite

    #Moves the turtle back to the left after hitting the right wall
    if turtle.xcor() > 400:
        turtle.pu()
        turtle.goto(-399,turtle.ycor()-1)
        turtle.pd()

    #updates our view of the turtle's progress
    if time.time() - st > 2:
        turtle.update()
        st = time.time()
#lets the user observe the completed convas
input('Done')
