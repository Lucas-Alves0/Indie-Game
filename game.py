import pygame
import game_classes

pygame.init()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Spritesheets')

sprites = {
    'generic_blue':'C:/Users/lucas.paula_kovi/VSCodeProjects/MyOwnProjects/GameProject/game_assets/players/generic_char_v0.2/generic_char_v0.2/png/blue/char_blue_1.png',
    'generic_red':'C:/Users/lucas.paula_kovi/VSCodeProjects/MyOwnProjects/GameProject/game_assets/players/generic_char_v0.2/generic_char_v0.2/png/blue/char_red_1.png',
    'generic_green':'C:/Users/lucas.paula_kovi/VSCodeProjects/MyOwnProjects/GameProject/game_assets/players/generic_char_v0.2/generic_char_v0.2/png/blue/char_green_1.png'
}

sprite_sheet_image = pygame.image.load(sprites['generic_blue']).convert_alpha()
sprite_sheet = game_classes.player_1(sprite_sheet_image)

bg = (50, 50, 50)
black = (0, 0, 0)

# create animation list
animation_list = []
animation_steps = 6
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 150
frame = 0

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x, 56, 56, 3, black))

run = True
while run:

    # update background
    screen.fill(bg)

    # update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0
    

    # show frame image
    screen.blit(animation_list[frame], (0, 0))

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
