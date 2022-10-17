import sys,json
import front
from PyQt5 import QtWidgets

def init():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = front.Ui_main()
    ui.setupUi(MainWindow)
    return app, ui, MainWindow
    
if __name__ == "__main__":
    app, ui, MainWindow = init()
    MainWindow.show()
    sys.exit(app.exec_())