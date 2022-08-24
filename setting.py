from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Setting(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(Form)

        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 50, 290, 100))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 50, 290, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 50, 290, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(900, 50, 290, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        
        
        #Add reg
        self.pushButton_addr = QtWidgets.QPushButton(Form)
        self.pushButton_addr.setGeometry(QtCore.QRect(0, 700, 140, 100))
        self.pushButton_addr.setObjectName("pushButton_addr")
        #delete reg 
        self.pushButton_delr = QtWidgets.QPushButton(Form)
        self.pushButton_delr.setGeometry(QtCore.QRect(150, 700, 140, 100))
        self.pushButton_delr.setObjectName("pushButton_delr")
        
        #Add cof
        self.pushButton_addc = QtWidgets.QPushButton(Form)
        self.pushButton_addc.setGeometry(QtCore.QRect(300, 700, 140, 100))
        self.pushButton_addc.setObjectName("pushButton_addc")
        #delete cof
        self.pushButton_delc = QtWidgets.QPushButton(Form)
        self.pushButton_delc.setGeometry(QtCore.QRect(450, 700, 140, 100))
        self.pushButton_delc.setObjectName("pushButton_delc")
        
        #Add mt
        self.pushButton_addm = QtWidgets.QPushButton(Form)
        self.pushButton_addm.setGeometry(QtCore.QRect(600, 700, 140, 100))
        self.pushButton_addm.setObjectName("pushButton_addm")
        #delete mt
        self.pushButton_delm = QtWidgets.QPushButton(Form)
        self.pushButton_delm.setGeometry(QtCore.QRect(750, 700, 140, 100))
        self.pushButton_delm.setObjectName("pushButton_delm")
        
        #Add food
        self.pushButton_addf = QtWidgets.QPushButton(Form)
        self.pushButton_addf.setGeometry(QtCore.QRect(900, 700, 140, 100))
        self.pushButton_addf.setObjectName("pushButton_addf")
        #delete food
        self.pushButton_delf = QtWidgets.QPushButton(Form)
        self.pushButton_delf.setGeometry(QtCore.QRect(1050, 700, 140, 100))
        self.pushButton_delf.setObjectName("pushButton_delf")
        
        #Register table
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget) 
        self.tableWidget.setGeometry(QtCore.QRect(0, 160, 290, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        
        #Coffee
        self.tableWidget1 = QtWidgets.QTableWidget(self.centralwidget) 
        self.tableWidget1.setGeometry(QtCore.QRect(300, 160, 290, 400))
        self.tableWidget1.setObjectName("tableWidget")
        self.tableWidget1.setColumnCount(3)
        self.tableWidget1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, item)
        self.tableWidget1.horizontalHeader().setDefaultSectionSize(70)
        
        
        #Milk Tea Table
        self.tableWidget2 = QtWidgets.QTableWidget(self.centralwidget) 
        self.tableWidget2.setGeometry(QtCore.QRect(600, 160, 290, 400))
        self.tableWidget2.setObjectName("tableWidget")
        self.tableWidget2.setColumnCount(3)
        self.tableWidget2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(2, item)
        self.tableWidget2.horizontalHeader().setDefaultSectionSize(70)
        
        #Food Table
        self.tableWidget3 = QtWidgets.QTableWidget(self.centralwidget) 
        self.tableWidget3.setGeometry(QtCore.QRect(900, 160, 290, 400))
        self.tableWidget3.setObjectName("tableWidget")
        self.tableWidget3.setColumnCount(3)
        self.tableWidget3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget3.setHorizontalHeaderItem(2, item)
        self.tableWidget3.horizontalHeader().setDefaultSectionSize(70)
        
        
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(1150, 750, 93, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        
        
        #############TEXT BOX################
        self.text1 = QtWidgets.QTextEdit(Form)
        self.text1.setGeometry(QtCore.QRect(0, 600, 280, 100))
        self.text1.setObjectName("Text_1")


        self.text2 = QtWidgets.QTextEdit(Form)
        self.text2.setGeometry(QtCore.QRect(300, 600, 280, 100))
        self.text2.setObjectName("Text_2")
        
        self.text3 = QtWidgets.QTextEdit(Form)
        self.text3.setGeometry(QtCore.QRect(600, 600, 280, 100))
        self.text3.setObjectName("Text_3")
        
        self.text4 = QtWidgets.QTextEdit(Form)
        self.text4.setGeometry(QtCore.QRect(900, 600, 280, 100))
        self.text4.setObjectName("Text_4")
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Setting"))
        Form.setWindowIcon(QIcon('./picture/logo.jpg'))
        self.pushButton.setText(_translate("Form", "Registration"))
        self.pushButton_2.setText(_translate("Form", "Coffee Menu"))
        self.pushButton_3.setText(_translate("Form", "Milk Tea Menu"))
        self.pushButton_4.setText(_translate("Form", "Food Menu"))     
        self.pushButton_6.setText(_translate("Form", "Back"))
        self.pushButton_addr.setText(_translate("Form", "Add"))

        self.pushButton_delr.setText(_translate("Form", "Delete"))
        self.pushButton_addc.setText(_translate("Form", "Add"))
        self.pushButton_delc.setText(_translate("Form", "Delete"))     
        self.pushButton_addm.setText(_translate("Form", "Add"))
        self.pushButton_delm.setText(_translate("Form", "Delete"))     
        self.pushButton_addf.setText(_translate("Form", "Add"))
        self.pushButton_delf.setText(_translate("Form", "Delete"))
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "owner"))
        
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item"))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        
        item = self.tableWidget2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item"))
        item = self.tableWidget2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))

        
        item = self.tableWidget3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item"))
        item = self.tableWidget3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))

