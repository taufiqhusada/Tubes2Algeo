# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import cv2
import numpy as np
import scipy
from matplotlib.pyplot import imread
import pickle as pickle
from scipy import spatial
import random
import os
import math
import matplotlib.pyplot as plt
import csv
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
        self.comboBox.addItems(['Distance Method', 'Cosine Method'])
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
        self.FindBtn.clicked.connect(self.findSimiliar)
        self.option = str(self.comboBox.currentText())
        print(self.comboBox.currentText())

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

    fileName = ""

    def setImage(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)") # Ask for file
        if self.fileName: # If the user gives a file
            pixmap = QtGui.QPixmap(self.fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageSrc.width(), self.imageSrc.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imageSrc.setPixmap(pixmap) # Set the pixmap onto the label
            self.imageSrc.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center
        print(self.fileName)

    pathDir = '/'

    def setPath(self):
        print("path set")
        startingDir = "/"
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode( QtWidgets.QFileDialog.FileMode() )
        self.pathDir = dialog.getExistingDirectory( None, 'Open working directory', startingDir )
        print(self.pathDir)

    def extract_features(self, image_path, vector_size=32):
        image = imread(image_path)
        try:
            # Using KAZE, cause SIFT, ORB and other was moved to additional module
            # which is adding addtional pain during install
            alg = cv2.KAZE_create()
            # Dinding image keypoints
            kps = alg.detect(image)
            # Getting first 32 of them.
            # Number of keypoints is varies depend on image size and color pallet
            # Sorting them based on keypoint response value(bigger is better)
            kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
            # computing descriptors vector
            kps, dsc = alg.compute(image, kps)
            # Flatten all of them in one big vector - our feature vector
            dsc = dsc.flatten()
            # Making descriptor of same size
            # Descriptor vector size is 64
            needed_size = (vector_size * 64)
            if dsc.size < needed_size:
                # if we have less the 32 descriptors then just adding zeros at the
                # end of our feature vector
                dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
        except cv2.error as e:
            print ('Error: ', e)
            return None
        #print(dsc)

        return dsc
    result = {}
    # fungsi distance
    def dist(self, vec1, vec2):
        result = 0;
        for i in range(len(vec1)):
            result+= ((vec1[i])-(vec2[i]))*((vec1[i])-(vec2[i]))
        return math.sqrt(result)

    # fungsi cosine similarity
    def CosSimilarity(self, vec1,vec2):
        result = 0.0;
        dotProduct = 0.0;

        for i in range(len(vec1)):
            dotProduct+=(vec1[i])*(vec2[i]);

        skalarVec1  = 0;
        for e in vec1:
            skalarVec1 += (e)*(e);
        skalarVec1 = math.sqrt(skalarVec1)

        skalarVec2  = 0;
        for e in vec2:
            skalarVec2 += (e)*(e);
        skalarVec2 = math.sqrt(skalarVec2)

        return dotProduct/(skalarVec1*skalarVec2)

    def batch_extractor(self,images_path):
        folders = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

        i = 0
        for f in folders:
            print ('Extracting features from image %s' % f)
            name = f.split('/')[-1]
            #print(name)
            self.result[name] = self.extract_features(f)

    def readFromCsv(self):
        with open('result_file.csv', mode='r') as result_file:
            csv_reader = csv.reader(result_file, delimiter=',')
            line_count = 0
            #result = {}
            print(csv_reader)
            for row in csv_reader:
                #print(row)
                if (len(row)==0): continue
                key = row[0].split('\\')[-1];
                row.pop(0);
                temp = []
                for e in row:
                    temp.append(float(e))
                self.result[key] = temp;

    def saveToCsv(self):
        with open('result_file.csv', mode='w') as result_file:
            result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for key in self.result:
                temp = []
                for e in self.result[key]:
                    temp.append(str(e))
                temp= [key] + temp
                result_writer.writerow(temp)

    def show_img(self,path):
        img = imread(path)
        plt.imshow(img)
        plt.show()

    def findSimiliar(self):
        print("process")
        pathFolder = self.pathDir
        print(pathFolder)
        #self.batch_extractor(pathFolder+'\\Reference')
        #self.saveToCsv();

        imageTargetName = self.fileName

        vectorTarget = self.extract_features(imageTargetName)


        self.readFromCsv();

        print("---Pilihan metode---\n1.Cos Similarity\n2.Euclidan Distance")
        #metode = int(input("Masukkan input : "))
        if (str(self.option)=="Distance Method"):
            metode = 2;
        else:
            metode = 1;
        resultComparison = []
        if (metode==1):
            for key in self.result:
                hasil = self.CosSimilarity(self.result[key],vectorTarget)
                resultComparison.append((hasil,key))
            resultComparison.sort(reverse = True);
        elif(metode==2):
            for key in self.result:
                hasil = self.dist(self.result[key],vectorTarget)
                resultComparison.append((hasil,key))
            resultComparison.sort();

        #self.show_img(imageTargetName)
        refDir = self.pathDir + '\\Reference\\'
        print(len(resultComparison))
        for i in range(10):
            print(resultComparison[i][0]);
            print(os.path.join(refDir,resultComparison[i][1]));
            pixmap = QtGui.QPixmap(os.path.join(refDir,resultComparison[i][1])) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageRes.width(), self.imageRes.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imageRes.setPixmap(pixmap) # Set the pixmap onto the label
            self.imageRes.setAlignment(QtCore.Qt.AlignCenter)
            break
            #self.show_img(os.path.join(refDir,resultComparison[i][1]));

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
