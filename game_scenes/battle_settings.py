from easy_dev.scene import Scene
from easy_dev.tools import PyGameTools


class Battle_settings(Scene):
    def __init__(self):
        self.font60 = PyGameTools.FontMod(self, 60)
        self.font50 = PyGameTools.FontMod(self, 50)
        self.size = 10

    def just_opened(self):
        self.boardsizechanger = PyGameTools.PlusMinus(self, (550, 80, 160, 40), '#66ff99')
        self.diagcbox = PyGameTools.Checkbox(self, (550, 130, 160, 40), '#ff5050', '#ccff66')
        self.butnext = PyGameTools.VisibleButton(self, (300, 500, 200, 80), '#b84f0b', 'Далее')
        self.ships = [[4 - i, PyGameTools.PlusMinus(self, (550, 220 + i * 50, 160, 40), '#66ff99')] for i in range(5)]

    def update(self):
        self.scene_manager.surface.fill('#d3c199')

        self.boardsizechanger.render()
        self.diagcbox.render()
        self.butnext.render()
        self.size = min([max([self.size + self.boardsizechanger.get_res(), 8]), 16])
        self.font60.print_on_scene('Настройка боя', 'white', (5, 5))
        self.font50.print_on_scene(f'Размер поля: {self.size}', 'white', (500, 100), 'right', 'center')
        self.font50.print_on_scene('Размещение по диагонали', 'white', (500, 150), 'right', 'center')
        for i in range(5):
            self.ships[i][1].render()
            self.ships[i][0] = min([max([self.ships[i][0] + self.ships[i][1].get_res(), 0]), 5])
            self.font50.print_on_scene(f'{i + 1}-палубные корабли: {self.ships[i][0]}', 'white', (500, 245 + i * 50),
                                       'right', 'center')
        self.butnext.set_locked(not any([i[0] for i in self.ships]))
