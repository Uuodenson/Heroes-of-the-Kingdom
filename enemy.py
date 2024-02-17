import pygame
#Player Class
class Enemy:
    def __init__(self, name, scale = 128):
        self.name = name
        self.hp = 20
        self.attack = 2
        self.defense = 1.5
        self.speed = 10
        self.element = pygame.image.load('pokemon/textures/entities/enemy-sprite.png')
        self.x = 800 - scale
        self.y = 0
        self.scale = scale
        self.mul = 0
        self.count = 0
        
    def draw(self, surface):
        #Scale the image
        screen = pygame.transform.scale(self.element, (self.scale*6, self.scale))
        #Draw the image onto the screen
        surface.blit(screen, (self.x, self.y),(self.scale * self.mul ,0,128,128))

    def movement(self,event):
            pass
    def animate(self):
        self.mul = (self.count // 5) % 5
        if self.count >= 25:
            self.count = 0
        else:
            self.count += 1