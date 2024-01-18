from easy_dev.scene import Scene
from easy_dev.tools import PyGameTools


class Battle_settings(Scene):
    def __init__(self):
        self.font60 = PyGameTools.FontMod(self, 60)
        self.font50 = PyGameTools.FontMod(self, 50)

    def just_opened(self):
        pass

    def update(self):
        self.scene_manager.surface.fill('#d3c199')
        self.font60.print_on_scene('Настройка боя', 'white', (5, 5))
        self.font50.print_on_scene(f'Размер поля: {5}', 'white', (500, 200), 'right', 'center')
        self.font50.print_on_scene('Размещение по диагонали', 'white', (500, 250), 'right', 'center')
