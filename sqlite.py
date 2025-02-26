import sqlite3

# Abrir a conexão com o banco
conn = sqlite3.connect('meuBanco.db')
print('Conexão aberta!')

#Criar tabela n o banco que esta aberto
conn.execute('''
CREATE TABLE IF NOT EXISTS Alunos(
        matricula integer,
        nome string,
        curso string
    );
''')
conn.commit()
print(' Tabela criada com sucesso!')

#inserir dados na tabela
conn.execute('INSERT INTO Alunos VALUES(1,"Vitor","Python");')
conn.execute('INSERT INTO Alunos VALUES(2,"Eduardo","SQL");')
conn.execute('INSERT INTO Alunos VALUES(3,"Amanda","Oracle");')
conn.execute('INSERT INTO Alunos VALUES(4,"Herinque","NASA");')


conn.commit()
print(' Os dados foram inseridos com sucesso!')

#consultar dados da tabela
alunos_econtrados = conn.execute('''
    SELECT matricula, nome FROM Alunos;
''')
for linha in alunos_econtrados:
    print("Matricula: " + str(linha [0]))
    print("Nome: " + str(linha [1]))
    #print("Curso: " + str(linha [2]))

import pandas as pd
pedido = """ SELECT * FROM Alunos; """
estruturadedados = pd.read_sql_query(pedido, conn)
estruturadedados

conn.close()