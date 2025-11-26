from turtle import *
tracer(0)
k = 20
left(90)
for i in range(7):
    fd(10*k)
    rt(120)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3,'pink')
exitonclick()


