import pygame
#Player Class
class Player:
    def __init__(self, name, surface):
        #Set Standart Values
        self.name = name
        self.hp = 20
        self.attack = 2
        self.defense = 1.5
        self.speed = 10
        #Visual Effects
        self.element = pygame.image.load('pokemon/textures/entities/player/player-sprite.png')
        self.x = 0
        self.y = 0
        self.scale = 128
        self.mul = 0
        self.count = 0
        #Attack Components
        self.surface = surface
        self.body = []
        
    def draw(self, surface):
        #Scale the image
        screen = pygame.transform.scale(self.element, (self.scale*6, self.scale))
        #Draw the image onto the screen
        return surface.blit(screen, (self.x, self.y),(self.scale * self.mul ,0,128,128))

    def movement(self, collidables):
        keys = pygame.key.get_pressed()
        new_x, new_y = self.x, self.y

        if keys[pygame.K_w]:  # handle w key press
            new_y -= self.speed
        elif keys[pygame.K_a]:  # handle a key press
            new_x -= self.speed
        elif keys[pygame.K_s]:  # handle s key press
            new_y += self.speed
        elif keys[pygame.K_d]:  # handle d key press
            new_x += self.speed
            # Inside the movement method, replace the collision check with a call to the new update_position method
        self.update_position(new_x, new_y, collidables)

        # Create a rect for the new position and check for collisions
        new_rect = pygame.Rect(new_x, new_y, self.scale*8, self.scale*8)
    def update_position(self, new_x, new_y, collidables):
        # Define a smaller hitbox within the larger sprite for more accurate collision detection
        hitbox_offset = 0
        # (self.scale - self.scale // 2) // 2
        hitbox_width = self.scale 
        hitbox_height = self.scale 
        hitbox = pygame.Rect(new_x + hitbox_offset, new_y + hitbox_offset, hitbox_width, hitbox_height)
        pygame.draw.rect(surface=self.surface, color=(255, 20, 200), rect=hitbox)
        # Check for collisions with the smaller hitbox
        if not any(hitbox.colliderect(collidable) for collidable in collidables):
            self.x, self.y = new_x, new_y  # Update the player's position if no collision is detected

    def animate(self):
        self.mul = (self.count // 5) % 5
        if self.count >= 25:
            self.count = 0
        else:
            self.count += 1
    def st(self):
        for entity in self.body:
            player_collision = pygame.draw.rect(surface=self.surface, color=(225,0,0), rect=(self.x,self.y,128,128))
            hit_rect = pygame.draw.rect(surface=self.surface,color=(255,20,0),rect=(entity[0],entity[1],128,128))
            if player_collision.colliderect(hit_rect):
                print("Attack!")
            else: print("lost mana... !")