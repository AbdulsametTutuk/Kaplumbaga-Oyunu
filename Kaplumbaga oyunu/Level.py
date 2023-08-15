from turtle import Turtle

class Skor(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.guncelle()
    def guncelle(self):
        self.clear()
        self.write(f"Level :{self.level}", align="left", font=("Courier", 18, "normal"))
    def arttir(self):
        self.level += 1
        self.guncelle()
    def bitti(self):
        self.goto(0,0)
        self.write(f"GAME OVER.",align="center",font=("Courier",18,"normal"))