from window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtGui
import sys, _thread, time
import conversion


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        # 开启自动填充背景
        self.centralwidget.setAutoFillBackground(True)
        palette = QtGui.QPalette()  # 调色板
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('img/bg.png')))  # 设置背景图
        self.centralwidget.setPalette(palette)  # 设置调色板
        input_img = QtGui.QPixmap('img/input_test.png')  # 打开位图
        self.label_input.setPixmap(input_img)
        export_img = QtGui.QPixmap('img/output_test.png')
        self.label_export.setPixmap(export_img)

    def show_input_img(self, file_path):  # 显示导入的图片
        input_img = QtGui.QPixmap(file_path)  # 打开位图
        self.label_input.setPixmap(input_img)  # 设置位图

    def openfile(self):  # 打开选择文件的对话框，进行图片的选择
        openfile_name = QFileDialog.getOpenFileName()
        if openfile_name[0] != '':
            self.input_path = openfile_name[0]  # 获取选中图片的路径
            self.show_input_img(self.input_path)  # 调用显示导入图片的方法

    def show_export_img(self, file_path):  # 显示转换后的字符画图片
        export_img = QtGui.QPixmap(file_path)  # 打开位图
        self.label_export.setPixmap(export_img)  # 设置位图

    def start_convert(self):
        if hasattr(main, 'input_path'):
            self.gif = QtGui.QMovie('img/loading.gif')  # 加载gif图片
            self.loding.setMovie(self.gif)  # 设置gif图片
            self.gif.start()  # 启动图片，实现等待gif图片的显示
            # 线程启动转换方法，避免与主窗体冲突
            _thread.start_new_thread(lambda: self.is_converting(main.input_path))
        else:
            print("没有选择指定的图片路径")

    def is_converting(self, file_path):
        t = str(int(time.time()))  # 当前时间戳，秒级
        # 转换后的字符画图片路径
        export_path = 'export_img/export_img' + t + '.png'
        input_char = main.textEdit.toPlainText()  # 获取输入的字符内容
        definition = main.comboBox.currentText()  # 获取选中的文字
        # 调用转换字符画的方法 file_path(),并为它指定图片路径
        is_over = conversion.picture_conversion(file_path, export_path, input_char, definition)
        if is_over is False:  # 判断图片是否转换完毕
            self.loding.clear()  # 转换完毕清除gif图片动画
            main.show_export_img(export_path)  # 调用显示转换后字符画的方法


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    main.pushButton_input.clicked.connect(main.openfile())  # 为导入图片按钮指定打开图片的事件
    main.pushButton_conver.clicked.connect(main.start_convert())  # 为转换按钮指定启动转换图片的方法
    sys.exit((app.exec_()))
