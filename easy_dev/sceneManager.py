import pygame


class SceneManager:
    def __init__(self, surface: pygame.surface.Surface, all_scenes: dict):
        self.public_dict = dict()
        self.surface = surface
        self.__scene_classes = all_scenes
        self.__opened_scenes = dict()
        self.current_scene = None
        self.clock = pygame.time.Clock()
        self.fps_limit = 60
        self.events = []
        self.current_fps = self.fps_limit

    def reopen_scene(self, scene_name: str, **kwargs_for_scene):
        self.__opened_scenes[scene_name] = self.__scene_classes[scene_name](**kwargs_for_scene)
        self.__opened_scenes[scene_name].scene_manager = self
        self.__opened_scenes[scene_name].just_opened()

    def switch_scene(self, scene_name: str):
        self.current_scene = scene_name
        self.__opened_scenes[scene_name].just_switched()

    def close_scene(self, scene_name: str):
        if scene_name in self.__opened_scenes:
            del self.__opened_scenes[scene_name]

    def tick(self):
        self.events = pygame.event.get()
        for e in self.events:
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
        self.clock.tick(60)
        self.current_fps = self.clock.get_fps()
        self.surface.fill((0, 0, 0))
        if self.current_fps != 0:
            self.__opened_scenes[self.current_scene].update()
        pygame.display.flip()

    def scene_is_started(self, scene_name: str):
        return scene_name in self.__opened_scenes
