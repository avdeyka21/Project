import pygame
from easy_dev.sceneManager import SceneManager
from game_scenes.test_scene1 import Menu
from game_scenes.test_scene2 import Game

if __name__ == '__main__':
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    scene_manager = SceneManager(screen, {
        'menu': Menu,
        'game': Game
    })
    scene_manager.reload_scene('game')
    scene_manager.reload_scene('menu')
    scene_manager.switch_scene('menu')
    while True:
        scene_manager.tick()
