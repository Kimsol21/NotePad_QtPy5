# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'x:\PyQT_Tutorial\NotePad\find.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(492, 124)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 321, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 25))
        self.label.setObjectName("label")
        self.pushButton_findnext = QtWidgets.QPushButton(Dialog)
        self.pushButton_findnext.setEnabled(False)
        self.pushButton_findnext.setGeometry(QtCore.QRect(410, 10, 75, 25))
        self.pushButton_findnext.setObjectName("pushButton_findnext")
        self.pushButton_cancle = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancle.setGeometry(QtCore.QRect(410, 40, 75, 25))
        self.pushButton_cancle.setObjectName("pushButton_cancle")
        self.checkBox_CaseSensitive = QtWidgets.QCheckBox(Dialog)
        self.checkBox_CaseSensitive.setGeometry(QtCore.QRect(10, 70, 111, 16))
        self.checkBox_CaseSensitive.setObjectName("checkBox_CaseSensitive")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(230, 60, 171, 51))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_down = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_down.setGeometry(QtCore.QRect(80, 20, 61, 16))
        self.radioButton_down.setChecked(True)
        self.radioButton_down.setObjectName("radioButton_down")
        self.radioButton_up = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_up.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.radioButton_up.setChecked(False)
        self.radioButton_up.setObjectName("radioButton_up")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "찾기"))
        self.label.setText(_translate("Dialog", "찾을 내용 : "))
        self.pushButton_findnext.setText(_translate("Dialog", "다음 찾기"))
        self.pushButton_cancle.setText(_translate("Dialog", "취소"))
        self.checkBox_CaseSensitive.setText(_translate("Dialog", "대/소문자 구분"))
        self.checkBox_2.setText(_translate("Dialog", "주위에 배치"))
        self.groupBox.setTitle(_translate("Dialog", "방향"))
        self.radioButton_down.setText(_translate("Dialog", "아래로"))
        self.radioButton_up.setText(_translate("Dialog", "위로"))

