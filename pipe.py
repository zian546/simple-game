from globals import game_images, window_height
import pygame
import random


class pipe:
    def create():
        offset = window_height / 3
        pipe_height = game_images["pipeimage"][0].get_height()
        sea_level = game_images["sea"]
        rand_start = window_height
        random_height = random.randrange()
