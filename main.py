import sys, os, re
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QSizePolicy
from PyQt5 import QtGui
from uitest1 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setUp()
        
    def setUp(self):
        self.scaleFactor = 1.0
        self.picIndex = 0
        self.pics = [x for x in os.listdir() if re.match(".*[.]jpg", x)]
        self.ui.label.setPixmap(QtGui.QPixmap("apple.jpg"))
        print(self.ui.label.pixmap().size())
        self.ui.label.setMinimumSize(self.ui.label.pixmap().size())
        self.ui.label.adjustSize()
        self.ui.actionNext.triggered.connect(self.nextActionHandler)
        self.ui.actionPrev.triggered.connect(self.prevActionHandler)
        self.ui.actionOpen.triggered.connect(self.openActionHandler)
        self.ui.actionZoom_In.triggered.connect(self.zoomInActionHandler)
        self.ui.actionZoom_Out.triggered.connect(self.zoomOutActionHandler)
        self.ui.actionZoom_Normal.triggered.connect(self.zoomNormalActionHandler)


    def nextActionHandler(self):
        self.picIndex = self.picIndex + 1 if self.picIndex + 1 < len(self.pics) else 0
        self.ui.label.setPixmap(QtGui.QPixmap(self.pics[self.picIndex]))
        self.ui.label.setMinimumSize(self.ui.label.pixmap().size())
        self.ui.label.adjustSize()
        self.scaleFactor = 1.0
        print(self.picIndex)
    
    def prevActionHandler(self):
        self.picIndex = self.picIndex - 1 if self.picIndex - 1 >= 0 else len(self.pics) - 1
        self.ui.label.setPixmap(QtGui.QPixmap(self.pics[self.picIndex]))
        self.ui.label.setMinimumSize(self.ui.label.pixmap().size())
        self.ui.label.adjustSize()
        self.scaleFactor = 1.0
        print(self.picIndex)
    
    def openActionHandler(self):
        filename = QFileDialog.getOpenFileName()[0]
        self.ui.label.setPixmap(QtGui.QPixmap(filename))
        self.zoomNormalActionHandler()
        print(filename)
        filepath = re.match(".+\/", filename).group(0)
        self.pics = [filepath + x for x in os.listdir(filepath) if re.match(".*[.]jpg|.*[.]png", x)]
        self.picIndex = self.pics.index(filename)
        self.scaleFactor = 1.0

    def zoomInActionHandler(self):
        factor = 1.25
        if self.scaleFactor < 5.0:
            self.scaleFactor *= factor
            self.ui.label.setMinimumSize(self.scaleFactor * self.ui.label.pixmap().size())
            self.ui.label.adjustSize()

    def zoomNormalActionHandler(self):
        self.scaleFactor = 1.0
        self.ui.label.setMinimumSize(self.ui.label.pixmap().size())
        self.ui.label.adjustSize()

    def zoomOutActionHandler(self):
        factor = .8
        if self.scaleFactor > .2:
            self.scaleFactor *= factor
            self.ui.label.setMinimumSize(self.scaleFactor * self.ui.label.pixmap().size())
            print(self.scaleFactor)
            self.ui.label.adjustSize()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())