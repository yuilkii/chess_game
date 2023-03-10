import pygame
import sqlite3

from pygame.event import Event

pos = []
acttiveWindoow = 'Menu'
import sqlite3

"""создаём таблицу в sqlite3"""

conn = sqlite3.connect('server.db')
sql = conn.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    rating INT
)""")

conn.commit()
player1 = ''
player2 = ''

import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)


# class InputBox:
#
#     def __init__(self, text=''):
#         self.rect = pg.Rect(200, 200, 600, 300)
#         self.color = (255, 255, 255)
#         self.text = text
#         self.txt_surface = FONT.render(text, True, self.color)
#         self.active = False

# def handle_event(self, event):
#     if event.type == pg.MOUSEBUTTONDOWN:
#         # If the user clicked on the input_box rect.
#         if self.rect.collidepoint(event.pos):
#             # Toggle the active variable.
#             self.active = not self.active
#         else:
#             self.active = False
#         # Change the current color of the input box.
#         self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
#     if event.type == pg.KEYDOWN:
#         if self.active:
#             print()
#             if event.key == pg.K_RETURN:
#                 print(self.text)
#                 player1.append(self.text)
#                 print(player1)
#                 self.text = ''
#             elif event.key == pg.K_BACKSPACE:
#                 self.text = self.text[:-1]
#             else:
#                 self.text += event.unicode
#             # Re-render the text.
#             self.txt_surface = FONT.render(self.text, True, self.color)
#
# def update(self):
#     # Resize the box if the text is too long.
#     width = max(200, self.txt_surface.get_width() + 10)
#     self.rect.w = width

def draw(screen, reg_or_log):
    # Blit the text.
    if reg_or_log == 'reg':
        print(23423423)

        pg.draw.rect(screen, (255, 255, 255), (200, 200, 600, 300), 2)
        back = pygame.image.load('data/back1.png')
        bc = back.get_rect(center=(600, 600))
        reg = pygame.image.load('data/profile.png')
        rg = back.get_rect(center=(80, 50))

        screen.blit(reg, rg)
        screen.blit(back, bc)
        intro_text = ["come up with an account name and password"]
        fon = pygame.transform.scale(load_image('data/profile.png'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 40)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 100
            intro_rect.top = text_coord
            intro_rect.x = 150
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        inpit_rect_1 = pygame.Rect(100, 250, 200, 50)
        pygame.draw.rect(screen, (0, 0, 0), inpit_rect_1, 2)

    else:
        pg.draw.rect(screen, (255), (200, 200, 600, 300), 2)
        back = pygame.image.load('data/back1.png')
        bc = back.get_rect(center=(600, 600))
        reg = pygame.image.load('data/profile.png')
        rg = back.get_rect(center=(80, 50))
        screen.blit(reg, rg)
        screen.blit(back, bc)
        intro_text = ["log in your account"]
        fon = pygame.transform.scale(load_image('data/profile.png'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 40)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 100
            intro_rect.top = text_coord
            intro_rect.x = 150
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        inpit_rect_1 = pygame.Rect(100, 250, 200, 50)
        pygame.draw.rect(screen, (0, 0, 0), inpit_rect_1, 2)


# def main(reg_or_log):
# clock = pg.time.Clock()
# input_box1 = InputBox(100, 100, 140, 32)
# input_box2 = InputBox(100, 300, 140, 32)
# input_boxes = [input_box1, input_box2]
# done = False
#
# while not done:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             done = True
#         for box in input_boxes:
#             box.handle_event(event)
#
#     for box in input_boxes:
#         box.update()
#
#     screen.fill((30, 30, 30))
#     for box in input_boxes:
#         box.draw(screen, reg_or_log)
#
#     pg.display.flip()
#     clock.tick(30)


class MainMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def makeamenu(self):
        asf = pygame.image.load('data/start_game.png')
        prof = pygame.image.load('data/prof1.png')
        reg = pygame.image.load('data/reg.png')
        rg = prof.get_rect(center=(500, 100))
        asd = prof.get_rect(center=(675, 88))
        pr = prof.get_rect(center=(180, 90))
        af = asf.get_rect(center=(width // 2, height // 2))

        screen.blit(asf, af)
        screen.blit(prof, pr)

        screen.blit(reg, rg)
        screen.blit(prof, asd)


class Prof:
    global player1, player2

    def reg(self):
        bd = sql.execute(f"SELECT login FROM users").fetchall()

        if player1[0] not in bd and player1[0] != '' and player1[1] != '':
            return 1
        return 0

    def log_1(self):
        bd = sql.execute(f"SELECT login FROM users").fetchall()

        pl1_pasw = sql.execute(f"SELECT password FROM users WHERE login = '{player1[0]}'")
        if player1[0] in bd:
            if pl1_pasw == player1[1]:
                return 1
            return 0
        else:
            return 0

    def log_2(self):
        bd = sql.execute(f"SELECT login FROM users").fetchall()

        pl2_pasw = sql.execute(f"SELECT password FROM users WHERE login = '{player2[0]}'")
        if player2[0] in bd:
            if pl2_pasw == player2[1]:
                return 1
            return 0
        else:
            return 0


class End:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def makeaend(self):
        if game_over() == 2:
            intro_text = ["white win"]
        if game_over() == 1:
            intro_text = ["black win"]
        fon = pygame.transform.scale(load_image('data/endgame.png'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 40)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 350
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)


def load_image(im):
    return pygame.image.load(im)


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
            if x1 == self.piece_coord[0] + 2 or x1 == self.piece_coord[0] - 2:
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


def pos_and():
    for i in pices:
        positions[i.piece_coord[1]][i.piece_coord[0]] = i
    for i in positions:
        for j in i:
            if j != '-' and j.is_alive:
                piece = pygame.image.load(j.path)
                screen.blit(piece, ((j.piece_coord[0] - 1) * 100 + 30, (j.piece_coord[1] - 1) * 100 + 30))


def game_over():
    bd = sql.execute(f"SELECT login FROM users").fetchall()
    if len(player1) != 0:
        if player1.split()[0] in bd:
            rat1 = sql.execute(f"SELECT rating FROM users WHERE login = '{player1[0]}'")
    if len(player2) != 0:
        if player2.split()[0] in bd:
            rat2 = sql.execute(f"SELECT  rating FROM users WHERE login = '{player2[0]}'")
    if (0, 0) == w_king.piece_coord:
        if Prof.log_1 == 1:
            sql.execute(
                f"UPDATE users SET rating = {rat1 + 30} WHERE login = '{player1}'")
        if Prof.log_2 == 1:
            sql.execute(
                f"UPDATE users SET rating = {rat2 - 30} WHERE login = '{player2}'")
        conn.commit()
        return 1
    elif b_king.piece_coord == (0, 0):
        if Prof.log_2 == 1:
            sql.execute(
                f"UPDATE users SET rating = {rat2 + 30} WHERE login = '{player2}'")
        if Prof.log_1 == 1:
            sql.execute(
                f"UPDATE users SET rating = {rat1 - 30} WHERE login = '{player1}'")
            conn.commit()
        return 2
    return 0


chei_hod = 'white'
flag = 0
a = 0
b = 0
c = 0
pl = 0


def get_coord(self, coord):
    x, y = coord
    if (self.left <= x <= self.left + self.width * self.cell_size and
            self.top <= y <= self.top + self.height * self.cell_size):
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        return x, y


global base_font
if __name__ == '__main__':
    pygame.init()
    size = width, height = 860, 860
    screen = pygame.display.set_mode(size)
    running = True
    # Board(1080, 1080).makeaboard()
    x, y = 0, 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_over() == 1 or game_over() == 2 and acttiveWindoow == '' and c == 0:
                c = 1
                acttiveWindoow = 'endgame'
                End(width, height).makeaend()
            if acttiveWindoow == 'prof':
                base_font = pygame.font.Font(None, 32)

                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     o, p = event.pos
                #     print(o, p)
                #     if 530 < o < 670 and 580 < p < 620:
                #         acttiveWindoow = 'Menu'
                if pl == 1:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            player1 = player1[:-1]
                        if event.key == pygame.K_SPACE:
                            player1 += ' '
                        else:
                            player1 += event.unicode

                        text_surface = base_font.render(player1[0], True, (255, 255, 255))
                        screen.blit(text_surface, (100, 260), )
                if pl == 2:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            player2 = player2[0][:-1]
                        if event.key == pygame.K_SPACE:
                            player2 += ' '
                        else:
                            player2 += event.unicode

                    text_surface = base_font.render(player2, True, (255, 255, 255))
                    screen.blit(text_surface, (100, 260), )

            elif acttiveWindoow == 'endgame':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    f, k = event.pos
                    if 200 < f < 660 and 360 < k < 500:
                        acttiveWindoow = 'Menu'
                        c = 0
                        a = 1
            elif acttiveWindoow == 'Menu':  # меню
                MainMenu(width, height).makeamenu()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    j, l = event.pos

                    if 260 < j < 600 and 380 < l < 480:
                        acttiveWindoow = ''
                        # asf = pygame.transform.scale(asf, (0, 0))
                        if a == 0:
                            Board(1080, 1080).makeaboard()
                            pos_and()
                            acttiveWindoow = ''
                        else:
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
                            a = 0
                            chei_hod = 'white'
                            Board(1080, 1080).makeaboard()
                            pos_and()

                            acttiveWindoow = ''

                    elif 50 < j < 350 and 50 < l < 130:
                        pl = 1

                        acttiveWindoow = 'prof'
                        draw(screen, "prof")
                    elif 540 < j < 810 and 50 < l < 120:
                        pl = 2

                        acttiveWindoow = 'prof'
                        draw(screen, "prof")
                    elif 360 < j < 510 and 65 < l < 100:
                        draw(screen, "reg")
                        acttiveWindoow = 'prof'
                        print(2)

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
            if a != 1 and acttiveWindoow != 'Menu' and acttiveWindoow != 'endgame' and acttiveWindoow != 'prof':
                pos_and()

        pygame.display.update()

    pygame.quit()
