from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit
import sys

from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Find Similiar"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindowr()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.btn1 = QPushButton("Open Image")
        self.btn1.clicked.connect(self.getImage)
        vbox.addWidget(self.btn1)

        self.label = QLabel("Hello")
        vbox.addWidget(self.label)

        self.btn2 = QPushButton("Find Similiar")
        self.btn2.clicked.connect(self.findSimiliar)
        vbox.addWidget(self.btn2)

        self.setLayout(vbox)
        self.show()

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, "Open file")
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaledToHeight(200)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(400, pixmap.height())

    def findSimiliar(self):
        self.label = QLabel("Hello Boys")
        vbox.addWidget(self.label)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
