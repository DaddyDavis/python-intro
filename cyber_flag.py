import turtle
import random

# 1. Setup the "Cyber Space"
screen = turtle.Screen()
screen.title("Austin's Cyber-Jolly Roger")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# 2. Create the "Hacker" Pen
pen = turtle.Turtle()
pen.speed(0)  # Maximum speed
pen.hideturtle()
pen.color("#00FF00")  # Matrix Green
pen.width(3)

# 3. Draw the "Digital Crossbones" (Binary Streams)
def draw_binary_stream(x, y, length, angle):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(angle)
    pen.pendown()
    for _ in range(15):
        # Draw random 1s and 0s instead of solid bones
        pen.write(random.choice(["1", "0"]), font=("Courier", 14, "bold"))
        pen.forward(length / 10)

# Draw the X shape
draw_binary_stream(-100, -100, 200, 45)
draw_binary_stream(100, -100, 200, 135)

# 4. Draw the "Skull" (Circuit Node)
pen.penup()
pen.goto(0, -40) # Center the skull
pen.pendown()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(60) # Main skull shape
pen.end_fill()

# 5. Draw "Cyber Eyes"
def draw_eye(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("red")
    pen.dot(20) # Glowing red eyes
    pen.color("#00FF00")

draw_eye(-25, 10)
draw_eye(25, 10)

# 6. The Text Label
pen.penup()
pen.goto(0, -150)
pen.color("white")
pen.write("DEAD MEN TELL NO TALES", align="center", font=("Courier", 18, "bold"))
pen.goto(0, -180)
pen.color("#00FF00")
pen.write("SYSTEM_OVERRIDE_INITIATED", align="center", font=("Courier", 12, "italic"))

# Keep window open
screen.mainloop()