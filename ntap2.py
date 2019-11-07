# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ImageBtn.setGeometry(QtCore.QRect(40, 110, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ImageBtn.setFont(font)
        self.ImageBtn.setObjectName("ImageBtn")
        self.imageSrc = QtWidgets.QLabel(self.centralwidget)
        self.imageSrc.setGeometry(QtCore.QRect(220, 10, 251, 181))
        self.imageSrc.setFrameShape(QtWidgets.QFrame.Box)
        self.imageSrc.setText("")
        self.imageSrc.setObjectName("imageSrc")
        self.FindBtn = QtWidgets.QPushButton(self.centralwidget)
        self.FindBtn.setGeometry(QtCore.QRect(310, 260, 151, 61))
        self.FindBtn.setObjectName("FindBtn")
        self.imageRes = QtWidgets.QLabel(self.centralwidget)
        self.imageRes.setGeometry(QtCore.QRect(20, 220, 271, 191))
        self.imageRes.setFrameShape(QtWidgets.QFrame.Box)
        self.imageRes.setText("")
        self.imageRes.setObjectName("imageRes")
        self.PathBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PathBtn.setGeometry(QtCore.QRect(40, 20, 101, 71))
        self.PathBtn.setObjectName("PathBtn")
        self.Socienvi = QtWidgets.QLabel(self.centralwidget)
        self.Socienvi.setGeometry(QtCore.QRect(380, 380, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Socienvi.setFont(font)
        self.Socienvi.setObjectName("Socienvi")
        self.NextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.NextBtn.setGeometry(QtCore.QRect(389, 340, 71, 21))
        self.NextBtn.setObjectName("NextBtn")
        self.PrevBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PrevBtn.setGeometry(QtCore.QRect(310, 340, 71, 21))
        self.PrevBtn.setObjectName("PrevBtn")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(310, 230, 151, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.ImageBtn.clicked.connect(self.setImage)
        self.PathBtn.clicked.connect(self.setPath)
        # self.FindBtn.clicked.connect(self.setImage)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ImageBtn.setText(_translate("MainWindow", "Select Image"))
        self.FindBtn.setText(_translate("MainWindow", "Find Similiar Image"))
        self.PathBtn.setText(_translate("MainWindow", "Select Path"))
        self.Socienvi.setText(_translate("MainWindow", "@SociEnvi 2019"))
        self.NextBtn.setText(_translate("MainWindow", "Next"))
        self.PrevBtn.setText(_translate("MainWindow", "Prev"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Distance Method"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cosine Method"))

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)") # Ask for file
        if fileName: # If the user gives a file
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageSrc.width(), self.imageSrc.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imageSrc.setPixmap(pixmap) # Set the pixmap onto the label
            self.imageSrc.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center

    def setPath(self):
        startingDir = '/'
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode( QtWidgets.QFileDialog.FileMode() )
        dialog.getExistingDirectory( None, 'Open working directory', startingDir )

    def findSimiliar(self):


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
