import pygame

pygame.init()
clock = pygame.time.Clock()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
preto = (0, 0, 0)
azul = (0, 0, 255)
x = largura_tela // 2
y = altura_tela // 2

def desenha(tela, cor, x, y):   
    area = (x, y, 50, 50)
    pygame.draw.rect(tela, cor, area)

terminou = False
while not terminou:
    clock.tick(60)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]      
        if event.type == pygame.QUIT:
            terminou = True
            
    tela.fill(preto)         
    if x == 0 and y == 0:    
        desenha(tela, azul, 400, 300)
    else:
        desenha(tela, azul, x, y)
        
pygame.display.quit()
pygame.quit()
