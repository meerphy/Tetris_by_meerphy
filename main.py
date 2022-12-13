import sys
import sqlite3
import ctypes

from random import choice
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QHBoxLayout, QLabel, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import QUrl, Qt, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from main_menu import Ui_Menu
from table_leaders import Ui_Leaders
from playing_scene import Ui_Play
from settings_ui import Ui_Settings
from enter_ui import Ui_Enter
from management_ui import Ui_Management
from register_ui import Ui_Register

player_game = QMediaPlayer()
player_main = QMediaPlayer()
playlist_game = QMediaPlaylist()
url = QUrl.fromLocalFile('files/music1.mp3')
playlist_game.addMedia(QMediaContent(url))
playlist_game.setPlaybackMode(QMediaPlaylist.Loop)
playlist_main = QMediaPlaylist()
url = QUrl.fromLocalFile('files/music1.mp3')
playlist_main.addMedia(QMediaContent(url))
playlist_main.setPlaybackMode(QMediaPlaylist.Loop)
player_game.setPlaylist(playlist_game)
player_main.setPlaylist(playlist_main)
nick = ''
user_id = None
myappid = u'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class LanguageError(Exception):
    pass


class RepetitionError(Exception):
    pass


class LenError(Exception):
    pass


class PasswordError(Exception):
    pass


class UpError(Exception):
    pass


class Enter(QMainWindow, Ui_Enter):
    def __init__(self):
        super(Enter, self).__init__()
        self.setupUi(self)
        self.button_enter.clicked.connect(self.enter_in)
        self.need_register.clicked.connect(self.set_scene)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.button_exit.clicked.connect(sys.exit)
        self.errors_label.setStyleSheet('color: rgb(255, 0, 0)')
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = log.geometry().x()
            y = log.geometry().y()
            cursor_x = QtGui.QCursor.pos().x()
            cursor_y = QtGui.QCursor.pos().y()
            if (x <= cursor_x <= x + self.label_up.geometry().width()) and \
                    (y <= cursor_y <= y + self.label_up.geometry().height()):
                self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if self.old_pos:
            new_pos = event.pos() - self.old_pos
            log.move(log.pos() + new_pos)

    def enter_in(self):
        if self.login.text() and self.password.text():
            global nick, user_id
            con = sqlite3.connect('data_bas/data_base.db')
            cur = con.cursor()
            check = cur.execute("""SELECT id, Login, Password FROM Log_in
            WHERE Login = ? AND Password = ?""", (self.login.text(), self.password.text())).fetchall()
            if not check:
                self.errors_label.setText('Неправильный логин или пароль!')
            else:
                user_id = str(check[0][0])
                best = cur.execute("""SELECT best_score FROM Data
                WHERE id = ?""", (user_id, )).fetchall()
                play.best_score.setText(str(best[0][0]))
                result = cur.execute("""SELECT volume_main, volume_game FROM Data
                WHERE id = ?""", (user_id, )).fetchall()
                vol_main = result[0][0]
                vol_game = result[0][1]
                sett.volume_slider_main.setValue(vol_main)
                player_main.setVolume(vol_main)
                sett.volume_slider_game.setValue(vol_game)
                player_game.setVolume(vol_game)
                con.close()
                nick = self.login.text()
                widget.show()
                log.close()
                player_main.play()
                self.errors_label.clear()
        else:
            self.errors_label.setText('Введите и логин, и пароль')

    @staticmethod
    def set_scene():
        log.setCurrentIndex(1)


class Regiter(QMainWindow, Ui_Register):
    def __init__(self):
        super(Regiter, self).__init__()
        self.setupUi(self)
        self.button_enter.clicked.connect(self.enter_in)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.button_exit.clicked.connect(sys.exit)
        self.errors_label.setStyleSheet('color: rgb(255, 0, 0)')
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = log.geometry().x()
            y = log.geometry().y()
            cursor_x = QtGui.QCursor.pos().x()
            cursor_y = QtGui.QCursor.pos().y()
            if (x <= cursor_x <= x + self.label_up.geometry().width()) and \
                    (y <= cursor_y <= y + self.label_up.geometry().height()):
                self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if self.old_pos:
            new_pos = event.pos() - self.old_pos
            log.move(log.pos() + new_pos)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            log.setCurrentIndex(0)

    def enter_in(self):
        if self.login.text() and self.password.text():
            if self.check_login() and self.check_password():
                global nick, user_id
                con = sqlite3.connect('data_bas/data_base.db')
                cur = con.cursor()
                cur.execute("""INSERT INTO Log_in(Login, Password) VALUES(?, ?)
                """, (self.login.text(), self.password.text()))
                user_id = str(cur.execute("""SELECT id FROM Log_in
                WHERE Login = ? AND Password = ?""", (self.login.text(), self.password.text())).fetchall()[0][0])
                cur.execute("""INSERT INTO Data(volume_main, volume_game, best_score) VALUES(10, 10, 0)""")
                con.commit()
                result = cur.execute("""SELECT volume_main, volume_game FROM Data
                WHERE id = ?""", (user_id, )).fetchall()
                vol_main = result[0][0]
                vol_game = result[0][1]
                sett.volume_slider_main.setValue(vol_main)
                player_main.setVolume(vol_main)
                sett.volume_slider_game.setValue(vol_game)
                player_game.setVolume(vol_game)
                con.close()
                nick = self.login.text()
                widget.show()
                log.close()
                player_main.play()
                self.errors_label.clear()
        else:
            self.errors_label.setText('Введите и логин, и пароль')

    def check_login(self):
        try:
            if len(self.login.text()) < 3:
                raise LenError
            letters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
            letters_up = 'QWERTYUIOPASDFGHJKLZXCVBNM'
            for letter in self.login.text():
                if letter not in letters and letter not in letters_up:
                    raise LanguageError
            con = sqlite3.connect('data_bas/data_base.db')
            cur = con.cursor()
            nickname = cur.execute("""SELECT Login FROM Log_in"
                                   "WHERE Login = ?""", (self.login.text(), )).fetchall()
            if nickname:
                password = cur.execute("""SELECT Password FROM Log_in"
                                       "WHERE Login = ?""", (self.login.text(), )).fetchall()
                if password[0][0] != self.password.text():
                    raise RepetitionError
            return True
        except LenError:
            self.errors_label.setText('Длина никнейма должна быть\nне менее 3 символов')
        except LanguageError:
            self.errors_label.setText('Никнейм может содержать только\nбуквы латинского алфавита и цифры!')
        except RepetitionError:
            self.errors_label.setText('Никнейм уже занят!')
        return False

    def check_password(self):
        try:
            letters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
            letters_up = 'QWERTYUIOPASDFGHJKLZXCVBNM'
            for letter in self.password.text():
                if letter not in letters and letter not in letters_up:
                    raise LanguageError
            if len(self.password.text()) < 8:
                raise LenError
            for letter in self.password.text():
                if letter.isupper():
                    break
            else:
                raise UpError
            return True
        except LanguageError:
            self.errors_label.setText('Пароль может содержать только\nбуквы латинского алфавита и цифры!')
        except LenError:
            self.errors_label.setText('Длина пароля должна быть\nне менее 8 символов')
        except UpError:
            self.errors_label.setText('Пароль должен содержать\nбуквы разного регистра')
        return False


class Menu(QMainWindow, Ui_Menu):
    def __init__(self):
        super(Menu, self).__init__()
        self.setupUi(self)
        self.buttonGroup.buttonClicked.connect(self.set_scene)
        self.button_exit.clicked.connect(sys.exit)
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = widget.geometry().x()
            y = widget.geometry().y()
            cursor_x = QtGui.QCursor.pos().x()
            cursor_y = QtGui.QCursor.pos().y()
            if (x <= cursor_x <= x + self.label_up1.geometry().width()) and \
                    (y <= cursor_y <= y + self.label_up1.geometry().height()):
                self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.pos() - self.old_pos
            widget.move(widget.pos() + delta)

    @staticmethod
    def set_scene(button):
        if button.text() == 'Играть':
            play.nickname.setText(nick)
            play.score.setText('0')
            widget.setCurrentIndex(1)
        elif button.text() == 'Таблица лидеров':
            widget.setCurrentIndex(2)
            lead.view_leaders()
        elif button.text() == 'Настройки':
            widget.setCurrentIndex(3)
        elif button.text() == 'Выход':
            sys.exit()


