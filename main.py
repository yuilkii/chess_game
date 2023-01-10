import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 30
        self.top = 30
        self.cell_size = 100

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
            return (x - self.left) // self.cell_size, (y - self.top) // self.cell_size
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

# class Pieces:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.left = 30
#         self.top = 30
#         self.cell_size = 100
#
#     def can_move(self, piece, ):
#         x, y, = self.get_coord(pygame.mouse.get_pos())
#         q, w = pygame.mouse.get_pos()
#         if piece == 'knight':
#             if 0 <= x + 1 < 8 and 0 <= y + 2 < 8:
#                 pygame.draw.circle(screen, (100, 100, 100), (q + 100, w + 200), 20)
#             if 0 <= x + 2 < 8 and 0 <= y + 1 < 8:
#                 pygame.draw.circle(screen, (100, 100, 100), (q + 200, w + 100), 20)
#             if 0 <= x + 2 < 8 and 0 <= y - 1 < 8:
#                 pygame.draw.circle(screen, (100, 100, 100), (q + 200, w - 100), 20)
#             if 0 <= x + 1 < 8 and 0 <= y - 2 < 8:
#                 pygame.draw.circle(screen, (100, 100, 100), (q + 100, w - 200), 20)
#             if 0 <= x - 1 < 8 and 0 <= y - 2 < 8:
#                 pygame.draw.circle(screen, (100, 100, 100), (q - 100, w - 200), 20)
#             if 0 <= x - 2 < 8 and 0 <= y - 1 < 8:
#                 pygame.draw.circle(screen, (100, 100, 100), (q - 200, w - 100), 20)
#             if 0 <= x - 2 < 8 and 0 <= y + 1 <= 8:
#                 pygame.draw.circle(screen, (100, 100, 100), (q - 200, w + 100), 20)
#             if 0 <= x - 1 < 8 and 0 <= y + 2 < 8:
#                 pygame.draw.circle(screen, (100, 100, 100), (q - 100, w + 200), 20)
#         elif piece == 'bishop':
#             pass
#         elif piece == 'king':
#             pass
#         elif piece == 'rock':
#             pass
#         elif piece == 'queen':
#             pass
#         elif piece == 'king':
#             pass
#         elif piece == 'pawn':
#             pass
#
#     def piece(self):
#         pass
#
#     def get_coord(self, coord):
#         x, y = coord
#         if (self.left <= x <= self.left + self.width * self.cell_size and
#                 self.top <= y <= self.top + self.height * self.cell_size):
#             print((x - self.left) // self.cell_size,
#                   (y - self.top) // self.cell_size)
#             return (x - self.left) // self.cell_size, (y - self.top) // self.cell_size
#
#     def color(self):
#         pass
#
#     def life(self):
#         pass
#
#
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


class Queen:
    def __init__(self, color, life=True):
        if color == 'white':
            self.makeapiece_w()
        else:
            self.makeapiece_b()

    def makeapiece_w(self):
        piece = pygame.image.load('data/white_queen.png')
        cr = piece.get_rect(center=(480, 782))
        cr2 = piece.get_rect(center=(480, 782))
        screen.blit(piece, cr)
        screen.blit(piece, cr2)
        pygame.display.update()

    def makeapiece_b(self):
        piece = pygame.image.load('data/black_queen.png')
        cr = piece.get_rect(center=(479, 80))
        cr2 = piece.get_rect(center=(479, 80))
        screen.blit(piece, cr)
        screen.blit(piece, cr2)
        pygame.display.update()


