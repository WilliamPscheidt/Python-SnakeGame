import pygame
import random

pygame.init()

tamanho = 512
largura = 512

screen = pygame.display.set_mode((tamanho,largura))

localizacaoInicial_x = 1
localizacaoInicial_y = 1

comidaX = random.randint(1, 512)
comidaY = random.randint(1, 512)

print("localizacao", comidaX, comidaY)

def spawnarComida():
    pygame.draw.circle(screen, (cor1, cor2, cor3), (comidaX, comidaY), 5)
    if localizacaoInicial_x==comidaX and localizacaoInicial_y==comidaY:
        print(localizacaoInicial_x)
        print(localizacaoInicial_y)

while True:
    screen.fill((0, 0, 0))

    cor1=255
    cor2=255
    cor3=255

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pressed = pygame.key.get_pressed()

    spawnarComida()

    if pressed[pygame.K_UP]:
        localizacaoInicial_x=localizacaoInicial_x-0.1
        pygame.draw.circle(screen, (cor1, cor2, cor3), (localizacaoInicial_y, localizacaoInicial_x), 5)
        if (localizacaoInicial_x <= 0):
            localizacaoInicial_x=512
        pygame.display.flip()

    elif pressed[pygame.K_DOWN]:
        localizacaoInicial_x=localizacaoInicial_x+0.1
        pygame.draw.circle(screen, (cor1, cor2, cor3), (localizacaoInicial_y, localizacaoInicial_x), 5)
        if (localizacaoInicial_x >= 512):
            localizacaoInicial_x=1
        pygame.display.flip()

    elif pressed[pygame.K_RIGHT]:
        localizacaoInicial_y=localizacaoInicial_y+0.1
        pygame.draw.circle(screen, (cor1, cor2, cor3), (localizacaoInicial_y, localizacaoInicial_x), 5)
        if (localizacaoInicial_y >= 512):
            localizacaoInicial_y=1
        pygame.display.flip()

    elif pressed[pygame.K_LEFT]:
        localizacaoInicial_y=localizacaoInicial_y-0.1
        pygame.draw.circle(screen, (cor1, cor2, cor3), (localizacaoInicial_y, localizacaoInicial_x), 5)
        if (localizacaoInicial_y <= 0):
            localizacaoInicial_y=512
        pygame.display.flip()
