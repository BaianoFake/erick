import random
import pygame

from dino_runner.utils.audio import fraco_audio, hammer_audio, time_audio
from dino_runner.utils.constants import TIME_TYPE, HAMMER_TYPE, SHIELD_TYPE
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.time import Time
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            power_up_classes = [Time, Hammer, Shield]
            power_up = random.choice(power_up_classes)()
            self.power_ups.append(power_up)

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
                game.game_speed = game.max_game_speed
                if power_up.type == TIME_TYPE:
                    time_audio()
                elif power_up.type == SHIELD_TYPE:
                    fraco_audio()
                elif power_up.type == HAMMER_TYPE:
                    hammer_audio()


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)