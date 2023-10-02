class TelaJogador():
  def tela_opcoes(self):
    print("-------- Tela Jogador ----------")
    print("Escolha a opcao")
    print("1 - Dados do Jogador")
    print("2 - Mostrar Histórico")
    print("3 - Mostrar Ranking dos jogadores")
    print("4 - Excluir ")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao