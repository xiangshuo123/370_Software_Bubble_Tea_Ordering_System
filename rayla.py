from raylamain import *
from coffee import *
from milktea import *
from food import *
from promotion import *
from setting import *
import sys
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import SQLconnector as sql
import SQLoperation as sqlop

class Rayla_Main(QMainWindow):
    def __init__(self):
        # initial the interface
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        # assign function to buttons
        btn_del = self.main_ui.pushButton_5
        btn_del.clicked.connect(self.order_del)
        btn_delone = self.main_ui.pushButton_8
        btn_delone.clicked.connect(self.next_order)
        btn_num = self.main_ui.pushButton_6
        btn_num.clicked.connect(self.order_num)
        self.btn_tip = self.main_ui.pushButton_7
        self.btn_tip.clicked.connect(self.order_tip)
        self.btn_tip.setEnabled(False)

        self.btn_info = self.main_ui.pushButton_9
        self.btn_info.clicked.connect(self.order_info)
        # set button not work
        self.btn_cashon = self.main_ui.pushButton_11
        self.btn_cashon.clicked.connect(self.cashier_on)
        
        self.btn_cashoff = self.main_ui.pushButton_12
        self.btn_cashoff.clicked.connect(self.cashier_off)
#        self.btn_cashoff.setEnabled(False)

        self.btn_baron = self.main_ui.pushButton_13
        self.btn_baron.clicked.connect(self.bar_on)
        
        self.btn_baroff = self.main_ui.pushButton_14
        self.btn_baroff.clicked.connect(self.bar_off)
#        self.btn_baroff.setEnabled(False)

        
        self.btn_info.setEnabled(False)
        self.num = []
        self.new_num = []

    # Main display
    def background(self):
        #set background color and logo
        self.main_ui.label_0.setPixmap(QPixmap('./Picture/wood.jpg'))
        self.main_ui.label_0.setScaledContents(True)
        self.main_ui.label_8.setPixmap(QPixmap('./Picture/Rayla Cafe.jpg'))
        self.main_ui.label_8.setScaledContents(True)
        self.order_number = 1
        self.main_ui.label_5.setText(str(self.order_number))
        raylamain.show()
        
    def cashier_on(self):
        global start_time
        start_time = datetime.datetime.now()
        self.btn_cashoff.setEnabled(True)
        with open("Cashier_attendance.txt", "a") as f:
            f.write("Cashier start @"+ str(start_time)+"\n")
            f.close()
        return start_time

    def cashier_off(start_time):
        end_time = datetime.datetime.now()
        print(start_time)
#        diff = start_time - end_time
        with open("Cashier_attendance.txt", "a") as f:
            f.write("Cashier End @"+ str(end_time)+"\n")
#            f.write("The time period is "+ str(diff)+"\n")
            f.close()

    def bar_on(self):
        global start_time
        start_time = datetime.datetime.now()
#        self.btn_baroff.setEnabled(True)
        with open("barista_attendance.txt", "a") as f:
            f.write("Cashier start @"+ str(start_time)+"\n")
            f.close()
        return start_time

    def bar_off(start_time):
        end_time = datetime.datetime.now()
#        deltaTime = datetime.strptime()
        with open("barista_attendance.txt", "a") as f:
            f.write("Barista End @"+ str(end_time)+"\n")
