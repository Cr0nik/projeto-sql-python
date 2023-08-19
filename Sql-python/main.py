import sqlite3 as sql 

#inserir o caminho do arquivo de conexão com a base de dados
conexao = sql.connect('bancodedados.db')

#apontador do banco de dados
cursor = conexao.cursor()


#colocar informação no banco de dados
while True:
    nome = input('Digite o seu nome:')
    idade = int(input('Digite a sua idade:'))

    cursor.execute(f"INSERT INTO tabela (nome, idade) VALUES ('{nome}', {idade})")

    #comitar/enviar as informações para oo banco de dados 
    conexao.commit()

    continuar = input('Deseja continuar? (S/N):').upper()
    if continuar == 'N':
        break

#ler informação do banco de dados
dados = cursor.execute("SELECT nome, idade FROM tabela").fetchall()

for dado in dados:
    print(f'Nome: {dado[0]}')
    print(f'Idade: {dado[1]}\n')



#encerrando a conexão com o banco de dados
conexao.close()