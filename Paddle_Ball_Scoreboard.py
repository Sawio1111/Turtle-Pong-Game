from turtle import Turtle


class Paddle(Turtle):
	def __init__(self, position_x, position_y):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.penup()
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.goto(position_x, position_y)


	def up(self):
		self.goto(self.xcor(), self.ycor() + 20)
		if self.ycor() > 270:
			self.goto(self.xcor(), 270)

	def down(self):
		self.goto(self.xcor(), self.ycor() - 20)
		if self.ycor() < -270:
			self.goto(self.xcor(), -270)


class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.x = 10
		self.y = 10
		self.speed = 0.05

	def move(self):
		self.goto(self.xcor() + self.x, self.ycor() + self.y)

	def speed_up(self):
		self.speed -= 0.001

	def speed_reset(self):
		self.speed = 0.05

	def collision_walls(self):
		self.y = self.y * -1

	def collision_paddle(self):
		self.x = self.x * -1

	def after_score(self):
		self.goto(0, 0)
		self.collision_walls()



class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.right_score = 0
		self.left_score = 0
		self.goto(0, 250)
		self.color("white")
		self.penup()
		self.hideturtle()
		self.write(f"Score: {self.left_score}    Score: {self.right_score}", False
				   , "center", ("Arial", 30, "normal"))
		self.speed("fastest")

	def increase_right(self):
		self.right_score += 1
		self.clear()
		self.write(f"Score: {self.left_score}    Score: {self.right_score}", False
				   , "center", ("Arial", 30, "normal"))

	def increase_left(self):
		self.left_score += 1
		self.clear()
		self.write(f"Score: {self.left_score}    Score: {self.right_score}", False
				   , "center", ("Arial", 30, "normal"))

	def result(self, player):
		self.goto(0, 0)
		self.clear()
		self.write(f"{player} won game", False
				   , "center", ("Arial", 30, "normal"))

