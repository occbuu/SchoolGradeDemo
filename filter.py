# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os.path
import json

class Ui_filterDialog(object):
    def setupUi(self, filterDialog):
        filterDialog.setObjectName("filterDialog")
        filterDialog.resize(1152, 679)
        self.label = QtWidgets.QLabel(filterDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(filterDialog)
        self.frame.setGeometry(QtCore.QRect(20, 30, 831, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.radioClassName = QtWidgets.QRadioButton(self.frame)
        self.radioClassName.setGeometry(QtCore.QRect(10, 20, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.radioClassName.setFont(font)
        self.radioClassName.setObjectName("radioClassName")
        self.cboClassName = QtWidgets.QComboBox(self.frame)
        self.cboClassName.setGeometry(QtCore.QRect(120, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cboClassName.setFont(font)
        self.cboClassName.setObjectName("cboClassName")
        self.radioGender = QtWidgets.QRadioButton(self.frame)
        self.radioGender.setGeometry(QtCore.QRect(360, 20, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.radioGender.setFont(font)
        self.radioGender.setObjectName("radioGender")
        self.cboGender = QtWidgets.QComboBox(self.frame)
        self.cboGender.setGeometry(QtCore.QRect(440, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cboGender.setFont(font)
        self.cboGender.setObjectName("cboGender")
        self.radioNo = QtWidgets.QRadioButton(self.frame)
        self.radioNo.setGeometry(QtCore.QRect(700, 20, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.radioNo.setFont(font)
        self.radioNo.setObjectName("radioNo")
        self.radioNo.setChecked(True)
        self.pushButton = QtWidgets.QPushButton(filterDialog)
        self.pushButton.setGeometry(QtCore.QRect(1030, 30, 93, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(filterDialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 1101, 551))
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName("tableWidget")
        ####
        self.pushButton.clicked.connect(self.filterStudent)
        ####
        self.addClassName()
        self.addGender()
        ####
        self.retranslateUi(filterDialog)
        QtCore.QMetaObject.connectSlotsByName(filterDialog)

    def retranslateUi(self, filterDialog):
        _translate = QtCore.QCoreApplication.translate
        filterDialog.setWindowTitle(_translate("filterDialog", "Filter Student List"))
        self.label.setText(_translate("filterDialog", "Filter by:"))
        self.radioClassName.setText(_translate("filterDialog", "Class Name"))
        self.radioGender.setText(_translate("filterDialog", "Gender"))
        self.radioNo.setText(_translate("filterDialog", "No Criteria"))
        self.pushButton.setText(_translate("filterDialog", "OK"))

    def addGender(self):
        s = ["Female","Male"]
        self.cboGender.addItems(s)

    def addClassName(self):
        with open("classes.json",'r', encoding= 'utf-8') as f:
            lst = json.load(f)
            self.cboClassName.addItems(lst)

    def filterStudent(self):
        data = []
        with open('students.json', 'r', encoding='utf-8') as f:
            if os.stat('students.json').st_size != 0:
                data = json.load(f)
        if self.radioClassName.isChecked():
            dat =[]
            cls = self.cboClassName.currentText()
            if cls != "" and cls != None:
                for i in data:
                    if i["class"] == cls:
                        dat.append(i)
            data = dat
        elif self.radioGender.isChecked():
            dat = []
            gen = self.cboGender.currentText()
            if gen != "" and gen != None:
                c = False
                if gen.lower() == "male":
                    c = True
                for i in data:
                    if i["gender"] == c:
                        dat.append(i)
            data = dat
        if len(data)>0:
            self.dataToTable(data)
        else:
            self.tableWidget.clearContents()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            # setting message for Message Box
            msg.setText("Không tìm thấy dữ liệu ! ")
            # setting Message box window title
            msg.setWindowTitle("Thông báo !!")
            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)
            # start the app
            retval = msg.exec_()


    def dataToTable(self, data):
        keys=["studentID", "class", "name", "email","phone","gender",
                 "notifyBy","english","science","math",
                 "art","history","music","gpa"]
        self.tableWidget.setHorizontalHeaderLabels(keys)
        self.tableWidget.clearContents()
        for i in range(len(data)):
            st = data[i]
            for j in range(len(keys)):
                if j ==6:
                    s = ",".join(st[keys[j]]).lower()
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(s))
                elif j == 5:
                    if st[keys[j]] == True:
                        self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem("Male"))
                    else:
                        self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem("Female"))
                elif j < 14:
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(st[keys[j]])))
        self.tableWidget.resizeColumnsToContents()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    filterDialog = QtWidgets.QDialog()
    ui = Ui_filterDialog()
    ui.setupUi(filterDialog)
    filterDialog.show()
    sys.exit(app.exec_())
