from limite.tela_partida import TelaPartida
from entidade.partida import Partida
from entidade.jogador import Jogador
from entidade.oceano import Oceano
from limite.tela_oceano import TelaOceano
from limite.tela_jogador import TelaJogador
from random import randrange

class ControladorPartida:
    def __init__(self, controlador_geral):
        self.__jogador = Jogador
        self.__partida = Partida(self.__jogador)
        self.__monta_oceano = Oceano(10)
        self.__tela_partida = TelaPartida()
        self.__controlador_geral = controlador_geral
        self.__tela_oceano = TelaOceano()
        self.__jogadas_player = []
        self.__jogadas_computador = []
        self.__score_player = 0
        self.__score_computador = 0
        self.__oceano_player = self.__monta_oceano.oceano_player
        self.__oceano_computador = self.__monta_oceano.oceano_computador
        self.__posicoes_navios_player = self.__monta_oceano.posicoes_navios_player
        self.__posicoes_navios_computador  = self.__monta_oceano.posicoes_navios_computador
        self.__tamanho = self.__monta_oceano.tamanho_oceano
        self.__oceano_modelo = [[0] * self.__tamanho for j in range(self.__tamanho)]

    def comecar_partida(self):
        info = self.__tela_partida.comecar_partida()
        # preciso desenovlver a logica de como pegar o jogador por id
        jogador = self.__controlador_geral.controlador_jogador.pega_jogador_por_id(str(info["id"]))
        tamanho_oceano = int(info["tamanho_oceano"])
        print(self.__jogador)
        if isinstance(jogador, Jogador) and isinstance(tamanho_oceano, int):
            print("Passou")
            self.__partida = Partida(self.__jogador)
            print("Passou2")
            self.__monta_oceano = Oceano(tamanho_oceano)
            print("Passou3")
            self.posiciona_navios(self.__partida.navios_player, self.__partida.navios_computador)
            print("Passou4")
            self.__controlador_geral.cadastra_oceano()
            print("Passou5")

    def partida(self):
        return self.__partida

    def navio_player(self):
        return self.__partida.navios_player()

    def navio_computador(self):
        return self.__partida.navios_computador()

    def pontuacao(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.comecar_partida, 0: self.retornar}

        while True:
            try:
                opcao_escolhida = self.__tela_partida.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                raise ValueError
            except ValueError:
                self.__tela_partida.mostra_mensagem("Valor inválido, digite um número Válido")

    def abre_tela_oceano(self):
        lista_opcoes = {1: self.jogada, 2:self.mostrar_jogadas, 3:self.mostrar_oceano, 0: self.retornar}

        while True:
            try:
                opcao_escolhida = self.__tela_oceano.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                raise ValueError
            except ValueError:
                self.__tela_partida.mostra_mensagem("Valor inválido, digite um número Válido")

    def score_player(self):
        return self.__score_player

    def jogada(self):
        tiro_player = True
        tiro_bot = False
        while tiro_player:
            if self.__score_player == 41:
                self.__tela_oceano.mostra_mensagem("Você Venceu a batalha, Parabéns")
                break
            tiro = self.__tela_oceano.jogada()
            if tiro in self.__jogadas_player:
                self.__tela_oceano.mostra_mensagem("Você já atirou nessa posição")
            else:
                errou = False
                for j in self.__posicoes_navios_computador:
                    if tiro in j:
                        self.__score_player += 1
                        self.__oceano_modelo[tiro[0]][tiro[1]] = self.__oceano_computador[tiro[0]][tiro[1]]
                        errou = False
                        self.__jogadas_player.append(tiro)
                        self.__tela_oceano.mostra_mensagem("Você acertou uma embarcação, jogue novamente")
                        self.mostrar_jogadas(tiro)
                        if j[0] == 0 or (j[0] - 1 == 0):
                            self.__score_player += 3
                            self.__tela_oceano.mostra_mensagem("Você destuiu uma embarcação adversária!! +3pts")
                        else:
                            j[0] = j[0] - 1
                    else:
                        errou = True
                if errou:
                    tiro_player = False
                    tiro_bot = True
                    self.__oceano_modelo[tiro[0]][tiro[1]] = 1
                    self.mostrar_jogadas(tiro)
                    self.__tela_oceano.mostra_mensagem("Você errou o alvo, espere sua próxima tentativa")
                    self.__jogadas_player.append(tiro)

        while tiro_bot:
            if self.__score_computador == 41:
                self.__tela_oceano.mostra_mensagem("Você Perdeu a Batalha!")
                break
            shot_y = randrange(self.__tamanho + 1)
            shot_x = randrange(self.__tamanho + 1)
            tiro_npc = shot_y, shot_x
            if tiro_npc in self.__jogadas_computador:
                continue
            else:
                for j in self.__posicoes_navios_player:
                    errou = False
                    if tiro_npc in j:
                        self.__score_computador += 1
                        self.__jogadas_computador.append(tiro_npc)
                        self.__tela_oceano.mostra_mensagem("O Computador acertou sua embarcação")
                        self.__oceano_player[tiro_npc[0]][tiro_npc[1]] = 'X'
                        if j[0] == 0 or (j[0] - 1 == 0):
                            self.__score_computador += 3
                            self.__tela_oceano.mostra_mensagem("O Computador destruiu uma embarcação sua")
                        else:
                            j[0] = j[0] - 1
                if errou:
                    tiro_bot = False
                    self.__jogadas_computador.append(tiro_npc)
                    self.__tela_oceano.mostra_mensagem("O Computador errou, agora é sua vez")

    def mostrar_jogadas(self, tiro):
        self.__jogadas_player.append(tiro)



    def posiciona_navios(self, barco_player, barco_bot):
        barcos_player = barco_player
        barcos_computador = barco_bot
        for boat in barcos_player:
            if boat.__class__.__name__ == "Bote":  
                self.posiciona_bote("player")
            elif boat.__class__.__name__ == "Fragata":
                self.posiciona_fragata(3 , "player")
            elif boat.__class__.__name__ == "PortaAvioes":
                self.posiciona_porta_avioes(4, "player")
            elif boat.__class__.__name__ == "Submarino":
                self.posiciona_submarino( 2 , "player")

        for boat in barcos_computador:
            if boat.__class__.__name__ == "Bote":
                self.posiciona_bote("computador")
            elif boat.__class__.__name__ == "Fragata":
                self.posiciona_fragata( 3, "computador")
            elif boat.__class__.__name__ == "PortaAvioes":
                self.posiciona_porta_avioes(4, "computador")
            elif boat.__class__.__name__ == "Submarino":
                self.posiciona_submarino( 2, "computador")

    def posiciona_bote(self, who):
        lista_temporaria = [1]
        if who == "player":
            while True:
                posicao = self.__tela_oceano.posiciona_navios()
                posicao_em_uso = False
                for i in self.__posicoes_navios_player:
                    if posicao in i:
                        posicao_em_uso = True
                    if posicao_em_uso:
                        self.__tela_oceano.mostra_mensagem("Está posição já está ocupada!")
                if not posicao_em_uso:
                    lista_temporaria.append(posicao)
                    self.__posicoes_navios_player.append(lista_temporaria)
                    self.__oceano_player[posicao[0]][posicao[1]] = 'B'
                    self.__tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player)
                    break

        elif who == "computador":
            while True:
                eixoy = randrange(self.__tamanho+1)
                opc = [eixoy, eixoy+1, eixoy-1]
                alea = randrange(3)
                eixox = opc[alea]
                posicao = eixoy, eixox
                for i in self.__posicoes_navios_computador:
                    while posicao in i:
                        eixoy = randrange(self.__tamanho+1)
                        opc = [eixoy, eixoy+1, eixoy-1]
                        alea = randrange(3)
                        eixox = opc[alea]
                        posicao = eixoy, eixox
                lista_temporaria.append(posicao)
                self.__posicoes_navios_computador.append(lista_temporaria)
                self.__oceano_computador[posicao[0]][posicao[1]] = 'B'

    def posiciona_porta_avioes(self, tamanho, who):
        lista_temporaria = [4]  # Inicializa a lista_temporaria com [4] como primeiro elemento
        if who == "player":
            porta_avioes_restantes = 1
            while porta_avioes_restantes > 0:
                try:
                    posicoes_x = list(map(int, input("Informe as coordenadas do eixo X (separadas por espaço): ").split()))
                    posicoes_y = list(map(int, input("Informe as coordenadas do eixo Y (separadas por espaço): ").split()))

                    while (len(posicoes_y) < 4  and len(posicoes_x) != 1) or (len(posicoes_x) < 4 and len(posicoes_y) != 1):
                        print("Por favor, insira 4 coordenadas em um dos eixos e 1 para o outro para inserir um porta-aviões.")
                        posicoes_x = list(map(int, input("Informe as coordenadas do eixo X (separadas por espaço): ").split()))
                        posicoes_y = list(map(int, input("Informe as coordenadas do eixo Y (separadas por espaço): ").split()))
                    
                    if (len(posicoes_x) > 1 and len(posicoes_x) <= 4) and len(posicoes_y) == 1 :
                        if any(x < 0 or x >= self.__tamanho for x in posicoes_x) or posicoes_y[0] < 0 or posicoes_y[0] >= self.__tamanho:
                            print("Posição inválida, por favor insira novamente.")
                            continue
                    elif (len(posicoes_y) > 1 and len(posicoes_y) <= 4) and len(posicoes_x) == 1:
                        if any(y < 0 or y >= self.__tamanho for y in posicoes_y) or posicoes_x[0] < 0 or posicoes_x[0] >= self.__tamanho:
                            print("Posição inválida, por favor insira novamente.")
                            continue
                        
                    elif any(self.__oceano_player[y][x] != 0 for x, y in zip(posicoes_x, posicoes_y)):
                        print("Não é possível adicionar um novo porta-aviões em uma posição ocupada! Por favor insira novamente.")
                        continue

                    if len(posicoes_x) == 4:
                        for x in posicoes_x:
                            lista_temporaria.append((posicoes_y[0], x))
                            self.__oceano_player[posicoes_y[0]][x] = 'P'
                    else:
                        for y in posicoes_y:
                            lista_temporaria.append((y, posicoes_x[0]))
                            self.__oceano_player[y][posicoes_x[0]] = 'P'

                    # Mostra a atualização do oceano
                    self.__tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player)

                    porta_avioes_restantes -= 1
                except ValueError:
                    print("Por favor, insira números inteiros válidos para as coordenadas.")


                
        # Restante do código...
   
    def posiciona_fragata(self, tamanho, who):
        lista_temporaria = [3]
        if who == "player":
            fragatas_restantes = 1
            while fragatas_restantes > 0:
                try:
                    posicoes_x = list(map(int, input("Informe as coordenadas do eixo X (separadas por espaço): ").split()))
                    posicoes_y = list(map(int, input("Informe as coordenadas do eixo Y (separadas por espaço): ").split()))

                    while (len(posicoes_y) < 3  and len(posicoes_x) != 1) or (len(posicoes_x) < 3 and len(posicoes_y) != 1):
                        print("Por favor, insira 3 coordenadas em um dos eixos e 1 para o outro para inserir uma Fragata.")
                        posicoes_x = list(map(int, input("Informe as coordenadas do eixo X (separadas por espaço): ").split()))
                        posicoes_y = list(map(int, input("Informe as coordenadas do eixo Y (separadas por espaço): ").split()))
                    
                    if (len(posicoes_x) > 1 and len(posicoes_x) <=3) and len(posicoes_y) == 1 :
                        if any(x < 0 or x >= self.__tamanho for x in posicoes_x) or posicoes_y[0] < 0 or posicoes_y[0] >= self.__tamanho:
                            print("Posição inválida, por favor insira novamente.")
                            continue
                    elif (len(posicoes_y) > 1 and len(posicoes_y) <=3) and len(posicoes_x) == 1:
                        if any(y < 0 or y >= self.__tamanho for y in posicoes_y) or posicoes_x[0] < 0 or posicoes_x[0] >= self.__tamanho:
                            print("Posição inválida, por favor insira novamente.")
                            continue
                    
                    elif any(self.__oceano_player[y][x] != 0 for x, y in zip(posicoes_x, posicoes_y)):
                        print("Não é possível adicionar uma nova fragata em uma posição ocupada! Por favor insira novamente.")
                        continue

                    if len(posicoes_x) == 3:
                        for x in posicoes_x:
                            lista_temporaria.append((posicoes_y[0], x))
                            self.__oceano_player[posicoes_y[0]][x] = 'F'
                    else:
                        for y in posicoes_y:
                            lista_temporaria.append((y, posicoes_x[0]))
                            self.__oceano_player[y][posicoes_x[0]] = 'F'

                    # Mostra a atualização do oceano
                    self.__tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player)

                    fragatas_restantes -= 1
                except ValueError:
                    print("Por favor, insira números inteiros válidos para as coordenadas.")

                    
            # Restante do código...
                            
        elif who == "computador":
            for i in range(tamanho):
                while True:
                    eixoy = randrange(self.__tamanho)
                    eixox = randrange(self.__tamanho)
                    posicao = eixoy, eixox

                    posicao_em_uso = False
                    for j in self.__posicoes_navios_computador:
                        if posicao in j:
                            posicao_em_uso = True

                    if not posicao_em_uso:
                        if i == 0:
                            lista_temporaria = [posicao]
                        elif i > 0:
                            distancia_valida = all(
                                (abs(lista_temporaria[k][0] - posicao[0]) <= 1) and
                                (abs(lista_temporaria[k][1] - posicao[1]) <= 1)
                                for k in range(len(lista_temporaria))
                            )
                            if distancia_valida:
                                lista_temporaria.append(posicao)

                        self.__posicoes_navios_computador.append(lista_temporaria)
                        self.__oceano_computador[posicao[0]][posicao[1]] = 'F'
                        break

    def posiciona_submarino(self, tamanho, who):
        lista_temporaria = [2]
        if who == "player":
            submarino_restantes = 1
            while submarino_restantes > 0:
                try:
                    posicoes_x = list(map(int, input("Informe as coordenadas do eixo X (separadas por espaço): ").split()))
                    posicoes_y = list(map(int, input("Informe as coordenadas do eixo Y (separadas por espaço): ").split()))

                    while (len(posicoes_y) < 2  and len(posicoes_x) != 1) or (len(posicoes_x) < 2 and len(posicoes_y) != 1):
                        print("Por favor, insira 2 coordenadas em um dos eixos e 1 para o outro para inserir um Submarino.")
                        posicoes_x = list(map(int, input("Informe as coordenadas do eixo X (separadas por espaço): ").split()))
                        posicoes_y = list(map(int, input("Informe as coordenadas do eixo Y (separadas por espaço): ").split()))
                    
                    if (len(posicoes_x) > 1 and len(posicoes_x) <=2) and len(posicoes_y) == 1 :
                        if any(x < 0 or x >= self.__tamanho for x in posicoes_x) or posicoes_y[0] < 0 or posicoes_y[0] >= self.__tamanho:
                            print("Posição inválida, por favor insira novamente.")
                            continue
                    elif (len(posicoes_y) > 1 and len(posicoes_y) <=2) and len(posicoes_x) == 1:
                        if any(y < 0 or y >= self.__tamanho for y in posicoes_y) or posicoes_x[0] < 0 or posicoes_x[0] >= self.__tamanho:
                            print("Posição inválida, por favor insira novamente.")
                            continue
                    
                    elif any(self.__oceano_player[y][x] != 0 for x, y in zip(posicoes_x, posicoes_y)):
                        print("Não é possível adicionar uma nova fragata em uma posição ocupada! Por favor insira novamente.")
                        continue

                    if len(posicoes_x) == 2:
                        for x in posicoes_x:
                            lista_temporaria.append((posicoes_y[0], x))
                            self.__oceano_player[posicoes_y[0]][x] = 'S'
                    else:
                        for y in posicoes_y:
                            lista_temporaria.append((y, posicoes_x[0]))
                            self.__oceano_player[y][posicoes_x[0]] = 'S'

                    # Mostra a atualização do oceano
                    self.__tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player)

                    submarino_restantes -= 1
                except ValueError:
                    print("Por favor, insira números inteiros válidos para as coordenadas.")

        elif who == "computador":
            for i in range(tamanho):
                while True:
                    eixoy = randrange(self.__tamanho+1)
                    opc = [eixoy, eixoy+1, eixoy-1]
                    alea = randrange(3)
                    eixox = opc[alea]
                    posicao = eixoy, eixox
                    for j in self.__posicoes_navios_computador:
                        while posicao in j:
                            eixoy = randrange(self.__tamanho+1)
                            opc = [eixoy, eixoy+1, eixoy-1]
                            alea = randrange(3)
                            eixox = opc[alea]
                            posicao = eixoy, eixox
                    if i == 0:
                        lista_temporaria.append(posicao)
                        self.__posicoes_navios_computador.append(lista_temporaria)
                        self.__oceano_computador[posicao[0]][posicao[1]] = 'S'
                        break

                    elif i == 1:
                        if (abs(lista_temporaria[0][0] - posicao[0] <= 1))\
                            and (abs(lista_temporaria[0][1] - posicao[1] <= 1))\
                            and (abs(lista_temporaria[0][0] - posicao[0]) + abs(lista_temporaria[0][1] - posicao[1]) <= 1):
                                lista_temporaria.append(posicao)
                                self.__posicoes_navios_computador.append(lista_temporaria)
                                self.__oceano_computador[posicao[0]][posicao[1]] = 'S'
                                break