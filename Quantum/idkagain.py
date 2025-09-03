from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.qasm import load_qasm_file

# Load your QASM file
qc = load_qasm_file("P4_golden_mountain.qasm")

# Simulate using statevector simulator
backend = Aer.get_backend("statevector_simulator")
qobj = assemble(transpile(qc, backend))
result = backend.run(qobj).result()
statevector = result.get_statevector()

# Print only non-zero amplitudes
for i, amp in enumerate(statevector):
    if abs(amp) > 1e-6:
        print(f"|{i:0{qc.num_qubits}b}>: {amp}")
