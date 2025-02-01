import copy
import sys
import pygame
import random
import numpy as np
from constants import *
pygame.init()

icone = pygame.image.load("assets/jogo_da_velhia.png")
pygame.display.set_icon(icone)
tela = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Jogo da VelhIA')
tela.fill( BCG_COLOR )

class Tabuleiro:
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
        self.quadradosVazios = self.squares
        self.marked_sqrs = 0

    def estadoFinal(self, gameover=False):
        # return 0 se não tiver vitória
        # return 1 se o player 1 vencer
        # return 2 se o player 2 vencer

        # Vitória na vertical
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if gameover:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20)
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                    pygame.draw.line(tela, color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col]

        # Vitória na horizontal
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if gameover:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    iPos = (20, row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(tela, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]


        # Vitória na diagonal descendente (\)
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if gameover:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, 20)
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(tela, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[0][0]

        # Vitória na diagonal ascendente (/)
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if gameover:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, HEIGHT - 20)
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(tela, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[2][0]

        # Sem vitórias
        return 0      



    
    def marcarQuadrado(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def quadradoVazio(self, row, col):
        return self.squares[row][col] == 0

    def get_quadradosVazios(self):
        quadradosVazios = []
        for row in range(ROWS):
            for col in range (COLS):
                if self.quadradoVazio(row, col):
                    quadradosVazios.append( (row, col) )
        return quadradosVazios

    def estaCheio(self):
        return self.marked_sqrs == 9

    def estaVazio(self):
        return self.marked_sqrs == 0


class IA:
    
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    def rndow(self, Tabuleiro):
        quadradosVazios = Tabuleiro.get_quadradosVazios()
        indx = random.randrange(0, len(quadradosVazios))

        return quadradosVazios[indx]

    def minimax(self, Tabuleiro, maximizing):
        #Caso Terminal
        t_case = Tabuleiro.estadoFinal()
        #Jogador ganhou
        if t_case == 1:
            return 1, None
        #IA ganhou
        if t_case == 2:
            return -1, None
        #Empate
        elif Tabuleiro.estaCheio():
            return 0, None

        if maximizing:
            max_avaliar = -float('inf')
            best_move = None
            quadradosVazios = Tabuleiro.get_quadradosVazios()

            for (row, col) in quadradosVazios:
                temp_Tabuleiro = copy.deepcopy(Tabuleiro)
                temp_Tabuleiro.marcarQuadrado(row, col, 1)
                avaliar = self.minimax(temp_Tabuleiro, False)[0]
                if avaliar > max_avaliar:
                    max_avaliar = avaliar
                    best_move = (row, col)
            
            return max_avaliar, best_move 

        elif not maximizing:
            min_avaliar = float('inf')
            best_move = None
            quadradosVazios = Tabuleiro.get_quadradosVazios()

            for (row, col) in quadradosVazios:
                temp_Tabuleiro = copy.deepcopy(Tabuleiro)
                temp_Tabuleiro.marcarQuadrado(row, col, self.player)
                avaliar = self.minimax(temp_Tabuleiro, True)[0]
                if avaliar < min_avaliar:
                    min_avaliar = avaliar
                    best_move = (row, col)
            
            return min_avaliar, best_move   

    def avaliar(self, m_Tabuleiro):
        if self.level == 0:
            #Decisão aleatoria
            move = self.rndow(m_Tabuleiro)
            return move
        else:
            #Algoritimo Minimax
            avaliar, move = self.minimax(m_Tabuleiro, False)
        
            if avaliar == -1:
                print(f'IA: Joguei na posição {move}, e eu vou ganhar!')
            elif avaliar == 1:
                print(f'IA: Joguei na posição {move}, parece que você via ganhar...')
            else:
                print(f'IA: Joguei na posição {move}, parece que vamos empatar!')
            return move

    
class Jogo:
    
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.ia = IA()
        self.player = 1
        self.gamemode = 'ia'
        self.running = True
        self.draw_lines()

    def movimentar(self, row, col):
        self.tabuleiro.marcarQuadrado(row, col, self.player)
        self.draw_figure(row, col)
        self.next_player()

    def draw_lines(self):
        # COR DE FUNDO
        tela.fill( BCG_COLOR )
        # VERTICAL
        pygame.draw.line( tela, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line( tela, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # HORIZONTAL
        pygame.draw.line( tela, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line( tela, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

    def draw_figure(self, row, col):
        if self.player == 1:
            # Linha descendente
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            # Linha ascendente
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(tela, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            pygame.draw.line(tela, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
        if self.player == 2:
            # Desenhar o círculo
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(tela, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

    def next_player(self):
        self.player = self.player % 2 + 1

    def mudar_modo(self):
        self.gamemode = 'ia' if self.gamemode == 'pvp' else 'pvp'
        modo_de_jogo = self.gamemode
        return modo_de_jogo
    
    def restart(self):
        self.__init__()

    def over(self):
        return self.tabuleiro.estadoFinal(gameover=True) != 0 or self.tabuleiro.estaCheio()

# mainloop
def main():

    jogo = Jogo()
    tabuleiro = jogo.tabuleiro
    ia = jogo.ia


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    modo_atual = jogo.mudar_modo()
                    print(f'Modo de jogo alterado para {modo_atual.upper()}')

                if event.key == pygame.K_r:
                    jogo.restart()
                    tabuleiro = jogo.tabuleiro
                    ia = jogo.ia
                    print('Reiniciando jogo...')    
                
                if event.key == pygame.K_0:
                    ia.level = 0
                    print('A IA agora irá atuar no modo fácil.')

                if event.key == pygame.K_1:
                    ia.level = 1
                    print('A IA agora irá atuar no modo inteligente.')
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                row = position[1] // SQSIZE
                col = position[0] // SQSIZE

                if tabuleiro.quadradoVazio(row, col) and jogo.running:
                    jogo.movimentar(row, col)

                    if jogo.over():
                        match tabuleiro.estadoFinal():
                            case 1:
                                print('O jogador 1 ganhou a partida!')
                            case 2:
                                print('O jogador 2/IA ganhou a partida!')
                            case 0:
                                print('Houve um empate!')
                        jogo.running = False

        if jogo.gamemode == 'ia' and jogo.player == ia.player and jogo.running:
            pygame.display.update()
            #IA "enxergando" a tela
            row, col = ia.avaliar(tabuleiro)
            #IA Jogando
            tabuleiro.marcarQuadrado(row, col, ia.player)
            jogo.draw_figure(row, col)
            jogo.next_player()

            #Se o jogo acabou, não fazer nada
            if jogo.over():
                match tabuleiro.estadoFinal():
                    case 2:
                        print('IA: Eu ganhei a partida!')
                    case 0:
                        print('IA: Houve um empate!')
                jogo.running = False


        pygame.display.update()

main()