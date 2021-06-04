from PyQt5 import QtCore, QtGui, QtWidgets
from emoji import UNICODE_EMOJI

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class Menu(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(QtWidgets.QMainWindow, self).__init__(parent)

        self.table = QtWidgets.QTableView()
        self.setMinimumSize(425, 500)
        self.setMaximumSize(425, 700)
        self.setWindowTitle("EmojiMenu")


        data = []
        for key, value in UNICODE_EMOJI.items():
            data.append([key, value])

        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.table.resizeColumnsToContents()
        self.setStyleSheet("color: black;" "background-color: white;")
        self.setCentralWidget(self.table)
        self.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Menu()
    window.show()
    window.adjustSize()
    app.exec_()
