import pygame

pos = []
acttiveWindoow = 'Menu'


class MainMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def makeamenu(self):
        brd = pygame.image.load('data/back.png')
        cr = brd.get_rect(center=(width // 2, height // 2))
        screen.blit(brd, cr)


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
        brd = pygame.image.load('data/board.png')
        cr = brd.get_rect(center=(width // 2, height // 2))
        screen.blit(brd, cr)
        # pygame.display.update()


class Piece:
    def __init__(self, piece_name, piece_coord, color1, path, is_alive=True):

        global positions, pos
        self.is_alive = is_alive
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
        self.rak = 0
        if self.color1 == 'white':
            self.clr = -1
        else:
            self.clr = 1

    def can_move(self):

        if self.piece_name == 'knight':
            try:
                self.drow_circle(self.piece_coord[0] + 2, self.piece_coord[1] - 1)  #
            except Exception:
                pass
            try:
                self.drow_circle(self.piece_coord[0] - 2, self.piece_coord[1] - 1)  #
            except Exception:
                pass
            try:
                self.drow_circle(self.piece_coord[0] - 2, self.piece_coord[1] + 1)  #
            except Exception:
                pass
            try:
                self.drow_circle(self.piece_coord[0] + 2, self.piece_coord[1] + 1)  #
            except Exception:
                pass
            try:
                self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1] - 2)  #
            except Exception:
                pass
            try:
                self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1] - 2)  #
            except Exception:
                pass
            try:
                self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1] + 2)
            except Exception:
                pass
            try:
                self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1] + 2)  #
            except Exception:
                pass

        elif self.piece_name == 'rock':
            line_xm = 1
            line_xp = 1
            line_ym = 1
            line_yp = 1
            for i in range(1, 9):
                try:
                    if positions[self.piece_coord[1]][self.piece_coord[0] - i] == '-' and line_xm == 1:
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1])
                    elif line_xm == 1:
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1])
                        line_xm = 0
                except:
                    pass
                try:
                    if line_ym == 1 and positions[self.piece_coord[1] - i][self.piece_coord[0]] == '-':
                        self.drow_circle(self.piece_coord[0], self.piece_coord[1] - i)
                    elif line_ym == 1:
                        self.drow_circle(self.piece_coord[0], self.piece_coord[1] - i)
                        line_ym = 0
                except:
                    pass
                try:
                    if line_xp == 1 and positions[self.piece_coord[1]][self.piece_coord[0] + i] == '-':
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1])
                    elif line_xp == 1:
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1])
                        line_xp = 0
                except:
                    pass
                try:
                    if line_yp == 1 and positions[self.piece_coord[1] + i][self.piece_coord[0]] == '-':
                        self.drow_circle(self.piece_coord[0], self.piece_coord[1] + i)
                    elif line_yp == 1:
                        self.drow_circle(self.piece_coord[0], self.piece_coord[1] + i)
                        line_yp = 0
                except Exception:
                    pass

        elif self.piece_name == 'bishop':
            for i in range(1, 9):
                if self.piece_coord[1] + i <= 8 and self.piece_coord[0] + i <= 8:
                    if positions[self.piece_coord[1] + i][self.piece_coord[0] + i] == '-':
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1] + i)
                    else:
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1] + i)
                        break
                else:
                    break
            for i in range(1, 9):
                if self.piece_coord[1] - i <= 8 and self.piece_coord[0] - i <= 8:
                    if positions[self.piece_coord[1] - i][self.piece_coord[0] - i] == '-':
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1] - i)
                    else:
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1] - i)
                        break
                else:
                    break

            for i in range(1, 9):
                if self.piece_coord[1] - i <= 8 and self.piece_coord[0] + i <= 8:
                    if positions[self.piece_coord[1] - i][self.piece_coord[0] + i] == '-':
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1] - i)
                    else:
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1] - i)
                        break
                else:
                    break
            for i in range(1, 9):
                # print(positions[self.piece_coord[0] + i - 1][self.piece_coord[1] - i - 1], positions[3][4])
                if self.piece_coord[1] + i <= 8 and self.piece_coord[0] - i <= 8:
                    if positions[self.piece_coord[1] + i][self.piece_coord[0] - i] == '-':
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1] + i)
                    else:
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1] + i)
                        break
                else:
                    break

        elif self.piece_name == 'queen':
            line_xm = 1
            line_xp = 1
            line_ym = 1
            line_yp = 1
            for i in range(1, 9):
                try:
                    if positions[self.piece_coord[1]][self.piece_coord[0] - i] == '-' and line_xm == 1:
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1])
                    elif line_xm == 1:
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1])
                        line_xm = 0
                except:
                    pass
                try:
                    if line_ym == 1 and positions[self.piece_coord[1] - i][self.piece_coord[0]] == '-':
                        self.drow_circle(self.piece_coord[0], self.piece_coord[1] - i)
                    elif line_ym == 1:
                        self.drow_circle(self.piece_coord[0], self.piece_coord[1] - i)
                        line_ym = 0
                except:
                    pass
                try:
                    if line_xp == 1 and positions[self.piece_coord[1]][self.piece_coord[0] + i] == '-':
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1])
                    elif line_xp == 1:
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1])
                        line_xp = 0
                except:
                    pass
                try:
                    if line_yp == 1 and positions[self.piece_coord[1] + i][self.piece_coord[0]] == '-':
                        self.drow_circle(self.piece_coord[0], self.piece_coord[1] + i)
                    elif line_yp == 1:
                        self.drow_circle(self.piece_coord[0], self.piece_coord[1] + i)
                        line_yp = 0
                except Exception:
                    pass

            for i in range(1, 9):
                if self.piece_coord[1] + i <= 8 and self.piece_coord[0] + i <= 8:
                    if positions[self.piece_coord[1] + i][self.piece_coord[0] + i] == '-':
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1] + i)
                    else:
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1] + i)
                        break
                else:
                    break
            for i in range(1, 9):
                if self.piece_coord[1] - i <= 8 and self.piece_coord[0] - i <= 8:
                    if positions[self.piece_coord[1] - i][self.piece_coord[0] - i] == '-':
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1] - i)
                    else:
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1] - i)
                        break
                else:
                    break

            for i in range(1, 9):
                if self.piece_coord[1] - i <= 8 and self.piece_coord[0] + i <= 8:
                    if positions[self.piece_coord[1] - i][self.piece_coord[0] + i] == '-':
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1] - i)
                    else:
                        self.drow_circle(self.piece_coord[0] + i, self.piece_coord[1] - i)
                        break
                else:
                    break
            for i in range(1, 9):
                # print(positions[self.piece_coord[0] + i - 1][self.piece_coord[1] - i - 1], positions[3][4])
                if self.piece_coord[1] + i <= 8 and self.piece_coord[0] - i <= 8:
                    if positions[self.piece_coord[1] + i][self.piece_coord[0] - i] == '-':
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1] + i)
                    else:
                        self.drow_circle(self.piece_coord[0] - i, self.piece_coord[1] + i)
                        break
                else:
                    break

        elif self.piece_name == 'king':

            if self.piece_coord[1] > 1:
                self.drow_circle(self.piece_coord[0], self.piece_coord[1] - 1)

            if self.piece_coord[1] < 8:
                self.drow_circle(self.piece_coord[0], self.piece_coord[1] + 1)

            if self.piece_coord[0] < 8:
                self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1])

            if self.piece_coord[0] > 1:
                self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1])

            if self.piece_coord[1] < 8 and self.piece_coord[0] < 8:
                self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1] + 1)

            if self.piece_coord[0] > 1 and self.piece_coord[1] < 8:
                self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1] + 1)

            if self.piece_coord[0] > 1 and 1 < self.piece_coord[1] > 1:
                self.drow_circle(self.piece_coord[0] - 1, self.piece_coord[1] - 1)

            if self.piece_coord[0] < 8 and self.piece_coord[1] > 1:
                self.drow_circle(self.piece_coord[0] + 1, self.piece_coord[1] - 1)
            if self.clr == -1:
                if positions[8][8] == w_rock2:

                    if positions[8][6] == '-' and positions[8][7] == '-':
                        self.drow_circle(self.piece_coord[0] + 2, self.piece_coord[1])
                        self.rak = 1

                if positions[8][1] == w_rock:
                    if positions[8][2] == '-' and positions[8][3] == '-' and positions[8][4] == '-':
                        self.drow_circle(self.piece_coord[0] - 2, self.piece_coord[1])
                        self.rak = 2
            else:
                if positions[1][8] == b_rock:
                    for i in range(6, 8):
                        if positions[1][6] == '-' and positions[1][7] == '-':
                            self.drow_circle(self.piece_coord[0] + 2, self.piece_coord[1])
                            self.rak = 3

                if positions[1][1] == b_rock2:
                    if positions[1][2] == '-' and positions[1][3] == '-' and positions[1][4] == '-':
                        self.drow_circle(self.piece_coord[0] - 2, self.piece_coord[1])
                        self.rak = 4
        elif self.piece_name == 'pawn':
            self.drow_circle(self.piece_coord[0], self.piece_coord[1] + self.clr)
            if self.piece_coord[1] == 2 and self.color1 == 'black':
                self.drow_circle(self.piece_coord[0], self.piece_coord[1] + 2 * self.clr)
            if self.piece_coord[1] == 7 and self.color1 == 'white':
                self.drow_circle(self.piece_coord[0], self.piece_coord[1] + 2 * self.clr)

    def drow_circle(self, x, y):
        # print(x, y, positions[y - 1][x - 1])
        if 1 <= x <= 8 and 1 <= y <= 8 and positions[y][x] == '-':
            pos.append((x, y))
            pygame.draw.circle(screen, (100, 100, 100), (x * 100 - 20, y * 100 - 20), 20)
        if positions[y][x] != '-' and positions[y][x].color1 != self.color1 and self.piece_name != 'pawn':
            pos.append((x, y))
            pygame.draw.circle(screen, (255, 0, 0), (x * 100 - 20, y * 100 - 20), 20)
        if self.piece_name == 'pawn':
            if self.piece_coord[0] < 8:
                if positions[self.piece_coord[1] + self.clr][self.piece_coord[0] + 1] != '-' and \
                        positions[self.piece_coord[1] + self.clr][self.piece_coord[0] + 1].color1 != self.color1:
                    pos.append((self.piece_coord[0] + 1, self.piece_coord[1] + self.clr))
                    pygame.draw.circle(screen, (255, 0, 0),
                                       ((self.piece_coord[0] + 1) * 100 - 20,
                                        (self.piece_coord[1] + self.clr) * 100 - 20),
                                       20)
            if self.piece_coord[0] > 1:
                if positions[self.piece_coord[1] + self.clr][self.piece_coord[0] - 1] != '-' and \
                        positions[self.piece_coord[1] + self.clr][self.piece_coord[0] - 1].color1 != self.color1:
                    pos.append((self.piece_coord[0] - 1, self.piece_coord[1] + self.clr))
                    pygame.draw.circle(screen, (255, 0, 0),
                                       ((self.piece_coord[0] - 1) * 100 - 20,
                                        (self.piece_coord[1] + self.clr) * 100 - 20),
                                       20)

    def move(self, x1, y1):
        global chei_hod
        if (x1, y1) in pos:
            if self.rak == 1:
                w_rock2.piece_coord = (6, 8)
                positions[self.piece_coord[1]][self.piece_coord[0]] = '-'
            elif self.rak == 2:
                positions[self.piece_coord[1]][self.piece_coord[0]] = '-'
                w_rock.piece_coord = (4, 8)
            elif self.rak == 3:
                b_rock.piece_coord = (6, 1)
                positions[self.piece_coord[1]][self.piece_coord[0]] = '-'
            elif self.rak == 4:
                b_rock2.piece_coord = (4, 1)
                positions[self.piece_coord[1]][self.piece_coord[0]] = '-'

            if positions[y1][x1] != '-':
                positions[y1][x1].piece_coord = (0, 0)
            positions[self.piece_coord[1]][self.piece_coord[0]] = '-'
            self.piece_coord = (x1, y1)
        else:
            if chei_hod == 'white':
                chei_hod = 'black'
            else:
                chei_hod = 'white'


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
w_rock = Piece('rock', (1, 8), 'white', 'data/white_rock.png')
w_rock2 = Piece('rock', (8, 8), 'white', 'data/white_rock.png')
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
    ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', b_rock2, b_knight, b_bishop, b_queen, b_king, b_bishop2, b_knight2, b_rock],
    ['-', b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8],
    ['-', w_rock, w_knight, w_bishop, w_queen, w_king, w_bishop2, w_knight2, w_rock2],
]

