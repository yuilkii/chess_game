import pygame


class MainMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def makeamenu(self):
        brd = pygame.image.load('data/back.png')
        cr = brd.get_rect(center=(width // 2, height // 2))
        screen.blit(brd, cr)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1500, 1100
    screen = pygame.display.set_mode(size)
    running = True
    MainMenu(1600, 1080).makeamenu()
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            # 390x520:1110x720
    pygame.quit()
