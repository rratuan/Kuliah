from tkinter.ttk import Style
from turtle import *
from colorsys import *

hue = 0.8

bgcolor("black")
speed(0)

for i in range(264):
    col =hsv_to_rgb(hue, 1, 1)
    hue += 0.0005
    color(col,col)
    begin_fill()
    circle(240 - i, 90)
    lt(90)
    circle(240 - i, 90)
    lt(10)
    end_fill()
    
t.up()
t.setpos(0, -200-10)
t.down()

t.write("HAI HERA", align="center", font=("Verdana", 35, "bold"))

t.up()
t.setpos(0, -245-10)
t.down()

t.write("HAPPY GRADUATION", align="center", font=("Verdana", 28, "bold"))

t.up()
t.setpos(0, -295-10)
t.down()

t.write("PERJALANANMU MASIH PANJANG,SEMANGAT TERUS YAAA", align="center", font=("Verdana", 30, "bold"))

t.hideturtle()

turtle.exitonclick()
done()