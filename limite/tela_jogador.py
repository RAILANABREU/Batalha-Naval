class TelaJogador():
  def tela_opcoes(self):
    print("-------- Tela Jogador --------")
    print("Escolha uma opçâo")
    print("1 - Incluir Jogador")
    print("2 - Alterar Jogador")
    print("3 - Listar Jogadores")
    print("4 - Mostrar Histórico")
    print("5 - Mostrar Ranking dos jogadores")
    print("6 - Seção de Partida")
    print("7 - Excluir ")
    print("0 - Retornar")

    opcao = int(input("Escolha a opção: "))
    return opcao
  
  def dados_jogador(self):
    print("-------- DADOS JOGADOR ----------")
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    id = input("ID: ")

    return {"nome": nome, "data_nascimento": data_nascimento, "id": id}

  def seleciona_jogador(self):
    id = input('Digite o ID do jogador que deseja selecionar: ')
    return id
  
  def mostra_jogador(self, dados_jogador):
    print("NOME DO JOGADOR: ", dados_jogador["nome"])
    print("NASCIMENTO DO JOGADOR: ", dados_jogador["data_nascimento"])
    print("ID DO JOGADOR: ", dados_jogador["id"])
    print("\n")

  def mostra_rank(self, rank):
    print(rank)
  
  def mostra_mensagem(self, msg):
    print(msg)