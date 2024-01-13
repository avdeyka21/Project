import pygame

from easy_dev.scene import Scene
from easy_dev.tools import PyGameTools


class Temp2(Scene):
    def __init__(self):
        self.font = PyGameTools.FontMod(self, 50)
        self.evs = PyGameTools.Events(self)  # готовые инструменты реагирования на события pygame - нажатие конкретной
        # клавиши на клавиатуре или кнопки мыши

    def update(self):
        self.font.print_on_scene('Сцена N2\n'
                                 'Чтобы открыть сцену 1, нажмите клавишу B\n'
                                 'или левую кнопку мыши', 'white', (20, 20))
        self.font.print_on_scene('FontMod test\n'
                                 'PyGameTools', 'white', (790, 590), 'right', 'bottom')
        if self.evs.key_down(pygame.K_b) or self.evs.mouse_button_down(pygame.BUTTON_LEFT):
            self.scene_manager.switch_scene('temp1')  # в PyGameTools.events передаём pygame.<клавиша или кнопка мыши>
