
import pygame
from pipe import pipe


class game:

    # TODO : maybe make this dynamics later on

    # screen res
    window_width = 600
    window_height = 499

    # var constant keywords
    score_prefix = "score_"
    BIRD = "brd"
    SEA_LEVEL = "sea_level"
    BACKGROUND = "bg"
    UP_PIPE = "up_pipe"
    DOWN_PIPE = "down_pipe"
    X = "x"
    Y = "y"

    # assets stuff
    window = pygame.display.set_mode((window_width, window_height))
    elevation = window_height * 0.8
    fps = 32
    pipe_image_path = "./assets/pipe.png"
    bg_image_path = "./assets/background.jpg"
    bird_image_path = "./assets/bird.png"
    sea_image_path = "./assets/base.jfif"
    flip = 180
    game_images = {}
    fps_clock: pygame.time.Clock

    # builders
    pipe_builder = pipe

    def add_image(self, name: str, path: str):
        self.game_images[name] = pygame.image.load(path).convert_alpha()

    def _load_pipe_image(self):
        pipe_image = pygame.image.load(self.pipe_image_path).convert_alpha()
        flip_pipe_image = pygame.transform.rotate(pipe_image, self.flip)
        self.game_images[self.UP_PIPE] = flip_pipe_image
        self.game_images[self.DOWN_PIPE] = pipe_image

    def init(self, title: str):
        pygame.init()

        self.fps_clock = pygame.time.Clock()

        pygame.display.set_caption(title)

        self.pipe_builder = pipe(self.window_height, self.window_width)

        for i in range(0, 10):
            path = f"./assets/{i}.png"
            name = f"{self.score_prefix}{i}"

            # load assets image
            self.add_image(name, path)
            self.add_image(self.BIRD, self.bird_image_path)
            self.add_image(self.SEA_LEVEL, self.sea_image_path)
            self.add_image(self.BACKGROUND, self.bg_image_path)
            self._load_pipe_image()

        print("welcome")
        print("press space or enter to start")
