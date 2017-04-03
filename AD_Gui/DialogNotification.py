# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DialogNotification.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogNotification(object):
    def setupUi(self, DialogNotification):
        DialogNotification.setObjectName("DialogNotification")
        DialogNotification.resize(208, 114)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogNotification.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(DialogNotification)
        self.gridLayout.setObjectName("gridLayout")
        self.labelText = QtWidgets.QLabel(DialogNotification)
        self.labelText.setAlignment(QtCore.Qt.AlignCenter)
        self.labelText.setObjectName("labelText")
        self.gridLayout.addWidget(self.labelText, 0, 0, 1, 1)
        self.pushButtonOK = QtWidgets.QPushButton(DialogNotification)
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.gridLayout.addWidget(self.pushButtonOK, 1, 0, 1, 1)

        self.retranslateUi(DialogNotification)
        QtCore.QMetaObject.connectSlotsByName(DialogNotification)

    def retranslateUi(self, DialogNotification):
        _translate = QtCore.QCoreApplication.translate
        DialogNotification.setWindowTitle(_translate("DialogNotification", "DialogNotification"))
        self.labelText.setText(_translate("DialogNotification", "Notification text here"))
        self.pushButtonOK.setText(_translate("DialogNotification", "OK"))

