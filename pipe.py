import pygame
import random
from globals import game


class pipe:

    def __init__(self, window_height, window_width, game_images):
        self.window_height = window_height
        self.window_width = window_width
        self.game_images = game_images

    def create(self):
        offset_value = self.window_height / 3
        offset_multiplier = 1.2
        offset = offset_multiplier * offset_value

        pipe_height = self.game_images[game.UP_PIPE].get_height()
        sea_level_height = self.game_images[game.SEA_LEVEL].get_height()

        end_range = int(self.window_height - sea_level_height - offset)

        y2 = random.randrange(0, end_range)

        pipe_x_value = 10
        pipe_x_coord = self.window_width + pipe_x_value

        y1 = pipe_height - y2 + offset_value

        pipe = [
            # upper pipe coordinates
            {'x': pipe_x_coord, 'y': -y1},

            # lower pipe coordinates
            {'x': pipe_x_coord, 'y': y2}

        ]

        return pipe
