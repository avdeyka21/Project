import pygame
from easy_dev.sceneManager import SceneManager
from game_scenes.gameplay_scene import Game
from game_scenes.ship_configurating import ShipConfiger
from game_scenes.player_switcher import Switcher
from game_scenes.battle_settings import Battle_settings

if __name__ == '__main__':
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Морской бой')
    scene_manager = SceneManager(screen, {
        'game': Game,
        'config': ShipConfiger,
        'switcher': Switcher,
        'bset': Battle_settings
    })  # в менеджер сцен при инициализации передаются сцены и их имена в виду словаря
    scene_manager.public_dict['c1'] = '#f3684f'
    scene_manager.public_dict['c2'] = '#6d94f3'
    scene_manager.open_scene('bset')
    scene_manager.switch_scene('bset')
    while True:
        scene_manager.tick()
