# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'out.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from os import system
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle("Output")
        Form.resize(273, 104)
        Form.setMinimumSize(QtCore.QSize(273, 104))
        Form.setMaximumSize(QtCore.QSize(273, 104))

        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setGeometry(QtCore.QRect(10, 60, 111, 30))
        self.btn_save.setText("Save")
        self.btn_save.setObjectName("btn_save")
        self.btn_save.clicked.connect(lambda: self.save())

        self.btn_done = QtWidgets.QPushButton(Form)
        self.btn_done.setGeometry(QtCore.QRect(170, 60, 80, 30))
        self.btn_done.setText("Done")
        self.btn_done.setObjectName("btn_done")
        self.btn_done.clicked.connect(lambda: Form.close())

        self.txt_name = QtWidgets.QLineEdit(Form)
        self.txt_name.setGeometry(QtCore.QRect(10, 10, 113, 30))
        self.txt_name.setText("")
        self.txt_name.setPlaceholderText("output.wav")
        self.txt_name.setObjectName("txt_name")

        self.btn_play = QtWidgets.QPushButton(Form)
        self.btn_play.setGeometry(QtCore.QRect(170, 10, 80, 30))
        self.btn_play.setText("Play")
        self.btn_play.setObjectName("btn_play")
        self.btn_play.clicked.connect(lambda: self.play())

        self.directory = "out_audio/"
        self.filename = "output"

        QtCore.QMetaObject.connectSlotsByName(Form)

    def play(self):
        system("mpv "+self.directory+self.filename+".wav")

    def save(self):
        self.filename = self.txt_name.text()
        system("cp "+self.directory+"output.wav "+self.directory+self.filename+".wav")
        system("echo saved as "+self.directory+self.filename+".wav")