class Leaders(QMainWindow, Ui_Leaders):
    def __init__(self):
        super(Leaders, self).__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.set_scene)
        self.old_pos = None
        self.button_exit.clicked.connect(sys.exit)
        self.sort_button.clicked.connect(self.set_sort)
        self.sort_index = 0
        self.view_leaders()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = widget.geometry().x()
            y = widget.geometry().y()
            cursor_x = QtGui.QCursor.pos().x()
            cursor_y = QtGui.QCursor.pos().y()
            if (x <= cursor_x <= x + self.label_up1.geometry().width()) and \
                    (y <= cursor_y <= y + self.label_up1.geometry().height()):
                self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.pos() - self.old_pos
            widget.move(widget.pos() + delta)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            widget.setCurrentIndex(0)

    @staticmethod
    def set_scene():
        widget.setCurrentIndex(0)

    def set_sort(self):
        if self.sort_button.text() == 'Сортировка↑':
            self.sort_button.setText('Сортировка↓')
            self.sort_index = 1
        elif self.sort_button.text() == 'Сортировка↓':
            self.sort_button.setText('Сортировка а↑')
            self.sort_index = 2
        elif self.sort_button.text() == 'Сортировка а↑':
            self.sort_button.setText('Сортировка а↓')
            self.sort_index = 3
        elif self.sort_button.text() == 'Сортировка а↓':
            self.sort_button.setText('Сортировка↑')
            self.sort_index = 0
        self.view_leaders()

    def view_leaders(self):
        con = sqlite3.connect('data_bas/data_base.db')
        cur = con.cursor()
        list_users = cur.execute('''SELECT Log_in.Login, Data.best_score
        FROM Log_in
        LEFT JOIN Data
        ON Log_in.id = Data.id''').fetchall()
        if list_users:
            if self.sort_index == 0:
                list_users.sort(reverse=True, key=lambda x: x[1])
            elif self.sort_index == 1:
                list_users.sort(reverse=False, key=lambda x: x[1])
            elif self.sort_index == 2:
                list_users.sort(reverse=False, key=lambda x: x[0].lower())
            elif self.sort_index == 3:
                list_users.sort(reverse=True, key=lambda x: x[0].lower())
            self.leaders_table.setStyleSheet('color: rgb(170, 85, 255);')
            self.leaders_table.setColumnCount(len(list_users[0]))
            self.leaders_table.setRowCount(len(list_users))
            self.leaders_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            list_column = ['Nickname', 'Best score']
            self.leaders_table.setHorizontalHeaderLabels(list_column)
            for i, elem in enumerate(list_users):
                for j, val in enumerate(elem):
                    self.leaders_table.setItem(i, j, QTableWidgetItem(str(val)))


