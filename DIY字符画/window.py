# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_input = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_input.setGeometry(QtCore.QRect(550, 160, 101, 31))
        self.pushButton_input.setStyleSheet("background-image: url(:/img/img/import.png);")
        self.pushButton_input.setText("")
        self.pushButton_input.setObjectName("pushButton_input")
        self.pushButton_conver = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_conver.setGeometry(QtCore.QRect(550, 420, 101, 101))
        self.pushButton_conver.setStyleSheet("background-image: url(:/img/img/conversion.png);")
        self.pushButton_conver.setText("")
        self.pushButton_conver.setObjectName("pushButton_conver")
        self.label_export = QtWidgets.QLabel(self.centralwidget)
        self.label_export.setGeometry(QtCore.QRect(674, 85, 500, 500))
        self.label_export.setText("")
        self.label_export.setScaledContents(True)
        self.label_export.setObjectName("label_export")
        self.label_input = QtWidgets.QLabel(self.centralwidget)
        self.label_input.setGeometry(QtCore.QRect(28, 85, 500, 500))
        self.label_input.setScaledContents(True)
        self.label_input.setObjectName("label_input")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(550, 220, 101, 94))
        self.textEdit.setStyleSheet("color: rgb(255, 0, 0);")
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(550, 350, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.loding = QtWidgets.QLabel(self.centralwidget)
        self.loding.setGeometry(QtCore.QRect(550, 250, 100, 100))
        self.loding.setText("")
        self.loding.setObjectName("loding")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_input.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox.setItemText(0, _translate("MainWindow", "清晰"))
        self.comboBox.setItemText(1, _translate("MainWindow", "一般"))
        self.comboBox.setItemText(2, _translate("MainWindow", "字符"))


import img_qc_rc
