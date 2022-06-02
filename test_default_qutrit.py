import pennylane as qml
from pennylane import numpy as np

from pennylane.devices import DefaultQutrit
from pennylane.ops.qutrit import QutritUnitary


shift = np.array(
            [[0, 0, 1],
             [1, 0, 0],
             [0, 1, 0]])


# dev = DefaultQutrit(wires=1)
# op = QutritUnitary(shift, wires=0)
# dev.apply([op])

# print(dev.probability(wires=0))

dev = qml.device('default.qutrit', wires=2)

@qml.qnode(dev)
def test(iters):
    for _ in range(iters):
        qml.QutritUnitary(shift, wires=0)

    return qml.probs(wires=0)


# for i in range(4):
#     print(test(i))


@qml.qnode(dev)
def test_swap():
    qml.QutritUnitary(shift, wires=0)       # |00> -> |10>
    qml.QutritUnitary(shift.T, wires=1)     # |10> -> |12>
    qml.TSWAP(wires=[0, 1])                 # |12> -> |21>
    qml.TAdd(wires=[0, 1])                  # |21> -> |20>

    return qml.state()

print(test_swap())
