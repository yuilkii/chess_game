import pygame

pos = []


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 30
        self.top = 30
        self.cell_size = 100

    def get_coord(self, coord):
        x, y = coord
        if (self.left <= x <= self.left + self.width * self.cell_size and
                self.top <= y <= self.top + self.height * self.cell_size):
            return (x - self.left) // self.cell_size, (y - self.top) // self.cell_size

    def makeaboard(self):
        brd = pygame.image.load('data/board.jpg')
        cr = brd.get_rect(center=(width // 2, height // 2))
        screen.blit(brd, cr)
        # pygame.display.update()


class Piece:
    def __init__(self, piece_name, piece_coord, color1, path):
        global positions, pos
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
        self.piece_name = piece_name
        self.cmove = []

    def update_pos(self):
        if self.piece_name == 'pawn':
            positions[y][x] = '-'
        if self.piece_name == 'knight':
            positions[y][x] = '-'
        if self.piece_name == 'bishop':
            positions[y][x] = '-'
        if self.piece_name == 'queen':
            positions[y][x] = '-'
        if self.piece_name == 'rock':
            positions[y][x] = '-'
        if self.piece_name == 'king':
            positions[y][x] = '-'

    def can_move(self):
        if self.color1 == 'white':
            self.clr = -1
        else:
            self.clr = 1

        if self.piece_name == 'knight':
            try:
                if positions[self.piece_coord[0] - 1][self.piece_coord[1] + 2] == '-':  #
                    self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1] + 2)  #
                if positions[self.piece_coord[0] - 1][self.piece_coord[1] - 2] == '-':  #
                    self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1] - 2)  #
                if positions[self.piece_coord[0] + 1][self.piece_coord[1] - 2] == '-':  #
                    self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1] - 2)  #
                if positions[self.piece_coord[0] + 1][self.piece_coord[1] + 2] == '-':  #
                    self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1] + 2)  #
                if positions[self.piece_coord[0] - 2][self.piece_coord[1] - 1] == '-':  #
                    self.drow_circle(self.piece_coord[0] - 2, self.piece_coord[1] - 1)  #
                if positions[self.piece_coord[0] - 2][self.piece_coord[1] + 1] == '-':  #
                    self.drow_circle(self.piece_coord[0] - 2, self.piece_coord[1] + 1)  #
                if positions[self.piece_coord[0] + 2][self.piece_coord[1] - 1] == '-':
                    self.drow_circle(self.piece_coord[0] + 2, self.piece_coord[1] - 1)
                if positions[self.piece_coord[0] + 2][self.piece_coord[1] + 1] == '-':  #
                    self.drow_circle(self.piece_coord[0] + 2, self.piece_coord[1] + 1)  #
            except Exception:
                print('error')

        elif self.piece_name == 'king':
            self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1] + 1)

            self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1] + 1)
            self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1] - 1)
            self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1] + 1)
            self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1] - 1)
            self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1])
            self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1])
        elif self.piece_name == 'rock':
            line_xm = 1
            line_xp = 1
            line_ym = 1
            line_yp = 1
            for i in range(1, 9):

                try:
                    if positions[self.piece_coord[0]][self.piece_coord[1] + i] == '-' and line_xm == 1:
                        self.drow_circle(self.piece_coord[0], i)
                    else:
                        line_xm = 0
                    if line_ym == 1 and positions[self.piece_coord[0] - i][self.piece_coord[1]] == '-':
                        self.drow_circle(i, self.piece_coord[1])
                    else:
                        line_ym = 0
                    if line_xp == 1 and positions[self.piece_coord[0] - i][self.piece_coord[1]] == '-':
                        self.drow_circle(i, self.piece_coord[1])
                    else:
                        line_xp = 0
                    if line_yp == 1 and positions[self.piece_coord[0] - i][self.piece_coord[1]] == '-':
                        self.drow_circle(i, self.piece_coord[1])
                    else:
                        line_yp = 0
                except Exception:
                    print('error')

        elif self.piece_name == 'bishop':
            for i in range(1, 8):
                if self.piece_coord[0] + i <= 8 and self.piece_coord[1] + i <= 8:
                    if positions[self.piece_coord[0] + i][self.piece_coord[1] + i] == '-':
                        pos.append((self.piece_coord[0] + i, self.piece_coord[1] + i))
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1] + i)
                    else:
                        break
                else:
                    break
            for i in range(1, 8):
                if self.piece_coord[0] - i <= 8 and self.piece_coord[1] - i <= 8:
                    if positions[self.piece_coord[0] - i][self.piece_coord[1] - i - 1] == '-':
                        pos.append((self.piece_coord[0] - i, self.piece_coord[1] - i))
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1] - i)
                    else:
                        break
                else:
                    break

            for i in range(1, 8):
                if self.piece_coord[0] - i <= 8 and self.piece_coord[1] + i <= 8:
                    if positions[self.piece_coord[0] - i][self.piece_coord[1] + i] == '-':
                        pos.append((self.piece_coord[0] - i, self.piece_coord[1] + i))
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1] + i)
                    else:
                        break
                else:
                    break
            for i in range(1, 8):
                # print(positions[self.piece_coord[0] + i - 1][self.piece_coord[1] - i - 1], positions[3][4])
                if self.piece_coord[0] + i <= 8 and self.piece_coord[1] - i <= 8:
                    if positions[self.piece_coord[0] + i][self.piece_coord[1] - i] == '-':
                        pos.append((self.piece_coord[0] + i, self.piece_coord[1] - i))
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1] - i)
                    else:
                        break
                else:
                    break

        elif self.piece_name == 'queen':
            for i in range(8):
                self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1] + i)
                self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1] - i)
                self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1] + i)
                self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1] - i)
                self.drow_circle(self.piece_coord[0], i)
                self.drow_circle(i, self.piece_coord[1])
        elif self.piece_name == 'king':
            self.drow_circle(self.piece_coord[0], self.piece_coord[1] - 1)
            self.drow_circle(self.piece_coord[0], self.piece_coord[1] + 1)
            self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1])
            self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1])
            self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1] + 1)
            self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1] + 1)
            self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1] - 1)
            self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1] - 1)
        elif self.piece_name == 'pawn':
            if positions[self.piece_coord[1] + self.clr][self.piece_coord[0]] == '-':
                self.drow_circle(self.piece_coord[0], self.piece_coord[1] + self.clr)
                pos.append((self.piece_coord[0], self.piece_coord[1]+ self.clr))
            # if positions[self.piece_coord[0]][
            #     self.piece_coord[1] + self.clr] != '-':  # leva moжно есть права нет
            #     self.drow_circle(self.piece_coord[0], self.piece_coord[1] + self.clr)
            #     pos.append((self.piece_coord[0], self.piece_coord[1]))
            # if positions[self.piece_coord[0]][self.piece_coord[1] + q - 1] != '-':
            #     self.drow_circle(self.piece_coord[0], self.piece_coord[1] + q)

    def drow_circle(self, x, y):
        # print(x, y, positions[y - 1][x - 1])
        if 1 <= x <= 8 and 1 <= y <= 8 and positions[y][x] == '-':
            pygame.draw.circle(screen, (100, 100, 100), (x * 100 - 20, y * 100 - 20), 20)

    def move(self, x1, y1):
        print((x1, y1), pos)
        if (x1, y1) in pos:
            if self.piece_name == 'pawn':

                if self.clr == -1:

                    brd = pygame.image.load('data/white_pawn.png')
                    print(234234234)

                    self.piece_coord = x1, y1
                else:
                    brd = pygame.image.load('data/black_pawn.png')

                    self.piece_coord = x1, y1

                if self.piece_name == 'knight':
                    pass
                if self.piece_name == 'king':
                    pass
                if self.piece_name == 'bishop':
                    pass
                if self.piece_name == 'rock':
                    pass
                if self.piece_name == 'queen':
                    pass


