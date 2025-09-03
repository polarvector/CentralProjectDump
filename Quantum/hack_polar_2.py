from qiskit import QuantumCircuit
import bluequbit
import numpy as np

qc = QuantumCircuit.from_qasm_file("P4_golden_mountain.qasm")
qc.measure_all()

bq = bluequbit.init("MRByT4s0TPkXWWuPkAdUfKydf9DrnDhP")

bq.estimate(qc)  # Optional but gives resource usage info

options = {
    "mps_bond_dimension": 200,  # Adjust depending on success
}

result = bq.run(qc, device="mps.cpu", options=options)
counts = result.get_counts()

peak_bitstring = max(counts, key=counts.get)
print("Peak bitstring:", peak_bitstring)
