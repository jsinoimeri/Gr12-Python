import random
import pygame
game_size = (640, 480)

class Ball(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("soccerball.bmp")
        self.image.set_colorkey(self.image.get_at((0,0)))
        
        self.rect = self.image.get_rect()        
        self.rect.left = start_x
        self.rect.top = start_y
        
        self.dx = random.randint(0,7)        
        if random.randint(0,1) == 0:
            self.dx *= -1
        
        self.dy = random.randint(0,7)        
        if random.randint(0,1) == 0:
            self.dy *= -1
        
        if self.dx == 0 and self.dy == 0:
            self.dx = random.randint(1,7)
    def x(self):
        return self.dx
    def y(self):
        return self.dy
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
    
    all_sprites = pygame.sprite.Group()
    b = Ball(0, 40)
    all_sprites.add(b)
    
    clock = pygame.time.Clock()
    keep_going = True
    
    while keep_going:
        clock.tick(10)
        
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                keep_going = False
        
        print b.x(), b.y()
        all_sprites.clear(screen, background)
        all_sprites.update()
        all_sprites.add(Ball(all_sprites.sprites()[-1].rect.x, all_sprites.sprites()[-1].rect.y)) 
        all_sprites.draw(screen)
           
        pygame.display.flip()