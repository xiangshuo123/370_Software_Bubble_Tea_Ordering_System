from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.label_0.setObjectName("label_8")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect( 400, 20, 200, 100))
        self.pushButton_2.setObjectName("pushButton_2") # Milk Tea button

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 130, 200, 100))
        self.pushButton_3.setObjectName("pushButton_3") # Fresh Tea button

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 240, 200, 100))
        self.pushButton_4.setObjectName("pushButton_4") #Coffee Buttom

#        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
#        self.pushButton_9.setGeometry(QtCore.QRect(400, 350, 200, 100))
#        self.pushButton_9.setObjectName("pushButton_9") #Snacks Buttom

        # Promotions Setting
    
    
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(950, 650, 200, 100))
        self.pushButton_10.setObjectName("pushButton_10") 
 
        # Cashier start working
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(1000, 10, 100, 50))
        self.pushButton_11.setObjectName("pushButton_11") 
        # Cashier finish working
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(1100, 10, 100, 50))
        self.pushButton_12.setObjectName("pushButton_12") 
        # Brasier start working
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(1000, 65, 100, 50))
        self.pushButton_13.setObjectName("pushButton_13") 
        # Brasier finish working
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(1100, 65, 100, 50))
        self.pushButton_14.setObjectName("pushButton_14") 
        
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(1000, 125, 200, 50))
        self.pushButton_15.setObjectName("pushButton_15") 
        
        

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 20, 120, 100))
        self.label_6.setObjectName("label_6")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 20, 120, 100))
        self.label_5.setObjectName("label_5")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 130, 100))
        self.label_7.setObjectName("label_7")
        
        # Order table display
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)   
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 300, 500))
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 650, 145, 100))
        self.pushButton_5.setObjectName("pushButton_5")                    #delete
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 550, 200, 100))      #Checkout
        self.pushButton_6.setObjectName("pushButton_6") 
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)       #Print
        self.pushButton_7.setGeometry(QtCore.QRect(400, 650, 200, 100))
        self.pushButton_7.setObjectName("pushButton_7")
        
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 650, 150, 100))  #nextorder
        self.pushButton_8.setObjectName("pushButton_8")
        
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget) #codiment
        self.pushButton_9.setGeometry(QtCore.QRect(610, 650, 200, 100))  
        self.pushButton_9.setObjectName("pushButton_8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(650, 200, 500, 400))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 893, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rayla Cafe Order System"))
        MainWindow.setWindowIcon(QIcon("./Picture/logo.jpgjpg"))
        self.pushButton_2.setText(_translate("MainWindow", "COFFEE"))
        self.pushButton_3.setText(_translate("MainWindow", "MILK TEA"))
        self.pushButton_4.setText(_translate("MainWindow", "FOOD"))
#        self.pushButton_9.setText(_translate("MainWindow", "Snack"))
        self.label_6.setText(_translate("MainWindow", "Order Number:"))
        self.label_7.setText(_translate("MainWindow", "Quick Service Order"))
        self.label_5.setText(_translate("MainWindow", "x"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quality"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        self.pushButton_5.setText(_translate("MainWindow", "Delete the Item"))
        self.pushButton_6.setText(_translate("MainWindow", "Checkout"))
        self.pushButton_7.setText(_translate("MainWindow", "Print the Receipt"))
        self.pushButton_8.setText(_translate("MainWindow", "Next Order"))
        self.pushButton_9.setText(_translate("MainWindow", "Print the Condiment"))
        self.pushButton_10.setText(_translate("MainWindow", "Set Promotions"))
        self.pushButton_11.setText(_translate("MainWindow", "Cashier On"))
        self.pushButton_12.setText(_translate("MainWindow", "Cashier Off"))
        self.pushButton_13.setText(_translate("MainWindow", "Barista On"))
        self.pushButton_14.setText(_translate("MainWindow", "Barista Off"))
        self.pushButton_15.setText(_translate("MainWindow", "Setting"))
        self.label_8.setText(_translate("MainWindow", "Picture"))
        self.label_0.setText(_translate("MainWindow", "Picture"))

