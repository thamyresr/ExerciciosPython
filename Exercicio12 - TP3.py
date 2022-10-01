import pygame
from pygame.locals import *
  
pygame.init()
 
amarelo = (255, 255, 0)
preto = (0, 0, 0) 
 
comprimento_tela = 640
altura_tela = 480
 
tela = pygame.display.set_mode((comprimento_tela, altura_tela))

fpsClock = pygame.time.Clock()
fps = 200

raio_circulo = 50
 
xpos = comprimento_tela // 2
ypos = altura_tela // 2

def desenharCirculo():
    circulo = pygame.draw.circle(tela, amarelo, (xpos, ypos), raio_circulo)
 
andarl = -1
andarr = 1
pygame.display.flip()


pygame.key.set_repeat(100, 100)
 
while True:
    for event in pygame.event.get():
        pass
 
    tecla_pressionada = pygame.key.get_pressed()
 
    if tecla_pressionada[K_LEFT]:
        xpos += andarl
        if xpos == -raio_circulo:
            xpos = 640
        
    elif tecla_pressionada[K_RIGHT]:  
        xpos += andarr
        if xpos == comprimento_tela:
            xpos = -50
    elif tecla_pressionada[K_UP]:
        ypos += andarl
        if ypos == -raio_circulo:
            ypos = altura_tela
    elif tecla_pressionada[K_DOWN]:
        ypos += andarr
        if ypos == altura_tela + raio_circulo:
            ypos = -raio_circulo
    
    
    tela.fill(preto)
    desenharCirculo()
    pygame.display.flip()
    fpsClock.tick(fps)