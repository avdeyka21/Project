import pygame
from easy_dev.tools import PyGameTools
from easy_dev.scene import Scene
from game_scenes.board_class import Board


class ShipConfiger(Scene):
    def just_opened(self):
        if self.scene_manager.public_dict['p_conf'] == 1:
            self.board = Board(self, self.scene_manager.public_dict['board1'], self.scene_manager.public_dict['c1'])
        else:
            self.board = Board(self, self.scene_manager.public_dict['board2'], self.scene_manager.public_dict['c2'])
        self.board.set_rect((200, 100, 400, 400))
        self.evs = PyGameTools.Events(self)
        self.lbutton = 0
        self.rbutton = 0
        self.but_next = PyGameTools.VisibleButton(self, (610, 510, 180, 80), '#b84f0b', 'Далее')
        self.but_next.set_locked(True)
        self.font = PyGameTools.FontMod(self, 40)

    def update(self):
        ready = self.board.check_ready()
        self.scene_manager.surface.fill('#d3c199')
        self.board.render(True)
        self.but_next.render()
        self.font.print_on_scene(f'Игрок {self.scene_manager.public_dict["p_conf"]}, разместите корабли', 'white',
                                 (400, 5), 'center')
        self.font.print_on_scene('Корабли:', 'white', (100, 100), 'center')
        scount = self.scene_manager.public_dict.get('ships_count')
        sconf = self.scene_manager.public_dict.get('ships_conf')
        if self.but_next.is_clicked():
            if self.scene_manager.public_dict['p_conf'] == 1:
                self.scene_manager.public_dict['p_conf'] = 2
                self.scene_manager.reload_scene('config')
            else:
                self.scene_manager.reload_scene('game')
                self.scene_manager.switch_scene('game')
        if self.evs.mouse_button_down(pygame.BUTTON_LEFT):
            self.lbutton = 1
        if self.evs.mouse_button_up(pygame.BUTTON_LEFT):
            self.lbutton = 0
            print(scount, sconf, scount == sconf, ready)
            if ready and sconf == scount:
                self.but_next.set_locked(False)
            else:
                self.but_next.set_locked(True)
        if self.evs.mouse_button_down(pygame.BUTTON_RIGHT):
            self.rbutton = 1
        if self.evs.mouse_button_up(pygame.BUTTON_RIGHT):
            self.rbutton = 0
            if ready and sconf == scount:
                self.but_next.set_locked(False)
            else:
                self.but_next.set_locked(True)  # for debug set False
        if self.lbutton:
            cords = self.board.global_to_local_cords(pygame.mouse.get_pos())
            if cords:
                self.board.draw(cords)
        elif self.rbutton:
            cords = self.board.global_to_local_cords(pygame.mouse.get_pos())
            if cords:
                self.board.erase(cords)
        for i in range(5):
            self.font.print_on_scene(f'{i + 1}П: {0 if not scount else scount[i]}/{sconf[i]}', 'white',
                                     (100, 150 + i * 50), 'center')
