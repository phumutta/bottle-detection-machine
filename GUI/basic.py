# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        Form.setMaximumSize(QtCore.QSize(16777213, 16777215))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(-20, -30, 1281, 721))
        self.graphicsView.setStyleSheet("background: url(D:ObjectDetection.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 110, 891, 501))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1010, 530, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(3, 219, 172)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1010, 440, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(3, 219, 172)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(1020, 100, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(1020, 210, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.user_id = QtWidgets.QLabel(Form)
        self.user_id.setGeometry(QtCore.QRect(1020, 160, 141, 41))
        self.user_id.setStyleSheet("background-color: rgb(3, 219, 172)")
        self.user_id.setText("")
        self.user_id.setObjectName("user_id")
        self.user_point = QtWidgets.QLabel(Form)
        self.user_point.setGeometry(QtCore.QRect(1020, 260, 141, 41))
        self.user_point.setStyleSheet("background-color: rgb(3, 219, 172);")
        self.user_point.setText("")
        self.user_point.setObjectName("user_point")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Finish"))
        self.pushButton_2.setText(_translate("Form", "START"))
        self.label_2.setText(_translate("Form", "USER_ID"))
        self.label_3.setText(_translate("Form", "POINT"))
