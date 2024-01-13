import pygame
from easy_dev.scene import Scene


class PyGameTools:
    class FontMod(pygame.font.Font):
        def __init__(self, scene: Scene, size=40):
            super().__init__(None, size)
            self.scene = scene

        def print_on_scene(self, text, cords, color, horizontal_align='left', vertical_align='bottom'):
            rendered = self.render(str(text), True, color)
            rect = rendered.get_rect()
            self.scene.scene_manager.surface.blit(rendered, rect.move(
                -rect.width / 2 if horizontal_align.lower() == 'center' else
                -rect.width if horizontal_align.lower() == 'right' else 0,
                -rect.height / 2 if vertical_align.lower() == 'center' else
                -rect.height if vertical_align.lower() == 'bottom' else 0).move(cords))
