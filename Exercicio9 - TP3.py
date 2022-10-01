import pygame
from pygame.locals import * 
 
pygame.init() 
 
azul = (0, 0, 255)
preto = (0, 0, 0) 
 
comprimento_tela = 640
altura_tela = 480
 
tela = pygame.display.set_mode((comprimento_tela, altura_tela))
 
def desenharCirculo(): 
    raio_circulo = 50    
    xpos = comprimento_tela // 2
    ypos = altura_tela // 2
    
    circulo = pygame.draw.circle(tela, azul, (xpos, ypos), raio_circulo)
desenharCirculo() 
pygame.display.flip()
