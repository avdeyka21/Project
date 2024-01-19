import copy

import pygame
from easy_dev.scene import Scene


class Board:
    def __init__(self, scene: Scene, board: list, color):
        self.board = board
        self.scene = scene
        self.surface = scene.scene_manager.surface
        self.rows, self.columns = len(self.board), len(self.board[0])
        self.rect = pygame.rect.Rect(0, 0, 0, 0)
        c = pygame.color.Color(color)
        self.color1 = [c.r, c.g, c.b]
        self.color2 = [i * 0.85 for i in self.color1]
        self.color3 = [i * 0.5 for i in self.color1]

    def set_rect(self, rect):
        self.rect = pygame.rect.Rect(rect)
        size = (self.rect.width / self.columns, self.rect.height / self.rows)
        self.ALIVE1 = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.ALIVE2 = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.EDGES = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.DEATH = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.ALIVE1.fill(self.color2)
        self.DEATH.fill(self.color3)
        rect2 = self.ALIVE2.get_rect()
        pygame.draw.polygon(self.ALIVE2, self.color1, [rect2.midtop, rect2.midright, rect2.midbottom, rect2.midleft])
        pygame.draw.rect(self.EDGES, '#b89f37', rect2, 1)

    def render(self, show_ships: bool):
        l, t, w, h = self.rect
        cw = w / self.columns
        ch = h / self.rows
        self.surface.fill('#a2bbc8', self.rect)
        for y in range(self.rows):
            for x in range(self.columns):
                rect = pygame.rect.Rect(l + x * cw, t + y * ch, cw, ch)
                cell = self.board[y][x]
                if show_ships and cell == 1:
                    self.surface.blit(self.ALIVE1, rect)
                    self.surface.blit(self.ALIVE2, rect)
                elif cell == 2:
                    pygame.draw.ellipse(self.surface, '#72abb8', rect.scale_by(0.7, 0.7), 5)
                elif cell == 3:
                    self.surface.blit(self.DEATH, rect)
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

    def check_ready(self, mode=0):
        ships = []
        board = copy.deepcopy(self.board)
        for y in range(self.rows):
            for x in range(self.columns):
                if board[y][x] in [1, 3]:
                    maxs = 1
                    old = (x, y)
                    board[y][x] = 0
                    rot = 0
                    if mode == 0 and self.diag(board, x, y):
                        return False
                    while x + 1 < self.columns and board[y][x + 1] in [1, 3]:
                        x += 1
                        board[y][x] = 0
                        maxs += 1
                        if mode == 0 and self.diag(board, x, y):
                            return False
                    if maxs == 1:
                        x, y = old
                        rot = 1
                        while y + 1 < self.rows and board[y + 1][x] in [1, 3]:
                            y += 1
                            board[y][x] = 0
                            maxs += 1
                            if mode == 0 and self.diag(board, x, y):
                                return False
                    if mode:
                        ships.append([old, rot, maxs])
                    else:
                        ships.append(maxs)
                    x, y = old
        self.scene.scene_manager.public_dict['ships_count'] = [ships.count(i + 1) for i in range(5)]
        if mode:
            return ships
        if self.scene.scene_manager.public_dict['ships_conf'] == self.scene.scene_manager.public_dict['ships_count']:
            return True
        return False

    def diag(self, board, x, y):
        if not self.scene.scene_manager.public_dict.get('diag') and y + 1 < self.rows:
            return (x - 1 >= 0 and board[y + 1][x - 1]) or (x + 1 < self.columns and board[y + 1][x + 1])

    def shoot(self, x, y):
        if self.board[y][x] == 0:
            self.board[y][x] = 2
            return 'miss'
        elif self.board[y][x] == 1:
            self.board[y][x] = 3
            if not any([any([j == 1 for j in i]) for i in self.board]):
                self.scene.scene_manager.public_dict['winner'] = self.scene.scene_manager.public_dict['player']
            self.mark_voids(self.check_ready(1))
            return 'hit'
        else:
            return 'error'

    def mark_voids(self, ships):
        diag = not self.scene.scene_manager.public_dict['diag']
        for s in ships:
            ship = []
            x, y = s[0]
            rot, maxs = s[1], s[2]
            for i in range(maxs):
                if rot:
                    ship.append(self.board[y + i][x] == 3)
                else:
                    ship.append(self.board[y][x + i] == 3)
            if all(ship):
                for i in range(maxs):
                    if rot:
                        x2, y2 = x, y + i
                    else:
                        x2, y2 = x + i, y
                    up = y2 - 1 >= 0
                    down = y2 + 1 < self.rows
                    left = x2 - 1 >= 0
                    right = x2 + 1 < self.columns
                    if up and self.board[y2 - 1][x2] == 0:
                        self.board[y2 - 1][x2] = 2
                    if down and self.board[y2 + 1][x2] == 0:
                        self.board[y2 + 1][x2] = 2
                    if left and self.board[y2][x2 - 1] == 0:
                        self.board[y2][x2 - 1] = 2
                    if right and self.board[y2][x2 + 1] == 0:
                        self.board[y2][x2 + 1] = 2
                    if diag and  left and up and self.board[y2 - 1][x2 - 1] == 0:
                        self.board[y2 - 1][x2 - 1] = 2
                    if diag and up and right and self.board[y2 - 1][x2 + 1] == 0:
                        self.board[y2 - 1][x2 + 1] = 2
                    if diag and right and down and self.board[y2 + 1][x2 + 1] == 0:
                        self.board[y2 + 1][x2 + 1] = 2
                    if diag and down and left and self.board[y2 + 1][x2 - 1] == 0:
                        self.board[y2 + 1][x2 - 1] = 2
