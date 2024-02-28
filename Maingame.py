import pygame
import os
import random
import pygame.mixer

pygame.init()

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("data/Default_dino/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("data/Default_dino/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("data/Default_dino/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("data/Default_dino/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("data/Default_dino/Dino", "DinoDuck2.png"))]

DEAD = pygame.image.load(os.path.join("data/Default_dino/Dino", "DinoDead.png"))

SMALL_CACTUS = [pygame.image.load(os.path.join("data/Default_dino/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("data/Default_dino/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("data/Default_dino/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("data/Default_dino/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("data/Default_dino/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("data/Default_dino/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("data/Default_dino/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("data/Default_dino/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("data/Default_dino/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("data/Default_dino/Other", "Track.png"))

GAME_OVER = pygame.image.load(os.path.join("data/Default_dino/Other", "GameOver.png"))
RESET_ARROW = pygame.image.load(os.path.join("data/Default_dino/Other", "Reset.png"))

jump_sound = pygame.mixer.Sound('data/Default_dino/Sounds/jump_sound.mp3')
death_sound = pygame.mixer.Sound('data/Default_dino/Sounds/death_sound.mp3')
points_sound = pygame.mixer.Sound('data/Default_dino/Sounds/reached.mp3')