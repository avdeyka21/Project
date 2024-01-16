import pygame
from easy_dev.sceneManager import SceneManager
from game_scenes.gameplay_scene import Game
from game_scenes.ship_configurating import ShipConfiger
import copy

if __name__ == '__main__':
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    scene_manager = SceneManager(screen, {
        'game': Game,
        'config': ShipConfiger
    })  # в менеджер сцен при инициализации передаются сцены и их имена в виду словаря
    scene_manager.public_dict['board1'] = [[0 for _ in range(10)] for _ in range(10)]
    scene_manager.public_dict['board2'] = copy.deepcopy(scene_manager.public_dict['board1'])
    scene_manager.public_dict['p_conf'] = 1
    scene_manager.public_dict['player'] = 1
    scene_manager.public_dict['c1'] = '#f3684f'
    scene_manager.public_dict['c2'] = '#6d94f3'
    scene_manager.open_scene('config')  # перед выбором сцены (switch) нужно эту сцену открыть (open), иначе ошибка
    scene_manager.switch_scene('config')
    while True:
        scene_manager.tick()