#            f.write("The time period is "+ str(end_time - start_time)+"\n")
            f.close()

    def order_del(self):
        row_index = raylamain.main_ui.tableWidget.currentRow()
        if row_index != -1:
            raylamain.main_ui.tableWidget.removeRow(row_index)
            
    def next_order(self):        
        button = QMessageBox.information(self, "Next Order", "Would you like to start next order?", QMessageBox.Yes | QMessageBox.No)
        if button == QMessageBox.Yes:
            self.btn_tip.setEnabled(False)
            self.btn_info.setEnabled(False)
            self.order_number = self.order_number +1
            self.main_ui.label_5.setText(str(self.order_number))
            for row_index in range(raylamain.main_ui.tableWidget.rowCount()):
                raylamain.main_ui.tableWidget.removeRow(0)
                # ERROR about cannot clear the table

    # Check out
    def order_num(self):
        # Set Print button available
        self.btn_tip.setEnabled(True)
        self.btn_info.setEnabled(True)

        for row_index in range(raylamain.main_ui.tableWidget.rowCount()):
            self.num.append(raylamain.main_ui.tableWidget.item(row_index, 2).text())

        # price str - int
        self.new_num = eval('[' + (','.join(self.num)) + ']')
        # summ up
        self.money = sum(self.new_num)

        button = QMessageBox.information(self, "Here or Togo", "Would you like your drink to go?", QMessageBox.Yes | QMessageBox.No)
        if button == QMessageBox.No:
                    QMessageBox.information(self, "Payment success", "Payment success. Please wait your order here!", QMessageBox.Yes)
        else:
                    QMessageBox.information(self, "Payment success", "Payment success. Please wait your order to be packing!", QMessageBox.Yes)

    # Print the receipts
    def order_tip(self):
        # Open the txt file
        with open("RaylaReceipt.txt", "w") as f:
            for row_index in range(raylamain.main_ui.tableWidget.rowCount()):
                for column_index in range(raylamain.main_ui.tableWidget.columnCount()):
                    # pass the receipt information to the txt file 
                    f.write(raylamain.main_ui.tableWidget.item(row_index, column_index).text() + "\n")
            f.write("Total:" + "$" + str(self.money))
        f.close()
        QMessageBox.information(self, "OK", "The Receipt is successfully printed for customer", QMessageBox.Yes)

    # Print the condiments
    def order_info(self):
        # Open the txt file
        with open("condiment.txt", "w") as f:
            for row_index in range(raylamain.main_ui.tableWidget.rowCount()):
                for column_index in range(raylamain.main_ui.tableWidget.columnCount()):
                    # pass the receipt information to the txt file 
                    f.write(raylamain.main_ui.tableWidget.item(row_index, column_index).text() + "\n")
        f.close()
        QMessageBox.information(self, "OK", "The Order info is successfully printed for Barista", QMessageBox.Yes)

        
