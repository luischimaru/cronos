import sqlite3

# conectando...
conn = sqlite3.connect('cronos.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE cliente (
        CNPJ int not null,
        nome fantasia text not null,
        data_vencimento
        );
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()
