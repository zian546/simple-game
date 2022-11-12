import sys
import pygame

# screen res
window_width = 600
window_height = 499

window = pygame.display.set_mode((window_width, window_height))
elevation = window_height * 0.8
game_images = {}
fps = 32
pipe_image_path = "./assets/pipe.png"
bg_image_path = "./assets/background.jpg"
bird_image_path = "./assets/bird.png"
sea_image_path = "./assets/base.jfif"
