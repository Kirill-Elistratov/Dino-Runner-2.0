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


class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 6.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.dead_img = DEAD

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.dino_dead = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if not self.dino_dead:
            if self.dino_duck:
                self.duck()
            elif self.dino_run:
                self.run()
            elif self.dino_jump:
                self.jump()
        else:
            self.image = self.dead_img
        if userInput[pygame.K_UP] and not self.dino_jump and not self.dino_dead:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
            jump_sound.play()
        elif userInput[pygame.K_DOWN] and not self.dino_jump and not self.dino_dead:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        if self.step_index // 5 < len(self.duck_img):
            self.image = self.duck_img[self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS_DUCK
            self.step_index += 1
        else:
            self.step_index = 0

    def run(self):
        if self.step_index // 5 < len(self.run_img):
            self.image = self.run_img[self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS
            self.step_index += 1
        else:
            self.step_index = 0

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.45
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self, is_stop):
        if not is_stop:
            self.x -= game_speed
            if self.x < -self.width:
                self.x = SCREEN_WIDTH + random.randint(2500, 3000)
                self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.is_stop=False

    def update(self, is_dead):
        if is_dead:
            self.is_stop=True
        if not self.is_stop:
            self.rect.x -= game_speed
            if self.rect.x < -self.rect.width:
                obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if not self.is_stop:
            if self.index >= 9:
                self.index = 0
            self.index += 0.5
        SCREEN.blit(self.image[int(self.index // 5)], self.rect)


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 10
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score(is_dead):
        global points, game_speed

        if not is_dead:
            points += 1
            if points % 500 == 0:
                points_sound.play()
            if points % 100 == 0:
                game_speed += 0.5

        text = font.render("Points: " + str(int(points)), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background(is_dead):
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if not is_dead:
            if x_pos_bg <= -image_width:
                SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_rect.collidepoint(event.pos):
                    main()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if not player.dino_dead and len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(player.dino_dead)
            if not player.dino_dead and player.dino_rect.colliderect(obstacle.rect):
                death_count += 1
                player.dino_dead = True
                death_sound.play()
        if player.dino_dead:
            game_over_rect = GAME_OVER.get_rect()
            game_over_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)
            SCREEN.blit(GAME_OVER, game_over_rect)
            reset_rect = RESET_ARROW.get_rect()
            reset_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 45)
            SCREEN.blit(RESET_ARROW, reset_rect)

        score(player.dino_dead)
        cloud.update(player.dino_dead)
        background(player.dino_dead)
        cloud.draw(SCREEN)

    clock.tick(60)
    pygame.display.update()