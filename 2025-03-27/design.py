# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 830)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lentele = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.lentele.setGeometry(QtCore.QRect(20, 350, 730, 431))
        self.lentele.setMinimumSize(QtCore.QSize(730, 0))
        self.lentele.setMaximumSize(QtCore.QSize(581, 16777215))
        self.lentele.setObjectName("lentele")
        self.lentele.setColumnCount(5)
        self.lentele.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.lentele.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lentele.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lentele.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lentele.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.lentele.setHorizontalHeaderItem(4, item)
        self.lentele.horizontalHeader().setVisible(True)
        self.lentele.horizontalHeader().setCascadingSectionResizes(True)
        self.lentele.horizontalHeader().setDefaultSectionSize(100)
        self.lentele.horizontalHeader().setMinimumSectionSize(60)
        self.lentele.verticalHeader().setVisible(False)
        self.pavadinimas = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.pavadinimas.setGeometry(QtCore.QRect(20, 140, 581, 31))
        self.pavadinimas.setObjectName("pavadinimas")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 211, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 201, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 180, 47, 13))
        self.label_3.setObjectName("label_3")
        self.prideti = QtWidgets.QPushButton(parent=self.centralwidget)
        self.prideti.setGeometry(QtCore.QRect(530, 200, 71, 31))
        self.prideti.setObjectName("prideti")
        self.kaina = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.kaina.setGeometry(QtCore.QRect(20, 200, 111, 31))
        self.kaina.setObjectName("kaina")
        self.kiekis = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.kiekis.setGeometry(QtCore.QRect(150, 200, 101, 31))
        self.kiekis.setObjectName("kiekis")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.filtras_pavadinimas = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.filtras_pavadinimas.setGeometry(QtCore.QRect(20, 310, 271, 31))
        self.filtras_pavadinimas.setObjectName("filtras_pavadinimas")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 290, 161, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 290, 101, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(390, 290, 101, 16))
        self.label_9.setObjectName("label_9")
        self.filtras_kaina_nuo = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.filtras_kaina_nuo.setGeometry(QtCore.QRect(300, 310, 81, 31))
        self.filtras_kaina_nuo.setObjectName("filtras_kaina_nuo")
        self.filtras_kaina_iki = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.filtras_kaina_iki.setGeometry(QtCore.QRect(390, 310, 81, 31))
        self.filtras_kaina_iki.setObjectName("filtras_kaina_iki")
        self.filtras_kiekis = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.filtras_kiekis.setGeometry(QtCore.QRect(480, 310, 121, 31))
        self.filtras_kiekis.setObjectName("filtras_kiekis")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 290, 101, 16))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Apskaitos programa"))
        self.lentele.setSortingEnabled(True)
        item = self.lentele.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.lentele.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Produkto pavadinimas"))
        item = self.lentele.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Kaina"))
        item = self.lentele.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Kiekis"))
        item = self.lentele.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Veiksmai"))
        self.label.setText(_translate("MainWindow", "Produkto pavadinimas:"))
        self.label_2.setText(_translate("MainWindow", "Kaina"))
        self.label_3.setText(_translate("MainWindow", "Kiekis"))
        self.prideti.setText(_translate("MainWindow", "Pridėti"))
        self.label_4.setText(_translate("MainWindow", "Apskaitos Programa"))
        self.label_5.setText(_translate("MainWindow", "Produkto įvedimas"))
        self.label_6.setText(_translate("MainWindow", "Produktų filtras"))
        self.label_7.setText(_translate("MainWindow", "Pagal pavadinimą"))
        self.label_8.setText(_translate("MainWindow", "Kaina nuo"))
        self.label_9.setText(_translate("MainWindow", "Kaina iki"))
        self.label_10.setText(_translate("MainWindow", "Kiekis"))
