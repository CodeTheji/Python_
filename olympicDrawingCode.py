Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.penup()
>>> turtle.pensize(3)
>>> turtle.goto(-200, 50)
>>> turtle.pendown()
>>> turle.begin_fill()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    turle.begin_fill()
NameError: name 'turle' is not defined
>>> turtle.begin_fill()
>>> turtle.color("black")
>>> turtle.circle(40)
>>> 
>>> turtle.penup()
>>> turtle.goto(-100, -50)
>>> turtle.undo()
>>> turtle.goto(-180, -40)
>>> turtle.undo()
>>> turtle.goto(-200, -40)
>>> turtle.undo()
>>> turtle.goto(-190, -50)
>>> turtle.pendown()
>>> turtle.begin_fill()
>>> turtle.color("red")
>>> turtle.circle(40)
>>> turtle.undo()
>>> turtle.undo()
>>> turtle.undo()
>>> turtle.undo()
>>> turtle.undo()
>>> turtle.goto(-150, 0)
>>> turtle.pendown()
>>> turtle.begin_fill()
>>> turtle.color("red")
>>> turtle.circle(40)
>>> 
>>> turtle.penup()
>>> turtle.goto(-100, 50)
>>> turtle.pendown()
>>> turtle.begin_fill()
>>> turtle.color("green")
>>> turtle.circle(40)
>>> turtle.penup()
>>> turtle.goto(-50, 0)
>>> turtle.pendown()
>>> turtle.begin_fill()
>>> turtle.color("blue")
>>> turtle.circle(40)
>>> turtle.penup()
>>> turtle.goto(0, 50)
>>> turtle.pendown()
>>> turtle.begin_fill()
>>> turtle.color("gold")
>>> turtle.circle(40)
>>> 