# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(533, 451)
        self.gridLayout = QtWidgets.QGridLayout(Widget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(569, 78, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBox = QtWidgets.QSpinBox(Widget)
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Widget)
        self.doubleSpinBox.setMinimum(0.01)
        self.doubleSpinBox.setMaximum(200.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.radioButton = QtWidgets.QRadioButton(Widget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(Widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addLayout(self.verticalLayout_2, 4, 0, 1, 3)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "Количество отсчетов:"))
        self.label_2.setText(_translate("Widget", "Постоянная времени цепи:"))
        self.label_3.setText(_translate("Widget", "Тип цепи:"))
        self.radioButton.setText(_translate("Widget", "Интегрирующая цепь"))
        self.radioButton_2.setText(_translate("Widget", "Дифференцирующая цепь"))
        self.pushButton.setText(_translate("Widget", "Построить"))
