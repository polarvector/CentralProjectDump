import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2]).reshape(2, 1)  # Reshape x to be a column vector
A = np.matrix([[0.7, 0.3], [0.2, 0.9]])

plt.figure()

for i in range(90):  # Specify the range, for example, 1 to 4
    y = (A**i) * x  # Matrix multiplication
    plt.scatter(y[0, 0], y[1, 0], label=f"A^{i} * x")  # Plotting the components of the result

plt.show()