w_pawn1 = Piece('pawn', (2, 6), 'white', 'data/white_pawn.png')
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
w_rock = Piece('rock', (1, 8), 'white', 'data/white_rock.png')
w_rock2 = Piece('rock', (8, 8), 'white', 'data/white_rock.png')
b_rock = Piece('rock', (8, 1), 'black', 'data/black_rock.png')
b_rock2 = Piece('rock', (1, 1), 'black', 'data/black_rock.png')
w_knight = Piece('knight', (2, 8), 'white', 'data/white_knight.png')
w_knight2 = Piece('knight', (4, 4), 'white', 'data/white_knight.png')
b_knight = Piece('knight', (2, 1), 'black', 'data/black_knight.png')
b_knight2 = Piece('knight', (7, 1), 'black', 'data/black_knight.png')
w_bishop = Piece('bishop', (4, 5), 'white', 'data/white_bishop.png')
w_bishop2 = Piece('bishop', (6, 8), 'white', 'data/white_bishop.png')
b_bishop = Piece('bishop', (3, 1), 'black', 'data/black_bishop.png')
b_bishop2 = Piece('bishop', (6, 1), 'black', 'data/black_bishop.png')
w_queen = Piece('queen', (4, 8), 'white', 'data/white_queen.png')
b_queen = Piece('queen', (4, 1), 'black', 'data/black_queen.png')
w_king = Piece('king', (5, 8), 'white', 'data/white_king.png')
b_king = Piece('king', (5, 1), 'black', 'data/black_king.png')

positions = [
    ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', b_rock2, b_knight, b_bishop, b_queen, b_king, b_bishop2, b_knight2, b_rock],
    ['-', b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', w_knight2, '-', '-', '-', '-'],
    ['-', '-', '-', '-', w_bishop, '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8],
    ['-', w_rock, w_knight, '-', w_queen, w_king, w_bishop2, '-', w_rock2],
]

pices = [b_rock2, b_knight, b_bishop, b_queen, b_king, b_bishop2, b_knight2, b_rock,
         b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8,
         w_knight2, w_bishop,
         w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8,
         w_rock, w_knight, w_queen, w_king, w_bishop2, w_rock2]


def ya_eblan():
    for i in pices:
        positions[i.piece_coord[1]][i.piece_coord[0]] = i
    for i in positions:
        for j in i:

            if j != '-':
                piece = pygame.image.load(j.path)
                screen.blit(piece, ((j.piece_coord[0] - 1) * 100 + 30, (j.piece_coord[1] - 1) * 100 + 30))


if __name__ == '__main__':
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
                x += 1
                y += 1
                # if w_knight == positions[x][y]:
                if positions[y][x] != '-':
                    positions[y][x].can_move()

                    print(x, y, positions[y][x])
                # Knight('white').can_move(x, y, q, w)
                # pygame.draw.circle(screen, (100, 100, 100), (x, y - 100), 20)
            if event.type == pygame.MOUSEBUTTONUP:
                q, w = pygame.mouse.get_pos()
                x1, y1 = Board(width, height).get_coord(event.pos)
                x1 += 1
                y1 += 1
                if positions[y][x] != '-':
                    positions[y][x].move(x1, y1)
                    print(112)
                    pos = []
                Board(1080, 1080).makeaboard()

                pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)
        ya_eblan()
        pygame.display.update()
    pygame.quit()
