# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1196, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1181, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.metreKareAraligi1 = QtWidgets.QLineEdit(self.tab)
        self.metreKareAraligi1.setGeometry(QtCore.QRect(190, 20, 81, 21))
        self.metreKareAraligi1.setObjectName("metreKareAraligi1")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 20, 161, 21))
        self.label.setObjectName("label")
        self.metreKareAraligi2 = QtWidgets.QLineEdit(self.tab)
        self.metreKareAraligi2.setGeometry(QtCore.QRect(300, 20, 71, 21))
        self.metreKareAraligi2.setObjectName("metreKareAraligi2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(570, 10, 181, 41))
        self.label_3.setObjectName("label_3")
        self.odaSayisi = QtWidgets.QComboBox(self.tab)
        self.odaSayisi.setGeometry(QtCore.QRect(650, 20, 141, 31))
        self.odaSayisi.setObjectName("odaSayisi")
        self.odaSayisi.addItem("")
        self.odaSayisi.addItem("")
        self.odaSayisi.addItem("")
        self.odaSayisi.addItem("")
        self.odaSayisi.addItem("")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(890, 10, 141, 41))
        self.label_4.setObjectName("label_4")
        self.ilce = QtWidgets.QComboBox(self.tab)
        self.ilce.setGeometry(QtCore.QRect(930, 10, 221, 41))
        self.ilce.setObjectName("ilce")
        self.ilce.addItem("")
        self.ilce.addItem("")
        self.aramaYapButton = QtWidgets.QPushButton(self.tab)
        self.aramaYapButton.setGeometry(QtCore.QRect(380, 50, 151, 31))
        self.aramaYapButton.setObjectName("aramaYapButton")
        self.tabloWidget = QtWidgets.QTableWidget(self.tab)
        self.tabloWidget.setGeometry(QtCore.QRect(0, 90, 1171, 451))
        self.tabloWidget.setObjectName("tabloWidget")
        self.tabloWidget.setColumnCount(0)
        self.tabloWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Metre Kare Aralığı : "))
        self.label_2.setText(_translate("MainWindow", "-"))
        self.label_3.setText(_translate("MainWindow", "Oda Sayısı :"))
        self.odaSayisi.setItemText(0, _translate("MainWindow", "1+0"))
        self.odaSayisi.setItemText(1, _translate("MainWindow", "1+1"))
        self.odaSayisi.setItemText(2, _translate("MainWindow", "2+1"))
        self.odaSayisi.setItemText(3, _translate("MainWindow", "3+1"))
        self.odaSayisi.setItemText(4, _translate("MainWindow", "4+1"))
        self.label_4.setText(_translate("MainWindow", "İlçe :"))
        self.ilce.setItemText(0, _translate("MainWindow", "Battalgazi"))
        self.ilce.setItemText(1, _translate("MainWindow", "Yeşilyurt"))
        self.aramaYapButton.setText(_translate("MainWindow", "Arama Yap"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "SAHIBINDEN ORTALAMA FIYAT"))