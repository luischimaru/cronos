import sqlite3
import main

##funções do banco de dados##
class Database():
    def __init__(self, name = "cronos.db") -> None:
        self.name = name
    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except AttributeError:
            print("faça a conexão")

    def insert_users(self, ID, nome, data_nascimento, cpf, email, CEL, cidade, uf, CEP, rua, número, bairro, complemento, senha, nivel, limite, estatus):
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("""insert into usuarios(ID, nome, data_nascimento, cpf, email, CEL, cidade, uf, CEP, rua, número, bairro, complemento, senha, nivel, limite, estatus) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (ID, nome, data_nascimento, cpf, email, CEL, cidade, uf, CEP, rua, número, bairro, complemento, senha, nivel, limite, estatus))
            self.connection.commit()
        except AttributeError:
            print("faça a conexão")

    def check_usersc(self, id):

        try:

            cursor = self.connection.cursor()
            cursor.execute("""

                select * from usuarios where id = id;

            """)

            for linha in cursor.fetchall():
                if linha[16] == 1:
                    return True
                else:
                    return False
        
        except Exception as e:
            print(str(e))
    
    def comanda(self, numero, horario_abertura, codigo_abertura, horario_fechamento, codigo_fechamento, itens, quantidade, valor, metodo_pagamento, valor_troco, estado, ICMS, IPI, CONFINS):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""insert into comanda(numero, horario_abertura, codigo_abertura, horario_fechamento, codigo_fechamento, itens, quantidade, valor, metodo_pagamento, valor_troco, estado, ICMS, IPI, CONFINS) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,)""", (numero, horario_abertura, codigo_abertura, horario_fechamento, codigo_fechamento, itens, quantidade, valor, metodo_pagamento, valor_troco, estado, ICMS, IPI, CONFINS))
            self.connection.commit()
        except AttributeError:
            print("faça a conexão")

    def localiza_prdt(self, codigo):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" select codigo from produto; """)
            for linha in cursor.fetchall():
                linha[1]

        except AttributeError:
            print("faça a conexão")

    def nome(self, codigo):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" select * from produto where codigo = codigo; """)
            for linha in cursor.fetchall():
                linha[3]


        except AttributeError:
            print("faça a conexão")

    def valor(self, codigo):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" select * from produto where codigo = codigo or codigo = nome""")
            if codigo == codigo:
                for linha in cursor.fetchall():
                    linha[5]
            elif codigo == nome:
                for linha in cursor.fetchall():
                    linha[3]
            else:
                print("protudo não existe")
        except AttributeError:
            print("faça a conexão")






con = Database()
con.conecta()
con.close_connection()