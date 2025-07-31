import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



#checando todos os eventos
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #pygame.quit()  # fecha a janela
                    #quit() #encerra o jogo
