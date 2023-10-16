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
    
    def jogada(self):
        eixo_y = int(input("Selecione a cordenada Y do tiro: "))
        eixo_x = int(input("selecione a cordenada X do tiro: "))

        return eixo_y, eixo_x
    
    def mostrar_jogadas(self):
        pass

    def mostra_mensagem(self, msg):
        return msg
    
    def mostrar_oceano(self, tamanho, oceano):
        for linha in range(tamanho):
            if linha == 0:
                print(f'Y/X   {linha}', end='   ')
            else:
                print(f'{linha}', end='   ')
        print()
        for linha in range(tamanho):
            for coluna in range(tamanho):
                if coluna == 0:
                    print(f' {linha}   [{oceano[linha][coluna]}]', end=' ')
                else:
                    print(f'[{oceano[linha][coluna]}]', end=' ')
            print()