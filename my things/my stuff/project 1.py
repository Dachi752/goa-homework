code = 90345
gues = 0

while gues != code:
    gues = int(input("code plese:"))
if gues < code:
    print("wrong code!")
if gues > code:
    print("wrong code")
if gues == code:
    from turtle import *
speed(1)
color("green")
begin_fill()
width(9)
left(70)
forward(70)
color("red")
right(60)
forward(60)
color("blue")
right(50)
forward(132)
color("green")
left(50)
forward(400)
color("red")
right(45)
forward(45)
color("blue")
width(20)
right(45)
forward(100)
