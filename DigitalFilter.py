from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from matplotlib import pyplot as pp
from math import exp


def IntCircuit (M, t):
    X = [0] * M
    impulseMin = int(M * 0.3)
    impulseMax = int(M * 0.6)
    for i in range (impulseMin, impulseMax):
        X[i] = 1
    # X - исходный сигнал (прямоугольный импульс)
    Y = [0] * len(X)
    pp.plot(X)
    H = [0] * M
    SH = 0
    for i in range (0, M):
        H[i] = (1 / t) * exp(-i / t)
        SH += H[i]
        if SH >= 1:
            SH -= H[i]
            break
    for i in range (len(H)):
        for j in range (len(H)):
            Y[i] += H[j] * X[i - j]
    pp.plot(Y)
    pp.show()


def DiffCircuit (M, t):
    X = [0] * M
    impulseMin = int(M * 0.3)
    impulseMax = int(M * 0.6)
    for i in range (impulseMin, impulseMax):
        X[i] = 1
    Y = [0] * len(X)
    pp.plot(X)
    H = [0] * M
    SH = 0
    for i in range (0, M):
        H[i] = (1 / t) * (1 - exp(-i / t))
        SH += H[i]
        if SH >= 0.9905:
            SH -= H [i]
            break
    for i in range(len(H)):
        for j in range(len(H)):
            Y[j] += H[i] * X[j - i]
    pp.plot(Y)
    pp.show()


def onClick():
    M = ui.spinBox.value()
    t = ui.doubleSpinBox.value()
    if (ui.radioButton.isChecked()):
        IntCircuit (M, t)
    if (ui.radioButton_2.isChecked()):
        DiffCircuit (M, t)


if __name__ == '__main__':
    app = QApplication([])
    ui = uic.loadUi("form.ui")
    ui.setWindowTitle("DigFil")
    ui.show()
    ui.spinBox.setValue(1000)
    ui.doubleSpinBox.setValue(30)
    ui.radioButton.setChecked(True)
    ui.pushButton.clicked.connect(onClick)
    exit(app.exec())
