import turtle as t
import winsound

window = t.Screen()
window.title("Pong by @DarishkaAMS")
window.bgcolor("black")
window.setup(width=800, height=600)
# prevent window from updating
window.tracer(0)

# Score
score_yellow = 0
score_blue = 0

# Paddle A - yellow square
paddle_a = t.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B - blue square
paddle_b = t.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("turtle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25

# Pen
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player Yellow: 0  Player Blue: 0", align="center", font=("Courier", 18, "normal"))


# Moving
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("catmeow.mp3", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_yellow += 1
        winsound.PlaySound("horse.mp3", winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"Player Yellow: {score_yellow}  Player Blue: {score_blue}", align="center",
                  font=("Courier", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_blue += 1
        winsound.PlaySound("horse.mp3", winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"Player Yellow: {score_yellow}  Player Blue: {score_blue}", align="center",
                  font=("Courier", 18, "normal"))

    # Paddle and ball collision
    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

