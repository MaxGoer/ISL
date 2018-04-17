from PyQt5 import QtWidgets
from EDECore import EDECore


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EDECore()
    ui.setupUi(MainWindow)
    ui.setup_callbacks()
    MainWindow.show()

    sys.exit(app.exec_())
