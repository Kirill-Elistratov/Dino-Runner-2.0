import os
import pygame
import sys

# pygame.init()
# size = width, height = 800, 800
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption('Boom them all')
# all_sprites = pygame.sprite.Group()


class KeyButton(pygame.sprite.Sprite):
    image = pygame.image.load('data/key-border.png')
    width, height = image.get_width(), image.get_height()

    # 50, 50

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.width, self.height = KeyButton.width, KeyButton.height
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.image = KeyButton.image


class Keyboard(pygame.sprite.Sprite):
    image = pygame.image.load('data/key-board.png')

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.width, self.height = 240, 125
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.keys = [KeyButton((self.rect.x + 10, self.rect.y + 10)),
                     KeyButton((self.rect.x + 10 + (KeyButton.width + 5), self.rect.y + 10)),
                     KeyButton((self.rect.x + 10 + (KeyButton.width + 5) * 3, self.rect.y + 10)),
                     KeyButton((self.rect.x + 10 + (KeyButton.width + 5) * 4, self.rect.y + 10)),
                     KeyButton((self.rect.x + 35, self.rect.y + 65)),
                     KeyButton((self.rect.x + 35 + (KeyButton.width + 5), self.rect.y + 65)),
                     KeyButton((self.rect.x + 35 + (KeyButton.width + 5) * 2, self.rect.y + 65)),
                     KeyButton((self.rect.x + 35 + (KeyButton.width + 5) * 3, self.rect.y + 65))]
        self.image = Keyboard.image


# example = Keyboard((50, 50))
#
# running = True
# while running:
#     screen.fill(pygame.Color('black'))
    #
    # перебор событий
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False
    #
    # основной код
    # all_sprites.draw(screen)
    #
    # отрисовка кадра
    # pygame.display.flip()
# pygame.quit()
