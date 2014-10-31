import pygame

class Ball(object):
    def __init__(self, surf, x = 0, y = 0):
        self.surf = surf.convert()
        self.x = x
        self.y = y
        self.surf.set_colorkey(self.surf.get_at((0,0)))
        
    def __str__(self):
        return "(%i,%i)" %(self.x, self.y)

def main():
    pygame.mixer.init(22050, -16, 2, 512)
    pygame.init()
    
    
    size = (640, 480)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Movement")
    
    box = []
    start_x = 100
    start_y = 100
    background = pygame.Surface(size).convert()    
    background.fill((255, 255, 255))
    
    bounce = pygame.mixer.Sound("bounce.ogg")

    box += [Ball(pygame.image.load("soccerball.bmp"), start_x, start_y)]   
        
    delta = 5
    dir_horiz = 1
    dir_vert = 1
    clock = pygame.time.Clock()
    keep_going = True
    
    while keep_going:
        clock.tick(60)
        
        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                keep_going = False
                       
            
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    delta += 1
                
                elif ev.key == pygame.K_DOWN:
                    delta -= 1
                    delta = max(0, delta)
                
                elif ev.key == pygame.K_LEFT:
                    dir_horiz = -1
            
                elif ev.key == pygame.K_RIGHT:
                    dir_horiz = 1
         
        
        if box[-1].x > screen.get_width() - box[-1].surf.get_width():
            dir_horiz = -1
            bounce.play()
        
        elif box[-1].x < 0:
            dir_horiz = 1
            bounce.play()
    
        if box[-1].y > screen.get_height() - box[-1].surf.get_height(): 
            dir_vert = -1
            bounce.play()
        
        elif box[-1].y < 0:
            dir_vert = 1
            bounce.play()
        
        #for i in range(len(box)-1):
            #box[i].x = box[i+1].x
            #box[i].y = box[i+1].y
        
        box += [Ball(pygame.image.load("soccerball.bmp"), box[-1].x, box[-1].y)]
        box[-1].x += (delta*dir_horiz)
        box[-1].y += (delta*dir_vert)
                   
        screen.blit(background, (0,0))
        for b in box:
            screen.blit(b.surf, (b.x,b.y))
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()