# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_leaders.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Leaders(object):
    def setupUi(self, Leaders):
        Leaders.setObjectName("Leaders")
        Leaders.resize(600, 700)
        Leaders.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(Leaders)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label_up1 = QtWidgets.QLabel(self.centralwidget)
        self.label_up1.setGeometry(QtCore.QRect(10, 10, 581, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)
        self.label_up1.setFont(font)
        self.label_up1.setStyleSheet("color: rgb(170, 85, 255);")
        self.label_up1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_up1.setObjectName("label_up1")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(430, 610, 121, 41))
        self.back.setStyleSheet("background-color: #22222e;\n"
"border: 20px sold #f66867;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20;\n"
"")
        self.back.setObjectName("back")
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(570, 10, 16, 16))
        self.button_exit.setStyleSheet("border-radius: 7px;\n"
"background-color: rgb(231, 76, 60);")
        self.button_exit.setText("")
        self.button_exit.setObjectName("button_exit")
        self.leaders_table = QtWidgets.QTableWidget(self.centralwidget)
        self.leaders_table.setGeometry(QtCore.QRect(15, 91, 571, 501))
        self.leaders_table.setStyleSheet("border-color: rgb(54, 54, 54);")
        self.leaders_table.setObjectName("leaders_table")
        self.leaders_table.setColumnCount(0)
        self.leaders_table.setRowCount(0)
        self.sort_button = QtWidgets.QPushButton(self.centralwidget)
        self.sort_button.setGeometry(QtCore.QRect(50, 600, 101, 41))
        self.sort_button.setStyleSheet("background-color: #22222e;\n"
"border: 20px sold #f66867;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20;\n"
"")
        self.sort_button.setObjectName("sort_button")
        Leaders.setCentralWidget(self.centralwidget)

        self.retranslateUi(Leaders)
        QtCore.QMetaObject.connectSlotsByName(Leaders)

    def retranslateUi(self, Leaders):
        _translate = QtCore.QCoreApplication.translate
        Leaders.setWindowTitle(_translate("Leaders", "MainWindow"))
        self.label_up1.setText(_translate("Leaders", "??????????????"))
        self.back.setText(_translate("Leaders", "??????????"))
        self.sort_button.setText(_translate("Leaders", "???????????????????????"))
