class TelaOceano:
    def tela_opcoes(self):
        print("-------- Tela Oceano --------")
        print("Escolha Uma Opção")
        print("1 - Posicionar Os Navios")
        print("2 - Realizar Jogada")
        print("3 - Mostar Jogadas")
        print("4 - Mostrar Meu Oceano")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def tamanho_oceano(self):
        tamanho = int(input("Digite o tamanho do oceano(MxM) que deseja jogar: "))
        return tamanho

    def posiciona_navios(self):
        cordenada_y = int(input("Selecione a cordenada do eixo Y: "))
        cordenada_x = int(input("Selecione a cordenada do eixo X: "))
        return cordenada_y, cordenada_x