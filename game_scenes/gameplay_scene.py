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
        self.board1.set_rect((50, 100, 320, 320))
        self.board2 = Board(self, self.scene_manager.public_dict.get('board2'), self.scene_manager.public_dict['c2'])
        self.board2.set_rect((430, 100, 320, 320))
        self.boards = [self.board1, self.board2]
        self.butnext = PyGameTools.VisibleButton(self, (250, 510, 300, 70), '#b84f0b', 'Следующий игрок')
        self.butnext.set_locked(True)
        self.scene_manager.public_dict['nextp'] = False

    def just_switched(self):
        if self.scene_manager.public_dict.get('replace'):
            self.butnext.set_locked(True)
            r1, r2 = self.board1.rect, self.board2.rect
            self.board1.set_rect(r2)
            self.board2.set_rect(r1)
            self.scene_manager.public_dict['replace'] = False

    def update(self):
        player = self.scene_manager.public_dict['player'] - 1
        self.scene_manager.surface.fill('#e9c16a')
        self.board1.render(not player or self.scene_manager.public_dict.get('break'))
        self.board2.render(player or self.scene_manager.public_dict.get('break'))
        self.butnext.render()
        if not self.scene_manager.public_dict.get('winner'):
            note1 = 'Моё поле'
            note2 = 'Поле врага'
            if not self.scene_manager.public_dict['nextp']:
                self.font40.print_on_scene(f'Игрок {player + 1} делает ход',
                                           'white', self.boards[player].rect.move(0, -5).topleft, 'left', 'bottom')
                if self.evs.mouse_button_down(pygame.BUTTON_LEFT):
                    mcords = pygame.mouse.get_pos()
                    cords = self.boards[not player].global_to_local_cords(mcords)
                    if cords:
                        result = self.boards[not player].shoot(*cords)
                        if result == 'miss':
                            self.scene_manager.public_dict['nextp'] = True
                            self.butnext.set_locked(False)
                        else:
                            if self.scene_manager.public_dict.get('winner'):
                                self.butnext.set_locked(False)
                                self.butnext.text = 'Завершить игру'
            else:
                self.font40.print_on_scene(f'Каррамба! Вы промазали. Передайте ход {(not player) + 1} игроку',
                                           'white', self.boards[player].rect.move(0, -5).topleft, 'left', 'bottom')
            if self.butnext.is_clicked():
                self.scene_manager.reload_scene('switcher')
                self.scene_manager.switch_scene('switcher')
        else:
            note1 = 'Игрок' + str(player + 1)
            note2 = 'Игрок' + str((not player) + 1)
            self.font40.print_on_scene(f'Игра завершена!\n'
                                       f'Игрок {self.scene_manager.public_dict["winner"]} побеждает.',
                                       'white', (400, 10), 'center')
        self.font40.print_on_scene(note1, 'white', self.boards[player].rect.move(0, 5).midbottom, 'center')
        self.font40.print_on_scene(note2, 'white', self.boards[not player].rect.move(0, 5).midbottom, 'center')

        if not (self.board1 and self.board2):
            self.font40.print_on_scene('Поля не обнаружены', 'red', (5, 5))
