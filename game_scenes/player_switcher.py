from easy_dev.scene import Scene
from easy_dev.tools import PyGameTools


class Switcher(Scene):
    def just_opened(self):
        self.scene_manager.public_dict['player'] = 1 if self.scene_manager.public_dict['player'] == 2 else 2
        self.font40 = PyGameTools.FontMod(self, 40)
        self.button = PyGameTools.VisibleButton(self, (250, 400, 300, 180), self.scene_manager.public_dict[
            'c1' if self.scene_manager.public_dict['player'] == 1 else 'c2'],
                                                'Приступить\n'
                                                f'(для игрока {self.scene_manager.public_dict["player"]})')

    def update(self):
        self.scene_manager.surface.fill('#e9c16a')
        self.font40.print_on_scene(
            f'Игрок {1 if self.scene_manager.public_dict["player"] == 2 else 2} промазал.\nАтакуйте.', 'white',
            (400, 200), 'center', 'center')
        self.button.render()
        if self.button.is_clicked():
            self.scene_manager.public_dict['nextp'] = False
            self.scene_manager.public_dict['replace'] = True
            self.scene_manager.switch_scene('game')
