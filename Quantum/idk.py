from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

# Create the 2-qubit circuit
qc = QuantumCircuit(2)
qc.u(2.00576, -0.88174, 1.79827, 0)
qc.u(1.09684, 2.52377, -2.25169, 1)
qc.cz(0, 1)

# Get the final statevector
state = Statevector.from_instruction(qc)
print("Final statevector:\n", state)

# Get probabilities
prob_dict = state.probabilities_dict()

# Sort by bitstring for plotting
bitstrings = sorted(prob_dict.keys())
probs = [prob_dict[b] for b in bitstrings]

# Plot histogram
plt.figure(figsize=(6,4))
plt.bar(bitstrings, probs, color='purple')
plt.xlabel("Bitstring")
plt.ylabel("Probability")
plt.title("Measurement Probabilities after CZ")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
