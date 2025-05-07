import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()
x = np.linspace(0, 4 * np.pi, 100)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))  # Shift wave to the right
    return line,


ani = animation.FuncAnimation(fig, animate, interval=50)

plt.title("Simple Sine Wave Animation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
