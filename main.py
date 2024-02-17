import pygame

# import class Player from the folder pokemon/classes
from player import Player
from enemy import Enemy
from tilesets import tileset, draw_tileset, getkey, setcollsion

# icon
icon = pygame.image.load("pokemon/textures/ui/icon.png")
pygame.display.set_icon(icon)

# Title
pygame.display.set_caption("Pokemon")

# Screen Setting
window = (800, 600)
screen = pygame.display.set_mode(window, pygame.RESIZABLE)

# set player
player = Player("player", screen)
player.surface = screen
# set enemy
enemy = Enemy("enemy")

#set terrain
terrainkey = getkey(tileset, "images")
collidables = []
setcollsion(tileset, collidables, 0)
# Variablles
running = True
FPS = 20
clock = pygame.time.Clock()
#
body = []
body.append((enemy.x, enemy.y))
player.body = body
print(player.body)


# Game Loop
def main(running):
    while running:

        # Input Handeling
        for event in pygame.event.get():
            player.movement(collidables=collidables)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_SPACE:
                    player.st()
        # Background + Debug mode
        screen.fill((0, 30, 225))
        draw_tileset(surface=screen, tileset=tileset, tile_images=terrainkey,scale_factor=8)
        player.st()
        # Enemy Draw + Movement
        enemy.draw(surface=screen)
        enemy.animate()
        # Player DrawiPng + Movement
        player.draw(surface=screen)
        player.animate()
        #Draw Collsion object
        for coll in collidables:
            pygame.draw.rect(surface=screen, color=(255, 0, 0), rect=coll)
        # Uppdate Screen Display
        pygame.display.update()
        #
        # Clock
        clock.tick(FPS)
    pygame.quit()


main(running=running)
