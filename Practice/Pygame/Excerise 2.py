import pygame

class Ball(object):
    def __init__(self, surf, x = 0, y = 0, alpha = 255):
        self.surf = surf.convert()
        self.x = x
        self.y = y
        self.surf.set_alpha(alpha)
        
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
    
    tail_length = 9
    alpha_diff = 255.0/tail_length
    for i in range(tail_length):
        box += [Ball(pygame.image.load("soccerball.bmp"), start_x, start_y, (i+1)*alpha_diff)]   
    
    bounce = pygame.mixer.Sound("bounce.ogg")
    
    background.fill((255, 255, 255))
    
    box_x = box[-1].width()
    box_y = box[-1].get_height()
    delta = 5
    dir_horiz = 1
    dir_vert = 1
    clock = pygame.time.Clock()
    keep_going = True
    
    while keep_going:
        clock.tick(30)
        
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
         
                    
        box_x += (delta * dir_horiz)
        box_y += (delta * dir_vert)
        
        if box_x >= screen.get_width() - box.get_width():
            dir_horiz = -1
            bounce.play()
        
        elif box_x <= 0:
            dir_horiz = 1
            bounce.play()
    
        if box_y >= screen.get_height() - box.get_height(): 
            dir_vert = -1
            bounce.play()
        
        elif box_y <= 0:
            dir_vert = 1
            bounce.play()
        
        screen.blit(background, (0,0))
        screen.blit(box, (box_x,box_y))
        
        pygame.display.flip()
    
if __name__ == "__main__":
    main()