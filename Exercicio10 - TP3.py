import pygame
from pygame.locals import *
 
pygame.init() 
 
vermelho = (255, 0, 0)
preto = (0, 0, 0)

fps = 200
 
comprimento_tela = 800
altura_tela = 600
 
tela = pygame.display.set_mode((comprimento_tela, altura_tela)) 
 
xpos = comprimento_tela / 2
ypos = altura_tela / 2

def desenharQuadrado(): 
    quadrado = pygame.draw.rect(tela, vermelho, (xpos, ypos,100,100))

movimento_em_x = -1
movimento_em_y = 1
 
pygame.display.flip()
fps_clock = pygame.time.Clock()
pygame.key.set_repeat(100, 100)
 
while True:
    for event in pygame.event.get():
        pass
 
    tecla_pressionada = pygame.key.get_pressed()
 
    if tecla_pressionada[K_LEFT]:
        xpos += movimento_em_x
 
    if tecla_pressionada[K_RIGHT]:
        xpos -= movimento_em_x 
 
    if tecla_pressionada[K_UP]:
        ypos -= movimento_em_y
 
    if tecla_pressionada[K_DOWN]:
        ypos += movimento_em_y
 
    tela.fill(preto)
    
    desenharQuadrado()
    
    pygame.display.flip()
    
    fps_clock.tick(fps)
