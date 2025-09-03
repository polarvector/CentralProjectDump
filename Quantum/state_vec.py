from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

# Define the quantum circuit
qc = QuantumCircuit(4)

# Apply the gates as per the QASM code
qc.x(0)
qc.x(3)
qc.ry(0.8 * np.pi, 0)
qc.ry(0.8 * np.pi, 1)
qc.ry(0.8 * np.pi, 2)
qc.ry(0.8 * np.pi, 3)

# Simulate the statevector
state = Statevector.from_instruction(qc)

# Plot the Bloch spheres
plot_bloch_multivector(state)
plt.show()

# Optional: print the statevector
print(state)
