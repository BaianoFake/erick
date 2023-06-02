import pygame
import os

pygame.mixer.init()

AUD_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")


def jump_audio():
    audio = pygame.mixer.Sound(os.path.join(AUD_DIR, "audio/jump.mp3"))
    audio.play()

def score_reach_audio():
    audio = pygame.mixer.Sound(os.path.join(AUD_DIR, "audio/score.mp3"))
    audio.play()

def dead_audio():
    audio = pygame.mixer.Sound(os.path.join(AUD_DIR, "audio/dead.mp3"))
    audio.play()

def start_audio():
    audio = pygame.mixer.Sound(os.path.join(AUD_DIR, "audio/start.mp3"))
    audio.play()

def loop_music():
    pygame.mixer.music.load(os.path.join(AUD_DIR, "audio/music.mp3"))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()