from conexao import Conexao as Conn

nova_conexao = Conn("database.db", "admin", "1234")

novo_user = input("Deseja criar o seu usuario?:(S/N)").upper()
if novo_user == 'S':
    nick = input('Digite o seu nickname:')
    fname = input('Digite o seu primeiro nome:')
    lname = input('Digite o seu sobrenome:')
    nova_conexao.inserir_dado(nickname = nick, first_name = fname, last_name = lname, score = 0)
