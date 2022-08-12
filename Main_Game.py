from turtle import Screen
from Paddle_Ball_Scoreboard import Paddle, Ball, ScoreBoard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

our_paddle = Paddle(360, 0)
enemy_paddle = Paddle(-370, 0)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(our_paddle.up, "Up")
screen.onkey(our_paddle.down, "Down")
screen.onkey(enemy_paddle.up, "w")
screen.onkey(enemy_paddle.down, "s")


game_is_on = True
while game_is_on:
	screen.update()
	ball.move()
	time.sleep(ball.speed)

	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.collision_walls()

	if ball.distance(our_paddle) < 60 and ball.xcor() > 340:
		ball.collision_paddle()
		ball.speed_up()

	if ball.distance(enemy_paddle) < 60 and ball.xcor() < -340:
		ball.collision_paddle()
		ball.speed_up()

	if ball.xcor() > 380:
		ball.after_score()
		ball.speed_reset()
		scoreboard.increase_left()

	if ball.xcor() < -380:
		ball.after_score()
		ball.speed_reset()
		scoreboard.increase_right()

	if scoreboard.left_score >= 5:
		scoreboard.result("Left Player")
		game_is_on = False

	if scoreboard.right_score >= 5:
		scoreboard.result("Right Player")
		game_is_on = False


screen.exitonclick()