pices = [b_rock2, b_knight, b_bishop, b_queen, b_king, b_bishop2, b_knight2, b_rock,
         b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8,
         w_knight2, w_bishop,
         w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8,
         w_rock, w_knight, w_queen, w_king, w_bishop2, w_rock2]


def ya_eblan():
    for i in pices:
        positions[i.piece_coord[1]][i.piece_coord[0]] = i
    for i in positions:
        for j in i:
            if j != '-' and j.is_alive:
                piece = pygame.image.load(j.path)
                screen.blit(piece, ((j.piece_coord[0] - 1) * 100 + 30, (j.piece_coord[1] - 1) * 100 + 30))


def game_over():
    if (0, 0) == w_king.piece_coord or b_king.piece_coord == (0, 0):
        print(1)


chei_hod = 'white'
flag = 0
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
            if acttiveWindoow == 'Menu':
                MainMenu(width, height)
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    q, w = pygame.mouse.get_pos()
                    x, y = Board(width, height).get_coord(event.pos)
                    x1, y1 = Board(width, height).get_coord(event.pos)
                    x += 1
                    y += 1
                    if positions[y][x] != '-' and positions[y][x].color1 == chei_hod:
                        flag = 1
                        positions[y][x].can_move()

                if event.type == pygame.MOUSEBUTTONUP:
                    game_over()
                    q, w = pygame.mouse.get_pos()
                    x1, y1 = Board(width, height).get_coord(event.pos)
                    x1 += 1
                    y1 += 1
                    if positions[y][x] != '-' and positions[y][x].color1 == chei_hod:
                        if y1 == y and x1 == x:
                            pass
                        else:
                            positions[y][x].move(x1, y1)
                            if chei_hod == 'white':
                                chei_hod = 'black'
                            else:
                                chei_hod = 'white'
                            pos = []
                        flag = 0
                    Board(1080, 1080).makeaboard()

                if flag == 1:
                    try:
                        Board(1080, 1080).makeaboard()
                        positions[y][x].can_move()
                        piece = pygame.image.load(positions[y][x].path)
                        screen.blit(piece, (event.pos[0] - 50, event.pos[1] - 50))
                    except:
                        pass

            ya_eblan()
        pygame.display.update()
    pygame.quit()
