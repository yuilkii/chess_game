import pygame
import sqlite3

pygame.init()
FPS = 50
size = WIDTH, HEIGHT = 1600, 1080


# board = Board(size[0], size[1])


def draw_screen(display):
    display.fill('black')
    # Board.draw(display)
    pygame.display.update()


def terminate():
    pygame.quit()
    sys.exit()


class Game:
    def __init__(self):
        window_title = "Chess"
        self.menu_showed = False
        pygame.display.init()
        self.clock = pygame.time.Clock()


class Square:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.modulx = x * width
        self.moduly = y * height
        self.modul = (self.modulx, self.moduly)
        self.pos = (x, y)

        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )

    def get_coord(self):
        positions = 'abcdefgh'


class Board:
    def __init__(self):
        width = 1000
        height = 1000
        self.square_width = width // 8
        self.square_height = height // 8


class Piece(pygame.sprite.Sprite):
    def __init__(self, filename, cols, rows):
        pygame.sprite.Sprite.__init__(self)
        self.pieces = {
            "white_pawn": 5,
            "white_knight": 3,
            "white_bishop": 2,
            "white_rook": 4,
            "white_king": 0,
            "white_queen": 1,
            "black_pawn": 11,
            "black_knight": 9,
            "black_bishop": 8,
            "black_rook": 10,
            "black_king": 6,
            "black_queen": 7
        }
        self.spritesheet = pygame.image.load(filename).convert_alpha()

        self.cols = cols
        self.rows = rows
        self.cell = cols * rows

        self.rect = self.spritesheet.get_rect()
        w = self.cell_width = self.rect.width // self.cols
        h = self.cell_height = self.rect.height // self.rows

        self.cells = list([(i % cols * w, i // cols * h, w, h) for i in range(self.cell)])


class Knight(pygame.sprite.Sprite):
    def __init__(self, row, col, color, *groups: AbstractGroup):
        super().__init__(*groups)
        self.row = row
        self.col = col
        self.color = color

    def can_move(self):
        row1, col1 = self.get_coord()
        if 0 <= row1 < 8 and col1 >= 0 and col1 < 8:
            if self.row + 1 == row1 and self.col + 2 == col1:
                pass
            elif self.row + 2 == row1 and self.col + 1 == col1:
                pass
            elif self.row + 2 == row1 and self.col - 1 == col1:
                pass
            elif self.row + 1 == row1 and self.col - 2 == col1:
                pass
            elif self.row - 1 == row1 and self.col - 2 == col1:
                pass
            elif self.row - 2 == row1 and self.col - 1 == col1:
                pass
            elif self.row - 2 == row1 and self.col + 1 == col1:
                pass
            elif self.row - 1 == row1 and self.col + 2 == col1:
                pass

    def get_coord(self, coord):
        x, y = coord
        if (
                self.left > x or x > self.left + self.width * self.cell_size) or y < self.top or y > self.top + self.height * self.cell_size:
            return
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        return x, y


class Bishop(pygame.sprite.Sprite):
    def __init__(self, row, col, color, *groups: AbstractGroup):
        super().__init__(*groups)
        self.row = row
        self.col = col
        self.color = color

    def can_move(self):
        row1, col1 = self.get_coord(coord)
        if 0 <= row1 < 8 and 0 <= col1 < 8:
            for i in range(1, 9):
                for j in range(1, 9):
                    if self.row + i == row1 and self.col + i == col1:
                        pass
                    elif self.row + i == row1 and self.col - i == col1:
                        pass
                    elif self.row - i == row1 and self.col + i == col1:
                        pass
                    elif self.row - i == row1 and self.col - i == col1:
                        pass
        pass

    def get_coord(self, coord):
        x, y = row, col
        coord = x, y
        if x < self.left or x > self.left + self.width * self.cell_size or y < self.top or y > self.top + self.height * self.cell_size:
            return
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        return x, y


class Queen(pygame.sprite.Sprite):
    def __init__(self, row, col, color, *groups: AbstractGroup):
        super().__init__(*groups)
        self.row = row
        self.col = col
        self.color = color

    def can_move(self, row1, col1):
        if 0 <= row1 < 8 and 0 <= col1 < 8:
            for i in range(1, 9):
                for j in range(1, 9):
                    if self.row + i == row1 and self.col + i == col1:
                        pass
                    elif self.row + i == row1 and self.col - i == col1:
                        pass
                    elif self.row - i == row1 and self.col + i == col1:
                        pass
                    elif self.row - i == row1 and self.col - i == col1:
                        pass
            if self.row == row1 or self.col == col1:
                pass
        pass

    def get_coord(self, coord):
        x, y = coord
        if x < self.left or x > self.left + self.width * self.cell_size or y < self.top or y > self.top + self.height * self.cell_size:
            return
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        return x, y


clock = pygame.time.Clock()
running = True
if __name__ == '__main__':
    while running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.init()
        size = 1600, 1000
        screen = pygame.display.set_mode(size)
        pygame.display.update()
        all_sprites.update()
        all_sprites.draw(screen)
