import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.show()
    sys.exit(app.exec_())
