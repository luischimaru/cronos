import sqlite3

conn = sqlite3.connect('teste.db')
cursor = conn.cursor()


código = int(input("digite o código: "))
nome = str(input("digite o nome: "))
CPF = int(input("digite o CPF: "))
email = str(input("digite seu email: "))
celular = int(input("digite o número de celular: "))
cidade = str(input("digite a cidade "))
UF = celular = str(input("digite a UF: "))
CEP = int(input("digite o CEP: "))
rua = str(input("digite o nome da rua: "))
número = int(input("digite o número da casa: "))
bairro = str(input("digite o bairro: "))
complemento = str(input("digite o complemento: "))
senha = str(input("digite a senha: "))
confirmação = str(input("digite novamente a senha: "))
while senha != confirmação:
    print("as senhas não coneferem")
    senha = str(input("digite a senha: "))
    confirmação = str(input("digite novamente a senha: "))
nivel = int(input("digite o nível: "))
estatus = 1
limite = float(input("digite o limite: "))

print("confirmar os dados?", código, nome, CPF, email, celular, cidade, UF, CEP, rua, número, bairro, complemento)
dados = int(input("confirma? 1 para sim ou 2 para não: "))
while dados == 2:
    código = int(input("digite o código: "))
    nome = str(input("digite o nome: "))
    CPF = int(input("digite o CPF: "))
    email = str(input("digite seu email: "))
    celular = int(input("digite o número de celular: "))
    cidade = str(input("digite a cidade "))
    UF = celular = str(input("digite a UF: "))
    CEP = int(input("digite o CEP: "))
    rua = str(input("digite o nome da rua: "))
    número = int(input("digite o número da casa: "))
    bairro = str(input("digite o bairro: "))
    complemento = str(input("digite o complemento: "))
    senha = str(input("digite a senha: "))
    confirmação = str(input("digite novamente a senha: "))
    while senha != confirmação:
        print("as senhas não coneferem")
        senha = str(input("digite a senha: "))
        confirmação = str(input("digite novamente a senha: "))
    nivel = int(input("digite o nível: "))
    estatus = 1
    limite = float(input("digite o limite: "))
    
if dados == 1:
    cursor.execute("""
    INSERT INTO usuarios (id, nome, cpf, email, CEL, cidade, UF, CEP, rua, número, bairro, complemento, senha, nivel, estatus, limite)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
    )
    """, (código, nome, CPF, email, celular, cidade, UF, CEP, rua, número, bairro, complemento, senha, nivel, estatus, limite))

    conn.commit()
    print("dados salvos com sucesso")
