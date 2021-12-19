import pygame

# Colours
COLOURS = {"Black": (0, 0, 0), "White": (255, 255, 255), "Dark Grey": (25, 25, 25)}

# Scene events
# Used to switch between scenes
MAIN_MENU = pygame.event.custom_type()
RAYCAST_DEMO = pygame.event.custom_type()