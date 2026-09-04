import pygame
from scenes.home import main as home_main
from gamebasic.objects.scene import Scene, SceneName
clock = pygame.time.Clock()

scene = Scene()

# game inits.
scene.set_current_scene_enum(SceneName.HOME)


def main():

