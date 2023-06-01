import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

FONT_STYLE = "freesansbold.ttf"

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.max_game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.high_score = 0
        self.second_score = 0
        self.death_count = 0

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()       

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        
        pygame.display.quit()
        pygame.quit()

    def reset(self):
        self.playing = False
        self.game_speed = 20
        self.score = 0
        self.player = Dinosaur()
        self.obstacle_manager.reset_obstacles()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        if self.score > self.high_score:  # Atualiza o high_score se o score atual for maior
            self.high_score = self.score
        if self.score > 10:
            self.second_score = self.score
        self.reset()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()

    def create_text(self, message, font_size, position, color):
        font = pygame.font.Font(FONT_STYLE, font_size)
        text = font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = position
        self.screen.blit(text, text_rect)

    def update_score(self):
        self.score += 1
        if self.score % 10 == 0:
            self.game_speed += 0.1
        if self.game_speed > 20:
            self.max_game_speed = self.game_speed


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) # "#FFFFFF"
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        self.create_text(f"Score: {self.score}", 22, (1000, 50), (0, 0, 0))
        self.create_text(f"Game Speed: {self.game_speed:.1f}", 22, (1000, 70), (0, 0, 0))

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.create_text("Press any key to start", 22, (half_screen_width, half_screen_height), (0, 0, 0))
        else:
            self.screen.blit(ICON, (half_screen_width - 20, half_screen_height - 140))
            self.create_text("Press any key to restart", 22, (half_screen_width, half_screen_height), (0, 0, 0))
            self.create_text(f"Score: {self.second_score}", 22, (half_screen_width, half_screen_height + 80), (0, 0, 0))  
            self.create_text(f"High Score: {self.high_score}", 22, (half_screen_width, half_screen_height + 60), (0, 0, 0))  
            self.create_text(f"Deaths: {self.death_count}", 22, (half_screen_width, half_screen_height + 40), (0, 0, 0))
            self.create_text(f"Game Speed: {self.max_game_speed:.1f}", 22, (half_screen_width, half_screen_height + 20), (0, 0, 0))

        pygame.display.update()
        self.handle_events_on_menu()