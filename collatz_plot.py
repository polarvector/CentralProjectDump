import numpy as np
import time
import matplotlib.pyplot as plt
from collatz import collatz

plt.figure()

for i in range(204, 270):
    collatz(i)
    plt.draw()
    plt.pause(0.05) # plot in real-time
