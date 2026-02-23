# to run the game type in terminal: python window.py
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen, can change it to any size you want
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption("Connect 4 dots")

# run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# quit pygame after closing window
pygame.quit()

