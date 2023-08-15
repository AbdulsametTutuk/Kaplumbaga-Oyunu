from turtle import Turtle
class Kaplumbaga(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.left(90)
    def hareket(self):
        self.forward(10)