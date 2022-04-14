import sys

from PyQt4 import QtGui
from PyQt4.QtGui import QLabel, QLineEdit

from src.func_flip import flip


class flipGUI(QtGui.QMainWindow):
    def __init__(self):
        super(flipGUI, self).__init__()
        self.label = None
        self.input_line = None
        self.initUI()

    def initUI(self):
        font = QtGui.QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.setWindowTitle('Gui Flip')
        self.setGeometry(100, 100, 300, 200)
        self.input_line = QLineEdit(self)
        self.input_line.setGeometry(20, 20, 150, 20)
        self.label = QLabel(self)
        self.label.setGeometry(20, 50, 150, 50)
        self.input_line.textChanged.connect(self.changeEditText)

    def changeEditText(self, txt):
        self.label.setText(flip(txt))


def main():
    app = QtGui.QApplication(sys.argv)
    flipForm = flipGUI()
    flipForm.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
