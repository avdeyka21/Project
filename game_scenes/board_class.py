import copy

import pygame
from easy_dev.scene import Scene


class Board:
    def __init__(self, scene: Scene, board: list, color):
        self.board = board
        self.surface = scene.scene_manager.surface
        self.rows, self.columns = len(self.board), len(self.board[0])
        self.rect = pygame.rect.Rect(0, 0, 0, 0)
        c = pygame.color.Color(color)
        self.color1 = (c.r, c.g, c.b)

    def set_rect(self, rect):
        self.rect = pygame.rect.Rect(rect)

    def render(self, show_ships: bool):
        l, t, w, h = self.rect
        cw = w / self.columns
        ch = h / self.rows
        self.surface.fill('#a2bbc8', self.rect)
        for y in range(self.rows):
            for x in range(self.columns):
                rect = (l + x * cw, t + y * ch, cw, ch)
                if show_ships and self.board[y][x] == 1:
                    pygame.draw.rect(self.surface, self.color1, rect)
                pygame.draw.rect(self.surface, '#b89f37', rect, 1)

    def draw(self, cords):
        self.set_elem(cords, 1)

    def erase(self, cords):
        self.set_elem(cords, 0)

    def set_elem(self, cords: tuple, value):
        self.board[cords[1]][cords[0]] = value

    def global_to_local_cords(self, mouse_pos: tuple):
        if pygame.mouse.get_focused() and self.rect.collidepoint(*mouse_pos):
            mx, my = mouse_pos
            return (int((mx - self.rect.left) / (self.rect.width / self.columns)),
                    int((my - self.rect.top) / (self.rect.height / self.rows)))

    def check_ready(self):
        ships = []
        board = copy.deepcopy(self.board)
        for y in range(self.rows):
            for x in range(self.columns):
                if board[y][x] == 1:
                    maxs = 1
                    old = (x, y)
                    board[y][x] = 2
                    if self.diag(board, x, y):
                        return False
                    while x + 1 < self.columns and board[y][x + 1] == 1:
                        x += 1
                        board[y][x] = 2
                        maxs += 1
                        if self.diag(board, x, y):
                            return False
                    if maxs == 1:
                        x, y = old
                        while y + 1 < self.rows and board[y + 1][x] == 1:
                            y += 1
                            board[y][x] = 2
                            maxs += 1
                            if self.diag(board, x, y):
                                return False
                    ships.append(maxs)
                    x, y = old
        if ships.count(1) == 4 and ships.count(2) == 3 and ships.count(3) == 2 and ships.count(4) == 1:
            return True
        return False

    def diag(self, board, x, y):
        if y + 1 < self.rows:
            return (x - 1 >= 0 and board[y + 1][x - 1]) or (x + 1 < self.columns and board[y + 1][x + 1])
