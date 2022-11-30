# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playing_scene.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Play(object):
    def setupUi(self, Play):
        Play.setObjectName("Play")
        Play.resize(600, 700)
        Play.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(Play)
        self.centralwidget.setObjectName("centralwidget")
        self.nickname = QtWidgets.QLabel(self.centralwidget)
        self.nickname.setGeometry(QtCore.QRect(400, 50, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.nickname.setFont(font)
        self.nickname.setStyleSheet("color: rgb(170, 85, 255);")
        self.nickname.setAlignment(QtCore.Qt.AlignCenter)
        self.nickname.setObjectName("nickname")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 201, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 85, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(410, 280, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(170, 85, 255);")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(400, 490, 161, 51))
        self.play.setStyleSheet("background-color: #22222e;\n"
"border: 20px sold #f66867;\n"
"color: white;\n"
"border-radius: 20;\n"
"")
        self.play.setObjectName("play")
        self.buttonGroup_playing = QtWidgets.QButtonGroup(Play)
        self.buttonGroup_playing.setObjectName("buttonGroup_playing")
        self.buttonGroup_playing.addButton(self.play)
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(400, 560, 161, 51))
        self.pause.setStyleSheet("background-color: #22222e;\n"
"border:  20px sold #f66867;\n"
"color: white;\n"
"border-radius: 20;\n"
"")
        self.pause.setObjectName("pause")
        self.buttonGroup_playing.addButton(self.pause)
        self.quit_to_menu = QtWidgets.QPushButton(self.centralwidget)
        self.quit_to_menu.setGeometry(QtCore.QRect(400, 630, 161, 51))
        self.quit_to_menu.setStyleSheet("background-color: #22222e;\n"
"border: 20px sold #f66867;\n"
"color: white;\n"
"border-radius: 20;\n"
"")
        self.quit_to_menu.setObjectName("quit_to_menu")
        self.buttonGroup_playing.addButton(self.quit_to_menu)
        self.complexity = QtWidgets.QSpinBox(self.centralwidget)
        self.complexity.setGeometry(QtCore.QRect(430, 390, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.complexity.setFont(font)
        self.complexity.setStyleSheet("color: rgb(170, 85, 255);")
        self.complexity.setAlignment(QtCore.Qt.AlignCenter)
        self.complexity.setMinimum(1)
        self.complexity.setMaximum(3)
        self.complexity.setObjectName("complexity")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 360, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setStyleSheet("color: rgb(170, 85, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_up1 = QtWidgets.QLabel(self.centralwidget)
        self.label_up1.setGeometry(QtCore.QRect(10, 10, 581, 31))
        self.label_up1.setText("")
        self.label_up1.setObjectName("label_up1")
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(570, 10, 16, 16))
        self.button_exit.setStyleSheet("border-radius: 7px;\n"
"background-color: rgb(231, 76, 60);")
        self.button_exit.setText("")
        self.button_exit.setObjectName("button_exit")
        self.best_score = QtWidgets.QLabel(self.centralwidget)
        self.best_score.setGeometry(QtCore.QRect(410, 310, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.best_score.setFont(font)
        self.best_score.setStyleSheet("color: rgb(170, 85, 255);")
        self.best_score.setAlignment(QtCore.Qt.AlignCenter)
        self.best_score.setObjectName("best_score")
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(410, 220, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.score.setFont(font)
        self.score.setStyleSheet("color: rgb(170, 85, 255);")
        self.score.setAlignment(QtCore.Qt.AlignCenter)
        self.score.setObjectName("score")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 300, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.play_board = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.play_board.setContentsMargins(0, 0, 0, 0)
        self.play_board.setObjectName("play_board")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(420, 80, 131, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.next_plate = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.next_plate.setContentsMargins(0, 0, 0, 0)
        self.next_plate.setObjectName("next_plate")
        self.gameover_label = QtWidgets.QLabel(self.centralwidget)
        self.gameover_label.setGeometry(QtCore.QRect(60, 660, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        self.gameover_label.setFont(font)
        self.gameover_label.setStyleSheet("color: rgb(170, 85, 255);")
        self.gameover_label.setText("")
        self.gameover_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gameover_label.setObjectName("gameover_label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 440, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setStyleSheet("color: rgb(170, 85, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        Play.setCentralWidget(self.centralwidget)

        self.retranslateUi(Play)
        QtCore.QMetaObject.connectSlotsByName(Play)

    def retranslateUi(self, Play):
        _translate = QtCore.QCoreApplication.translate
        Play.setWindowTitle(_translate("Play", "MainWindow"))
        self.nickname.setText(_translate("Play", "NICKNAME из базы дынных"))
        self.label_3.setText(_translate("Play", "SCORE"))
        self.label_1.setText(_translate("Play", "BEST SCORE"))
        self.play.setText(_translate("Play", "Start"))
        self.pause.setText(_translate("Play", "Pause"))
        self.quit_to_menu.setText(_translate("Play", "Exit"))
        self.label_2.setText(_translate("Play", "Сложность игры"))
        self.best_score.setText(_translate("Play", "0"))
        self.score.setText(_translate("Play", "0"))
        self.label_4.setText(_translate("Play", "F1 - управление"))
