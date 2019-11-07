# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Face Recognition")
        MainWindow.resize(481, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectImageBtn.setGeometry(QtCore.QRect(20, 110, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.selectImageBtn.setFont(font)
        self.selectImageBtn.setObjectName("selectImageBtn")
        self.imageSrc = QtWidgets.QLabel(self.centralwidget)
        self.imageSrc.setGeometry(QtCore.QRect(220, 10, 251, 181))
        self.imageSrc.setFrameShape(QtWidgets.QFrame.Box)
        self.imageSrc.setText("")
        self.imageSrc.setObjectName("imageSrc")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(310, 220, 141, 61))
        self.addBtn.setObjectName("addBtn")
        self.imageRes = QtWidgets.QLabel(self.centralwidget)
        self.imageRes.setGeometry(QtCore.QRect(20, 220, 271, 191))
        self.imageRes.setFrameShape(QtWidgets.QFrame.Box)
        self.imageRes.setText("")
        self.imageRes.setObjectName("imageRes")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 101, 71))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 370, 101, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.selectImageBtn.clicked.connect(self.setImage)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition"))
        self.selectImageBtn.setText(_translate("MainWindow", "Select Image"))
        self.addBtn.setText(_translate("MainWindow", "Find Similiar Image"))
        self.pushButton.setText(_translate("MainWindow", "Select Path"))
        self.label.setText(_translate("MainWindow", "@SociEnvi 2019"))

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)") # Ask for file
        if fileName: # If the user gives a file
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageSrc.width(), self.imageSrc.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imageSrc.setPixmap(pixmap) # Set the pixmap onto the label
            self.imageSrc.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center
            self.addBtn.setText(_translate("MainWindow", "Find Similiar Image"))

    def findSimiliar(self):
        self.addBtn.setText(_translate("MainWindow", "Next Image"))
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
