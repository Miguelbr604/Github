import pygame
import random

pygame.init()

largura = 500
altura = 500

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cobrinha IA")

preto = (0,0,0)
verde = (0,255,0)
vermelho = (255,0,0)
branco = (255,255,255)

tamanho_bloco = 10
fps = 144

clock = pygame.time.Clock()

fonte = pygame.font.SysFont(None, 35)

def mostrar_pontuacao(pontos):
    texto = fonte.render("Pontos: " + str(pontos), True, branco)
    tela.blit(texto, (10,10))


# IA da cobra
def ia_movimento(x, y, comida_x, comida_y):

    if x < comida_x:
        return 10,0

    elif x > comida_x:
        return -10,0

    elif y < comida_y:
        return 0,10

    elif y > comida_y:
        return 0,-10

    return 0,0


x = largura // 2
y = altura // 2

x_mudanca = 0
y_mudanca = 0

cobra = []
tamanho_cobra = 1

comida_x = random.randrange(0, largura, tamanho_bloco)
comida_y = random.randrange(0, altura, tamanho_bloco)

pontuacao = 0

rodando = True

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

    # movimento com IA
    x_mudanca, y_mudanca = ia_movimento(x, y, comida_x, comida_y)

    x += x_mudanca
    y += y_mudanca

    # colisão com parede
    if x >= largura or x < 0 or y >= altura or y < 0:
        rodando = False

    tela.fill(preto)

    pygame.draw.rect(tela, vermelho, (comida_x, comida_y, tamanho_bloco, tamanho_bloco))

    cabeca = [x,y]
    cobra.append(cabeca)

    if len(cobra) > tamanho_cobra:
        del cobra[0]

    # colisão com corpo
    for parte in cobra[:-1]:
        if parte == cabeca:
            rodando = False

    for parte in cobra:
        pygame.draw.rect(tela, verde, (parte[0], parte[1], tamanho_bloco, tamanho_bloco))

    # colisão com comida
    if x == comida_x and y == comida_y:

        comida_x = random.randrange(0, largura, tamanho_bloco)
        comida_y = random.randrange(0, altura, tamanho_bloco)

        tamanho_cobra += 1
        pontuacao += 1

    mostrar_pontuacao(pontuacao)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()