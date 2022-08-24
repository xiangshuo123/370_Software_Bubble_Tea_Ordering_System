from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon,QPixmap

class Ui_Coffee(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(728, 459)
        self.pushButton = QtWidgets.QPushButton(Form)
        # setGeometry()
        self.pushButton.setGeometry(QtCore.QRect(40, 190, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 190, 93, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 190, 93, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 400, 93, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 400, 93, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(620, 400, 93, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(62, 170, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(65, 140, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 121, 111))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(280, 170, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(295, 140, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(240, 10, 131, 111))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(500, 170, 72, 15))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(514, 140, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(460, 10, 131, 111))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(60, 380, 72, 15))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(63, 360, 51, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(30, 250, 121, 101))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(280, 380, 72, 15))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(280, 360, 131, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(240, 250, 131, 101))
        self.label_15.setObjectName("label_15")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Coffee Menu"))
        Form.setWindowIcon(QIcon("./Picture/normal.png"))
        self.pushButton.setText(_translate("Form", "Add"))
        self.pushButton_2.setText(_translate("Form", "Add"))
        self.pushButton_3.setText(_translate("Form", "Add"))
        self.pushButton_4.setText(_translate("Form", "Add"))
        self.pushButton_5.setText(_translate("Form", "Add"))
        self.pushButton_6.setText(_translate("Form", "Back"))
        self.label.setText(_translate("Form", "m1"))
        self.label_2.setText(_translate("Form", "Cappuccino"))
        self.label_3.setText(_translate("Form", "TextLabel"))

        self.label_3.setScaledContents(True)
        self.label_4.setText(_translate("Form", "m2"))
        self.label_5.setText(_translate("Form", "Latte"))
        self.label_6.setText(_translate("Form", "TextLabel"))

        self.label_6.setScaledContents(True)
        self.label_7.setText(_translate("Form", "m3"))
        self.label_8.setText(_translate("Form", "Mocha"))
        self.label_9.setText(_translate("Form", "TextLabel"))

        self.label_9.setScaledContents(True)
        self.label_10.setText(_translate("Form", "m4"))
        self.label_11.setText(_translate("Form", "Americano"))
        self.label_12.setText(_translate("Form", "TextLabel"))

        self.label_12.setScaledContents(True)
        self.label_13.setText(_translate("Form", "m5"))
        self.label_14.setText(_translate("Form", "Caramel macchiato"))
        self.label_15.setText(_translate("Form", "TextLabel"))

        self.label_15.setScaledContents(True)