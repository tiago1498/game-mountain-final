import pygame

print('Setup start')
pygame.init()
window = pygame.display.set_mode(size=(600,480))
print('Setup end')

while True:
    #checando todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #fecha a janela
            quit()