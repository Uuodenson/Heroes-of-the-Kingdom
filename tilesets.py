import pygame
tileset = {
    "main": 
    [
        [1,0,0,0,0,1,2,2,0,1],
        [1,0,0,0,2,1,2,2,0,1],
        [1,0,0,2,2,1,2,2,0,1],
        [1,0,2,2,2,1,2,2,0,1],
        [1,1,2,2,1,1,1,1,1,1],
        [2,2,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,1,0,1,1,1],
        [1,1,2,2,2,2,2,2,1,1],
    ],
    "images":[
        pygame.image.load("pokemon/textures/terrain/water.png"),
        pygame.image.load("pokemon/textures/terrain/grass.png"),
        pygame.image.load("pokemon/textures/terrain/dirt.png")
        ]
}
def getkey(dict,key):
    if isinstance(key, str):
        return dict[key]
def draw_tileset(surface, tileset, tile_images, scale_factor):
    scaled_tile_images = [pygame.transform.scale(image, (int(image.get_width()*scale_factor), int(image.get_height()*scale_factor))) for image in tile_images]
    tile_width, tile_height = scaled_tile_images[1].get_size()
    for y, row in enumerate(tileset['main']):
        for x, tile_value in enumerate(row):
            if tile_value in [0, 1, 2]:
                # Draw the corresponding tile
                surface.blit(scaled_tile_images[tile_value], (x * tile_width, y * tile_height))
def setcollsion(tileset, dict,value):
    for y, row in enumerate(tileset['main']):
        for x, tile_value in enumerate(row):
            if tile_value == value:
                # Draw the corresponding tile
                dict.append(pygame.Rect(x * 128, y * 128, 128, 128))