
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)  # -1 para continuar tocando

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

            # checando todos os eventos
            for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()  # fecha a janela
                quit()  # encerra o jogo

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, antialias=True, color=text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

