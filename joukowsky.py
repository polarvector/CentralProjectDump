# To rotate the airfoil by the angle of attack alpha, we need to apply a rotation transformation to the airfoil points after the Joukowsky transform. 
# Let's modify the previous code to include this rotation and then re-visualize the flow.

import numpy as np
import matplotlib.pyplot as plt

# Define parameters
radius = 1.1
offset = 0.1
U_inf = 1.0  # Freestream velocity
alpha = np.radians(20)  # Angle of attack in degrees, converted to radians

# Define the circle in the zeta-plane (circle before transformation)
theta = np.linspace(0, 2 * np.pi, 500)
circle_zeta = radius * np.exp(1j * theta) + offset

# Joukowsky transform function
def joukowsky_transform(z):
    return z + 1 / z

# Velocity field calculation in the zeta plane
def compute_velocity(zeta, U=U_inf, alpha=alpha):
    f_prime = U * np.exp(-1j * alpha)  # Derivative of the complex potential
    dzdzeta = 1 - 1 / (zeta ** 2)  # Derivative of the Joukowsky transform
    velocity = f_prime / dzdzeta
    return velocity

# Calculate velocity on the circle
velocity_zeta = compute_velocity(circle_zeta)

# Calculate the circulation by integrating around the airfoil
dl = radius * np.diff(theta)
circulation = np.sum(velocity_zeta[:-1] * dl * 1j * np.exp(1j * theta[:-1]))

# Apply Joukowsky transform to the circle
airfoil = joukowsky_transform(circle_zeta)

# Rotate the airfoil by the angle of attack alpha
rotation_matrix = np.exp(1j * alpha)
airfoil_rotated = airfoil * rotation_matrix

# Plot the velocity field using streamlines and airfoil shape
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)
zeta_grid = X + 1j * Y

# Calculate the velocity field for the grid
velocity_grid = compute_velocity(zeta_grid)
u = velocity_grid.real
v = -velocity_grid.imag

# Plotting
plt.figure(figsize=(10, 8))
plt.streamplot(X, Y, u, v, density=2, linewidth=1, color='b')

# Plot the rotated airfoil
plt.plot(airfoil_rotated.real, airfoil_rotated.imag, 'r', linewidth=2)

# Set plot limits and labels
plt.title(f'Flow Around Rotated Joukowsky Airfoil (AoA = {np.degrees(alpha)}°)\nCirculation (Gamma) = {circulation.real:.4f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.grid(True)

# Show the plot
plt.show()
