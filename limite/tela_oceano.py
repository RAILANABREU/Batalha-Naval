class TelaOceano:
    def tela_opcoes(self):
        print("-------- Tela Oceano --------")
        print("Escolha Uma Opção")
        print("1 - Realizar Jogada")
        print("2 - Mostrar Jogadas")
        print("3 - Mostrar Meu Oceano")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def posiciona_navios(self):
        print("---Posicionando Navios---")
        cordenada_y = int(input("Selecione a cordenada do eixo Y: "))
        cordenada_x = int(input("Selecione a cordenada do eixo X: "))

        return cordenada_y, cordenada_x
    
    def mostrar_jogadas(self):
        pass

    def mostra_mensagem(self, msg):
        return msg