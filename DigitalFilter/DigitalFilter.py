from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from matplotlib import pyplot as pp
from math import exp


def int_circuit(m, t):
    x = [0] * m
    impulse_min = int(m * 0.3)
    impulse_max = int(m * 0.6)
    for i in range(impulse_min, impulse_max):
        x[i] = 1
    # X - исходный сигнал (прямоугольный импульс)
    y = [0] * len(x)
    pp.plot(x)
    h = [0] * m
    sh = 0
    for i in range(0, m):
        h[i] = (1 / t) * exp(-i / t)
        sh += h[i]
        if sh >= 1:
            sh -= h[i]
            break
    for i in range(len(h)):
        for j in range(len(h)):
            y[i] += h[j] * x[i - j]
    pp.plot(y)
    pp.show()


def diff_circuit(m, t):
    x = [0] * m
    impulse_min = int(m * 0.3)
    impulse_max = int(m * 0.6)
    for i in range(impulse_min, impulse_max):
        x[i] = 1
    y = [0] * len(x)
    pp.plot(x)
    h = [0] * m
    sh = 0
    for i in range(0, m):
        h[i] = (1 / t) * (1 - exp(-i / t))
        sh += h[i]
        if sh >= 0.9905:
            sh -= h[i]
            break
    for i in range(len(h)):
        for j in range(len(h)):
            y[j] += h[i] * x[j - i]
    pp.plot(y)
    pp.show()


def onClick():
    m = ui.spinBox.value()
    t = ui.doubleSpinBox.value()
    if ui.radioButton.isChecked():
        int_circuit(m, t)
    if ui.radioButton_2.isChecked():
        diff_circuit(m, t)


if __name__ == '__main__':
    app = QApplication([])
    ui = uic.loadUi("form.ui")
    ui.setWindowTitle("Digital Filter")
    ui.show()
    ui.spinBox.setValue(1000)
    ui.doubleSpinBox.setValue(30)
    ui.radioButton.setChecked(True)
    ui.pushButton.clicked.connect(onClick)
    exit(app.exec())
