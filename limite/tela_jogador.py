class TelaJogador():
  def tela_opcoes(self):
    print("-------- Tela Jogador ----------")
    print("Escolha a opcao")
    print("1 - Incluir Jogador")
    print("2 - Alterar Jogador")
    print("3 - Listar Jogadores")
    print("4 - Dados do Jogador")
    print("5 - Mostrar Histórico")
    print("6 - Mostrar Ranking dos jogadores")
    print("7 - Excluir ")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao