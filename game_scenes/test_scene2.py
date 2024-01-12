import pygame
from easy_dev.scene import Scene
from easy_dev.tools import PyGameTools


class Game(Scene):
    def __init__(self):
        self.font = PyGameTools.Text(self, 60)

    def update(self):
        self.scene_manager.surface.fill((0, 0, 255))
        for e in self.scene_manager.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    self.scene_manager.switch_scene('menu')
                if e.key == pygame.K_r:
                    self.scene_manager.reopen_scene('game')
        self.font.print_on_scene('Tools.Text test', (800, 600), 'Red', 'right', 'bottom')

    def just_switched(self):
        pygame.display.set_caption(str(self.scene_manager.public_dict['ct']))
