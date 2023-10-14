from entidade.oceano import Oceano
from limite.tela_oceano import TelaOceano
from controlador_partida import ControladorPartida
from entidade.partida import Partida
from random import randrange, random

class ControladorOceano:
    def __init__(self, controlador_geral):
        self.__tela_oceano = TelaOceano()
        self.__oceano_player = Oceano.oceano_player()
        self.__oceano_computador = Oceano.oceano_computador()
        self.__controlador_geral = controlador_geral

    def mostrar_oceano(self):
        for linha in range(len(self.__oceano_player)):
            if linha == 0:
                print(f'Y/X   {linha}', end='   ')
            else:
                print(f'{linha}', end='   ')
        print()
        for linha in range(len(self.__oceano_player)):
            for coluna in range(len(self.__oceano_player)):
                if coluna == 0:
                    print(f' {linha}   [{self.__oceano_player[linha][coluna]}]', end=' ')
                else:
                    print(f'[{self.__oceano_player[linha][coluna]}]', end=' ')
            print()
    
    def posiciona_navios(self):
        barcos_player = Partida.navios_player()
        barcos_computador = Partida.navios_computador()
        for boat in barcos_player:
            if boat.__class__.__name__ == "Bote":  
                self.posiciona_bote("player")
            elif boat.__class__.__name__ == "Fragata":
                self.posiciona_fragata(boat.tamanho, "player")
            elif boat.__class__.__name__ == "PortaAvioes":
                self.posiciona_porta_avioes(boat.tamanho, "player")
            elif boat.__class__.__name__ == "Submarino":
                self.posiciona_submarino(boat.tamanho, "player")

        for boat in barcos_computador:
            if boat.__class__.__name__ == "Bote":
                self.posiciona_bote("computador")
            elif boat.__class__.__name__ == "Fragata":
                self.posiciona_fragata(boat.tamanho, "computador")
            elif boat.__class__.__name__ == "PortaAvioes":
                self.posiciona_porta_avioes(boat.tamanho, "computador")
            elif boat.__class__.__name__ == "Submarino":
                self.posiciona_submarino(boat.tamanho, "computador")

    def posiciona_bote(self, who):
        if who == "player":
            while True:
                posicao = self.__tela_oceano.posiciona_navios()
                posicao_em_uso = False
                if posicao in Oceano.posicoes_navios_player():
                    posicao_em_uso = True
                if posicao_em_uso:
                    self.__tela_oceano.mostra_mensagem("Está posição já está ocupada!")
                else:
                    Oceano.posicoes_navios_player.append(posicao)
                    self.__oceano_player[posicao[0]][posicao[1]] = 'B'
                    break

        elif who == "computador":
            while True:
                eixoy = randrange(Oceano.tamanho_oceano+1)
                opc = [eixoy, eixoy+1, eixoy-1]
                alea = randrange(3)
                eixox = opc[alea]
                posicao = eixoy, eixox
                while posicao in Oceano.posicoes_navios_computador():
                    eixoy = randrange(Oceano.tamanho_oceano+1)
                    opc = [eixoy, eixoy+1, eixoy-1]
                    alea = randrange(3)
                    eixox = opc[alea]
                    posicao = eixoy, eixox
                Oceano.posicoes_navios_computador.append(posicao)
                self.__oceano_computador[posicao[0]][posicao[1]] = 'B'

    def posiciona_fragata(self, tamanho, who):
        if who == "player":
            lista_temporaria =  []
            for i in range(tamanho):
                while True:
                    posicao = self.__tela_oceano.posiciona_navios()
                    posicao_em_uso = False
                    if i == 0:
                        if posicao in Oceano.posicoes_navios_player():
                            posicao_em_uso = True
                        if posicao_em_uso:
                            self.__tela_oceano.mostra_mensagem("Está posição já está ocupada!")
                        else:
                            Oceano.posicoes_navios_player.append(posicao)
                            lista_temporaria.append(posicao)
                            self.__oceano_player[posicao[0]][posicao[1]] = 'F'
                            break

                    elif i == 1:
                        if posicao in Oceano.posicoes_navios_player():
                            posicao_em_uso = True
                        if posicao_em_uso:
                            self.__tela_oceano.mostra_mensagem("Está posição já está ocupada!")
                        elif (abs(lista_temporaria[0][0] - posicao[0] <= 1))\
                        and (abs(lista_temporaria[0][1] - posicao[1] <= 1))\
                        and (abs(lista_temporaria[0][0] - posicao[0]) + abs(lista_temporaria[0][1] - posicao[1]) <= 1):
                            Oceano.posicoes_navios_player.append(posicao)
                            lista_temporaria.append(posicao)
                            self.__oceano_player[posicao[0]][posicao[1]] = 'F'
                            break
                        else:
                            self.__tela_oceano.mostra_mensagem("Está Posição é inválida, por favor insira novamente")

                    elif i == 2:
                        if posicao in Oceano.posicoes_navios_player():
                            posicao_em_uso = True
                        if posicao_em_uso:
                            self.__tela_oceano.mostra_mensagem("Está posição já está ocupada!")
                        elif (abs(lista_temporaria[1][0] - posicao[0] <= 1))\
                        and (abs(lista_temporaria[1][1] - posicao[1] <= 1))\
                        and (abs(lista_temporaria[1][0] - posicao[0]) + abs(lista_temporaria[1][1] - posicao[1]) <= 1):
                            lista_temporaria.append(posicao)
                            self.__oceano_player[posicao[0]][posicao[1]] = 'F'
                            break                        
                        else:
                            self.__tela_oceano.mostra_mensagem("Está Posição é inválida, por favor insira novamente")
        
        elif who == "computador":
            lista_temporaria = []
            for i in range(tamanho):
                while True:
                    eixoy = randrange(Oceano.tamanho_oceano+1)
                    opc = [eixoy, eixoy+1, eixoy-1]
                    alea = randrange(3)
                    eixox = opc[alea]
                    posicao = eixoy, eixox
                    while posicao in Oceano.posicoes_navios_computador():
                        eixoy = randrange(Oceano.tamanho_oceano+1)
                        opc = [eixoy, eixoy+1, eixoy-1]
                        alea = randrange(3)
                        eixox = opc[alea]
                        posicao = eixoy, eixox
                    if i == 0:
                        Oceano.posicoes_navios_player.append(posicao)
                        lista_temporaria.append(posicao)
                        self.__oceano_player[posicao[0]][posicao[1]] = 'F'
                        break
                    elif i == 1:
                        if (abs(lista_temporaria[0][0] - posicao[0] <= 1))\
                            and (abs(lista_temporaria[0][1] - posicao[1] <= 1))\
                            and (abs(lista_temporaria[0][0] - posicao[0]) + abs(lista_temporaria[0][1] - posicao[1]) <= 1):
                                Oceano.posicoes_navios_computador.append(posicao)
                                lista_temporaria.append(posicao)
                                self.__oceano_computador[posicao[0]][posicao[1]] = 'F'
                                break
                    elif i == 2:
                        if (abs(lista_temporaria[1][0] - posicao[0] <= 1))\
                        and (abs(lista_temporaria[1][1] - posicao[1] <= 1))\
                        and (abs(lista_temporaria[1][0] - posicao[0]) + abs(lista_temporaria[1][1] - posicao[1]) <= 1):
                            lista_temporaria.append(posicao)
                            self.__oceano_player[posicao[0]][posicao[1]] = 'F'
                            break                        

    def posiciona_porta_avioes(self, tamanho, who):
        if who == "player":
            lista_temporaria =  []
            for i in range(tamanho):
                while True:
                    posicao = self.__tela_oceano.posiciona_navios()
                    posicao_em_uso = False
                    if i == 0:
                        if posicao in Oceano.posicoes_navios_player():
                            posicao_em_uso = True
                        if posicao_em_uso:
                            self.__tela_oceano.mostra_mensagem("Está posição já está ocupada!")
                        else:
                            Oceano.posicoes_navios_player.append(posicao)
                            lista_temporaria.append(posicao)
                            self.__oceano_player[posicao[0]][posicao[1]] = 'P'
                            break

                    elif i == 1:
                        if posicao in Oceano.posicoes_navios_player():
                            posicao_em_uso = True
                        if posicao_em_uso:
                            self.__tela_oceano.mostra_mensagem("Está posição já está ocupada!")
                        elif (abs(lista_temporaria[0][0] - posicao[0] <= 1))\
                        and (abs(lista_temporaria[0][1] - posicao[1] <= 1))\
                        and (abs(lista_temporaria[0][0] - posicao[0]) + abs(lista_temporaria[0][1] - posicao[1]) <= 1):
                            Oceano.posicoes_navios_player.append(posicao)
                            lista_temporaria.append(posicao)
                            self.__oceano_player[posicao[0]][posicao[1]] = 'P'
                            break
                        else:
                            self.__tela_oceano.mostra_mensagem("Está Posição é inválida, por favor insira novamente")

                    elif i == 2:
                        if posicao in Oceano.posicoes_navios_player():
                            posicao_em_uso = True
                        if posicao_em_uso:
                            self.__tela_oceano.mostra_mensagem("Está posição já está ocupada!")
                        elif (abs(lista_temporaria[1][0] - posicao[0] <= 1))\
                        and (abs(lista_temporaria[1][1] - posicao[1] <= 1))\
                        and (abs(lista_temporaria[1][0] - posicao[0]) + abs(lista_temporaria[1][1] - posicao[1]) <= 1):
                            Oceano.posicoes_navios_player.append(posicao)
                            lista_temporaria.append(posicao)
                            self.__oceano_player[posicao[0]][posicao[1]] = 'P'
                            break 
                        else:
                            self.__tela_oceano.mostra_mensagem("Está Posição é inválida, por favor insira novamente")

                    elif i == 3:
                        if posicao in Oceano.posicoes_navios_player():
                            posicao_em_uso = True
                        if posicao_em_uso:
                            self.__tela_oceano.mostra_mensagem("Está posição já está ocupada!")
                        elif (abs(lista_temporaria[2][0] - posicao[0] <= 1))\
                        and (abs(lista_temporaria[2][1] - posicao[1] <= 1))\
                        and (abs(lista_temporaria[2][0] - posicao[0]) + abs(lista_temporaria[2][1] - posicao[1]) <= 1):
                            Oceano.posicoes_navios_player.append(posicao)
                            lista_temporaria.append(posicao)
                            self.__oceano_player[posicao[0]][posicao[1]] = 'P'
                            break                                 
                        else:
                            self.__tela_oceano.mostra_mensagem("Está Posição é inválida, por favor insira novamente")
        
        elif who == "computador":
            lista_temporaria = []
            for i in range(tamanho):
                while True:
                    eixoy = randrange(Oceano.tamanho_oceano+1)
                    opc = [eixoy, eixoy+1, eixoy-1]
                    alea = randrange(3)
                    eixox = opc[alea]
                    posicao = eixoy, eixox
                    while posicao in Oceano.posicoes_navios_computador():
                        eixoy = randrange(Oceano.tamanho_oceano+1)
                        opc = [eixoy, eixoy+1, eixoy-1]
                        alea = randrange(3)
                        eixox = opc[alea]
                        posicao = eixoy, eixox
                    if i == 0:
                        Oceano.posicoes_navios_player.append(posicao)
                        lista_temporaria.append(posicao)
                        self.__oceano_player[posicao[0]][posicao[1]] = 'P'
                        break
                    elif i == 1:
                        if (abs(lista_temporaria[0][0] - posicao[0] <= 1))\
                            and (abs(lista_temporaria[0][1] - posicao[1] <= 1))\
                            and (abs(lista_temporaria[0][0] - posicao[0]) + abs(lista_temporaria[0][1] - posicao[1]) <= 1):
                                Oceano.posicoes_navios_computador.append(posicao)
                                lista_temporaria.append(posicao)
                                self.__oceano_computador[posicao[0]][posicao[1]] = 'P'
                                break
                    elif i == 2:
                        if (abs(lista_temporaria[1][0] - posicao[0] <= 1))\
                        and (abs(lista_temporaria[1][1] - posicao[1] <= 1))\
                        and (abs(lista_temporaria[1][0] - posicao[0]) + abs(lista_temporaria[1][1] - posicao[1]) <= 1):
                            lista_temporaria.append(posicao)
                            self.__oceano_player[posicao[0]][posicao[1]] = 'P'
                            break           

                    elif i == 3:
                        if (abs(lista_temporaria[2][0] - posicao[0] <= 1))\
                        and (abs(lista_temporaria[2][1] - posicao[1] <= 1))\
                        and (abs(lista_temporaria[2][0] - posicao[0]) + abs(lista_temporaria[2][1] - posicao[1]) <= 1):
                            lista_temporaria.append(posicao)
                            self.__oceano_player[posicao[0]][posicao[1]] = 'P'
                            break                         

    def posiciona_submarino(self, tamanho, who):
        if who == "player":
            lista_temporaria =  []
            for i in range(tamanho):
                while True:
                    posicao = self.__tela_oceano.posiciona_navios()
                    posicao_em_uso = False
                    if i == 0:
                        if posicao in Oceano.posicoes_navios_player():
                            posicao_em_uso = True
                        if posicao_em_uso:
                            self.__tela_oceano.mostra_mensagem("Está posição já está ocupada!")
                        else:
                            Oceano.posicoes_navios_player.append(posicao)
                            lista_temporaria.append(posicao)
                            self.__oceano_player[posicao[0]][posicao[1]] = 'S'
                            break

                    elif i == 1:
                        if posicao in Oceano.posicoes_navios_player():
                            posicao_em_uso = True
                        if posicao_em_uso:
                            self.__tela_oceano.mostra_mensagem("Está posição já está ocupada!")
                        elif (abs(lista_temporaria[0][0] - posicao[0] <= 1))\
                        and (abs(lista_temporaria[0][1] - posicao[1] <= 1))\
                        and (abs(lista_temporaria[0][0] - posicao[0]) + abs(lista_temporaria[0][1] - posicao[1]) <= 1):
                            Oceano.posicoes_navios_player.append(posicao)
                            lista_temporaria.append(posicao)
                            self.__oceano_player[posicao[0]][posicao[1]] = 'S'
                            break
                        else:
                            self.__tela_oceano.mostra_mensagem("Está Posição é inválida, por favor insira novamente")

        elif who == "computador":
            lista_temporaria = []
            for i in range(tamanho):
                while True:
                    eixoy = randrange(Oceano.tamanho_oceano+1)
                    opc = [eixoy, eixoy+1, eixoy-1]
                    alea = randrange(3)
                    eixox = opc[alea]
                    posicao = eixoy, eixox
                    while posicao in Oceano.posicoes_navios_computador():
                        eixoy = randrange(Oceano.tamanho_oceano+1)
                        opc = [eixoy, eixoy+1, eixoy-1]
                        alea = randrange(3)
                        eixox = opc[alea]
                        posicao = eixoy, eixox
                    if i == 0:
                        Oceano.posicoes_navios_player.append(posicao)
                        lista_temporaria.append(posicao)
                        self.__oceano_player[posicao[0]][posicao[1]] = 'S'
                        break

                    elif i == 1:
                        if (abs(lista_temporaria[0][0] - posicao[0] <= 1))\
                            and (abs(lista_temporaria[0][1] - posicao[1] <= 1))\
                            and (abs(lista_temporaria[0][0] - posicao[0]) + abs(lista_temporaria[0][1] - posicao[1]) <= 1):
                                Oceano.posicoes_navios_computador.append(posicao)
                                lista_temporaria.append(posicao)
                                self.__oceano_computador[posicao[0]][posicao[1]] = 'S'
                                break