class Coffee(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.coffee_ui = Ui_Coffee()
        self.coffee_ui.setupUi(self)

        # initial number of click of each item
        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0
        self.bt4 = 0
        self.bt6 = 0
        # initial back click times
        self.bt5 = 0
        # bind the buttom 
        btn_Cappuccino = self.coffee_ui.pushButton
        btn_Cappuccino.clicked.connect(self.order_Cappuccino)
        btn_Latte = self.coffee_ui.pushButton_2
        btn_Latte.clicked.connect(self.order_Latte)
        btn_Mocha = self.coffee_ui.pushButton_3
        btn_Mocha.clicked.connect(self.order_Mocha)
        btn_Americano = self.coffee_ui.pushButton_4
        btn_Americano.clicked.connect(self.order_Americano)
        btn_ice = self.coffee_ui.pushButton_5
        btn_ice.clicked.connect(self.order_ice)
        btn_return = self.coffee_ui.pushButton_6
        btn_return.clicked.connect(self.nor_show)

    # Specific order interface
    def nor_order(self):
        self.coffee_ui.label_3.setPixmap(QPixmap('./picture/coffee.jpg'))
        self.coffee_ui.label_3.setScaledContents(True)
        self.coffee_ui.label_6.setPixmap(QPixmap('./picture/coffee.jpg'))
        self.coffee_ui.label_6.setScaledContents(True)
        self.coffee_ui.label_9.setPixmap(QPixmap('./picture/coffee.jpg'))
        self.coffee_ui.label_9.setScaledContents(True)
        self.coffee_ui.label_12.setPixmap(QPixmap('./picture/coffee.jpg'))
        self.coffee_ui.label_12.setScaledContents(True)
        self.coffee_ui.label_15.setPixmap(QPixmap('./picture/coffee.jpg'))
        self.coffee_ui.label_15.setScaledContents(True)
        # Set Price
        self.price_Cappuccino = float(sql.fetch_coffee("Cappuccino")[1])
        self.price_Latte = float(sql.fetch_coffee("Latte")[1])
        self.price_Mocha = float(sql.fetch_coffee("Mocha")[1])
        self.price_Americano = float(sql.fetch_coffee("Americano")[1])
        self.price_Macchiato = float(sql.fetch_coffee("Caramel Macchiato")[1])
        # Display Price
        self.coffee_ui.label.setText("$"+str(self.price_Cappuccino)+"Cup")
        self.coffee_ui.label_4.setText("$"+str(self.price_Latte)+"Cup")
        self.coffee_ui.label_7.setText("$"+str(self.price_Mocha)+"Cup")
        self.coffee_ui.label_10.setText("$"+str(self.price_Americano)+"Cup")
        self.coffee_ui.label_13.setText("$"+str(self.price_Macchiato)+"Cup")
        
        coffee.show()

    # count click times
    def order_Cappuccino(self):
        self.bt1 += 1

    def order_Latte(self):
        self.bt2 += 1

    def order_Mocha(self):
        self.bt3 += 1

    def order_Americano(self):
        self.bt4 += 1


    def order_ice(self):
        self.bt5 += 1

    def nor_show(self):
        self.bt6 += 1

        # hide the window 
        coffee.hide()

        # Calculate the summ up price
        self.num_Cappuccino = self.price_Cappuccino * self.bt1
        self.num_Latte = self.price_Latte * self.bt2
        self.num_Mocha = self.price_Mocha * self.bt3
        self.num_Americano = self.price_Americano * self.bt4
        self.num_Macchiato = self.price_Macchiato * self.bt6

        # Not first enter
        if self.bt6 > 1:
            for row_index in range(raylamain.main_ui.tableWidget.rowCount()):
                # Get tableWidget's name and put together
                name.append(raylamain.main_ui.tableWidget.item(row_index, 0).text())
            if 'Cappuccino' in name:
                raylamain.main_ui.tableWidget.setItem(name.index('Cappuccino'), 1, QTableWidgetItem("×" + str(self.bt1)))
                raylamain.main_ui.tableWidget.setItem(name.index('Cappuccino'), 2, QTableWidgetItem(str(self.num_Cappuccino)))
            if 'Cappuccino' not in name:
                if self.bt1 != 0:
                    # add
                    row_count = raylamain.main_ui.tableWidget.rowCount()
                    raylamain.main_ui.tableWidget.insertRow(row_count)
                    raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(coffee.coffee_ui.label_2.text()))
                    raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_Cappuccino)))
            if 'Latte' in name:
                raylamain.main_ui.tableWidget.setItem(name.index('Latte'), 1, QTableWidgetItem("×" + str(self.bt2)))
                raylamain.main_ui.tableWidget.setItem(name.index('Latte'), 2, QTableWidgetItem(str(self.num_Latte)))
            if 'Latte' not in name:
                if self.bt2 != 0:
                    row_count = raylamain.main_ui.tableWidget.rowCount()
                    raylamain.main_ui.tableWidget.insertRow(row_count)
                    raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(coffee.coffee_ui.label_5.text()))
                    raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                    raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_Latte)))
            if 'Mocha' in name:
                raylamain.main_ui.tableWidget.setItem(name.index('Mocha'), 1, QTableWidgetItem("×" + str(self.bt3)))
                raylamain.main_ui.tableWidget.setItem(name.index('Mocha'), 2, QTableWidgetItem(str(self.num_Mocha)))
            if 'Mocha' not in name:
                if self.bt3 != 0:
                    row_count = raylamain.main_ui.tableWidget.rowCount()
                    raylamain.main_ui.tableWidget.insertRow(row_count)
                    raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(coffee.coffee_ui.label_8.text()))
                    raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt3)))
                    raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_Mocha)))
            if 'Americano'in name:
                raylamain.main_ui.tableWidget.setItem(name.index('Americano'), 1, QTableWidgetItem("×" + str(self.bt4)))
                raylamain.main_ui.tableWidget.setItem(name.index('Americano'), 2, QTableWidgetItem(str(self.num_Americano)))
            if 'Americano' not in name:
                if self.bt4 != 0:
                    row_count = raylamain.main_ui.tableWidget.rowCount()
                    raylamain.main_ui.tableWidget.insertRow(row_count)
                    raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(coffee.coffee_ui.label_11.text()))
                    raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                    raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_Americano)))
            if 'Caramel macchiato' in name:
                raylamain.main_ui.tableWidget.setItem(name.index('Caramel macchiato'), 1, QTableWidgetItem("×" + str(self.bt6)))
                raylamain.main_ui.tableWidget.setItem(name.index('Caramel macchiato'), 2, QTableWidgetItem(str(self.num_Macchiato)))
            if 'Caramel macchiato' not in name:
                if self.bt5 != 0:
                    row_count = raylamain.main_ui.tableWidget.rowCount()
                    raylamain.main_ui.tableWidget.insertRow(row_count)
                    raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(coffee.coffee_ui.label_14.text()))
                    raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt6)))
                    raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_Macchiato)))
                    
        else:
            if self.bt1 != 0:
                row_count = raylamain.main_ui.tableWidget.rowCount()
                raylamain.main_ui.tableWidget.insertRow(row_count)
                raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(coffee.coffee_ui.label_2.text()))
                raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_Cappuccino)))
            if self.bt2 != 0:
                row_count = raylamain.main_ui.tableWidget.rowCount()
                raylamain.main_ui.tableWidget.insertRow(row_count)
                raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(coffee.coffee_ui.label_5.text()))
                raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_Latte)))
            if self.bt3 != 0:
                row_count = raylamain.main_ui.tableWidget.rowCount()
                raylamain.main_ui.tableWidget.insertRow(row_count)
                raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(coffee.coffee_ui.label_8.text()))
                raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt3)))
                raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_Mocha)))
            if self.bt4 != 0:
                row_count = raylamain.main_ui.tableWidget.rowCount()
                raylamain.main_ui.tableWidget.insertRow(row_count)
                raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(coffee.coffee_ui.label_11.text()))
                raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_Americano)))
            if self.bt5 != 0:
                row_count = raylamain.main_ui.tableWidget.rowCount()
                raylamain.main_ui.tableWidget.insertRow(row_count)
                raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(coffee.coffee_ui.label_14.text()))
                raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt6)))
                raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_Macchiato)))
        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0
        self.bt4 = 0
        self.bt5 = 0


