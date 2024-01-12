from easy_dev.sceneManager import SceneManager


class Scene:
    scene_manager: SceneManager

    def update(self):
        pass

    def just_switched(self):
        '''Вызывается при переключении на эту сцену'''
        pass

    def just_opened(self):
        '''Вызывается при открытии сцены'''
        pass
