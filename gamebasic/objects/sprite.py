"""
movable sprite for 2d gaming.

abandoned. just use pygame.sprite.Sprite and pygame.sprite.Group
"""

from pygame import sprite

class Sprite(sprite.Sprite):
    def __init__(self, *groups: sprite.AbstractGroup) -> None:
        super().__init__(*groups)