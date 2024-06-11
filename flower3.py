import turtle

def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

def draw_flower(t, num_petals, radius, angle):
    for _ in range(num_petals):
        draw_petal(t, radius, angle)
        t.left(360 / num_petals)

def draw_center(t, radius):
    t.penup()
    t.goto(0, -radius / 2)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(radius / 2)
    t.end_fill()
    t.penup()
    t.goto(0, 0)
    t.pendown()

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(10)

    # Draw flower petals
    t.color("red")
    t.begin_fill()
    draw_flower(t, 6, 100, 60)
    t.end_fill()

    # Draw flower center
    draw_center(t, 100)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
