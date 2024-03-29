import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        self.type = 0
        self.image = BIRD
        super().__init__(self.image, self.type)
        self.Y_POS = 250
        random_high = random.random()
        if random_high <= 0.3:
            self.Y_POS = 300
        elif random_high >= 0.8:
            self.Y_POS = 200
        self.rect.y = self.Y_POS
        self.step_index = 0

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed * 1.2
        if self.rect.x < -self.rect.width:
            obstacles.pop()

        if self.step_index >= 8:
            self.step_index = 0

        self.type = 0 if self.step_index < 4 else 1
        self.step_index += 1