from constant import constants
import pygame
from pipe import pipe


class game:

    # assets stuff
    window = pygame.display.set_mode(
        (constants.window_width, constants.window_height))
    elevation = constants.window_height * 0.8
    game_images = {}
    fps_clock: pygame.time.Clock

    # builders
    pipe_builder = pipe

    def add_image(self, name: str, path: str):
        self.game_images[name] = pygame.image.load(path).convert_alpha()

    def _load_pipe_image(self):
        pipe_image = pygame.image.load(
            constants.pipe_image_path).convert_alpha()
        flip_pipe_image = pygame.transform.rotate(pipe_image, constants.flip)
        self.game_images[constants.UP_PIPE] = flip_pipe_image
        self.game_images[constants.DOWN_PIPE] = pipe_image

    def init(self, title: str):
        pygame.init()

        self.fps_clock = pygame.time.Clock()

        pygame.display.set_caption(title)

        self.pipe_builder = pipe(
            constants.window_height, constants.window_width)

        for i in range(0, 10):
            path = f"./assets/{i}.png"
            name = f"{constants.score_prefix}{i}"

            # load assets image
            self.add_image(name, path)
            self.add_image(constants.BIRD, constants.bird_image_path)
            self.add_image(constants.SEA_LEVEL, constants.sea_image_path)
            self.add_image(constants.BACKGROUND, constants.bg_image_path)
            self._load_pipe_image()

        print("welcome")
        print("press space or enter to start")

        # TODO : create game state ticks
