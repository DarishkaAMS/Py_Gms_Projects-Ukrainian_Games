import turtle as t

window = t.Screen()
window.title("Pong by @DarishkaAMS")
window.bgcolor("black")
window.setup(width=800, height=600)
# prevent window from updating
window.tracer(0)

# Paddle A
paddle_a = t.Turtle()
paddle_a.speed(0)
paddle_a.shape("turtle")
paddle_a.color("yellow")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

# Ball

# Main Game Loop
while True:
    window.update()