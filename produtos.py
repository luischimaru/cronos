import sqlite3

conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

codigo_interno = int(input('digite o código do produto: '))
codigo_barras = int(input('digite o código de barras: '))
nome = str(input('digite o nome: '))
data = int(input('digite a validade do produto: '))
preco = float(input('digite o valor: '))
quantidade = int(input('digite a quantidade do produto: '))
CFOP = int(input('digite o CFOP do produto: '))
ICMS = int(input('digite o ICMS: '))
IPI = int(input('digite o IPI: '))
CONFINS = int(input('digite o CONFINS: '))
grupo = str(input('qual o grupo: '))
subgrupo = str(input('qual o subgrupo: '))

cursor.execute("""
    INSERT INTO produto (codigo, barras, nome, data, preço, quantidade, CFOP, ICMS, IPI, CONFINS, grupo, subgrupo)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?
    )
    """, (codigo_interno, codigo_barras, nome, data, preco, quantidade, CFOP, ICMS, IPI, CONFINS, grupo, subgrupo))

conn.commit()
print("dados salvos com sucesso")
