from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.ymove = 10
        self.xmove = 10
        self.speedy = 0.1
    def move(self):
        new_x = self.xcor()+self.xmove
        new_y = self.ycor()+self.ymove
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.ymove *= -1
        self.speedy *= 0.9
    def bounce_x(self):
        self.xmove *= -1
        self.speedy *= 0.9
    def reset_ball(self):
        self.goto(0, 0)
        self.speedy = 0.1
        self.bounce_x()