class Milktea(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.milktea_ui = Ui_Milktea()
        self.milktea_ui.setupUi(self)

        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0
        btn_bbcs = self.milktea_ui.pushButton
        btn_bbcs.clicked.connect(self.order_bbcs)
        btn_bs = self.milktea_ui.pushButton_2
        btn_bs.clicked.connect(self.order_bs)
        btn_return = self.milktea_ui.pushButton_3
        btn_return.clicked.connect(self.pac_show)

    def milktea(self):
        self.milktea_ui.label_5.setPixmap(QPixmap('./picture/blueberry.jpg'))
        self.milktea_ui.label_5.setScaledContents(True)
        self.milktea_ui.label_6.setPixmap(QPixmap('./picture/bs.jpg'))
        self.milktea_ui.label_6.setScaledContents(True)
        self.price_bbcs = float(sql.fetch_milk_tea("Blueberry Cheese Storm")[1])
        self.price_bs = float(sql.fetch_milk_tea("Brown Sugar Milk Tea")[1])
        self.milktea_ui.label.setText("$"+str(self.price_bbcs)+"/Cup")
        self.milktea_ui.label_2.setText("$"+str(self.price_bs)+"/Cup")
        milktea.show()

    def order_bbcs(self):
        self.bt1 += 1

    def order_bs(self):
        self.bt2 += 1

    def pac_show(self):
        self.bt3 += 1

        milktea.hide()

        self.num_bbcs = self.price_bbcs * self.bt1
        self.num_bs = self.price_bs * self.bt2

        if self.bt3 > 1:
            for row_index in range(raylamain.main_ui.tableWidget.rowCount()):
                name.append(raylamain.main_ui.tableWidget.item(row_index, 0).text())
            if 'Blueberry Cheese Strom' in name:
                raylamain.main_ui.tableWidget.setItem(name.index('Blueberry Cheese Strom'), 1, QTableWidgetItem("×" + str(self.bt1)))
                raylamain.main_ui.tableWidget.setItem(name.index('Blueberry Cheese Strom'), 2, QTableWidgetItem(str(self.num_bbcs)))
            if 'Blueberry Cheese Strom' not in name:
                if self.bt1 != 0:
                    row_count = raylamain.main_ui.tableWidget.rowCount()
                    raylamain.main_ui.tableWidget.insertRow(row_count)
                    raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(milktea.milktea_ui.label_3.text()))
                    raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_bbcs)))
            if 'Brown Sugar Milk Tea' in name:
                raylamain.main_ui.tableWidget.setItem(name.index('Brown Sugar Milk Tea'), 1, QTableWidgetItem("×" + str(self.bt2)))
                raylamain.main_ui.tableWidget.setItem(name.index('Brown Sugar Milk Tea'), 2, QTableWidgetItem(str(self.num_bs)))
            if 'Brown Sugar Milk Tea' not in name:
                if self.bt2 != 0:
                    row_count = raylamain.main_ui.tableWidget.rowCount()
                    raylamain.main_ui.tableWidget.insertRow(row_count)
                    raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(milktea.milktea_ui.label_4.text()))
                    raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                    raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_bs)))
        else:
            if self.bt1 != 0:
                row_count = raylamain.main_ui.tableWidget.rowCount()
                raylamain.main_ui.tableWidget.insertRow(row_count)
                raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(milktea.milktea_ui.label_3.text()))
                raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_bbcs)))
            if self.bt2 != 0:
                row_count = raylamain.main_ui.tableWidget.rowCount()
                raylamain.main_ui.tableWidget.insertRow(row_count)
                raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(milktea.milktea_ui.label_4.text()))
                raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_bs)))
        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0


