import sys
import pygame

# screen res
window_width = 600
window_height = 499

# assets stuff
window = pygame.display.set_mode((window_width, window_height))
elevation = window_height * 0.8
game_images = {}
fps = 32
pipe_image_path = "./assets/pipe.png"
bg_image_path = "./assets/background.jpg"
bird_image_path = "./assets/bird.png"
sea_image_path = "./assets/base.jfif"
flip = 180


if __name__ == "__main__":
    pygame.init()
    fps_clock = pygame.time.Clock()

    pygame.display.set_caption("pak anta")

    game_images["scoreimages"] = (
        pygame.image.load("./assets/0.png").convert_alpha(),
        pygame.image.load("./assets/1.png").convert_alpha(),
        pygame.image.load("./assets/2.png").convert_alpha(),
        pygame.image.load("./assets/3.png").convert_alpha(),
        pygame.image.load("./assets/4.png").convert_alpha(),
        pygame.image.load("./assets/5.png").convert_alpha(),
        pygame.image.load("./assets/6.png").convert_alpha(),
        pygame.image.load("./assets/7.png").convert_alpha(),
        pygame.image.load("./assets/8.png").convert_alpha(),
        pygame.image.load("./assets/9.png").convert_alpha(),
    )

    game_images["bird"] = pygame.image.load(bird_image_path).convert_alpha()
    game_images["sea_level"] = pygame.image.load(
        sea_image_path).convert_alpha()
    game_images["bg"] = pygame.image.load(bg_image_path).convert_alpha()

    pipe_image = pygame.image.load(pipe_image_path).convert_alpha()
    flip_pipe_image = pygame.transform.rotate(pipe_image, flip)

    game_images["pipe"] = (flip_pipe_image, pipe_image)

    print("welcome")
    print("press space or enter to start")
