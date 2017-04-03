# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DialogSuccess.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogSuccess(object):
    def setupUi(self, DialogSuccess):
        DialogSuccess.setObjectName("DialogSuccess")
        DialogSuccess.resize(208, 119)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogSuccess.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(DialogSuccess)
        self.gridLayout.setObjectName("gridLayout")
        self.labelText = QtWidgets.QLabel(DialogSuccess)
        self.labelText.setAlignment(QtCore.Qt.AlignCenter)
        self.labelText.setObjectName("labelText")
        self.gridLayout.addWidget(self.labelText, 0, 0, 1, 2)
        self.pushButtonOK = QtWidgets.QPushButton(DialogSuccess)
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.gridLayout.addWidget(self.pushButtonOK, 1, 0, 1, 1)
        self.pushButtonOpenFile = QtWidgets.QPushButton(DialogSuccess)
        self.pushButtonOpenFile.setObjectName("pushButtonOpenFile")
        self.gridLayout.addWidget(self.pushButtonOpenFile, 1, 1, 1, 1)

        self.retranslateUi(DialogSuccess)
        QtCore.QMetaObject.connectSlotsByName(DialogSuccess)

    def retranslateUi(self, DialogSuccess):
        _translate = QtCore.QCoreApplication.translate
        DialogSuccess.setWindowTitle(_translate("DialogSuccess", "Success"))
        self.labelText.setText(_translate("DialogSuccess", "Notification text here"))
        self.pushButtonOK.setText(_translate("DialogSuccess", "OK"))
        self.pushButtonOpenFile.setText(_translate("DialogSuccess", "Open File"))

