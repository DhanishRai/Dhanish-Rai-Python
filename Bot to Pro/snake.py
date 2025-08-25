import turtle
import time
import random

delay = 0.1
score = 0

# Screen setup
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=400, height=400)
win.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake body
segments = []

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# Main game loop
while True:
    win.update()

    # Check for collision with border
    if abs(head.xcor()) > 190 or abs(head.ycor()) > 190:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide segments
        for seg in segments:
            seg.goto(1000, 1000)
        segments.clear()
        score = 0

    # Check for collision with food
    if head.distance(food) < 20:
        # Move food to random spot
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)
        food.goto(x, y)

        # Add new segment
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("green")
        new_seg.penup()
        segments.append(new_seg)
        score += 10

    # Move segments
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check for collision with itself
    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for s in segments:
                s.goto(1000, 1000)
            segments.clear()
            score = 0

    time.sleep(delay)