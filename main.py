import pygame
import random
import os
import sys

from game import Game

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
