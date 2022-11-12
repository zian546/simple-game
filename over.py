from globals import game


class over:
    def __init__(self, game_images):
        self.game_images = game_images

    def is_game_over(self, horizontal, vertical, elevation, up_pipes, dowen_pipes):
        pipe_width = self.game_images[game.UP_PIPE].get_width()
        pipe_height = self.game_images[game.UP_PIPE].get_height()
        bird_height = self.game_images[game.BIRD].get_height()

        if vertical > elevation - 25 or vertical < 0:
            return True

        # check if it hits up pipes or down pipes
        is_hit_above_pipes = self._is_hit_above_pipes(
            up_pipes, vertical, horizontal, pipe_width, pipe_height)

        is_hit_down_pipes = self._is_hit_down_pipes(
            dowen_pipes, vertical, horizontal, pipe_width, bird_height)

        if(is_hit_above_pipes or is_hit_down_pipes):
            return True
        else:
            return False

    def _is_hit_above_pipes(self, pipes, vertical, horizontal, pipe_width, pipe_height):

        for pipe in pipes:

            is_y_hit = self._is_y_hit(vertical, pipe, pipe_height)
            is_x_hit = self._is_x_hit(horizontal, pipe, pipe_width)

            if(is_y_hit and is_x_hit):
                return True
            else:
                return False

        return False

    def _is_hit_down_pipes(self, pipes, vertical, horizontal, pipe_width, bird_height):
        player_value = vertical + bird_height

        for pipe in pipes:
            is_bird_hit_pipe = self._is_bird_hit_pipe(
                vertical, pipe, player_value)
            is_x_hit = self._is_x_hit(horizontal, pipe, pipe_width)

            if(is_bird_hit_pipe and is_x_hit):
                return True
            else:
                return False

        return False

    def _is_above_sea_level(self, horizontal, vertical, elevation):
        sea_level_value = 25

        if vertical > elevation - sea_level_value or self._is_below_ground:
            return True

    def _is_bird_hit_pipe(self, vertical, pipe, player_value):
        if(player_value > pipe[game.Y].get_height()):
            return True
        else:
            return False

    def _is_y_hit(self, vertical, pipe, pipe_height):

        if(vertical < pipe_height + pipe[game.Y]):
            return True
        else:
            return False

    def _is_x_hit(self, horizontal, pipe, pipe_width):
        x_value = abs(horizontal - pipe[game.X])

        if(x_value < pipe_width):
            return True
        else:
            return False

    def _is_below_ground(vertical):
        ground = 0

        if vertical < ground:
            return True
