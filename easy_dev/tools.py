import pygame
from easy_dev.scene import Scene


class PyGameTools:
    class FontMod(pygame.font.Font):
        def __init__(self, scene: Scene, size=40):
            super().__init__(None, size)
            self.scene = scene

        def print_on_scene(self, text, color, cords, horizontal_align='left', vertical_align='top'):
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
        def __init__(self, scene: Scene):
            self.scene = scene

        def key_down(self, pygame_key):
            for e in self.scene.scene_manager.events:
                if e.type == pygame.KEYDOWN and e.key == pygame_key:
                    return True
            return False

        def mouse_button_down(self, pygame_button):
            for e in self.scene.scene_manager.events:
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == pygame_button:
                    return True
            return False

    class Button:
        def __init__(self, scene: Scene, rect):
            self.scene = scene
            self.events = PyGameTools.Events(self.scene)
            self.rect = rect

        def is_clicked(self):
            if self.events.mouse_button_down(pygame.BUTTON_LEFT):
                if self.is_cursor_on():
                    return True
            return False

        def is_cursor_on(self):
            cords = pygame.mouse.get_pos()
            if self.rect[0] <= cords[0] < (self.rect[0] + self.rect[2]) and self.rect[1] <= cords[1] < (
                    self.rect[1] + self.rect[3]):
                return True
            return False
