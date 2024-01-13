import pygame
from easy_dev.scene import Scene
from easy_dev.tools import PyGameTools


class Temp1(Scene):  # обязательно указать класс Scene как родительский класс, чтобы всё работало
    def __init__(self):
        self.font = PyGameTools.FontMod(self, 50)  # такой же pygame.font.Font, но с новым методом print_on_surface
        self.next_scene_button = PyGameTools.Button(self, (20, 400, 760, 180))  # класс кнопка
        # кнопка создаёт невидимую область, которая реагирует на нажатие левой кнопкой мыши

    def update(self):  # в update вписывать код сцены. Update вызывается когда у менеджера сцен вызван метод tick()
        self.scene_manager.surface.fill((60, 200, 20))  # потому считай, что update находится в цикле while true
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
