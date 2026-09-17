import pygame
from os.path import join


ERR_IMG:pygame.Surface = pygame.image.load(join("gamebasic", "debug", "missing_img.jpg")).convert()