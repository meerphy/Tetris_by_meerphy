# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(391, 300)
        Register.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(160, 90, 121, 20))
        self.login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login.setObjectName("login")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 85, 255);")
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(160, 140, 121, 21))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setObjectName("password")
        self.button_enter = QtWidgets.QPushButton(self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(150, 240, 91, 23))
        self.button_enter.setStyleSheet("background-color: #22222e;\n"
"border: 2px sold #f66867;\n"
"color: white;\n"
"border-radius: 9;")
        self.button_enter.setObjectName("button_enter")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 85, 255);")
        self.label.setObjectName("label")
        self.label_up = QtWidgets.QLabel(self.centralwidget)
        self.label_up.setGeometry(QtCore.QRect(10, 10, 371, 41))
        self.label_up.setStyleSheet("color: rgb(170, 85, 255);")
        self.label_up.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_up.setObjectName("label_up")
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(360, 10, 16, 16))
        self.button_exit.setStyleSheet("border-radius: 7px;\n"
"background-color: rgb(231, 76, 60);")
        self.button_exit.setText("")
        self.button_exit.setObjectName("button_exit")
        self.errors_label = QtWidgets.QLabel(self.centralwidget)
        self.errors_label.setGeometry(QtCore.QRect(40, 200, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.errors_label.setFont(font)
        self.errors_label.setStyleSheet("color: rgb(170, 85, 255);")
        self.errors_label.setText("")
        self.errors_label.setAlignment(QtCore.Qt.AlignCenter)
        self.errors_label.setObjectName("errors_label")
        Register.setCentralWidget(self.centralwidget)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "MainWindow"))
        self.label_2.setText(_translate("Register", "Password"))
        self.button_enter.setText(_translate("Register", "Register"))
        self.label.setText(_translate("Register", "Username"))
        self.label_up.setText(_translate("Register", "Registration"))
