import pygame
from easy_dev.sceneManager import SceneManager
from game_scenes.scene_template1 import Temp1
from game_scenes.scene_template2 import Temp2

if __name__ == '__main__':
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    scene_manager = SceneManager(screen, {
        'temp1': Temp1,
        'temp2': Temp2
    })
    scene_manager.open_scene('temp1')
    scene_manager.open_scene('temp2')
    scene_manager.switch_scene('temp1')
    while True:
        scene_manager.tick()
