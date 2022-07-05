# import turtle
# for i in range(60):
#     turtle.color("pink")
#     turtle.circle(100)
#     turtle.home()
#     turtle.left(90)
#     turtle.forward(50)

#     turtle.color("blue")
#     turtle.forward(50)

# turtle.done()
import time
import turtle

for s in range(60):
    turtle.speed(0)
    turtle.penup()
for s in range(60):
    for i in range(13):
        turtle.forward(100)
        turtle.stamp()
        turtle.home()
        turtle.right(30 * i)

    turtle.home()
    turtle.right(6 * s)
    turtle.pendown()
    turtle.forward(100)
    time.sleep(0.4)
    turtle.clear()

turtle.done