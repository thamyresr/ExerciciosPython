import pygame
from pygame.locals import *
 
pygame.init() 
 
azul = (0, 0, 255)
preto = (0, 0, 0)
 
fps = 200 
 
comprimento_tela = 640
altura_tela = 480
 
tela = pygame.display.set_mode((comprimento_tela, altura_tela))
 
fps_clock = pygame.time.Clock()

raio_circulo = 50
 
xpos = comprimento_tela // 2 
ypos = altura_tela // 2

def desenharCirculo():
    circulo = pygame.draw.circle(tela, azul, (xpos, ypos), raio_circulo)
 
andar = 5
 
pygame.display.flip()
 
pygame.key.set_repeat(100, 100)
 
while True:       
    tela.fill(preto)
    xpos += andar
    if xpos == comprimento_tela:
        xpos = 0
    desenharCirculo()

    pygame.display.flip()
    
    fps_clock.tick(fps)
