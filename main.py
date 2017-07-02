import sys
import cv2
import numpy as np
from ui import *
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication,QFileDialog
from PyQt5.QtGui import QPixmap

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.loadimage)
        self.ui.pushButton_2.clicked.connect(self.gradient)
        self.ui.radioButton.clicked.connect(self.rb1)
        self.ui.radioButton_2.clicked.connect(self.rb2)
        self.show()

    def rb1(self):
        self.ui.comboBox.setVisible(True)
        self.ui.comboBox_2.setVisible(False)

    def rb2(self):
        self.ui.comboBox_2.setVisible(True)
        self.ui.comboBox.setVisible(False)

    def loadimage(self):
        self.fname = QFileDialog.getOpenFileName(self,'Open File', '/')[0]
        pixmap = QPixmap(self.fname)
        self.ui.label.setPixmap(pixmap)
        self.ui.groupBox.setVisible(True)
        self.ui.groupBox_3.setVisible(True)

    def gradient(self):
        img = cv2.imread(self.fname)
        if self.ui.radioButton.isChecked():
            if self.ui.comboBox.currentIndex() == -1:
                QMessageBox.question(self,'Error','Please select a variant!!',QMessageBox.Ok)
            if self.ui.comboBox.currentIndex() == 0:
                res_img = cv2.applyColorMap(img,cv2.COLORMAP_JET)
                cv2.imwrite("gradient.jpg",res_img)
                pixmap = QPixmap("gradient.jpg")
                self.ui.label_2.setPixmap(pixmap)
                self.ui.groupBox_2.setVisible(True)
            if self.ui.comboBox.currentIndex() == 1:
                res_img = cv2.applyColorMap(img, cv2.COLORMAP_HSV)
                cv2.imwrite("gradient.jpg", res_img)
                pixmap = QPixmap("gradient.jpg")
                self.ui.label_2.setPixmap(pixmap)
                self.ui.groupBox_2.setVisible(True)
            if self.ui.comboBox.currentIndex() == 2:
                res_img = cv2.applyColorMap(img, cv2.COLORMAP_COOL)
                cv2.imwrite("gradient.jpg", res_img)
                pixmap = QPixmap("gradient.jpg")
                self.ui.label_2.setPixmap(pixmap)
                self.ui.groupBox_2.setVisible(True)
            if self.ui.comboBox.currentIndex() == 3:
                res_img = cv2.applyColorMap(img, cv2.COLORMAP_RAINBOW)
                cv2.imwrite("gradient.jpg", res_img)
                pixmap = QPixmap("gradient.jpg")
                self.ui.label_2.setPixmap(pixmap)
                self.ui.groupBox_2.setVisible(True)
        if self.ui.radioButton_2.isChecked():
            if self.ui.comboBox_2.currentIndex() == -1:
                QMessageBox.question(self, 'Error', 'Please select a variant!!', QMessageBox.Ok)
            if self.ui.comboBox_2.currentIndex() == 0:
                lst = np.zeros((256, 1, 3), dtype=np.uint8)
                for i in range(256):
                    for j in range(3):
                        lst[i,0,j] = 255-i
                res_img=cv2.LUT(img,lst)
                cv2.imwrite("gradient.jpg", res_img)
                pixmap = QPixmap("gradient.jpg")
                self.ui.label_2.setPixmap(pixmap)
                self.ui.groupBox_2.setVisible(True)
            if self.ui.comboBox_2.currentIndex() == 1:
                lst1 = np.zeros((256, 1, 3), dtype=np.uint8)
                for i in range(256):
                    lst1[i,0,0] = 255-i
                for i in range(256):
                    lst1[i,0,1] = abs(50-i)
                for i in range(256):
                    lst1[i,0,2] = 255 - (i // 4)
                res_img = cv2.LUT(img,lst1)
                cv2.imwrite("gradient.jpg", res_img)
                pixmap = QPixmap("gradient.jpg")
                self.ui.label_2.setPixmap(pixmap)
                self.ui.groupBox_2.setVisible(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fm = Form()
    sys.exit(app.exec())
