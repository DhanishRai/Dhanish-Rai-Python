import turtle

# Setup screen
win = turtle.Screen()
win.title("Moving Ball Example")
win.bgcolor("black")
win.setup(width=600, height=600)

# Create ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()  # so it doesn't draw lines
ball.speed(0) # instant movement

# Move functions
def move_up():
    y = ball.ycor()
    ball.sety(y + 20)

def move_down():
    y = ball.ycor()
    ball.sety(y - 20)

def move_left():
    x = ball.xcor()
    ball.setx(x - 20)

def move_right():
    x = ball.xcor()
    ball.setx(x + 20)

# Keyboard bindings
win.listen()
win.onkeypress(move_up, "Up")
win.onkeypress(move_down, "Down")
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")

# Keep the window open
win.mainloop()