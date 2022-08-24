from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Promotion(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(639, 335)
        # Discount on different category
        # promotion1
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 240, 93, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 240, 93, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        

        #Back
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(620, 400, 93, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Promotions"))
        Form.setWindowIcon(QIcon('./picture/logo.jpgjpg'))
        self.pushButton.setText(_translate("Form", "Discount 1"))
        self.pushButton_2.setText(_translate("Form", "Discount 2"))
        self.pushButton_6.setText(_translate("Form", "Back"))
