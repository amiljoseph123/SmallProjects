import turtle
import time

print("Running turtle animation...")

screen = turtle.Screen()
star = turtle.Turtle()

for i in range(36):
    star.forward(100)
    star.right(170)

print("Done drawing.")

time.sleep(5)  # Keeps window alive for 5 seconds

turtle.done()
