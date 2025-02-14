import pygame

pygame.init()

screen_width = 720
screen_height = 480

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Spritesheets')

bg = (50, 50, 50)

run = True
while run:

    screen.fill(bg)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
