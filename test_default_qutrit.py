import pennylane as qml
from pennylane import numpy as np

from pennylane.devices import DefaultQutrit
from pennylane.ops.qutrit import QutritUnitary

OMEGA = np.exp(2 * np.pi * 1j / 3)

U = np.array(
            [[0, 0, 1],
             [1, 0, 0],
             [0, 1, 0]])


# dev = DefaultQutrit(wires=1)
# op = QutritUnitary(U, wires=0)
# dev.apply([op])

# print(dev.probability(wires=0))

dev = qml.device('default.qutrit', wires=3)

@qml.qnode(dev)
def test(iters):
    for _ in range(iters):
        qml.QutritUnitary(U, wires=0)

    return qml.probs(wires=0)


for i in range(4):
    print(test(i))

print("\n")

@qml.qnode(dev)
def test_swap():
    qml.TShift(wires=0)                     # |000>         -> |100>
    qml.adjoint(qml.TShift)(wires=1)        # |100>         -> |120>
    qml.TSWAP(wires=[0, 1])                 # |120>         -> |210>
    qml.TAdd(wires=[0, 1])                  # |210>         -> |200>
    qml.TShift(wires=1)                     # |200>         -> |210>
    qml.TClock(wires=2)                     # |210>         -> |210>
    qml.TClock(wires=1)                     # |210>         -> \omega|210>
    qml.TClock(wires=0)                     # |\omega|210>  -> \omega^3|210>

    return qml.state()

state=test_swap()
print(state)
print(state[21])
print(np.allclose(state[21], OMEGA**3))

# for i in range(5):
#     print(OMEGA**i)
