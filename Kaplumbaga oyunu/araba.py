from turtle import Turtle
import random
import time
renk = ["red","green","yellow","blue","black","purple","pink"]
class Araba:
    def __init__(self):
        self.arac = []
        self.arabahizi = 10

    def arabayap(self):
        sayı=random.randint(1,6)
        if sayı == 1:
            araba = Turtle("square")
            araba.color(random.choice(renk))
            araba.shapesize(1, 2)
            y = random.randint(-280,280)
            araba.penup()
            araba.goto(300,y)
            self.arac.append(araba)

    def git(self):
        for araba in self.arac:
            araba.backward(self.arabahizi)
    def artır(self):
        self.arabahizi += 10