class Food(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.food_ui = Ui_Food()
        self.food_ui.setupUi(self)
        self.bt1 = 0
        self.bt3 = 0
        btn_takoyaki = self.food_ui.pushButton
        btn_takoyaki.clicked.connect(self.order_takoyaki)
        btn_bbw = self.food_ui.pushButton_2
        btn_bbw.clicked.connect(self.order_bbw)
        btn_return = self.food_ui.pushButton_3
        btn_return.clicked.connect(self.act_show)

    def act_order(self):
        self.food_ui.label_4.setPixmap(QPixmap('./picture/takoyaki.jpg'))
        self.food_ui.label_4.setScaledContents(True)
        self.food_ui.label_8.setPixmap(QPixmap('./picture/bbw.jpg'))
        self.food_ui.label_8.setScaledContents(True)
        self.price_takoyaki = float(sql.fetch_food("Takoyaki")[1])
        self.price_bbw = float(sql.fetch_food("Bubble Waffle")[1])
        self.food_ui.label.setText("$"+str(self.price_takoyaki)+"/item")
        self.food_ui.label_5.setText("$"+str(self.price_bbw)+"/item")
        food.show()

    def order_takoyaki(self):
        self.bt1 += 1

    def order_bbw(self):
        QMessageBox.information(self, "Sorry", "The Item is out of stock", QMessageBox.Yes)

    def act_show(self):
        self.bt3 += 1

        food.hide()

        self.num_takoyaki = self.price_takoyaki * self.bt1

        if self.bt3 > 1:
            for row_index in range(raylamain.main_ui.tableWidget.rowCount()):
                name.append(raylamain.main_ui.tableWidget.item(row_index, 0).text())
            if 'Takoyaki' in name:
                raylamain.main_ui.tableWidget.setItem(name.index('Takoyaki'), 1, QTableWidgetItem("×" + str(self.bt1)))
                raylamain.main_ui.tableWidget.setItem(name.index('Takoyaki'), 2, QTableWidgetItem(str(self.num_takoyaki)))
            if 'Takoyaki' not in name:
                if self.bt1 != 0:
                    row_count = raylamain.main_ui.tableWidget.rowCount()
                    raylamain.main_ui.tableWidget.insertRow(row_count)
                    raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(food.food_ui.label_3.text()))
                    raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_takoyaki)))
        else:
            if self.bt1 != 0:
                row_count = raylamain.main_ui.tableWidget.rowCount()
                raylamain.main_ui.tableWidget.insertRow(row_count)
                raylamain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(food.food_ui.label_3.text()))
                raylamain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                raylamain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_takoyaki)))

                
        self.bt1 = 0
        self.bt3 = 0      