class Play(QMainWindow, Ui_Play):
    def __init__(self):
        super(Play, self).__init__()
        self.setupUi(self)
        self.buttonGroup_playing.buttonClicked.connect(self.set_scene)
        self.button_exit.clicked.connect(sys.exit)
        self.main_coords = [0, 4]
        self.old_pos = None
        self.label = {}
        self.next_label = {}
        self.plate = None
        self.next = None
        self.game_start = False
        self.height = 20
        self.width = 10
        self.timer = QTimer()
        self.timer.setInterval(700)
        self.timer.timeout.connect(self.event_time)
        self.the_first = True
        self.track = False
        for y in range(self.height):
            line = QHBoxLayout(self)
            for x in range(self.width):
                self.label[y, x] = QLabel(self)
                self.label[y, x].setStyleSheet("background-color: rgb(45, 45, 45)")
                line.addWidget(self.label[y, x])
            self.play_board.addLayout(line)

        for y in range(5):
            line_in_next = QHBoxLayout(self)
            for x in range(6):
                self.next_label[y, x] = QLabel(self)
                self.next_label[y, x].setStyleSheet("background-color: rgb(45, 45, 45)")
                line_in_next.addWidget(self.next_label[y, x])
            self.next_plate.addLayout(line_in_next)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.quit()
        elif event.key() == Qt.Key_F1:
            manage.show()
        elif event.key() == Qt.Key_P:
            if self.track:
                player_game.pause()
                self.timer.stop()
                self.track = False
            else:
                player_game.play()
                self.timer.start()
                self.track = True
        elif self.track:
            if event.key() == Qt.Key_Down:
                self.move_down()
            elif event.key() == Qt.Key_Right:
                self.move_right()
            elif event.key() == Qt.Key_Left:
                self.move_left()
            elif event.key() == Qt.Key_Up:
                self.rotation()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = widget.geometry().x()
            y = widget.geometry().y()
            cursor_x = QtGui.QCursor.pos().x()
            cursor_y = QtGui.QCursor.pos().y()
            if (x <= cursor_x <= x + self.label_up1.geometry().width()) and \
                    (y <= cursor_y <= y + self.label_up1.geometry().height()):
                self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.pos() - self.old_pos
            widget.move(widget.pos() + delta)

    def clear_board1(self):
        self.main_coords = [0, 4]
        for y in range(self.height):
            for x in range(self.width):
                self.label[y, x].setStyleSheet("background-color: rgb(45, 45, 45)")

    def clear_board2(self):
        for y in range(5):
            for x in range(6):
                self.next_label[y, x].setStyleSheet("background-color: rgb(45, 45, 45)")

    def set_scene(self, button):
        if button.text() == 'Start':
            player_game.play()
            player_main.stop()
            self.track = True
            self.gameover_label.setText('')
            if not self.game_start:
                self.plate = None
                self.next = None
                self.the_first = True
                self.clear_board1()
                self.clear_board2()
                self.new_plate()
                self.score.setText('0')
                self.game_start = True
            if self.complexity.text() == '1':
                self.timer.setInterval(700)
            elif self.complexity.text() == '2':
                self.timer.setInterval(500)
            else:
                self.timer.setInterval(300)
            self.timer.start()
        elif button.text() == 'Pause':
            player_game.pause()
            self.timer.stop()
            self.track = False
        elif button.text() == 'Exit':
            self.quit()

    def quit(self):
        widget.setCurrentIndex(0)
        player_game.stop()
        player_main.play()
        self.timer.stop()
        self.game_start = False
        self.complexity.setValue(1)
        self.clear_board1()
        self.clear_board2()
        self.gameover_label.setText('')

    def new_plate(self):
        self.main_coords = [0, 4]
        if self.the_first:
            while self.plate == self.next:
                self.plate = self.choice_plate()
                self.next = self.choice_plate()
            self.the_first = False
        else:
            self.plate = self.next
            while self.plate == self.next:
                self.next = self.choice_plate()
        for i in self.plate[:-1]:
            self.label[i[0] + self.main_coords[0],
                       i[1] + self.main_coords[1]].setStyleSheet(f'background-color: {self.plate[-1]}')
        for i in self.next[:-1]:
            if self.next[-1] != '#42aaff':
                self.next_label[i[0] + 1,
                                i[1] + self.main_coords[1] - 2].setStyleSheet(f'background-color: {self.next[-1]}')
            else:
                self.next_label[i[0] + 2,
                                i[1] + self.main_coords[1] - 2].setStyleSheet(f'background-color: {self.next[-1]}')
        self.check_game_over()

    @staticmethod
    def choice_plate():
        plates = [[[0, 0], [0, 1], [1, 0], [1, 1], '#ff0000'], [[0, -1], [0, 0], [0, 1], [0, 2], '#42aaff'],
                  [[0, -1], [0, 0], [0, 1], [1, 1], '#0000ff'], [[0, -1], [0, 0], [0, 1], [1, 0], '#ffff00'],
                  [[0, 0], [0, 1], [1, -1], [1, 0], '#8b00ff'], [[0, -1], [0, 0], [1, 0], [1, 1], '#ffa500'],
                  [[0, -1], [0, 0], [0, 1], [1, -1], '#008000']]
        return choice(plates)

    def event_time(self):
        if self.game_start:
            self.move_down()

    def move_down(self):
        if self.check_down():
            self.draw_default_plate()
            self.main_coords[0] += 1
            self.draw_plate()
        else:
            self.check_full_line()
            if self.check_game_over():
                self.game_over()
            else:
                self.clear_board2()
                self.new_plate()

    def move_right(self):
        self.draw_default_plate()
        for i in self.plate[:-1]:
            if i[1] + self.main_coords[1] + 1 > self.width - 1 or \
                    self.label[i[0] + self.main_coords[0], i[1] + self.main_coords[1] + 1].styleSheet() != \
                    "background-color: rgb(45, 45, 45)":
                self.draw_plate()
                return False
        else:
            self.main_coords[1] += 1
            self.draw_plate()

    def move_left(self):
        self.draw_default_plate()
        for i in self.plate[:-1]:
            if i[1] + self.main_coords[1] - 1 < 0 or \
                    self.label[i[0] + self.main_coords[0], i[1] + self.main_coords[1] - 1].styleSheet() != \
                    "background-color: rgb(45, 45, 45)":
                self.draw_plate()
                return False
        else:
            self.main_coords[1] -= 1
            self.draw_plate()

    def rotation(self):
        if self.plate[-1] != '#ff0000':
            self.draw_default_plate()
            for i in self.plate[:-1]:
                if i[1] + self.main_coords[0] < 0 or -i[0] + self.main_coords[1] < 0 or \
                        i[1] + self.main_coords[0] >= self.height or -i[0] + self.main_coords[1] >= self.width:
                    self.draw_plate()
                    break
                elif self.label[i[1] + self.main_coords[0], -i[0] + self.main_coords[1]].styleSheet() != \
                        "background-color: rgb(45, 45, 45)":
                    self.draw_plate()
                    break
            else:
                for j in self.plate[:-1]:
                    j[0], j[1] = j[1], -j[0]
                self.draw_plate()

    def draw_plate(self):
        for k in self.plate[:-1]:
            self.label[k[0] + self.main_coords[0], k[1] +
                       self.main_coords[1]].setStyleSheet(f'background-color: {self.plate[-1]}')

    def draw_default_plate(self):
        for j in self.plate[:-1]:
            self.label[j[0] + self.main_coords[0], j[1] +
                       self.main_coords[1]].setStyleSheet("background-color: rgb(45, 45, 45)")

    def check_full_line(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.label[y, x].styleSheet() == 'background-color: rgb(45, 45, 45)':
                    break
            else:
                for i in range(y, 0, -1):
                    for j in range(self.width):
                        self.label[i, j].setStyleSheet(self.label[i - 1, j].styleSheet())
                self.score.setText(str(int(self.score.text()) + 100))

    def check_down(self):
        for i in self.plate[:-1]:
            if i[0] + self.main_coords[0] == self.height - 1:
                return False
            else:
                self.draw_default_plate()
                if self.label[i[0] + self.main_coords[0] + 1,
                              i[1] + self.main_coords[1]].styleSheet() != "background-color: rgb(45, 45, 45)":
                    self.draw_plate()
                    return False
                else:
                    self.draw_plate()
        return True

    def check_game_over(self):
        for coord in self.next[:-1]:
            '''
            начальные координаты каждой новой фигуры y = 0, x = 4
            '''
            if self.label[coord[0], coord[1] + 4].styleSheet() != \
                    "background-color: rgb(45, 45, 45)":
                return True
        else:
            for coord_x in range(self.width):
                if self.label[0, coord_x].styleSheet() != \
                        "background-color: rgb(45, 45, 45)":
                    return True

    def game_over(self):
        self.timer.stop()
        self.track = False
        self.gameover_label.setText('GAME OVER')
        self.game_start = False
        self.the_first = True
        self.save_best_score()
        player_game.stop()
        player_main.play()

    def save_best_score(self):
        if int(self.score.text()) > int(self.best_score.text()):
            self.best_score.setText(self.score.text())
            con = sqlite3.connect('data_base.db')
            cur = con.cursor()
            cur.execute('''UPDATE Data
            SET best_score = ?
            WHERE id = ?''', (self.score.text(), user_id))
            con.commit()
            con.close()
            lead.view_leaders()


class Settings(QMainWindow, Ui_Settings):
    def __init__(self):
        super(Settings, self).__init__()
        self.setupUi(self)
        self.volume_slider_game.sliderReleased.connect(self.set_volume_game)
        self.volume_slider_main.sliderReleased.connect(self.set_volume_main)
        self.back_.clicked.connect(self.back)
        self.save_setting.clicked.connect(self.save)
        self.delete_account.clicked.connect(self.delete)
        self.choice_music_game.clicked.connect(self.music_game)
        self.choice_music_main.clicked.connect(self.music_main)
        self.reset_best_score.clicked.connect(self.reset)
        self.old_pos = None
        self.button_exit.clicked.connect(sys.exit)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.back()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = widget.geometry().x()
            y = widget.geometry().y()
            cursor_x = QtGui.QCursor.pos().x()
            cursor_y = QtGui.QCursor.pos().y()
            if (x <= cursor_x <= x + self.label_up1.geometry().width()) and \
                    (y <= cursor_y <= y + self.label_up1.geometry().height()):
                self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.pos() - self.old_pos
            widget.move(widget.pos() + delta)

    def set_volume_game(self):
        player_game.setVolume(self.volume_slider_game.value())

    def set_volume_main(self):
        player_main.setVolume(self.volume_slider_main.value())

    def music_game(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать музыку', '',
            'Аудиофайл (*.mp3)')[0]
        if fname:
            playlist_game.clear()
            url = QUrl.fromLocalFile(fname)
            playlist_game.addMedia(QMediaContent(url))
            playlist_game.setPlaybackMode(QMediaPlaylist.Loop)
            player_game.setPlaylist(playlist_game)

    def music_main(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать музыку', '',
            'Аудиофайл (*.mp3)')[0]
        if fname:
            playlist_main.clear()
            url = QUrl.fromLocalFile(fname)
            playlist_main.addMedia(QMediaContent(url))
            playlist_main.setPlaybackMode(QMediaPlaylist.Loop)
            player_main.setPlaylist(playlist_main)
            player_main.play()

    def save(self):
        con = sqlite3.connect('data_bas/data_base.db')
        cur = con.cursor()
        cur.execute("""UPDATE Data
        SET volume_main = ?, volume_game = ?
        WHERE id = ?""", (self.volume_slider_main.value(), self.volume_slider_game.value(), user_id))
        con.commit()
        con.close()

    @staticmethod
    def reset():
        con = sqlite3.connect('data_bas/data_base.db')
        cur = con.cursor()
        cur.execute("""UPDATE Data
        SET best_score = 0
        WHERE id = ?""", (user_id, ))
        con.commit()
        con.close()
        play.best_score.setText('0')

    @staticmethod
    def delete():
        con = sqlite3.connect('data_bas/data_base.db')
        cur = con.cursor()
        cur.execute("""DELETE from Data
        WHERE id = ?""", (user_id, ))
        cur.execute("""DELETE from Log_in
        WHERE id = ?""", (user_id, ))
        con.commit()
        con.close()
        widget.setCurrentIndex(0)
        widget.close()
        entering.show()
        player_main.stop()
        entering.login.clear()
        entering.password.clear()

    @staticmethod
    def back():
        widget.setCurrentIndex(0)


class Management(QMainWindow, Ui_Management):
    def __init__(self):
        super(Management, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.key_pause.setStyleSheet("background-image: url(key_p.png)")
        self.key_up.setStyleSheet("background-image: url(key_up.png)")
        self.key_left.setStyleSheet("background-image: url(key_left.png)")
        self.key_down.setStyleSheet("background-image: url(key_down.png)")
        self.key_right.setStyleSheet("background-image: url(key_right.png)")
        self.button_exit.clicked.connect(self.close)
        radius = 30
        self.centralwidget.setStyleSheet(
            """
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius))
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = self.geometry().x()
            y = self.geometry().y()
            cursor_x = QtGui.QCursor.pos().x()
            cursor_y = QtGui.QCursor.pos().y()
            if (x <= cursor_x <= x + self.label_up.geometry().width()) and \
                    (y <= cursor_y <= y + self.label_up.geometry().height()):
                self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if self.old_pos:
            new_pos = event.pos() - self.old_pos
            self.move(self.pos() + new_pos)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    log = QtWidgets.QStackedWidget()
    log.setWindowTitle('Tetris by merphy')
    log.setWindowIcon(QtGui.QIcon('icon.ico'))
    log.setWindowFlags(Qt.FramelessWindowHint)
    log.setAttribute(Qt.WA_TranslucentBackground)
    log.setStyleSheet(
        """
        border-top-left-radius:{0}px;
        border-bottom-left-radius:{0}px;
        border-top-right-radius:{0}px;
        border-bottom-right-radius:{0}px;
        """.format(30))
    log.setFixedSize(391, 300)
    entering = Enter()
    log.addWidget(entering)
    reg = Regiter()
    log.addWidget(reg)
    log.show()
    manage = Management()
    manage.setWindowTitle('Management')
    manage.setWindowIcon(QtGui.QIcon('icon.ico'))
    widget = QtWidgets.QStackedWidget()
    widget.setWindowFlags(Qt.FramelessWindowHint)
    widget.setAttribute(Qt.WA_TranslucentBackground)
    widget.setStyleSheet(
        """
        border-top-left-radius:{0}px;
        border-bottom-left-radius:{0}px;
        border-top-right-radius:{0}px;
        border-bottom-right-radius:{0}px;
        """.format(30))
    widget.setWindowTitle('Tetris by merphy')
    widget.setWindowIcon(QtGui.QIcon('icon.ico'))
    menu = Menu()
    widget.addWidget(menu)
    play = Play()
    widget.addWidget(play)
    lead = Leaders()
    widget.addWidget(lead)
    sett = Settings()
    widget.addWidget(sett)
    widget.setFixedSize(600, 700)
    sys.excepthook = except_hook
    sys.exit(app.exec())
