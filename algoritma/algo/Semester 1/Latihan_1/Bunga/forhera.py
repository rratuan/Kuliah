import turtle

turtle.title("FOR YOU MY HERA")
turtle.setup(1.0, 1.0)

t = turtle.Turtle()

t.speed(0)

turtle.Screen().bgcolor("#282D48")

t.up()
t.setpos(0, 100)
t.down()

for i in range(215):
	if i % 2 == 0:
		t.color('#FFB6C1')
	else:
		t.color('#FFB6C1')

	t.circle(180-i/2, 90)
	t.left(90)

	if i % 2 == 0:
		t.color('#FFB6C1')
	else:
		t.color('#FFB6C1')

	t.circle(180-i/2, 90)
	t.left(10)

t.up()
t.setpos(0, -200-10)
t.down()

t.write("HAI HERA", align="center", font=("Verdana", 35, "bold"))

t.up()
t.setpos(0, -245-10)
t.down()

t.write("HAPPY GRADUATION", align="center", font=("Verdana", 23, "bold"))

t.up()
t.setpos(0, -295-10)
t.down()

t.write("PERJALANANMU MASIH PANJANG,SEMANGAT TERUS YAAA", align="center", font=("Verdana", 25, "bold"))

t.hideturtle()

turtle.exitonclick()