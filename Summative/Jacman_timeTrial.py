import pygame
import database
import keyboard_typing


WINDOW_SIZE = (560, 600)
GAME_SIZE = (560, 560)
MOVEMENT_STEP = 16


data_base = database.Database()



class Pacman(pygame.sprite.Sprite):
    '''Pacman starts in the middle of the screen automatically going to the left
    of the screen and uses the arrow keys'''
    
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()        
        self.rect.left = 495
        self.rect.top = 526
        
    def update(self, x, y, image):
        '''P.update(x, y, image) --> None
        Player 1's update method which takes the x-cordinate movement, 
        y-cordinate movement as well as the new image. It will moves the player 
        by x, y movements.'''
              
        self.rect.left += x
        self.rect.top += y     
            
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey(self.image.get_at((0,0)))



        
        
            
class Points(pygame.sprite.Sprite):
    '''
    Creates the class for the dots that Pacman eats to score points
    '''
    
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()        
        self.rect.left = x
        self.rect.top = y

            

        
        
        
def main():
    '''
    main() --> int and bool
    Returns the score and the boolean value of the main game loop
    '''
        
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("JACMAN: Time Trial - JETON SINOIMERI")
    
    background = pygame.image.load("images/time trial/Map.png").convert()

    
    time = 45
    
    x = MOVEMENT_STEP
    y = 0
    
    image = "images/time trial/pacman - right.png"
    
    score = 0
    
    player_sprites = pygame.sprite.Group()
    points_sprites = pygame.sprite.OrderedUpdates()
    time_sprites = pygame.sprite.Group()
    
    player_sprites.add(Pacman(image))
    
    counter = 0
    
    # adds dots to the field
    for vert in range (MOVEMENT_STEP, GAME_SIZE[1], MOVEMENT_STEP):
        for horiz in range(MOVEMENT_STEP, GAME_SIZE[0], MOVEMENT_STEP):
            counter += 1
        
            if counter % 25 == 0 and background.get_at((horiz, vert)) != (0, 0, 0):
                time_sprites.add(Points("images/time trial/cherries.png", horiz-1, vert -2))
            
            else:
                if background.get_at((horiz, vert)) != (0, 0, 0):
                    points_sprites.add(Points("images/time trial/little dot.png", horiz-1, vert-2))
       
    
    direction = "right"
    
    clock = pygame.time.Clock()
    keep_going = True
    game_play = True
        
    # countdown to the start of the game
    starting = ["3", "2", "1", "GO!"]
    
    font = pygame.font.SysFont("Courier New", 28)
    
    for start in starting:
        rendered_text = font.render(start, True, ((255, 255, 255)))
        rendered_text_rect = rendered_text.get_rect()
        
        rendered_text_rect.centerx = screen.get_rect().centerx
        rendered_text_rect.centery = screen.get_rect().centery
        
        screen.blit(background, (0,0))
        screen.blit(rendered_text, rendered_text_rect)
        
        
        pygame.display.update()
        
        pygame.time.delay(1000)
        
    
    screen.blit(background, (0,0))

    
    # scoreboard
    font = pygame.font.SysFont("Courier New", 28)
    
    message = "score: %i      time: %.2f" %(score, time)
    rendered_text = font.render(message, True, ((255, 255, 255)))
                        
    screen.blit(rendered_text, (32, WINDOW_SIZE[1]*0.925))    
    
    
    
    # main game loop
    while keep_going:
        
        #secondary game loop
        while game_play:

            time -= 0.1
            
            if time < 0:
                time = 0
            
            
            clock.tick(6)
           
            
            # event handling
            for ev in pygame.event.get():
                
                if ev.type == pygame.QUIT:
                    game_play = False
                    keep_going = False
                
                
                if ev.type == pygame.KEYDOWN:
                    
                    # move up
                    if ev.key == pygame.K_UP and direction != "up":
                        
                        if background.get_at((player_sprites.sprites()[0].rect.midtop[0], player_sprites.sprites()[0].rect.midtop[1] - 1)) != (0, 0, 0):
                            
                            image = "images/time trial/pacman - up.png"
                            y = - MOVEMENT_STEP
                            x = 0
    
                    
                    # move down    
                    elif ev.key == pygame.K_DOWN and direction != "down":
                        
                        if background.get_at((player_sprites.sprites()[0].rect.midbottom[0], player_sprites.sprites()[0].rect.midbottom[1] + 1)) != (0, 0, 0):
                            
                            image = "images/time trial/pacman - down.png"    
                            y = MOVEMENT_STEP
                            x = 0
                            
                   
                    # move right    
                    elif ev.key == pygame.K_RIGHT and direction != "right":
                        
                        if background.get_at((player_sprites.sprites()[0].rect.midright[0] + 1, player_sprites.sprites()[0].rect.midright[1])) != (0, 0, 0):
                            
                            image = "images/time trial/pacman - right.png"    
                            y = 0
                            x = MOVEMENT_STEP
                        
                    
                    # move left    
                    elif ev.key == pygame.K_LEFT and direction != "left":
                        
                        if background.get_at((player_sprites.sprites()[0].rect.midleft[0] - 1 , player_sprites.sprites()[0].rect.midleft[1])) != (0, 0, 0):
                            
                            image = "images/time trial/pacman - left.png"    
                            y = 0
                            x = - MOVEMENT_STEP
    
            
            
            # to check if the pacman hit the black borders
            if image == "images/time trial/pacman - right.png":
    
                if background.get_at((player_sprites.sprites()[0].rect.midright[0] + 1, player_sprites.sprites()[0].rect.midright[1])) == (0, 0, 0):
                        
                    x = 0
                    y = 0
                
                direction = "right"
                
            
            elif image == "images/time trial/pacman - left.png":
                
                
                if background.get_at((player_sprites.sprites()[0].rect.midleft[0] - 1 , player_sprites.sprites()[0].rect.midleft[1])) == (0, 0, 0):
                        
                    x = 0
                    y = 0
                
                direction = "left"
            
            elif image == "images/time trial/pacman - down.png":
               
                if background.get_at((player_sprites.sprites()[0].rect.midbottom[0], player_sprites.sprites()[0].rect.midbottom[1] + 1)) == (0, 0, 0):
                       
                    x = 0
                    y = 0
                
                direction = "down"
    
            
            elif image == "images/time trial/pacman - up.png":
               
                if background.get_at((player_sprites.sprites()[0].rect.midtop[0], player_sprites.sprites()[0].rect.midtop[1] - 1)) == (0, 0, 0):
                       
                    x = 0
                    y = 0
                
                direction = "up"
        
                
            # sprite collide
            
            if pygame.sprite.spritecollide(player_sprites.sprites()[0], points_sprites, False):
                points_sprites.remove(pygame.sprite.spritecollide(player_sprites.sprites()[0], points_sprites, False))
                score += 10
                
            
            elif pygame.sprite.spritecollide(player_sprites.sprites()[0], time_sprites, False):            
                score += 50
                time_sprites.remove(pygame.sprite.spritecollide(player_sprites.sprites()[0], time_sprites, False))
                time += 3
              
                
            if time == 0 or len(points_sprites.sprites()) == 0:
                game_play = False
                
            
            # draw to screen    
            points_sprites.clear(screen, background)
            points_sprites.draw(screen)
            
            time_sprites.clear(screen, background)
            time_sprites.draw(screen)
            
            player_sprites.clear(screen, background)
            
            player_sprites.update(x, y, image)
            player_sprites.draw(screen)
    
            
            #score board
            message = "score: %i      time: %.2f" %(score, time)
                
            rendered_text = font.render(message, True, ((255, 255, 255)))
            screen.blit(pygame.Surface((608, 39)), (0, 561))    
                
            screen.blit(rendered_text, (32, WINDOW_SIZE[1]*0.925))
            
            
            pygame.display.update()
        
            
        # game over message    
                   
        font = pygame.font.SysFont("Courier New", 80)
        font.set_italic(True)
        
        game_over = "GAME OVER!"
            
        rendered_text = font.render(game_over, True, ((255, 255, 255)))
        rendered_text_rect = rendered_text.get_rect()
        
        rendered_text_rect.centerx = screen.get_rect().centerx
        rendered_text_rect.centery = screen.get_rect().centery
            
        screen.blit(rendered_text, rendered_text_rect)
        
        pygame.display.update()
        
        pygame.time.delay(5000)
        
        keep_going = False
        
    
    return score, keep_going


if __name__ == "__main__":
    main()
    