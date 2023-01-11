import pygame


# positions = [[
#     ['wr', 'wkn', 'wb', 'wq', 'wk', 'wb2', 'wkn2', 'wr2'],
#     ['wp1', 'wp2', 'wp3', 'wp4', 'wp5', 'wp6', 'wp7', 'wp8'],
#     ['-', '-', '-', '-', '-', '-', '-', '-'],
#     ['-', '-', '-', '-', '-', '-', '-', '-'],
#     ['-', '-', '-', '-', '-', '-', '-', '-'],
#     ['-', '-', '-', '-', '-', '-', '-', '-'],
#     ['bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6', 'bp7', 'bp8'],
#     ['br', 'bkn', 'bb', 'bq', 'bk', 'bb2', 'bkn2', 'br2']
# ]]

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

    def can_move(self, x, y, q, w):
        if 0 <= x + 1 < 8 and 0 <= y + 2 < 8:
            pygame.draw.circle(screen, (100, 100, 100), (q + 100, w + 200), 20)
        if 0 <= x + 2 < 8 and 0 <= y + 1 < 8:
            pygame.draw.circle(screen, (100, 100, 100), (q + 200, w + 100), 20)
        if 0 <= x + 2 < 8 and 0 <= y - 1 < 8:
            pygame.draw.circle(screen, (100, 100, 100), (q + 200, w - 100), 20)
        if 0 <= x + 1 < 8 and 0 <= y - 2 < 8:
            pygame.draw.circle(screen, (100, 100, 100), (q + 100, w - 200), 20)
        if 0 <= x - 1 < 8 and 0 <= y - 2 < 8:
            pygame.draw.circle(screen, (100, 100, 100), (q - 100, w - 200), 20)
        if 0 <= x - 2 < 8 and 0 <= y - 1 < 8:
            pygame.draw.circle(screen, (100, 100, 100), (q - 200, w - 100), 20)
        if 0 <= x - 2 < 8 and 0 <= y + 1 <= 8:
            pygame.draw.circle(screen, (100, 100, 100), (q - 200, w + 100), 20)
        if 0 <= x - 1 < 8 and 0 <= y + 2 < 8:
            pygame.draw.circle(screen, (100, 100, 100), (q - 100, w + 200), 20)


class Piece:
    def __init__(self, piece_names, piece_coord, color1, path):
        global positions
        self.piece_names = {
            "pawn",
            "rock",
            "queen",
            "king",
            "bishop",
            "knight"
        }
        self.piece_coord = piece_coord
        self.color1 = color1
        self.path = path

    def update_pos(self):
        pass


w_pawn1 = Piece('pawn', (1, 7), 'white', 'data/white_pawn.png')
w_pawn2 = Piece('pawn', (2, 7), 'white', 'data/white_pawn.png')
w_pawn3 = Piece('pawn', (3, 7), 'white', 'data/white_pawn.png')
w_pawn4 = Piece('pawn', (4, 7), 'white', 'data/white_pawn.png')
w_pawn5 = Piece('pawn', (5, 7), 'white', 'data/white_pawn.png')
w_pawn6 = Piece('pawn', (6, 7), 'white', 'data/white_pawn.png')
w_pawn7 = Piece('pawn', (7, 7), 'white', 'data/white_pawn.png')
w_pawn8 = Piece('pawn', (8, 7), 'white', 'data/white_pawn.png')
b_pawn1 = Piece('pawn', (1, 2), 'black', 'data/black_pawn.png')
b_pawn2 = Piece('pawn', (2, 2), 'black', 'data/black_pawn.png')
b_pawn3 = Piece('pawn', (3, 2), 'black', 'data/black_pawn.png')
b_pawn4 = Piece('pawn', (4, 2), 'black', 'data/black_pawn.png')
b_pawn5 = Piece('pawn', (5, 2), 'black', 'data/black_pawn.png')
b_pawn6 = Piece('pawn', (6, 2), 'black', 'data/black_pawn.png')
b_pawn7 = Piece('pawn', (7, 2), 'black', 'data/black_pawn.png')
b_pawn8 = Piece('pawn', (8, 2), 'black', 'data/black_pawn.png')
w_rock = Piece('rock', (8, 8), 'white', 'data/white_rock.png')
w_rock2 = Piece('rock', (1, 8), 'white', 'data/white_rock.png')
b_rock = Piece('rock', (8, 1), 'black', 'data/black_rock.png')
b_rock2 = Piece('rock', (1, 1), 'black', 'data/black_rock.png')
w_knight = Piece('knight', (2, 8), 'white', 'data/white_knight.png')
w_knight2 = Piece('knight', (7, 8), 'white', 'data/white_knight.png')
b_knight = Piece('knight', (2, 1), 'black', 'data/black_knight.png')
b_knight2 = Piece('knight', (7, 1), 'black', 'data/black_knight.png')
w_bishop = Piece('bishop', (3, 8), 'white', 'data/white_bishop.png')
w_bishop2 = Piece('bishop', (6, 8), 'white', 'data/white_bishop.png')
b_bishop = Piece('bishop', (3, 1), 'black', 'data/black_bishop.png')
b_bishop2 = Piece('bishop', (6, 1), 'black', 'data/black_bishop.png')
w_queen = Piece('queen', (4, 8), 'white', 'data/white_queen.png')
b_queen = Piece('queen', (4, 1), 'black', 'data/black_queen.png')
w_king = Piece('king', (5, 8), 'white', 'data/white_king.png')
b_king = Piece('king', (5, 1), 'black', 'data/black_king.png')

positions = [
    [w_rock, w_knight, w_bishop, w_queen, w_king, w_bishop2, w_knight2, w_rock2],
    [w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    [b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8],
    [b_rock, b_knight, b_bishop, b_queen, b_king, b_bishop2, b_knight2, b_rock2]
]


def ya_eblan():
    for i in positions:
        for j in i:
            if j == '-':
                continue
            piece = pygame.image.load(j.path)
            screen.blit(piece, ((j.piece_coord[0] - 1) * 100 + 30, (j.piece_coord[1] - 1) * 100 + 30))
            pygame.display.update()


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
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(pygame.mouse.get_pos())
                # print(Board(width, height).get_coord(event.pos))
                q, w = pygame.mouse.get_pos()
                x, y = Board(width, height).get_coord(event.pos)
                if w_knight in positions[x][y]:
                    Knight('white').can_move(x, y, q, w)
                pygame.draw.circle(screen, (100, 100, 100), (x, y - 100), 20)
            if event.type == pygame.MOUSEBUTTONUP:
                Board(1080, 1080).makeaboard()
        # pygame.display.flip()
        # Pieces(1080, 1080)
        # King('white', life=True)
        # King('black', life=True)
        # Rock('white', life=True)
        # Rock('black', life=True)
        # Knight('white', life=True)
        # Knight('black', life=True)
        # Bishop('white', life=True)
        # Bishop('black', life=True)
        # Queen('white', life=True)
        # Queen('black', life=True)
        # Pawn('white', life=True)
        # Pawn('black', life=True)
        ya_eblan()
    pygame.quit()

