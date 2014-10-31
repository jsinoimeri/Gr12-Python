import pygame

class Ball(object):
    def __init__(self, surf, x, y):
        self.surf = surf.convert()
        self.x = x
        self.y = y
        
    def __str__(self):
        return "(%i,%i)" %(self.x, self.y)

def main():
    pygame.init()
        
    size = (640, 480)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Movement")


    background = pygame.Surface(size).convert()    
    background.fill((255, 255, 255))
    
    box2 = pygame.Surface((size[0]*0.01, size[1]*0.01))
    tail_length = 1
    #alpha_diff = 255.0/tail_length   
    
    box = []

    
    box += [Ball(box2, 0, 0)]

        
    clock = pygame.time.Clock()
    keep_going = True
    
    
    while keep_going:
        clock.tick(30)
        
        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                keep_going = False
                                    
            elif ev.type == pygame.MOUSEMOTION:
            
                box[-1].x = ev.pos[0] - box[-1].surf.get_width()/2
                box[-1].y = ev.pos[1] - box[-1].surf.get_height()/2
                             
        
        
        box += [Ball(box2, box[-1].x, box[-1].y )]
        print len(box)
                   
        screen.blit(background, (0,0))
        for b in box:
            screen.blit(b.surf, (b.x,b.y))
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()