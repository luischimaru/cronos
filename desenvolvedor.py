# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desenvolvedor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 590)
        Form.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.lb_desenvolvedor = QtWidgets.QLabel(Form)
        self.lb_desenvolvedor.setGeometry(QtCore.QRect(10, 10, 611, 51))
        self.lb_desenvolvedor.setObjectName("lb_desenvolvedor")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(530, 290, 94, 264))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.bt_adm = QtWidgets.QPushButton(self.widget)
        self.bt_adm.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.bt_adm.setObjectName("bt_adm")
        self.verticalLayout.addWidget(self.bt_adm)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.bt_tables = QtWidgets.QPushButton(self.widget)
        self.bt_tables.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.bt_tables.setObjectName("bt_tables")
        self.verticalLayout.addWidget(self.bt_tables)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.bt_dias = QtWidgets.QPushButton(self.widget)
        self.bt_dias.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.bt_dias.setObjectName("bt_dias")
        self.verticalLayout.addWidget(self.bt_dias)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.bt_cadstro = QtWidgets.QPushButton(self.widget)
        self.bt_cadstro.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.bt_cadstro.setObjectName("bt_cadstro")
        self.verticalLayout.addWidget(self.bt_cadstro)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(210, 560, 89, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.bt_close = QtWidgets.QPushButton(self.widget1)
        self.bt_close.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.bt_close.setObjectName("bt_close")
        self.horizontalLayout.addWidget(self.bt_close)
        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lb_desenvolvedor.setText(_translate("Form", "<html><head/><body><p align=\"center\">Desenvolvedor</p></body></html>"))
        self.bt_adm.setText(_translate("Form", "administrativo"))
        self.bt_tables.setText(_translate("Form", "Tabelas"))
        self.bt_dias.setText(_translate("Form", "Dias de uso"))
        self.bt_cadstro.setText(_translate("Form", "cadastrar usuario"))
        self.bt_close.setText(_translate("Form", "fechar"))
