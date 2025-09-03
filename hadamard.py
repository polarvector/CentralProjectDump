import numpy as np
import matplotlib.pyplot as plt

H = np.array([[1, 1], [1, -1]])*(1/np.sqrt(2))
x = np.array([3, 2])

plt.figure(figsize=(6, 6))
plt.scatter(x[0], x[1], c='blue')  # initial point

xs = [x.copy()]
for _ in range(59):
    x = H @ x
    xs.append(x.copy())

xs = np.array(xs)
plt.plot(xs[:, 0], xs[:, 1], marker='o')
plt.title("Trajectory under repeated Hadamard transforms")
plt.grid(True)
plt.axis('equal')
plt.show()
