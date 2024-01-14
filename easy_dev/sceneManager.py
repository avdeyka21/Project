import pygame


class SceneManager:
    def __init__(self, surface: pygame.surface.Surface, all_scenes: dict):
        self.public_dict = dict()  # Публичный словарь для передачи информации между сценами
        self.surface = surface
        self.__scene_classes = all_scenes
        self.__opened_scenes = dict()
        self.current_scene_name = None
        self.clock = pygame.time.Clock()
        self.fps_limit = 60
        self.events = []
        self.current_fps = self.fps_limit

    def reload_scene(self, scene_name: str, **kwargs_for_scene):
        """Перезапускает сцену. Если сцена не была открыта, открывает её"""
        self.__opened_scenes[scene_name] = self.__scene_classes[scene_name](**kwargs_for_scene)
        self.__opened_scenes[scene_name].scene_manager = self
        self.__opened_scenes[scene_name].just_opened()

    def open_scene(self, scene_name: str, **kwargs_for_scene):
        """Открывает сцену"""
        if not self.__opened_scenes:
            self.current_scene_name = scene_name

        if scene_name not in self.__opened_scenes:
            self.reload_scene(scene_name, **kwargs_for_scene)

    def switch_scene(self, scene_name: str):
        """Назначает сцену с именем scene_name текущей сценой"""
        if not scene_name or scene_name not in self.__opened_scenes:
            exit()
        self.current_scene_name = scene_name
        self.__opened_scenes[scene_name].just_switched()

    def close_scene(self, scene_name: str):
        """Закрывает сцену"""
        if scene_name in self.__opened_scenes:
            del self.__opened_scenes[scene_name]

    def tick(self):
        """Обновление текущей сцены"""
        self.events = pygame.event.get()
        for e in self.events:
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
        self.clock.tick(60)
        self.current_fps = self.clock.get_fps()
        self.surface.fill((0, 0, 0))
        if self.current_fps != 0:
            self.__opened_scenes[self.current_scene_name].update()
        pygame.display.flip()

    def scene_is_started(self, scene_name: str):
        return scene_name in self.__opened_scenes
