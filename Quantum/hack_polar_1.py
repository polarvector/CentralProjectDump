from qiskit import QuantumCircuit
import bluequbit
import numpy as np

qc = QuantumCircuit.from_qasm_file("P4_golden_mountain.qasm")
qc.measure_all()

bq = bluequbit.init("MRByT4s0TPkXWWuPkAdUfKydf9DrnDhP")
bq.estimate(qc)
#result = bq.run(qc, device='cpu')
result = bq.run(qc, device='quantum',shots=1)
counts = result.get_counts()

peak_bitstring = max(counts, key=counts.get)

print("Peak bitstring:", peak_bitstring)

'''import matplotlib.pyplot as plt

Convert counts to probabilities
total_shots = sum(counts.values())
bitstrings = list(counts.keys())
probabilities = [counts[bs] / total_shots for bs in bitstrings]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(bitstrings, probabilities, color='skyblue')
plt.xlabel("Bitstrings")
plt.ylabel("Probability")
plt.title("Measured Bitstring Probabilities")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
'''
