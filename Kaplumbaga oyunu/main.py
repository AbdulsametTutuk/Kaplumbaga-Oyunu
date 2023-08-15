from turtle import Turtle,Screen
import time
from kaplumbaga import Kaplumbaga
from araba import Araba
from Level import Skor

screen = Screen()
screen.setup(600,600)
screen.tracer(0)
screen.listen()
kaplumbaga = Kaplumbaga()
level = Skor()
araba = Araba()
screen.onkey(key="w",fun=kaplumbaga.hareket)
durum = True
while durum:
    time.sleep(0.1)
    screen.update()
    araba.arabayap()
    araba.git()
    if kaplumbaga.ycor() > 280:
        kaplumbaga.goto(0,-280)
        araba.artır()
        level.arttir()
    for arabaa in araba.arac:
        if arabaa.distance(kaplumbaga) < 20:
            level.bitti()
            durum = False




screen.exitonclick()