class Promotion(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.promotion_ui = Ui_Promotion()
        self.promotion_ui.setupUi(self)
        
        # initial number of lick of each promotions
        self.bt1 = 0
        self.bt2 = 0
        self.bt6 = 0

        # bind the buttons
        btn_promotion1 = self.promotion_ui.pushButton
        btn_promotion1.clicked.connect(self.set_promotion_1)
        btn_promotion2 = self.promotion_ui.pushButton_2
        btn_promotion2.clicked.connect(self.set_promotion_2)
        btn_return = self.promotion_ui.pushButton_6
        btn_return.clicked.connect(self.nor_show)
        
    def nor_promotion(self):
        
        promotion.show()
        
    def set_promotion_1(self):
        self.bt1 +=1
        
    def set_promotion_2(self):
        self.bt2 +=1
        
    def nor_show(self):
        self.bt6 +=1
        # hide the windows
        promotion.hide()


class Log_in(QtWidgets.QMainWindow):

    def __init__(self):
        super(Log_in, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 150)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 100, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 50, 100, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(50, 24, 50, 12))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(50, 54, 50, 12))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(75, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(175, 100, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.pushButton.clicked.connect(self.check_login)
        self.pushButton_2.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "log in"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Log in"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))

    def check_login(self):
        login_user = self.lineEdit.text()
        login_password = self.lineEdit_2.text()
        if sql.check_passwd(login_user, login_password):
            raylamain.show()
        else:
            QMessageBox.warning(self, "Warning", "Username or password might be incorrect!", QMessageBox.Yes)
            self.lineEdit.setFocus()


class Setting(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setting_ui = Ui_Setting()
        self.setting_ui.setupUi(self)
        
        # initial number of lick of each promotions
        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0
        self.bt4 = 0

        self.bt6 = 0

        # bind the buttons
        btn_reg = self.setting_ui.pushButton
        btn_reg.clicked.connect(self.set_reg)
        
        btn_coffee = self.setting_ui.pushButton_2
        btn_coffee.clicked.connect(self.set_coffee)
        
        btn_milktea = self.setting_ui.pushButton_3
        btn_milktea.clicked.connect(self.set_milktea)
        
        btn_food = self.setting_ui.pushButton_4
        btn_food.clicked.connect(self.set_food)

        btn_return = self.setting_ui.pushButton_6
        btn_return.clicked.connect(self.nor_show)

        self.setting_ui.pushButton_delr.clicked.connect(self.delr)
        self.setting_ui.pushButton_delc.clicked.connect(self.delc)
        self.setting_ui.pushButton_delf.clicked.connect(self.delf)
        self.setting_ui.pushButton_delm.clicked.connect(self.delm)

        self.setting_ui.pushButton_addr.clicked.connect(self.addr)
        # self.setting_ui.pushButton_addc.clicked.connect(self.addc)
        # self.setting_ui.pushButton_addf.clicked.connect(self.addf)
        # self.setting_ui.pushButton_addm.clicked.connect(self.addm)
        
    def show_setting(self):
        
        setting.show()

    # four buttons, can link TableWidget 0-3 to show content
    def set_reg(self):
        for row_index in range(self.setting_ui.tableWidget.rowCount()):
            self.setting_ui.tableWidget.removeRow(0)
        self.bt1 +=1
        data = sql.fetch_all_reg()
        row_count = self.setting_ui.tableWidget.rowCount()
        for i in data:
            self.setting_ui.tableWidget.insertRow(row_count)
            self.setting_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(i[0])))
            self.setting_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem(str(i[1])))
            self.setting_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(i[2])))
            self.setting_ui.tableWidget.setItem(row_count, 3, QTableWidgetItem(str(i[3])))

    def set_coffee(self):
        for row_index in range(self.setting_ui.tableWidget1.rowCount()):
            self.setting_ui.tableWidget1.removeRow(0)
        self.bt1 += 1
        data = sql.fetch_all_coffee()
        row_count = self.setting_ui.tableWidget1.rowCount()
        for i in data:
            self.setting_ui.tableWidget1.insertRow(row_count)
            self.setting_ui.tableWidget1.setItem(row_count, 0, QTableWidgetItem(str(i[0])))
            self.setting_ui.tableWidget1.setItem(row_count, 1, QTableWidgetItem(str(i[1])))
            self.setting_ui.tableWidget1.setItem(row_count, 2, QTableWidgetItem(str(i[2])))

    def set_milktea(self):
        self.bt3 +=1

        for row_index in range(self.setting_ui.tableWidget2.rowCount()):
            self.setting_ui.tableWidget2.removeRow(0)
        self.bt1 += 1
        data = sql.fetch_all_milktea()
        row_count = self.setting_ui.tableWidget2.rowCount()
        for i in data:
            self.setting_ui.tableWidget2.insertRow(row_count)
            self.setting_ui.tableWidget2.setItem(row_count, 0, QTableWidgetItem(str(i[0])))
            self.setting_ui.tableWidget2.setItem(row_count, 1, QTableWidgetItem(str(i[1])))
            self.setting_ui.tableWidget2.setItem(row_count, 2, QTableWidgetItem(str(i[2])))
               
    def set_food(self):
        self.bt4 +=1

        for row_index in range(self.setting_ui.tableWidget3.rowCount()):
            self.setting_ui.tableWidget3.removeRow(0)
        self.bt1 += 1
        data = sql.fetch_all_food()
        row_count = self.setting_ui.tableWidget3.rowCount()
        for i in data:
            self.setting_ui.tableWidget3.insertRow(row_count)
            self.setting_ui.tableWidget3.setItem(row_count, 0, QTableWidgetItem(str(i[0])))
            self.setting_ui.tableWidget3.setItem(row_count, 1, QTableWidgetItem(str(i[1])))
            self.setting_ui.tableWidget3.setItem(row_count, 2, QTableWidgetItem(str(i[2])))

    def addr(self):
        if self.setting_ui.tableWidget.currentRow() == -1:
            row_count = self.setting_ui.tableWidget.rowCount()
            self.setting_ui.tableWidget.insertRow(row_count)
        else:
            row_count = self.setting_ui.tableWidget.rowCount()
            name = self.setting_ui.tableWidget.item(row_count-1,1).text()
            passwd = self.setting_ui.tableWidget.item(row_count-1,2).text()
            owner = self.setting_ui.tableWidget.item(row_count - 1, 3).text()
            sql.add_user(name,passwd,owner)

    def delr(self):
        selected_user = self.setting_ui.tableWidget.currentItem().text()
        sql.delete_user(selected_user)

    def addc(self):
        if self.setting_ui.tableWidget1.currentRow() == -1:
            row_count = self.setting_ui.tableWidget1.rowCount()
            self.setting_ui.tableWidget1.insertRow(row_count)
        else:
            row_count = self.setting_ui.tableWidget1.rowCount()
            name = self.setting_ui.tableWidget1.item(row_count - 1, 1).text()
            price = self.setting_ui.tableWidget1.item(row_count - 1, 2).text()
            sql.add_coffee(name,price)

    def delc(self):
        selected = self.setting_ui.tableWidget.currentItem().text()
        sql.delete_coffee(selected)

    def addm(self):
        if self.setting_ui.tableWidget2.currentRow() == -1:
            row_count = self.setting_ui.tableWidget2.rowCount()
            self.setting_ui.tableWidget2.insertRow(row_count)
        else:
            row_count = self.setting_ui.tableWidget2.rowCount()
            name = self.setting_ui.tableWidget2.item(row_count - 1, 1).text()
            price = self.setting_ui.tableWidget2.item(row_count - 1, 2).text()
            sql.add_milk_tea(name, price)

    def delm(self):
        selected = self.setting_ui.tableWidget.currentItem().text()
        sql.delete_milk_tea(selected)

    def addf(self):
        if self.setting_ui.tableWidget3.currentRow() == -1:
            row_count = self.setting_ui.tableWidget3.rowCount()
            self.setting_ui.tableWidget3.insertRow(row_count)
        else:
            row_count = self.setting_ui.tableWidget3.rowCount()
            name = self.setting_ui.tableWidget3.item(row_count - 1, 1).text()
            price = self.setting_ui.tableWidget3.item(row_count - 1, 2).text()
            sql.add_food(name, price)

    def delf(self):
        selected = self.setting_ui.tableWidget.currentItem().text()
        sql.delete_food(selected)

    def nor_show(self):
        self.bt6 +=1
        # hide the windows
        setting.hide()            


if __name__=="__main__":
    sqlop.addTable()
    app = QApplication(sys.argv)
    raylamain = Rayla_Main()
    coffee = Coffee()
    milktea = Milktea()
    food = Food()
    promotion = Promotion()
    setting = Setting()
    raylamain.background()
    btn_coffee = raylamain.main_ui.pushButton_2
    btn_coffee.clicked.connect(coffee.nor_order)
    btn_milktea = raylamain.main_ui.pushButton_3
    btn_milktea.clicked.connect(milktea.milktea)
    btn_food = raylamain.main_ui.pushButton_4
    btn_food.clicked.connect(food.act_order)
    btn_promotion = raylamain.main_ui.pushButton_10
    btn_promotion.clicked.connect(promotion.nor_promotion)
    btn_set = raylamain.main_ui.pushButton_15
    btn_set.clicked.connect(setting.show_setting)
    
    name = []

# login part
    raylamain.hide()
    MainWindow = QtWidgets.QMainWindow()
    ui = Log_in()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
