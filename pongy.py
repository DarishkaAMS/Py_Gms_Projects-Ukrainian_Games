import turtle as t

window = t.Screen()
window.title("Pong by @DarishkaAMS")
window.bgcolor("black")
window.setup(width=800, height=600)
# prevent window from updating
window.tracer(0)

# Paddle A - Yellow Turtle
paddle_a = t.Turtle()
paddle_a.speed(0)
paddle_a.shape("turtle")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B - Blue Square
paddle_a = t.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(350, 0)

# Ball

# Main Game Loop
while True:
    window.update()