import numpy as np
import matplotlib.pyplot as plt

def calculate_transformer_params(Vin_min, Vout, fs, Bmax, Pout, eta):
    # Constants
    mu_0 = 4 * np.pi * 1e-7

    # Estimate maximum duty cycle (Dmax)
    Dmax = Vout / (Vin_min + Vout)

    # Load current (Iout)
    Iout = Pout / Vout

    # Primary Turns (Np)
    Np = int(Vin_min / (4 * fs * Bmax * 1e-4))  # Example scaling for Ae (100 mm^2)

    # Core Area (Ae)
    Ae = (Vin_min * 1e4) / (4 * fs * Bmax * Np)

    # Secondary Turns (Ns)
    Ns = int(Np * Vout / Vin_min)

    # Primary Inductance (Lp)
    Lp = (Vin_min * Dmax) / (Iout * fs)

    # Air Gap (lg)
    lg = (mu_0 * Np**2 * Ae) / Lp

    return Np, Ns, Ae, lg

def visualize_transformer(Ae):
    # Standard transformer core comparison
    standard_Ae = 1e-4  # Example standard core area in m^2

    # Toroidal core visualization (relative scale)
    fig, ax = plt.subplots()

    # Draw standard core
    standard_circle = plt.Circle((0.3, 0.5), np.sqrt(standard_Ae / np.pi), color='blue', alpha=0.5, label='Standard Core')
    ax.add_artist(standard_circle)

    # Draw calculated core
    calculated_circle = plt.Circle((0.7, 0.5), np.sqrt(Ae / np.pi), color='red', alpha=0.5, label='Calculated Core')
    ax.add_artist(calculated_circle)

    # Set limits and aspect ratio
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')

    # Add legend and labels
    plt.legend()
    plt.title("Transformer Core Size Comparison")
    plt.xlabel("Relative X")
    plt.ylabel("Relative Y")

    # Show plot
    plt.show()

def main():
    # Input parameters
    Vin_min = float(input("Enter minimum input voltage (V): "))
    Vout = float(input("Enter output voltage (V): "))
    fs = float(input("Enter switching frequency (Hz): "))
    Bmax = float(input("Enter maximum flux density (T): "))
    Pout = float(input("Enter output power (W): "))
    eta = float(input("Enter efficiency (0-1): "))

    # Calculate parameters
    Np, Ns, Ae, lg = calculate_transformer_params(Vin_min, Vout, fs, Bmax, Pout, eta)

    # Print results
    print(f"Primary Turns (Np): {Np}")
    print(f"Secondary Turns (Ns): {Ns}")
    print(f"Core Area (Ae): {Ae:.6f} m^2")
    print(f"Air Gap (lg): {lg:.6f} m")

    # Visualize core
    visualize_transformer(Ae)

if __name__ == "__main__":
    main()
