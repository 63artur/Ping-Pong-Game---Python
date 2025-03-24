from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
ball = Ball()
score = Score()
l_paddle = Paddle((350,0))
r_paddle = Paddle((-350,0))
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.speedy)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(l_paddle) < 50 and ball.xcor() > 320 or (ball.distance(r_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_point()
screen.exitonclick()