import pygame
from easy_dev.scene import Scene
from easy_dev.tools import PyGameTools


class Menu(Scene):
    def __init__(self):
        self.counter = 0
        self.font = PyGameTools.FontMod(self, 60)

    def update(self):
        for e in self.scene_manager.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    self.scene_manager.switch_scene('game')
                if e.key == pygame.K_r:
                    self.scene_manager.reload_scene('menu')
        self.counter += self.scene_manager.clock.get_time() / 1000
        self.scene_manager.public_dict['ct'] = self.counter
        self.scene_manager.surface.fill((150, 120, 100))
        self.font.print_on_scene('Морской бой', (20, 20), 'Black', 'Left', 'Top')
        self.font.print_on_scene(self.counter, (20, 100), 'yellow', 'Left', 'Top')
        self.font.print_on_scene('a - следующая сцена, r - сброс сцены', (20, 580), 'green', 'Left', 'Bottom')
