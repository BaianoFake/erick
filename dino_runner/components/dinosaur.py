import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, TIME_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER, SCREEN_WIDTH


X_POS = 80
X_VEL = 10
Y_POS = 310
JUMP_VEL = 8.5

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, TIME_TYPE: DUCKING}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, TIME_TYPE: JUMPING}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, TIME_TYPE: RUNNING}


class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.dino_jump = False
        self.dino_duck = False
        self.dino_run = True
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.power_up_time = 0

    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        else:
            self.run()

        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            if self.dino_rect.x > 0:
                self.dino_rect.x -= X_VEL
        elif user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            if self.dino_rect.right < SCREEN_WIDTH:
                self.dino_rect.x += X_VEL


        if (user_input[pygame.K_UP] or user_input[pygame.K_w]) and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif (user_input[pygame.K_DOWN] or user_input[pygame.K_s]) and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not self.dino_jump and self.dino_duck:
            self.dino_jump = False
            self.dino_duck = False
            self.dino_run = True
        elif (user_input[pygame.K_DOWN] or user_input[pygame.K_s]) and self.dino_jump:
            self.jump_vel -= 0.4

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect.y = Y_POS + 40
        self.step_index += 1
        self.dino_duck = False

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

