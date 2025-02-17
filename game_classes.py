import pygame

class player_1():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, heigth, scale, colour):
        image = pygame.Surface((width, heigth)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, heigth))
        image = pygame.transform.scale(image, (width * scale, heigth * scale))
        image.set_colorkey(colour)

        return image