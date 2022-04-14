# coding=utf-8
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

mult_data = [[x * y for x in range(1, 11)] for y in range(1, 11)]


class MyWindow(QWidget):

    def __init__(self, *args):
        QWidget.__init__(self, *args)
        self.setGeometry(100, 100, 403, 347)
        self.setWindowTitle(u'Таблица умножения')

        table_model = MyTableModel(self, mult_data)
        table_view = QTableView()
        table_view.setModel(table_model)
        font = QFont("Courier New", 12)
        table_view.setFont(font)
        table_view.setShowGrid(False)
        table_view.resizeColumnsToContents()
        layout = QVBoxLayout()
        layout.addWidget(table_view)
        self.setLayout(layout)


class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, data, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.data = data

    def rowCount(self, parent=None):
        return len(self.data)

    def columnCount(self, parent=None):
        return len(self.data)

    def data(self, index, role):
        value = self.data[index.row()][index.column()]
        if role == Qt.DisplayRole:
            return value
        elif role == Qt.BackgroundRole:
            if value % 10 == 0:
                return QColor('Coral')
            elif value % 3 == 0:
                return QColor('YellowGreen')
            elif value % 5 == 0:
                return QColor('Crimson')
            elif value % 7 == 0:
                return QColor('Teal')
            return QColor('Lime')
        elif role == Qt.FontRole:
            if value % 2 == 0:
                return QFont("Times", 14, QFont.Bold)

        return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
