# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import os
from PIL import Image, ImageFont, ImageDraw, ImageEnhance


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(907, 544)
        MainWindow.setMinimumSize(QtCore.QSize(907, 544))
        MainWindow.setMaximumSize(QtCore.QSize(907, 544))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-image: url(:/newPrefix/back.png);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 907, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_1 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/mark.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_1.setIcon(icon)
        self.action_1.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.action_1.setShortcutVisibleInContextMenu(False)
        self.action_1.setObjectName("action_1")
        self.action_2 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/rename.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_2.setIcon(icon1)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/about.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_3.setIcon(icon2)
        self.action_3.setObjectName("action_3")
        self.menu.addSeparator()
        self.menu.addAction(self.action_1)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.action_1.triggered.connect(self.openMark)
        self.action_2.triggered.connect(self.openRename)
        self.action_3.triggered.connect(self.openAbout)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片批量处理工具"))
        self.menu.setTitle(_translate("MainWindow", "主菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.action_1.setText(_translate("MainWindow", "添加水印"))
        self.action_2.setText(_translate("MainWindow", "批量重命名"))
        self.action_3.setText(_translate("MainWindow", "关于本软件"))

    def openMark(self):
        self.another = Ui_Form()
        self.another.show()

    def openRename(self):
        pass

    def openAbout(self):
        QtWidgets.QMessageBox.information(None, "about this software", "this is my first gui software made by qt5",
                                          QtWidgets.QMessageBox.Ok)


import img_rc


class Ui_Form(QMainWindow):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 只显示关闭按钮
        self.setupUi(self)  # 初始化窗口

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        # self.totalpic = QtWidgets.QLabel(Form)
        # self.totalpic.setEnabled(False)
        # self.totalpic.setGeometry(QtCore.QRect(10, 560, 121, 31))
        # font = QtGui.QFont()
        # font.setFamily("Agency FB")
        # font.setPointSize(16)
        # font.setBold(False)
        # font.setWeight(50)
        # self.totalpic.setFont(font)
        # self.totalpic.setTextFormat(QtCore.Qt.AutoText)
        # self.totalpic.setObjectName("totalpic")
        self.piclist = QtWidgets.QListWidget(Form)
        self.piclist.setGeometry(QtCore.QRect(10, 10, 200, 550))
        self.piclist.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.piclist.setFrameShape(QtWidgets.QFrame.Box)
        self.piclist.setFrameShadow(QtWidgets.QFrame.Plain)
        self.piclist.setLineWidth(1)
        self.piclist.setMidLineWidth(0)
        self.piclist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.piclist.setObjectName("piclist")
        # self.totalpic_num = QtWidgets.QLabel(Form)
        # self.totalpic_num.setEnabled(False)
        # self.totalpic_num.setGeometry(QtCore.QRect(130, 560, 71, 34))
        # font = QtGui.QFont()
        # font.setFamily("Agency FB")
        # font.setPointSize(16)
        # font.setBold(True)
        # font.setWeight(75)
        # self.totalpic_num.setFont(font)
        # self.totalpic_num.setText("")
        # self.totalpic_num.setTextFormat(QtCore.Qt.AutoText)
        # self.totalpic_num.setObjectName("totalpic_num")
        self.radioButton1 = QtWidgets.QRadioButton(Form)
        self.radioButton1.setGeometry(QtCore.QRect(250, 90, 211, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton1.setFont(font)
        self.radioButton1.setObjectName("radioButton1")
        self.radioButton2 = QtWidgets.QRadioButton(Form)
        self.radioButton2.setGeometry(QtCore.QRect(250, 180, 211, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton2.setFont(font)
        self.radioButton2.setObjectName("radioButton2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(440, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_text = QtWidgets.QLineEdit(Form)
        self.textEdit_text.setGeometry(QtCore.QRect(330, 140, 311, 31))
        self.textEdit_text.setStyleSheet("border:2px groove gray;border-radius:10px;padding:1px 3px;")
        self.textEdit_text.setObjectName("textEdit_text")
        self.pushButton_text = QtWidgets.QPushButton(Form)
        self.pushButton_text.setGeometry(QtCore.QRect(650, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.pushButton_text.setFont(font)
        self.pushButton_text.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.pushButton_text.setObjectName("pushButton_text")
        self.pushButton_pic = QtWidgets.QPushButton(Form)
        self.pushButton_pic.setGeometry(QtCore.QRect(650, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.pushButton_pic.setFont(font)
        self.pushButton_pic.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.pushButton_pic.setObjectName("pushButton_pic")
        self.textEdit_pic = QtWidgets.QLineEdit(Form)
        self.textEdit_pic.setGeometry(QtCore.QRect(330, 230, 311, 31))
        self.textEdit_pic.setStyleSheet("border:2px groove gray;border-radius:10px;padding:1px 3px;")
        self.textEdit_pic.setObjectName("textEdit_pic")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 290, 171, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(250, 340, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Slider1 = QtWidgets.QSlider(Form)
        self.Slider1.setGeometry(QtCore.QRect(330, 341, 411, 31))
        self.Slider1.setOrientation(QtCore.Qt.Horizontal)
        self.Slider1.setObjectName("Slider1")
        self.Slider1.setMinimum(1)
        self.Slider1.setMaximum(10)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(250, 390, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(340, 390, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(250, 450, 171, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit_pos = QtWidgets.QLineEdit(Form)
        self.textEdit_pos.setGeometry(QtCore.QRect(330, 500, 311, 31))
        self.textEdit_pos.setStyleSheet("border:2px groove gray;border-radius:10px;padding:1px 3px;")
        self.textEdit_pos.setObjectName("textEdit_pos")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(250, 500, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_pos = QtWidgets.QPushButton(Form)
        self.pushButton_pos.setGeometry(QtCore.QRect(650, 500, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.pushButton_pos.setFont(font)
        self.pushButton_pos.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.pushButton_pos.setObjectName("pushButton_pos")
        self.pushButton_exec = QtWidgets.QPushButton(Form)
        self.pushButton_exec.setGeometry(QtCore.QRect(440, 550, 101, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.pushButton_exec.setFont(font)
        self.pushButton_exec.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.pushButton_exec.setObjectName("pushButton_exec")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(240, 50, 521, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(240, 270, 521, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(240, 430, 521, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(240, 530, 521, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.statusBar = QtWidgets.QStatusBar(Form)
        self.statusBar.setObjectName('statusBar')
        self.statusBar.showMessage('准备就绪')
        self.setStatusBar(self.statusBar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.statusBar.setFont(font)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(0)
        self.pushButton_text.clicked.connect(self.setTextFont)
        self.pushButton_pic.clicked.connect(self.setImg)
        self.pushButton_pos.clicked.connect(self.savePic)
        self.pushButton_exec.clicked.connect(self.exeCu)
        self.pushButton.clicked.connect(self.addPic)
        self.piclist.clicked.connect(self.itemClick)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.piclist.setSortingEnabled(True)
        self.radioButton1.setText(_translate("Form", "添加文字水印"))
        self.radioButton2.setText(_translate("Form", "添加图片水印"))
        self.label.setText(_translate("Form", "水印设置："))
        self.pushButton.setText(_translate("Form", "加载图片"))
        self.label_2.setText(_translate("Form", "水印文字："))
        self.label_3.setText(_translate("Form", "水印图片："))
        self.pushButton_text.setText(_translate("Form", "字体设置"))
        self.pushButton_pic.setText(_translate("Form", "浏览"))
        self.label_4.setText(_translate("Form", "透明度及位置设置："))
        self.label_5.setText(_translate("Form", "透明度："))
        self.label_6.setText(_translate("Form", "水印位置："))
        self.comboBox.setCurrentText(_translate("Form", "左上角"))
        self.comboBox.setItemText(0, _translate("Form", "左上角"))
        self.comboBox.setItemText(1, _translate("Form", "左下角"))
        self.comboBox.setItemText(2, _translate("Form", "右上角"))
        self.comboBox.setItemText(3, _translate("Form", "右下角"))
        self.comboBox.setItemText(4, _translate("Form", "居中"))
        self.label_7.setText(_translate("Form", "路径设置："))
        self.label_8.setText(_translate("Form", "保存位置："))
        self.pushButton_pos.setText(_translate("Form", "浏览"))
        self.pushButton_exec.setText(_translate("Form", "执行"))

    def exeCu(self):
        if self.textEdit_pos.text() == '':
            QtWidgets.QMessageBox.warning(None, 'warnring', '请选择添加水印后图片的保存路径', QtWidgets.QMessageBox.Ok)
            print('没有路径')
            return
        else:
            num = 0  # 记录图片处理数量
            for i in range(0, self.piclist.count()):
                filePath = os.path.join(self.imagePath + '/', self.piclist.item(i).text())  # 原始文件
                print(filePath)
                newFilePath = os.path.join(self.textEdit_pos.text() + '/', self.piclist.item(i).text())  # 新文件
                print(newFilePath)
                if self.radioButton1.isChecked():  # 判断是否选择文字水印
                    if self.textEdit_text.text() == '':  # 判断水印文字是否输入
                        QtWidgets.QMessageBox.warning(None, 'warning', '请输入水印文字', QtWidgets.QMessageBox.Ok)
                        print('没有文字')
                        return
                    else:  # 调用addWaterText 添加水印
                        self.addWaterText(filePath, newFilePath)
                        num += 1
                else:
                    if self.textEdit_pic.text() == '':
                        QtWidgets.QMessageBox.warning(None, 'warning', '请选择水印图片', QtWidgets.QMessageBox.Ok)
                    else:
                        self.addWaterPic(filePath, newFilePath)
                        num += 1
            self.statusBar.showMessage(str(num) + '张图片完成处理')

    def addPic(self):  # 点击加载图片，判断是否图片文件，加载图片进listwidget，并展示在状态栏
        try:
            self.imagePath = QtWidgets.QFileDialog.getExistingDirectory(None, '选择路径', os.getcwd())  # 选择文件夹路径
            # print(self.imagePath)
            self.list = os.listdir(self.imagePath)  # 遍历文件夹
            num = 0  # 图片数量
            self.piclist.clear()  # 清空列表
            for i in range(0, len(self.list)):
                filePath = os.path.join(self.imagePath, self.list[i])
                if os.path.isfile(filePath):  # 判断是否文件
                    imgType = os.path.splitext(filePath)[1]  # 判断是否图片
                    if self.isImg(imgType):
                        num += 1
                        self.item = QtWidgets.QListWidgetItem(self.piclist)  # 创建列表项

                        self.item.setText(self.list[i])
                        print(self.item.text())
            self.statusBar.showMessage('共有图片' + str(num) + '张')
        except Exception:
            QtWidgets.QMessageBox.warning(None, 'warning', '请输入一个有效路径', QtWidgets.QMessageBox.Ok)

    def isImg(self, imgType: str) -> bool:  # 判断是否图片
        imgTypeList = ['.png', '.jpg', '.bmp', '.tif', '.gif', '.tga', '.jpeg']
        if imgType in imgTypeList:
            return True
        else:
            return False

    def itemClick(self):  # 单击打开列表里的图片
        print('click' + self.item.text())
        os.startfile(self.imagePath + '\\' + self.item.text())

    def setTextFont(self):  # 设置水印文字格式
        self.waterFont, ok = QtWidgets.QFontDialog.getFont()  # 显示字体对话框
        if ok:
            self.textEdit_text.setFont(self.waterFont)  # 设置水印文字字体
            self.fontSize = QtGui.QFontMetrics(self.waterFont)  # 设置字体尺寸
            self.fontInfo = QtGui.QFontInfo(self.waterFont)  # 获取字体信息

    def setImg(self):  # 设置水印图片路径，并把路径展示在linetext
        try:
            self.waterImg = QtWidgets.QFileDialog.getOpenFileName(None, '选择水印图片', os.getcwd(),
                                                                  '图片文件(*.jpg;*.png;*.jpeg;*.bmp)')
            self.textEdit_pic.setText(self.waterImg[0])  # 显示选择的图
        except Exception as e:
            print(e)

    def savePic(self):  # 设置保存处理后图片的位置，并展示在linetext
        try:
            self.savePos = QtWidgets.QFileDialog.getExistingDirectory(None, '选择保存路径', os.getcwd())
            self.textEdit_pos.setText(self.savePos)
            # print(self.textEdit_pos.text())
        except Exception as e:
            print(e)

    def addWaterText(self, img, imgPath):  # 添加文字水印
        try:
            im = Image.open(img).convert('RGBA')  # 打开原始图片，并转换为RGBA
            newImage = Image.new('RGBA', im.size, (255, 255, 255, 0))  # 存储添加水印后的图片
            font = ImageFont.truetype('simkai.ttf', self.fontInfo.pointSize())
            imageDraw = ImageDraw.Draw(newImage)
            imgWidth, imgHeight = im.size
            textWidth = self.fontSize.maxWidth() * len(self.textEdit_text.text())
            textHeight = self.fontSize.height()
            if self.comboBox.currentText() == '左上角':
                pos = (0, 0)
            elif self.comboBox.currentText() == '左下角':
                pos = (0, imgHeight - textHeight)
            elif self.comboBox.currentText() == '右上角':
                pos = (imgWidth - textWidth, 0)
            elif self.comboBox.currentText() == '右下角':
                pos = (imgWidth - textWidth, imgHeight - textHeight)
            elif self.comboBox.currentText() == '居中':
                pos = (imgWidth / 2, imgHeight / 2)
            imageDraw.text(pos, self.textEdit_text.text(), font=font, fill="#FCA454")  # 设置文本颜色
            print('3')
            alpha = newImage.split()[3]
            print('4')
            alpha = ImageEnhance.Brightness(alpha).enhance(int(self.Slider1.value()) / 10.0)
            print('5')
            newImage.putalpha(alpha)
            print('6')
            Image.alpha_composite(im, newImage).save(imgPath)
        except Exception as e:
            print(e)

    def addWaterPic(self, img, imgPath):
        try:
            im = Image.open(img)  # 打开原始图片
            wp = Image.open(self.textEdit_pic.text()) # 打开水印图片
            rgba_im = im.convert('RGBA')  # 转换为RGBA模式
            rgba_wp = wp.convert('RGBA')
            imWidth, imHeight = rgba_im.size
            wp_width, wp_Height = rgba_wp.size
            scale = 10  # 缩放水印图片
            markScale = max(imWidth / (scale * wp_width), imHeight / (scale * wp_Height))
            newSize = (int(wp_width * markScale), int(wp_Height * markScale))  # 计算新的尺寸大小
            rgba_wp = rgba_wp.resize(newSize, resample=Image.ANTIALIAS)  # 重新设置水印图片大小
            wp_width, wp_Height = rgba_wp.size
            # 计算水印的位置
            if self.comboBox.currentText() == '左上角':
                pos = (0, 0)
            elif self.comboBox.currentText() == '左下角':
                pos = (0, imHeight - wp_Height)
            elif self.comboBox.currentText() == '右上角':
                pos = (imWidth - wp_width, 0)
            elif self.comboBox.currentText() == '右下角':
                pos = (imWidth - wp_width, imHeigt - wp_Height)
            elif self.comboBox.currentText() == '居中':
                pos = (imWidth / 2, imHeight / 2)
            rgba_waterPic_pha = rgba_wp.convert('L').point(lambda x: x / int(self.Slider1.value()))
            rgba_wp.putalpha(rgba_waterPic_pha)
            rgba_im.paste(rgba_wp, pos, rgba_waterPic_pha)
            try:
                rgba_im.save(imgPath)
            except Exception:
                QtWidgets.QMessageBox.warning(None, 'warning', '请选择其他路径', QtWidgets.QMessageBox.Ok)
        except Exception as e:
            print(e)
