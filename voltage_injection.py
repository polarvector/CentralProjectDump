import matplotlib.pyplot as plt
import numpy as np
from operator import add
from matplotlib.widgets import Slider

d0 = 1000
d1 = 17000
d2 = 21000
d3 = 30000
d4 = 48000
d5 = 78000
d6 = 23000
d7 = 31000
d8 = 28000
d9 = 7000
d10 = 19000

# Initial value for the speed of light (c)
c = 3e8
c = 0.5 * c

dist = [0, d1, d2 + d3 + d4, d1 + d2, d3 + d4, d3, d1 + d2 + d3, d4 + d5, d1 + d2 + d3 + d5, d4 + d5 + d6, d1 + d2 + d3 + d5 + d6, d4 + d5 + d7, d1 + d2 + d3 + d5 + d7, d4 + d5 + d8, d1 + d2 + d3 + d5 + d8, d1 + d2 + d9, d4 + d3 + d9, d1 + d10, d4 + d3 + d2 + d10]
time = [1e6 * d / c for d in dist]

fig, ax = plt.subplots()
ax.stem(time, np.ones(len(time)), basefmt=" ", linefmt="b-", markerfmt="bo")
ax.set_xlabel('Time [microseconds]')
ax.set_ylabel('S/H circuit state')

# Create a horizontal slider for the speed of light
ax_c = fig.add_axes([0.25, 0.02, 0.65, 0.03])
slider_c = Slider(ax_c, 'Speed of Light (c)', valmin=1e8, valmax=3e8, valinit=c)

def update(val):
    # Update the speed of light value
    c_new = slider_c.val
    time_new = [1e6 * d / c_new for d in dist]
    ax.lines[0].set_xdata(time_new)
    fig.canvas.draw_idle()

# Register the update function with the slider
slider_c.on_changed(update)

plt.show()
