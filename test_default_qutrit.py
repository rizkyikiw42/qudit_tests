import pennylane as qml
from pennylane import numpy as np

from pennylane.devices import DefaultQutrit
from pennylane.ops.qutrit import QutritUnitary


U = np.array([[0, 1, 0],
              [0, 0, 1],
              [1, 0, 0]])
# U = np.multiply(1 / np.sqrt(2), U)


# dev = DefaultQutrit(wires=1)
# op = QutritUnitary(U, wires=0)
# dev.apply([op])

# print(dev.probability(wires=0))

dev = qml.device('default.qutrit', wires=1)

@qml.qnode(dev)
def test(iters):
    for _ in range(iters):
        qml.QutritUnitary(U, wires=0)

    return qml.probs(wires=0)


for i in range(4):
    print(test(i))
