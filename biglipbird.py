import pygame
import sys
import os
import random
from pygame import mixer
from pygame.constants import WINDOWCLOSE

# Initialize Pygame modules
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Defining Pygame objects
WIDTH, HEIGHT = 400, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# PyGame window name
caption_name = ("Big Lip Bird")
pygame.display.set_caption(caption_name)

# Initialize Game Icon
GAME_ICON = pygame.image.load(
    os.path.join("assets/icon", "icon.png"))
pygame.display.set_icon(GAME_ICON)

# Background Music
mixer.music.load("assets/sound/music.wav")
mixer.music.play(-1)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:  # Quits Game
        run = False
    # Update game
    pygame.display.update()
