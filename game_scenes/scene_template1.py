import pygame
from easy_dev.scene import Scene
from easy_dev.tools import PyGameTools


class Temp1(Scene):
    def __init__(self):
        self.font = PyGameTools.FontMod(self, 50)
        self.next_scene_button = PyGameTools.Button(self, (20, 400, 760, 180))

    def update(self):
        self.scene_manager.surface.fill((60, 200, 20))
        self.font.print_on_scene('Шаблон сцен\n'
                                 'Сцена N1\n'
                                 '3 строка', 'Black', (0, 0))
        if self.next_scene_button.is_cursor_on():
            pygame.draw.rect(self.scene_manager.surface, (128, 20, 20), self.next_scene_button.rect)
        else:
            pygame.draw.rect(self.scene_manager.surface, 'red', self.next_scene_button.rect)
        self.font.print_on_scene('Открыть сцену N2', 'black', (400, 490), 'center', 'center')
        if self.next_scene_button.is_clicked():
            self.scene_manager.switch_scene('temp2')
