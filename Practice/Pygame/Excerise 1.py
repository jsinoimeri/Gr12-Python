import pygame
pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Yeah, pygame")

background = pygame.Surface(size).convert()

background.fill((0, 0, 255))

clock = pygame.time.Clock()
keep_going = True

while keep_going:
    clock.tick(30)
    
    for ev in pygame.event.get():
        
        if ev.type == pygame.QUIT:
            keep_going == False
        
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_r:
                background.fill((255, 0, 0))
            else:
                key_label = ev.unicode
                pygame.display.set_caption(str(key_label)*10)
    
    screen.blit(background, (0,0))
    
    pygame.display.flip()