import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from Database import *
from tela import *
from ADM1 import *
from login import *
from pedidoI import *
from balcão import *
from consulta import *
from transferencia import *





##tela de login##
class login(QWidget, Ui_login):
    def __init__(self) -> None:
        super(login, self).__init__()
        self.setupUi(self)

##tela de pedido##
class pedido(QWidget, Ui_pedidoI):
    def __init__(self) -> None:
        super(pedido, self).__init__()
        self.setupUi(self)

##tela de balcão##
class balcao(QWidget, Ui_balcao):
    def __init__(self) -> None:
        super(balcao, self).__init__()
        db = Database()
        db.conecta()
        self.setupUi(self)
        self.bt_voltar.clicked.connect(self.close)
        self.bt_transferir.clicked.connect(self.transferencia)
        self.bt_okID.clicked.connect(self.usuario)

    def usuario(self):
        id = self.lne_ID
        db = Database()
        db.conecta()
        existe  = db.check_usersc(id)
        if existe == True:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro de usuario")
            msg.setText("usuario não existe")





    def calcula_valorf(self):
        valorf = valor * qntd
        self.lcd_valort.display("valorf")
        self.lcd_valor.display("valor")
   

    def localiza_prdt(codigo):
        codigo


    def consulta(self):
        self.consulta = consulta()
        self.consulta.show()
    
    def transferencia(self):
        self.transferencia = transfer()
        self.transferencia.show()


                

        db.comanda(comanda, qntd, codigo, valorf, estado)
        db.close_connection()


    

class consulta(QWidget, Ui_consulta):
    def __init__(self) -> None:
        super(consulta, self).__init__()
        self.setupUi(self)

class transfer(QWidget, Ui_transfer):
    def __init__(self) -> None:
        super(transfer, self).__init__()
        self.setupUi(self)

##tela inicial##    
class tela(QWidget, Ui_tela):
    def __init__(self) -> None:
        super(tela, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cronos")
        self.bt_admin.clicked.connect(self.login)
        self.bt_caixa.clicked.connect(self.login)
        self.bt_desen.clicked.connect(self.login)
        self.bt_pedidos.clicked.connect(self.pedido)
        self.bt_balcao.clicked.connect(self.balcao)
        self.bt_fechar.clicked.connect(self.close)

    def pedido(self):
        self.pedido = pedido()
        self.pedido.show()

    def login(self):
        self.login = login()
        self.login.show()

    def balcao(self):
        self.balcao = balcao()
        self.balcao.show()



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


##abertura do sistema##
if __name__ == "__main__":
    root = QApplication(sys.argv)
    app = tela()
    app.show()
    sys.exit(root.exec())

    
