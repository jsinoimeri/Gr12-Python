import random
import pygame
game_size = (640, 480)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("soccerball.bmp")
        self.image.set_colorkey(self.image.get_at((0,0)))
        
        self.rect = self.image.get_rect()        
        self.rect.left = random.randint(0, game_size[0]-self.rect.width)
        self.rect.top = random.randint(0, game_size[1]-self.rect.height)
        
        self.dx = random.randint(0,7)        
        if random.randint(0,1) == 0:
            self.dx *= -1
        
        self.dy = random.randint(0,7)        
        if random.randint(0,1) == 0:
            self.dy *= -1
        
        if self.dx == 0 and self.dy == 0:
            self.dx = random.randint(1,7)
    
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        
        if self.rect.right > screen.get_width():
            self.dx *= -1
        
        elif self.rect.left < 0:
            self.dx *= -1
        
        if self.rect.bottom > screen.get_height():
            self.dy *= -1
        
        elif self.rect.top < 0:
            self.dy *= -1

if __name__ == "__main__":
    screen = pygame.display.set_mode(game_size)
    
    background = pygame.Surface(game_size).convert()
    background.fill((255,255,255))
    screen.blit(background, (0,0))
    
    box = []
    tail_length = 2
    alpha_diff = 255.0/tail_length
    all_sprites = pygame.sprite.OrderedUpdates()
    
    for num in range(tail_length):
        box += [Ball()]
    
    all_sprites.add(box)
    clock = pygame.time.Clock()
    keep_going = True
    
    while keep_going:
        clock.tick(30)
        
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                keep_going = False
        
        
        for i in box:
            all_sprites.clear(screen, background)
            all_sprites.update()
            all_sprites.draw(screen)
            
        pygame.display.flip()