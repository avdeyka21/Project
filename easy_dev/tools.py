import pygame
from easy_dev.scene import Scene


class PyGameTools:
    class FontMod(pygame.font.Font):
        """Модифицированный pygame.font.Font. Добавлен метод print_on_scene"""

        def __init__(self, scene: Scene, size=40):
            super().__init__(None, size)
            self.scene = scene

        def print_on_scene(self, text, color, cords, horizontal_align='left', vertical_align='top'):
            """Печатает текст на поверхности surface сцены"""
            lines = str(text).split('\n')
            n = len(lines)
            for i in range(n):
                rendered = self.render(lines[i], True, color)
                rect = rendered.get_rect()
                self.scene.scene_manager.surface.blit(rendered, rect.move(
                    -rect.width / 2 if horizontal_align.lower() == 'center' else
                    -rect.width if horizontal_align.lower() == 'right' else
                    0,
                    -rect.height * n / 2 + rect.height * i if vertical_align.lower() == 'center' else
                    -rect.height * n + rect.height * i if vertical_align.lower() == 'bottom' else
                    rect.height * i).move(cords))

    class Events:
        """Инструменты для удобной работы с событиями pygame"""

        def __init__(self, scene: Scene):
            self.scene = scene

        def key_down(self, pygame_key):
            """Возвращает True если клавиша pygame_key была нажата, иначе False"""
            for e in self.scene.scene_manager.events:
                if e.type == pygame.KEYDOWN and e.key == pygame_key:
                    return True
            return False

        def key_up(self, pygame_key):
            """Возвращает True если клавиша pygame_key была нажата, иначе False"""
            for e in self.scene.scene_manager.events:
                if e.type == pygame.KEYUP and e.key == pygame_key:
                    return True
            return False

        def mouse_button_down(self, pygame_button):
            """Возвращает True если кнопка мыши pygame_button была нажата, иначе False"""
            for e in self.scene.scene_manager.events:
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == pygame_button:
                    return True
            return False

        def mouse_button_up(self, pygame_button):
            for e in self.scene.scene_manager.events:
                if e.type == pygame.MOUSEBUTTONUP and e.button == pygame_button:
                    return True
            return False

    class Button:
        """Создаёт в сцене невидимую область, реагирующую на нажатия левой кнопки мыши"""

        def __init__(self, scene: Scene, rect):
            self.scene = scene
            self.events = PyGameTools.Events(self.scene)
            self.rect = pygame.rect.Rect(rect)

        def is_clicked(self):
            """Возвращает True если кнопка была нажата левой кнопкой мыши иначе False"""
            if self.events.mouse_button_down(pygame.BUTTON_LEFT):
                if self.is_cursor_on():
                    return True
            return False

        def is_cursor_on(self):
            """Возвращает True если курсор мыши внутри кнопки, иначе False"""
            if pygame.mouse.get_focused() and self.rect.collidepoint(*pygame.mouse.get_pos()):
                return True
            return False

    class VisibleButton:
        def __init__(self, scene: Scene, rect, color, text=''):
            self.dif = 2
            self.surface = scene.scene_manager.surface
            self.button = PyGameTools.Button(scene, rect)
            self.rect = self.button.rect
            c = pygame.color.Color(color)
            self.def_color = [c.r, c.g, c.b]
            self.locked = 0
            self.colorize(self.def_color)
            self.font = PyGameTools.FontMod(scene, 40)
            self.text = text

        def colorize(self, color):
            self.color1 = color
            self.color2 = [int(i * 0.9) for i in self.color1]
            self.color3 = [int(i * 0.8) for i in self.color1]

        def set_locked(self, lock: bool):
            self.locked = lock
            if lock:
                self.colorize((128, 128, 128))
            else:
                self.colorize(self.def_color)

        def render(self):
            if not self.locked and self.button.is_cursor_on():
                pygame.draw.rect(self.surface, self.color2, self.rect.move(-self.dif, self.dif))
                pygame.draw.rect(self.surface, self.color3, self.rect.move(self.dif, -self.dif))
            else:
                pygame.draw.rect(self.surface, self.color2, self.rect.move(self.dif, -self.dif))
                pygame.draw.rect(self.surface, self.color1, self.rect.move(-self.dif, self.dif))
            if self.text:
                self.font.print_on_scene(self.text, 'black', self.rect.center, 'center', 'center')

        def is_clicked(self):
            return not self.locked and self.button.is_clicked()