class Bishop:
    def __init__(self, color, life=True):
        if color == 'white':
            self.makeapiece_w()
        else:
            self.makeapiece_b()

    def makeapiece_w(self):
        piece = pygame.image.load('data/white_bishop.png')
        cr = piece.get_rect(center=(282, 782))
        cr2 = piece.get_rect(center=(580, 782))
        screen.blit(piece, cr)
        screen.blit(piece, cr2)
        pygame.display.update()

    def makeapiece_b(self):
        piece = pygame.image.load('data/black_bishop.png')
        cr = piece.get_rect(center=(282, 80))
        cr2 = piece.get_rect(center=(580, 80))
        screen.blit(piece, cr)
        screen.blit(piece, cr2)
        pygame.display.update()

    # def can_move(self, x, y, q, w):
    #     for i in range(1, 9):
    #         for j in range(1, 9):
    #             if self.row + i == row1 and self.col + i == col1:
    #                 return True
    #             elif self.row + i == row1 and self.col - i == col1:
    #                 return True
    #             elif self.row - i == row1 and self.col + i == col1:
    #                 return True
    #             elif self.row - i == row1 and self.col - i == col1:
    #                 return True


class Pawn:
    def __init__(self, color, life=True):
        if color == 'white':
            self.makeapiece_w()
        else:
            self.makeapiece_b()

    def makeapiece_w(self):
        piece = pygame.image.load('data/white_pawn.png')
        for x in range(80, 851, 100):
            cr = piece.get_rect(center=(x, 682))
            # cr2 = piece.get_rect(center=(580, 782))
            screen.blit(piece, cr)
            # screen.blit(piece, cr2)
            pygame.display.update()

    def makeapiece_b(self):
        piece = pygame.image.load('data/black_pawn.png')
        for x in range(80, 851, 100):
            cr = piece.get_rect(center=(x, 182))
            # cr2 = piece.get_rect(center=(580, 782))
            screen.blit(piece, cr)
            # screen.blit(piece, cr2)
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

    # def can_move(self, x, y, q, w):
    #     if 0 <= x + 1 < 8 and 0 <= y + 2 < 8:
    #         pygame.draw.circle(screen, (100, 100, 100), (q + 100, w + 200), 20)
    #     if 0 <= x + 2 < 8 and 0 <= y + 1 < 8:
    #         pygame.draw.circle(screen, (100, 100, 100), (q + 200, w + 100), 20)
    #     if 0 <= x + 2 < 8 and 0 <= y - 1 < 8:
    #         pygame.draw.circle(screen, (100, 100, 100), (q + 200, w - 100), 20)
    #     if 0 <= x + 1 < 8 and 0 <= y - 2 < 8:
    #         pygame.draw.circle(screen, (100, 100, 100), (q + 100, w - 200), 20)
    #     if 0 <= x - 1 < 8 and 0 <= y - 2 < 8:
    #         pygame.draw.circle(screen, (100, 100, 100), (q - 100, w - 200), 20)
    #     if 0 <= x - 2 < 8 and 0 <= y - 1 < 8:
    #         pygame.draw.circle(screen, (100, 100, 100), (q - 200, w - 100), 20)
    #     if 0 <= x - 2 < 8 and 0 <= y + 1 <= 8:
    #         pygame.draw.circle(screen, (100, 100, 100), (q - 200, w + 100), 20)
    #     if 0 <= x - 1 < 8 and 0 <= y + 2 < 8:
    #         pygame.draw.circle(screen, (100, 100, 100), (q - 100, w + 200), 20)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    size = width, height = 860, 860
    screen = pygame.display.set_mode(size)
    running = True
    Board(1080, 1080).makeaboard()
    while running:
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
                q, w = pygame.mouse.get_pos()
                x, y = Board(width, height).get_coord(event.pos)
                Knight('white').can_move(x, y, q, w)
                pygame.draw.circle(screen, (100, 100, 100), (x, y - 100), 20)
            if event.type == pygame.MOUSEBUTTONUP:
                Board(1080, 1080).makeaboard()
        # pygame.display.flip()
        # Pieces(1080, 1080)
        King('white', life=True)
        King('black', life=True)
        Rock('white', life=True)
        Rock('black', life=True)
        Knight('white', life=True)
        Knight('black', life=True)
        Bishop('white', life=True)
        Bishop('black', life=True)
        Queen('white', life=True)
        Queen('black', life=True)
        Pawn('white', life=True)
        Pawn('black', life=True)
    pygame.quit()
