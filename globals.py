
import pygame

# screen res
window_width = 600
window_height = 499

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
