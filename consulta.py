# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consulta.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_consulta(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(599, 300)
        Form.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 40, 272, 52))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lne_nome = QtWidgets.QLineEdit(self.widget)
        self.lne_nome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nome.setObjectName("lne_nome")
        self.horizontalLayout.addWidget(self.lne_nome)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lne_codigo = QtWidgets.QLineEdit(self.widget)
        self.lne_codigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_codigo.setObjectName("lne_codigo")
        self.horizontalLayout_2.addWidget(self.lne_codigo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(430, 270, 158, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_cancelar = QtWidgets.QPushButton(self.widget1)
        self.bt_cancelar.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.bt_cancelar.setObjectName("bt_cancelar")
        self.horizontalLayout_3.addWidget(self.bt_cancelar)
        self.bt_pesquisa = QtWidgets.QPushButton(self.widget1)
        self.bt_pesquisa.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.bt_pesquisa.setObjectName("bt_pesquisa")
        self.horizontalLayout_3.addWidget(self.bt_pesquisa)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "nome"))
        self.label_2.setText(_translate("Form", "código ou código de barras"))
        self.bt_cancelar.setText(_translate("Form", "cancelar"))
        self.bt_pesquisa.setText(_translate("Form", "pesquisar"))
