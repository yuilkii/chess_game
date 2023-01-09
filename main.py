import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 110

    def render(self, screen):
        for x in range(self.height):
            for y in range(self.width):
                coord = (self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, (255, 255, 255), coord, 2)

    def get_coord(self, coord):
        x, y = coord
        if (self.left <= x <= self.left + self.width * self.cell_size and
                self.top <= y <= self.top + self.height * self.cell_size):
            print((x - self.left) // self.cell_size,
                  (y - self.top) // self.cell_size)
        else:
            print(None)

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
    def __init__(self, color, life=True):
        if color == 'white':
            self.makeapiece_w()
        else:
            self.makeapiece_b()

    def makeapiece_w(self):
        piece = pygame.image.load('data/white_king.png')
        cr = piece.get_rect(center=(382, 782))
        screen.blit(piece, cr)
        pygame.display.update()
        # else:
        #     piece = pygame.image.load('data/black_king.png')
        #     self.color = 1

    def makeapiece_b(self):
        piece = pygame.image.load('data/black_king.png')
        cr = piece.get_rect(center=(378, 80))
        screen.blit(piece, cr)
        pygame.display.update()


class Rock:
    def __init__(self, color, life=True):
        if color == 'white':
            self.makeapiece_w()
        else:
            self.makeapiece_b()

    def makeapiece_w(self):
        piece = pygame.image.load('data/white_rock.png')
        cr = piece.get_rect(center=(78, 782))
        cr2 = piece.get_rect(center=(782, 782))
        screen.blit(piece, cr)
        screen.blit(piece, cr2)
        pygame.display.update()

    def makeapiece_b(self):
        piece = pygame.image.load('data/black_rock.png')
        cr = piece.get_rect(center=(78, 78))
        cr2 = piece.get_rect(center=(782, 78))
        screen.blit(piece, cr)
        screen.blit(piece, cr2)
        pygame.display.update()


class Knight:
    def __init__(self, color, life=True):
        if color == 'white':
            self.makeapiece_w()
        else:
            self.makeapiece_b()

    def makeapiece_w(self):
        piece = pygame.image.load('data/white_knight.png')
        cr = piece.get_rect(center=(180, 782))
        cr2 = piece.get_rect(center=(680, 782))
        screen.blit(piece, cr)
        screen.blit(piece, cr2)
        pygame.display.update()

    def makeapiece_b(self):
        piece = pygame.image.load('data/black_knight.png')
        cr = piece.get_rect(center=(180, 80))
        cr2 = piece.get_rect(center=(680, 80))
        screen.blit(piece, cr)
        screen.blit(piece, cr2)
        pygame.display.update()


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    size = width, height = 860, 860
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        Board(1080, 1080).makeaboard()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         King('white', life=True)
            #         King('black', life=True)
            #         Rock('white', life=True)
            #         Rock('black', life=True)
            #         Knight('white', life=True)
            #         Knight('black', life=True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                print(Board(width, height).get_coord(event.pos))
        # pygame.display.flip()
        King('white', life=True)
        King('black', life=True)
        Rock('white', life=True)
        Rock('black', life=True)
        Knight('white', life=True)
        Knight('black', life=True)
    pygame.quit()
