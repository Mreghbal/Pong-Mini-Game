# Importing Part
import turtle, winsound

# Inputs part
player_a = input ('Enter the Name of Player A: ')
player_a_up = input ('Player A, Please Select Your Key from Keyboard for Moving up with Your Paddle: ')
player_a_down = input ('Player A, Please Select Your Key from Keyboard for Moving down with Your Paddle: ')
player_b = input ('Enter the Name of Player B: ')
player_b_up = input ('Player B, Please Select Your Key from Keyboard for Moving up with Your Paddle: ')
player_b_down = input ('Player B, Please Select Your Key from Keyboard for Moving down with Your Paddle: ')
wn_color = input ('What is the Screen Color? Type here ')
ball_color = input ('What is the Ball Color? Type here ')
paddle_a_color = input ('What is the Paddle A Color? Type here ')
paddle_b_color = input ('What is the Paddle B Color? Type here ')
score_color = input ('What is the Scores Screen Color? Type here ')
center_color = input ('What is the Center Color? Type here ')

# Screen Part
wn = turtle.Screen()
wn.title(player_a.upper() + '    VS    ' + player_b.upper() + '                This Race arranged by ***github.com/MrEghbal***')
wn.setup(width=800, height=600)
wn.bgcolor(wn_color)
wn.tracer(0)

# Game Elements Part (Paddles & Ball & Scoreboard & Center)
# Center
center_tour = turtle.Turtle()
center_tour.pensize(5)
center_tour.speed(10)
center_tour.color('white')
center_tour.goto(0, 300)
center_tour.right(90)
center_tour.forward(600)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.color(paddle_a_color)
paddle_a.speed(0)
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(5,1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape('square')
paddle_b.color(paddle_b_color)
paddle_b.speed(0)
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(5,1)

# Ball
ball = turtle.Turtle()
ball.shape('square')
ball.color(ball_color)
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Scoreboard
score = turtle.Turtle()
score.speed(0)
score.color(score_color)
score.penup()
score.goto(-200, 260)
score.write("Player A: 0\nPlayer B: 0", align = 'center', font = ('Arial', 10, 'normal'))
score.hideturtle()

# Paddles Movement Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)

# Keyboard Shortcuts
wn.listen()
wn.onkeypress(paddle_a_up, player_a_up)
wn.onkeypress(paddle_a_down, player_a_down)
wn.onkeypress(paddle_b_up, player_b_up)
wn.onkeypress(paddle_b_down, player_b_down)

# Initial Scores
score_a = 0
score_b = 0

# Main Game Loop Here
while True:
    wn.update()

    # Moving Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Border Updating
    if ball.xcor() > 390:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("Player A: {}\nPlayer B: {}".format(score_a, score_b), align='center', font=('Arial', 10, 'normal'))

    if ball.xcor() < -390:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("Player A: {}\nPlayer B: {}".format(score_a, score_b), align='center', font=('Arial', 10, 'normal'))

    # Paddle & Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
        ball.setx(-340)
        ball.dx *= -1