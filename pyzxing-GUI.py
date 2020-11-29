import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow
from pyzxing import BarCodeReader

from ui.mainWindow import *

ALLOWED_EXT = ['.png', '.jpg', '.jpeg', '.bmp']


class MyWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.reader = BarCodeReader()
        self.imageLabel.dragEnterEvent = self.imageLabel_dragEnterEvent
        self.imageLabel.dropEvent = self.imageLabel_dropEvent

    def imageLabel_dragEnterEvent(self, e):
        filename = e.mimeData().urls()[0].toLocalFile()
        if os.path.splitext(filename)[-1] in ALLOWED_EXT:
            e.acceptProposedAction()

    def imageLabel_dropEvent(self, e):
        filename = e.mimeData().urls()[0].toLocalFile()
        results = self.reader.decode(filename)
        self.resultText.setText(results[0].get('raw', ''))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
