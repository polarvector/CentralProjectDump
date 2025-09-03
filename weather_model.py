import numpy as np
import matplotlib.pyplot as plt

# Constants
nx, ny = 50, 50  # Grid size
nt = 500  # Number of time steps
dx = 2.0 / (nx - 1)
dy = 2.0 / (ny - 1)
dt = 0.001  # Time step

# Physical constants
rho = 1.0  # Air density
nu = 0.1  # Kinematic viscosity (diffusivity of velocity)
f = 1e-4  # Coriolis parameter
g = 9.81  # Gravitational constant
R = 287.05  # Gas constant for dry air

# Initial conditions
u = np.zeros((ny, nx))  # Velocity in x (East-West) direction
v = np.zeros((ny, nx))  # Velocity in y (North-South) direction
p = np.ones((ny, nx))  # Pressure
T = np.ones((ny, nx))  # Temperature

# Discretized Navier-Stokes and continuity equations
def compute_velocity(u, v, p, rho, nu, dx, dy, dt, f):
    un = u.copy()
    vn = v.copy()
    
    u[1:-1, 1:-1] = (un[1:-1, 1:-1] - 
                     dt / dx * un[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[1:-1, :-2]) -
                     dt / dy * vn[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[:-2, 1:-1]) -
                     dt / (2 * rho * dx) * (p[1:-1, 2:] - p[1:-1, :-2]) + 
                     nu * (dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, :-2]) +
                           dt / dy**2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[:-2, 1:-1])) + 
                     dt * f * vn[1:-1, 1:-1])
    
    v[1:-1, 1:-1] = (vn[1:-1, 1:-1] -
                     dt / dx * un[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[1:-1, :-2]) -
                     dt / dy * vn[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[:-2, 1:-1]) -
                     dt / (2 * rho * dy) * (p[2:, 1:-1] - p[:-2, 1:-1]) +
                     nu * (dt / dx**2 * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, :-2]) +
                           dt / dy**2 * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[:-2, 1:-1])) -
                     dt * f * un[1:-1, 1:-1])
    
    return u, v

def compute_pressure(p, u, v, rho, dx, dy):
    pn = p.copy()
    b = rho * ((u[1:-1, 2:] - u[1:-1, :-2]) / (2 * dx) + (v[2:, 1:-1] - v[:-2, 1:-1]) / (2 * dy))
    
    for q in range(50):
        pn[1:-1, 1:-1] = (((pn[1:-1, 2:] + pn[1:-1, :-2]) * dy**2 +
                          (pn[2:, 1:-1] + pn[:-2, 1:-1]) * dx**2) /
                         (2 * (dx**2 + dy**2)) -
                         dx**2 * dy**2 / (2 * (dx**2 + dy**2)) * b)
    
    return pn

def compute_temperature(T, u, v, dx, dy, dt):
    Tn = T.copy()
    T[1:-1, 1:-1] = (Tn[1:-1, 1:-1] -
                     dt / dx * u[1:-1, 1:-1] * (Tn[1:-1, 1:-1] - Tn[1:-1, :-2]) -
                     dt / dy * v[1:-1, 1:-1] * (Tn[1:-1, 1:-1] - Tn[:-2, 1:-1]))
    
    return T

# Time-stepping
for n in range(nt):
    u, v = compute_velocity(u, v, p, rho, nu, dx, dy, dt, f)
    p = compute_pressure(p, u, v, rho, dx, dy)
    T = compute_temperature(T, u, v, dx, dy, dt)

    # Visualization every 100 steps
    if n % 100 == 0:
        plt.contourf(p, alpha=0.5, cmap='coolwarm')
        plt.colorbar()
        plt.quiver(u, v)
        plt.title(f'Time step: {n}')
        plt.show()
