import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def makeaboard(self):
        brd = pygame.image.load('data/board.png')
        cr = brd.get_rect(center=(width // 2, height // 2))
        screen.blit(brd, cr)
        pygame.display.update()


# class Piece:
#     def __init__(self, type, team, image, killable=False):
#         self.type = self.type
#         self.team = self.team
#         self.killable = self.killable
#         self.image = self.image

class King:
    def __init__(self, pos, color, image, life=True):
        self.pos = pos
        self.color = color
        self.image = image


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    size = width, height = 1780, 1080
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        Board(1080, 1080).makeaboard()
        pygame.display.flip()
    pygame.quit()
