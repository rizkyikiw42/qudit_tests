import math

import pytest
import pennylane as qml
from pennylane import numpy as np, DeviceError

# from pennylane.devices.default_qutrit import DefaultQutrit
from pennylane.wires import Wires, WireError
from tests.devices.test_default_qubit import TestInverseDecomposition

OMEGA = np.exp(2 * np.pi * 1j / 3)


U_thadamard_01 = np.multiply(
    1 / np.sqrt(2),
    np.array(
        [[1, 1, 0], [1, -1, 0], [0, 0, np.sqrt(2)]],
    ),
)

U_tswap = np.array(
    [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ],
    dtype=np.complex128,
)


# dev = qml.device("default.qutrit", wires=2)

dev2 = qml.device("default.qubit", wires=4, shots=[10, 5])


# @qml.qnode(dev)
# def test_qnode():
#     qml.TShift(wires=0)
#     qml.TShift(wires=1)
#     qml.TAdd(wires=[0, 1])

#     return qml.state()


@qml.qnode(dev2)
def test1():
    qml.PauliX(wires=0)
    qml.PauliY(wires=1)
    qml.CNOT(wires=[1, 2])
    return qml.sample(counts=True)


@qml.qnode(dev2)
def test2():
    qml.PauliX(wires=0)
    qml.Hadamard(wires=1)
    qml.CNOT(wires=[1, 2])
    return qml.sample()


if __name__ == "__main__":
    print(test1())

    print(test2())
