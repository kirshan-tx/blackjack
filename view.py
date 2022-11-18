# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 800))
        MainWindow.setStyleSheet("background-color: rgb(0, 103, 0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_hit = QtWidgets.QPushButton(self.centralwidget)
        self.button_hit.setGeometry(QtCore.QRect(620, 670, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_hit.setFont(font)
        self.button_hit.setStyleSheet("background-color: light gray")
        self.button_hit.setObjectName("button_hit")
        self.button_stand = QtWidgets.QPushButton(self.centralwidget)
        self.button_stand.setGeometry(QtCore.QRect(750, 670, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_stand.setFont(font)
        self.button_stand.setStyleSheet("background-color: light gray")
        self.button_stand.setObjectName("button_stand")
        self.button_shuffle = QtWidgets.QPushButton(self.centralwidget)
        self.button_shuffle.setGeometry(QtCore.QRect(880, 670, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_shuffle.setFont(font)
        self.button_shuffle.setStyleSheet("background-color: light gray")
        self.button_shuffle.setObjectName("button_shuffle")
        self.label_dealer1 = QtWidgets.QLabel(self.centralwidget)
        self.label_dealer1.setGeometry(QtCore.QRect(300, 40, 150, 220))
        self.label_dealer1.setText("")
        self.label_dealer1.setPixmap(QtGui.QPixmap("images/back.png"))
        self.label_dealer1.setScaledContents(True)
        self.label_dealer1.setObjectName("label_dealer1")
        self.label_dealer0 = QtWidgets.QLabel(self.centralwidget)
        self.label_dealer0.setGeometry(QtCore.QRect(120, 40, 150, 220))
        self.label_dealer0.setText("")
        self.label_dealer0.setPixmap(QtGui.QPixmap("images/2_of_clubs.png"))
        self.label_dealer0.setScaledContents(True)
        self.label_dealer0.setObjectName("label_dealer0")
        self.label_dealer2 = QtWidgets.QLabel(self.centralwidget)
        self.label_dealer2.setGeometry(QtCore.QRect(480, 40, 150, 220))
        self.label_dealer2.setText("")
        self.label_dealer2.setScaledContents(True)
        self.label_dealer2.setObjectName("label_dealer2")
        self.label_dealer3 = QtWidgets.QLabel(self.centralwidget)
        self.label_dealer3.setGeometry(QtCore.QRect(660, 40, 150, 220))
        self.label_dealer3.setText("")
        self.label_dealer3.setScaledContents(True)
        self.label_dealer3.setObjectName("label_dealer3")
        self.label_dealer4 = QtWidgets.QLabel(self.centralwidget)
        self.label_dealer4.setGeometry(QtCore.QRect(840, 40, 150, 220))
        self.label_dealer4.setText("")
        self.label_dealer4.setScaledContents(True)
        self.label_dealer4.setObjectName("label_dealer4")
        self.label_player3 = QtWidgets.QLabel(self.centralwidget)
        self.label_player3.setGeometry(QtCore.QRect(660, 370, 150, 220))
        self.label_player3.setText("")
        self.label_player3.setScaledContents(True)
        self.label_player3.setObjectName("label_player3")
        self.label_player4 = QtWidgets.QLabel(self.centralwidget)
        self.label_player4.setGeometry(QtCore.QRect(840, 370, 150, 220))
        self.label_player4.setText("")
        self.label_player4.setScaledContents(True)
        self.label_player4.setObjectName("label_player4")
        self.label_player1 = QtWidgets.QLabel(self.centralwidget)
        self.label_player1.setGeometry(QtCore.QRect(300, 370, 150, 220))
        self.label_player1.setText("")
        self.label_player1.setPixmap(QtGui.QPixmap("images/13_of_hearts.png"))
        self.label_player1.setScaledContents(True)
        self.label_player1.setObjectName("label_player1")
        self.label_player0 = QtWidgets.QLabel(self.centralwidget)
        self.label_player0.setGeometry(QtCore.QRect(120, 370, 150, 220))
        self.label_player0.setText("")
        self.label_player0.setPixmap(QtGui.QPixmap("images/14_of_spades.png"))
        self.label_player0.setScaledContents(True)
        self.label_player0.setObjectName("label_player0")
        self.label_player2 = QtWidgets.QLabel(self.centralwidget)
        self.label_player2.setGeometry(QtCore.QRect(480, 370, 150, 220))
        self.label_player2.setText("")
        self.label_player2.setScaledContents(True)
        self.label_player2.setObjectName("label_player2")
        self.label_player_total = QtWidgets.QLabel(self.centralwidget)
        self.label_player_total.setGeometry(QtCore.QRect(130, 630, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_player_total.setFont(font)
        self.label_player_total.setStyleSheet("color: white\n"
"")
        self.label_player_total.setObjectName("label_player_total")
        self.label_strat = QtWidgets.QLabel(self.centralwidget)
        self.label_strat.setGeometry(QtCore.QRect(190, 690, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_strat.setFont(font)
        self.label_strat.setStyleSheet("QLabel {\n"
"    color: rgb(0, 103, 0)\n"
"    \n"
"}\n"
"\n"
"QLabel::Hover{\n"
"    color: white\n"
"}")
        self.label_strat.setObjectName("label_strat")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(330, 290, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: white\n"
"")
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.label_dealer_total = QtWidgets.QLabel(self.centralwidget)
        self.label_dealer_total.setGeometry(QtCore.QRect(120, 290, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_dealer_total.setFont(font)
        self.label_dealer_total.setStyleSheet("color: white\n"
"")
        self.label_dealer_total.setText("")
        self.label_dealer_total.setObjectName("label_dealer_total")
        self.label_hint = QtWidgets.QLabel(self.centralwidget)
        self.label_hint.setGeometry(QtCore.QRect(130, 690, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_hint.setFont(font)
        self.label_hint.setStyleSheet("color: white\n"
"")
        self.label_hint.setObjectName("label_hint")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_hit.setText(_translate("MainWindow", "HIT"))
        self.button_stand.setText(_translate("MainWindow", "STAND"))
        self.button_shuffle.setText(_translate("MainWindow", "SHUFFLE"))
        self.label_player_total.setText(_translate("MainWindow", "Total: "))
        self.label_strat.setText(_translate("MainWindow", "Strat"))
        self.label_hint.setText(_translate("MainWindow", "Hint:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
