import pygame


def _make_error_image() -> pygame.Surface:
    """Create a fallback that does not require a display to be initialized."""
    image = pygame.Surface((64, 64))
    image.fill((255, 0, 255))
    pygame.draw.line(image, (0, 0, 0), (0, 0), (64, 64), 5)
    pygame.draw.line(image, (0, 0, 0), (64, 0), (0, 64), 5)
    return image


ERR_IMG: pygame.Surface = _make_error_image()