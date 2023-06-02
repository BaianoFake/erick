import pygame
import random 

from dino_runner.components.audio import dead_audio
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.choice([SMALL_CACTUS, LARGE_CACTUS, BIRD]) # incluir o tipo de obstáculo pássaro
            if obstacle_type == SMALL_CACTUS:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif obstacle_type == LARGE_CACTUS:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif obstacle_type == BIRD:
                self.obstacles.append(Bird()) 

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up or game.player.type == "time":
                    dead_audio()
                    pygame.time.delay(1000)
                    game.playing = False
                    game.death_count += 1
                    break
                elif game.player.type == "shield":
                    continue
                elif game.player.type == "hammer":
                    self.obstacles.remove(obstacle)

    def reset_obstacles(self):
        self.obstacles = []
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)