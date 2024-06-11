import turtle

def draw_petal(t):
    for _ in range(2):
        t.circle(100, 60)
        t.left(120)
        t.circle(100, 60)
        t.left(120)

def draw_flower():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("red")
    t.speed(10)

    for _ in range(6):
        draw_petal(t)
        t.right(60)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_flower()
