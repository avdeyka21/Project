import pygame.mouse

from easy_dev.scene import Scene
from easy_dev.tools import PyGameTools
from game_scenes.board_class import Board


class Game(Scene):
    def __init__(self):
        self.font40 = PyGameTools.FontMod(self, 40)
        self.evs = PyGameTools.Events(self)

    def just_opened(self):
        self.board1 = Board(self, self.scene_manager.public_dict.get('board1'), self.scene_manager.public_dict['c1'])
        self.board1.set_rect((50, 140, 320, 320))
        self.board2 = Board(self, self.scene_manager.public_dict.get('board2'), self.scene_manager.public_dict['c2'])
        self.board2.set_rect((430, 140, 320, 320))
        self.player = self.scene_manager.public_dict['player']

    def update(self):
        self.scene_manager.surface.fill('#e9c16a')
        self.board1.render(True)
        self.board2.render(False)
        if self.player == 1:
            self.font40.print_on_scene('Игрок 1 делает ход',
                                       'white', self.board1.rect.topleft, 'left', 'bottom')
        elif self.player == 2:
            self.font40.print_on_scene('Игрок 2 делает ход',
                                       'white', self.board2.rect.topleft, 'left', 'bottom')
        if not (self.board1 and self.board2):
            self.font40.print_on_scene('Поля не обнаружены', 'red', (5, 5))
        if self.evs.mouse_button_down(pygame.BUTTON_LEFT):
            mcords = pygame.mouse.get_pos()
