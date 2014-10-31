import random
import pygame
import os

#http://soundbible.com/1757-Car-Brake-Crash.html
#http://www.mariowiki.com/images/3/3b/TurtleyLeaf_SPM.png
#http://www.cgarena.eu/wp-content/uploads/2010/08/tron_legacy.jpg
#http://img213.imageshack.us/img213/6730/tronlegacywallhd.png
#http://www.youtube.com/watch?v=iFxMhlNC3ss

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.mixer.init(22050, -16, 2, 512)
pygame.font.init()

WINDOW_SIZE = (700, 490)
GAME_SIZE = (WINDOW_SIZE[0], int(WINDOW_SIZE[0]*0.62))
MOVEMENT_STEP = int(GAME_SIZE[0]*0.01)


class Player(pygame.sprite.Sprite):
    '''Player 1 who starts on the left side of the screen and is controlled by
    the arrow keys'''
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((MOVEMENT_STEP- 1, MOVEMENT_STEP - 1)).convert()  
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()        
        self.rect.right = GAME_SIZE[0]*0.1
        self.rect.top = self.rect.right
        
    def update(self, x, y):
        '''Player().update(x, y) --> None
        Player 1's update method which takes the x-cordinate movement as well as
        the y-cordinate movement. It will moves the player by x, y movements. It
        not move the player if he has made contact with the screen.'''
        
        if self.rect.right + x <= GAME_SIZE[0] and self.rect.left + x > 0:
            self.rect.right += x
        
        if self.rect.bottom + y <= GAME_SIZE[1] and self.rect.top + y >= 0:
            self.rect.top += y     


            
            
class Player2(pygame.sprite.Sprite):
    '''Player 2 who starts on the right side of the screen and is controlled by
    the WASD keys'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((MOVEMENT_STEP - 1, MOVEMENT_STEP - 1)).convert()  
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect()        
        self.rect.right = GAME_SIZE[0]*0.9
        self.rect.top = Player().rect.top
        
    def update(self, x, y):
        '''Player2().update(x, y) --> None
        Player 2's update method which takes the x-cordinate movement as well as
        the y-cordinate movement. It will moves the player by x, y movements. It
        not move the player if he/she has made contact with the screen.'''
        
        if self.rect.right + x <= GAME_SIZE[0] and self.rect.left + x > 0:
            self.rect.right += x
        
        if self.rect.bottom + y <= GAME_SIZE[1] and self.rect.top + y >= 0:
            self.rect.top += y     


            
                 
class Tail(pygame.sprite.Sprite):
    '''Tail is the tail of player 1 and it starts behind player 1 and continues
    to grow as he/she plays'''
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((MOVEMENT_STEP - 1, MOVEMENT_STEP - 1)).convert() 
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.right = Player().rect.left
        self.rect.top = Player().rect.top
    
    def update(self, x, y):
        '''Tail().update(x, y) --> None
        Tail's update method which takes the x-cordinate movement as well as
        the y-cordinate movement. It will make the left side of the tail equal
        to x value and the top equal to y value.'''
        
        self.rect.left = x
        self.rect.top = y


            
    
class Tail2(pygame.sprite.Sprite):
    '''Tail2 is the tail of player 2 and it starts behind player 2 and continues
    to grow as he/she plays'''
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((MOVEMENT_STEP - 1, MOVEMENT_STEP - 1)).convert() 
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.right = Player2().rect.right
        self.rect.top = Player2().rect.top
    
    def update(self, x, y):
        '''Tail2().update(x, y) --> None
        Tail2's update method which takes the x-cordinate movement as well as
        the y-cordinate movement. It will make the left side of the tail equal
        to x value and the top equal to y value.'''
        
        self.rect.left = x
        self.rect.top = y


            
              
class Obstacles(pygame.sprite.Sprite):
    '''Creates the Obstacles for the players to not be able to go through'''
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("rect.png")
        self.rect = self.image.get_rect()            
        self.rect.right = random.randint(self.image.get_width() / MOVEMENT_STEP , 99) * MOVEMENT_STEP
        self.rect.top = random.randint((Player().rect.top / MOVEMENT_STEP) + MOVEMENT_STEP, 54)* MOVEMENT_STEP


            
        
class Power(pygame.sprite.Sprite):
    '''Creates the power up for the players to use only once during the game'''
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("leaf.png")
        self.image.set_colorkey(self.image.get_at((self.image.get_width()-1 ,0)))
        self.rect = self.image.get_rect()            
        self.rect.right = random.randint(self.image.get_width(), 100) * MOVEMENT_STEP
        self.rect.top = random.randint(0, 62 - self.image.get_width())* MOVEMENT_STEP          


            
                
if __name__ == "__main__":
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("TRON REMAKE - JETON SINOIMERI")
    
    # loading of the sounds, and movie elements needed for the game
    background_music = pygame.mixer.Sound("slam - pendulum.ogg")    
    crash = pygame.mixer.Sound("car crash.ogg")    
    start_menu_music = pygame.mixer.Sound("push it - rick ross.ogg")   
    movie = pygame.movie.Movie("TRON LEGACY Trailer.mpg")

    
    start_menu_music.play(-1)
    
    
    start = False
    keep_going = True
    game_play = True
    movie_play = True
    
    font = pygame.font.SysFont("Rockwell", 48)
    font2 = pygame.font.SysFont("Arial", 20)
    
    font2 = font2.render("Press Spacebar to skip", True, ((255, 255, 255)))
    
    background = pygame.Surface(WINDOW_SIZE).convert()
    background.fill((0, 0, 0))
    

    # starting advertisements
    countdown_list = ["FOSTER INCORPORATED", "IN ASSOCIATION WITH", "JETON SINOIMERI", "PRESENT"]
    counter = 0
    while  counter < len(countdown_list):
        
        if counter < len(countdown_list):
            countdown = font.render(countdown_list[counter], True, ((255, 255, 255)))        
            counter += 1        
            countdown_rect = countdown.get_rect()
            countdown_rect.centerx = screen.get_rect().centerx
            countdown_rect.centery = screen.get_rect().centery
            
            screen.blit(font2, (100, WINDOW_SIZE[1]*0.9))    
            screen.blit(countdown, countdown_rect)
            pygame.display.update()
            
            pygame.time.delay(2000)
                   
            screen.blit(background, (0,0))
            pygame.display.update()
        
            
        # event handling    
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                start = True
                keep_going = False
                movie_play = False
                counter = 5
                
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    counter = 5
          
                    
        if counter == 4:
            
            # loads the image of the game being played
            title = pygame.image.load("Tron5.png")
            screen.blit(title, (0, 0))
            pygame.display.update()
            
            pygame.time.wait(3000)
            
            screen.blit(background, (0,0))
            pygame.display.update()
        
        
    pygame.time.delay(1000)        
    
    # plays the movie
    if movie_play:
        movie.play()
        screen.blit(font2, (100, WINDOW_SIZE[1]*0.9))
        pygame.display.update()
    
        
    # waits for a keyboard event to happen while the movie continues to play    
    while movie_play:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                movie_play = False
                keep_going = False
                start = True
                        
                    
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    movie.stop()
                        
        if movie.get_busy() == False:
            movie_play = False
    
            
    # waits for the movie to finish playing completely then continues with the
    # of the code execution
    pygame.time.delay(2100)
    
    # the start menu including the loading screen
    if start == False:
        
        # loading screen
        countdown_list = ["LOADING.", "LOADING..", "LOADING..."]
        for i in range(2):
            for countdown in countdown_list:
                screen.blit(background, (0, 0))
    
                font = pygame.font.SysFont("Rockwell", 24)
                countdown = font.render(countdown, True, ((255, 255, 255)))
                    
                countdown_rect = countdown.get_rect()
                countdown_rect.centerx = screen.get_rect().centerx
                countdown_rect.centery = screen.get_rect().centery
                    
                screen.blit(countdown, countdown_rect)
                
                pygame.display.update()
                
                pygame.time.wait(2000)
            
            
        # loads the start menu
        start_menu = pygame.image.load("Tron2.png")
        
        screen.blit(start_menu, (0,0))
        pygame.display.update()
    
    
        
    # the start menu
    while start == False:

        for ev in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                start = True
                keep_going = False
            
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                
                if mouse_pos[0] >= 139 and mouse_pos[0] <= 522:
                    
                    # makes sure the user clicks on the start button to start the game
                    if mouse_pos[1] >= 177 and mouse_pos[1] <= 219:
                             
                        start_menu_music.fadeout(3000)
                        pygame.time.delay(500)

                        start = True
                
                    # makes sure that the user clicks on the help menu if help is
                    # needed
                    elif mouse_pos[1] >= 235 and mouse_pos[1] <= 277:
                        help_menu = True

                        help_menu_img = pygame.image.load("help1.png")
                        screen.blit(help_menu_img, (0,0))
                        pygame.display.update()
                        
                        # the help menu
                        while help_menu:                          
                            
                            for ev in pygame.event.get():
                                mouse_pos = pygame.mouse.get_pos()
                                if ev.type == pygame.QUIT:
                                    start = True
                                    keep_going = False
                                    help_menu = False

                                    
                                
                                elif ev.type == pygame.MOUSEBUTTONDOWN:
                                    if mouse_pos[0] >= 204 and mouse_pos[0] <= 470:
                                        
                                        # makes sure the controls help is pressed
                                        if mouse_pos[1] >= 124 and mouse_pos[1] <= 180:
                                            control = True
                                            control_image = pygame.image.load("controls1.png")
                                            screen.blit(control_image, (0, 0))
                                            pygame.display.update()
                                            
                                            while control:
                                                
                                                for ev in pygame.event.get():
                                                    mouse_pos = pygame.mouse.get_pos()
                                                    if ev.type == pygame.QUIT:
                                                        start = True
                                                        keep_going = False
                                                        help_menu = False
                                                        control = False
                                                    

                                                    elif ev.type == pygame.MOUSEBUTTONDOWN:
                                                        
                                                        # makes sure that if the user presses
                                                        # the left arrow, it will go back
                                                        # to the help menu
                                                        if mouse_pos[0] >= 20 and mouse_pos[0] <= 64:
                                                            if mouse_pos[1] >= 453 and mouse_pos[1] <= 472:
                                                                control = False
                                                    
                                                                
                                                    # if the mouse is over the left arrow it loads
                                                    # the same image but with the arrow highlighted
                                                    elif mouse_pos[0] >= 20 and mouse_pos[0] <= 64:
                                                        if mouse_pos[1] >= 453 and mouse_pos[1] <= 472:
                                                            control_image = pygame.image.load("controls2.png")
                                                            screen.blit(control_image, (0, 0))
                                                            pygame.display.update()
                                                     
                                                            
                                                    # if the mouse leaves the left arrow it loads
                                                    # the first controls image
                                                    else:
                                                        control_image = pygame.image.load("controls1.png")
                                                        screen.blit(control_image, (0, 0))
                                                        pygame.display.update()
                                        
                                                        
                                        # makes sure the objective help is pressed
                                        elif mouse_pos[1] >= 243 and mouse_pos[1] <= 294:
                                            obj = True
                                            obj_image = pygame.image.load("objective1.png")
                                            screen.blit(obj_image, (0, 0))
                                            pygame.display.update()
                                            
                                            while obj:
                                                
                                                for ev in pygame.event.get():
                                                    mouse_pos = pygame.mouse.get_pos()
                                                    if ev.type == pygame.QUIT:
                                                        start = True
                                                        keep_going = False
                                                        help_menu = False
                                                        obj = False

                                                    elif ev.type == pygame.MOUSEBUTTONDOWN:
                                                        
                                                        # makes sure that if the user presses
                                                        # the left arrow, it will go back
                                                        # to the help menu
                                                        if mouse_pos[0] >= 20 and mouse_pos[0] <= 64:
                                                            if mouse_pos[1] >= 453 and mouse_pos[1] <= 472:
                                                                obj = False
                                                                
                                                                
                                                    # if the mouse is over the left arrow it loads
                                                    # the same image but with the arrow highlighted
                                                    elif mouse_pos[0] >= 20 and mouse_pos[0] <= 64:
                                                        if mouse_pos[1] >= 453 and mouse_pos[1] <= 472:
                                                            obj_image = pygame.image.load("objective2.png")
                                                            screen.blit(obj_image, (0, 0))
                                                            pygame.display.update()
                                                        
                                                            
                                                    # if the mouse leaves the left arrow it loads
                                                    # the first objective image
                                                    else:
                                                        obj_image = pygame.image.load("objective1.png")
                                                        screen.blit(obj_image, (0, 0))
                                                        pygame.display.update()
                                        
                                                        
                                        # makes sure the objective help is pressed               
                                        elif mouse_pos[1] >= 358 and mouse_pos[1] <= 410:
                                            about = True
                                            about_image = pygame.image.load("about1.png")
                                            screen.blit(about_image, (0, 0))
                                            pygame.display.update()
                                            
                                            while about:
                                                
                                                for ev in pygame.event.get():
                                                    mouse_pos = pygame.mouse.get_pos()
                                                    if ev.type == pygame.QUIT:
                                                        start = True
                                                        keep_going = False
                                                        help_menu = False
                                                        about = False

                                                    elif ev.type == pygame.MOUSEBUTTONDOWN:
                                                        
                                                        # makes sure that if the user presses
                                                        # the left arrow, it will go back
                                                        # to the help menu
                                                        if mouse_pos[0] >= 20 and mouse_pos[0] <= 64:
                                                            if mouse_pos[1] >= 453 and mouse_pos[1] <= 472:
                                                                about = False
                                                    
                                                                
                                                    # if the mouse is over the left arrow it loads
                                                    # the same image but with the arrow highlighted
                                                    elif mouse_pos[0] >= 20 and mouse_pos[0] <= 64:
                                                        if mouse_pos[1] >= 453 and mouse_pos[1] <= 472:
                                                            about_image = pygame.image.load("about2.png")
                                                            screen.blit(about_image, (0, 0))
                                                            pygame.display.update()
                                                            
                                                            
                                                    # if the mouse leaves the left arrow it loads
                                                    # the first objective image        
                                                    else:
                                                        about_image = pygame.image.load("about1.png")
                                                        screen.blit(about_image, (0, 0))
                                                        pygame.display.update()
                                    
                                                        
                                    # makes sure that if the user presses the 
                                    # left arrow, it will go back to the  
                                    # start menu
                                    elif mouse_pos[0] >= 20 and mouse_pos[0] <= 64:
                                        if mouse_pos[1] >= 453 and mouse_pos[1] <= 472:
                                            help_menu = False
                                
                                
                                # checks if the mouse is over a certain part of the image            
                                elif mouse_pos[0] >= 204 and mouse_pos[0] <= 470:
                                    
                                    # if the mouse is over the controls it loads
                                    # the same image but with controls highlighted 
                                    if mouse_pos[1] >= 124 and mouse_pos[1] <= 180:
                                        
                                        help_menu_img = pygame.image.load("help3.png")
                                        screen.blit(help_menu_img, (0,0))
                                        pygame.display.update()
                                    
                                        
                                    # if the mouse is over the objective it loads
                                    # the same image but with objective highlighted     
                                    elif mouse_pos[1] >= 243 and mouse_pos[1] <= 294:
                                        
                                        help_menu_img = pygame.image.load("help4.png")
                                        screen.blit(help_menu_img, (0,0))
                                        pygame.display.update()
                                    
                                        
                                    # if the mouse is over the about it loads
                                    # the same image but with about highlighted    
                                    elif mouse_pos[1] >= 358 and mouse_pos[1] <= 410:
                                        
                                        help_menu_img = pygame.image.load("help5.png")
                                        screen.blit(help_menu_img, (0,0))
                                        pygame.display.update()
                                    
                                        
                                    # if the mouse leaves any of the buttons it loads
                                    # the same image but with no hightlighted parts   
                                    else:
                                        help_menu_img = pygame.image.load("help1.png")
                                        screen.blit(help_menu_img, (0,0))
                                        pygame.display.update()
                                
                                        
                                # if the mouse is over the left arrow it loads
                                # the same image but with the left arrow highlighted 
                                elif mouse_pos[0] >= 20 and mouse_pos[0] <= 64:
                                    if mouse_pos[1] >= 453 and mouse_pos[1] <= 472:
                                        help_menu_img = pygame.image.load("help2.png")
                                        screen.blit(help_menu_img, (0,0))
                                        pygame.display.update()
                                        
                                        
                                    # if the mouse leaves left arrow it loads
                                    # the same image but with no hightlighted parts
                                    else:
                                        help_menu_img = pygame.image.load("help1.png")
                                        screen.blit(help_menu_img, (0,0))
                                        pygame.display.update()
                        
                                        
                        # loads the original help image
                        else:
                            help_menu_img = pygame.image.load("help1.png")
                            screen.blit(help_menu_img, (0,0))
                            pygame.display.update()
                        
            
            
            # checks if the mouse is over a certain part of the image 
            if mouse_pos[0] >= 139 and mouse_pos[0] <= 522:
                
                # if the mouse is over the start button it loads
                # the same image but with the start button highlighted
                if mouse_pos[1] >= 177 and mouse_pos[1] <= 219:
                        
                    start_menu = pygame.image.load("Tron3.png")
        
                    screen.blit(start_menu, (0,0))
                    pygame.display.update()

                    
                # if the mouse is over the help button it loads
                # the same image but with the help button highlighted
                elif mouse_pos[1] >= 235 and mouse_pos[1] <= 277:
                    start_menu = pygame.image.load("Tron4.png")
        
                    screen.blit(start_menu, (0,0))
                    pygame.display.update()
                    
                    
                # it loads the original start menu without any buttons highlighted
                else:
                    start_menu = pygame.image.load("Tron2.png")
        
                    screen.blit(start_menu, (0,0))
                    pygame.display.update()
                
                    
            # it loads the original start menu without any buttons highlighted        
            else:
                start_menu = pygame.image.load("Tron2.png")
        
                screen.blit(start_menu, (0,0))
                pygame.display.update()
    
    
    # game elements begin            
    background_music.set_volume(0.5)
    background_music.play(-1)
        
    background = pygame.Surface(WINDOW_SIZE).convert()
    background.fill((0,0,255))
    screen.blit(background, (0,0))
    
    background2 = pygame.Surface(GAME_SIZE).convert()
    background2.fill((125, 125, 125))
    screen.blit(background2, (0,0))
    
    p1_free_crash = False
    p2_free_crash = False
    reset = False
    
    x = MOVEMENT_STEP
    y = 0
    
    x2 = - MOVEMENT_STEP
    y2 = 0
    
    p1_score = 0
    p2_score = 0
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(Player(), Player2(), Obstacles(), Obstacles(), Obstacles())
    
    tail_sprites = pygame.sprite.OrderedUpdates()
    tail_sprites2 = pygame.sprite.OrderedUpdates()
    
    tail_sprites.add(Tail())
    tail_sprites2.add(Tail2())
    tail_len = 1
    
    power_sprite = pygame.sprite.Group()
    
    clock = pygame.time.Clock()
        
    direction = "right"
    direction2 = "left"
    
    # scoreboard
    font = pygame.font.SysFont("Courier New", 36)
    
    message = "Player 1: %i - %i :Player 2" %(p1_score, p2_score)
    rendered_text = font.render(message, True, ((255, 255, 255)))
            
    rendered_text_rect = rendered_text.get_rect()
    rendered_text_rect.centerx = screen.get_rect().centerx
    rendered_text_rect.centery = WINDOW_SIZE[1] - ((WINDOW_SIZE[1] - GAME_SIZE[1])/2)
            
    screen.blit(rendered_text, rendered_text_rect)    
    
    
    # main game loop
    while keep_going:
        
        
        # has two functions, one to start the next round and one to start a new
        # game depending on what keyboard event happens before this code executed
        if game_play == False:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                        keep_going = False
                    
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_RETURN:
                        game_play = True
                            
                        screen = pygame.display.set_mode(WINDOW_SIZE)
                            
                        background = pygame.Surface(WINDOW_SIZE).convert()
                        background.fill((0,0,255))
                        screen.blit(background, (0,0))
                            
                        background2 = pygame.Surface(GAME_SIZE).convert()
                        background2.fill((125, 125, 125))
                        screen.blit(background2, (0,0))
                            
                        x = MOVEMENT_STEP
                        y = 0

                        x2 = - MOVEMENT_STEP 
                        y2 = 0
                                                                              
                        all_sprites = pygame.sprite.Group()
                        all_sprites.add(Player(), Player2(), Obstacles(), Obstacles(), Obstacles())

                        tail_sprites = pygame.sprite.OrderedUpdates()
                        tail_sprites2 = pygame.sprite.OrderedUpdates()

                        tail_sprites.add(Tail())
                        tail_sprites2.add(Tail2())
                        tail_len = 1
                        
                        power_sprite = pygame.sprite.Group()
                        
                        if p1_free_crash:
                            p1_free_crash = True
                        
                        if p2_free_crash:
                            p2_free_crash = True
                        
                        if p1_free_crash == False and p2_free_crash == False:
                            p2_free_crash = False
                            p1_free_crash = False

                        clock = pygame.time.Clock()
    
                        direction = "right"
                        direction2 = "left"
                        
                        screen.blit(rendered_text, rendered_text_rect)

        
        # countdown to the start of the game
        if game_play:
            countdown_list = ["3", "2", "1", "Go!"]
            
            for countdown in countdown_list:
                countdown = font.render(countdown, True, ((255, 255, 255)))        
            
                countdown_rect = countdown.get_rect()
                countdown_rect.centerx = background2.get_rect().centerx
                countdown_rect.centery = background2.get_rect().centery
            
                screen.blit(countdown, countdown_rect)
                pygame.display.update()
            
                pygame.time.wait(1000)
            
                screen.blit(background2, (0,0))
                pygame.display.update()
            
                   
        # the loop that plays the actual game
        while game_play == True and p1_score < 3 and p2_score < 3:
            clock.tick(20)

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    keep_going = False
                
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_UP and direction != "down":                    
                        y = - MOVEMENT_STEP
                        x = 0
                        direction = "up"
                    
                    elif ev.key == pygame.K_DOWN and direction != "up":
                        y = MOVEMENT_STEP
                        x = 0
                        direction = "down"
                    
                    elif ev.key == pygame.K_RIGHT and direction != "left":
                        y = 0
                        x = MOVEMENT_STEP
                        direction = "right"
                        
                    elif ev.key == pygame.K_LEFT  and direction != "right":
                        y = 0
                        x = - MOVEMENT_STEP
                        direction = "left"    
                    
                    elif ev.key == pygame.K_a and direction2 != "right":
                        y2 = 0
                        x2 = - MOVEMENT_STEP
                        direction2 = "left"
                    
                    elif ev.key == pygame.K_d and direction2 != "left":
                        y2 = 0
                        x2 = MOVEMENT_STEP
                        direction2 = "right"
                    
                    elif ev.key == pygame.K_w and direction2 != "down":                    
                        y2 = - MOVEMENT_STEP
                        x2 = 0
                        direction2 = "up"
                    
                    elif ev.key == pygame.K_s and direction2 != "up":
                        y2 = MOVEMENT_STEP
                        x2 = 0
                        direction2 = "down"
                
            all_sprites.clear(screen, background2)        
            tail_sprites.clear(screen, background2)
            tail_sprites2.clear(screen, background2)
            
            tail_sprites.sprites()[-1].update(all_sprites.sprites()[0].rect.left, all_sprites.sprites()[0].rect.top)
            tail_sprites2.sprites()[-1].update(all_sprites.sprites()[1].rect.left, all_sprites.sprites()[1].rect.top)
            
            all_sprites.sprites()[0].update(x, y)
            all_sprites.sprites()[1].update(x2, y2)
    
            tail_sprites.draw(screen)
            tail_sprites2.draw(screen)
            all_sprites.draw(screen)
            
            tail_sprites.add(Tail())
            tail_sprites2.add(Tail2())
            tail_len += 1
            
                       
            # power up created as a sprite and then drawn to screen at random
            # intervals and random places
            if p1_free_crash == False and p2_free_crash == False:
                random_tail_len = random.randint(10, 30)
                
                if tail_len == random_tail_len and len(power_sprite.sprites()) <= 1:
                    power_sprite.clear(screen, background2)
                    power_sprite = pygame.sprite.Group()
                    power_sprite.add(Power())
                    
                    if len(power_sprite.sprites()) == 1:
                        
                        power_sprite.draw(screen)
                        
                        
                        # checks if the power up is inside any of the barriers
                        # if it is then the sprite is killed and remade and drawn
                        # to screen
                        if pygame.sprite.collide_rect(all_sprites.sprites()[2], power_sprite.sprites()[0]):
                            power_sprite.clear(screen, background2)
                            power_sprite = pygame.sprite.Group()
                            power_sprite.add(Power())
                            power_sprite.draw(screen)
                        
                        if pygame.sprite.collide_rect(all_sprites.sprites()[3], power_sprite.sprites()[0]):
                            power_sprite.clear(screen, background2)
                            power_sprite = pygame.sprite.Group()
                            power_sprite.add(Power())
                            power_sprite.draw(screen)
                            
                        if pygame.sprite.collide_rect(all_sprites.sprites()[4], power_sprite.sprites()[0]):
                            power_sprite.clear(screen, background2)
                            power_sprite = pygame.sprite.Group()
                            power_sprite.add(Power())
                            power_sprite.draw(screen)
            
                            
            # checks if the players collide with the power up if they do it
            # disappears and that player receives the power up of a free crash
            if pygame.sprite.spritecollide(all_sprites.sprites()[0], power_sprite, False):
                p1_free_crash = True
                power_sprite.clear(screen, background2)
                power_sprite.empty()
                tail_len = 1
                
            if pygame.sprite.spritecollide(all_sprites.sprites()[1],power_sprite, False):
                p2_free_crash = True
                power_sprite.clear(screen, background2)
                power_sprite.empty()
                tail_len = 1
                
    
                
            # COLLISIONS
            if pygame.sprite.spritecollide(all_sprites.sprites()[0],tail_sprites, False):
                if p1_free_crash == False:
                    p2_score += 1
                    crash.play()
    
                game_play = p1_free_crash
                p1_free_crash = False
     
         
            elif pygame.sprite.spritecollide(all_sprites.sprites()[0],tail_sprites2, False):
                if p1_free_crash == False:
                    p2_score += 1
                    crash.play()
                                 
                game_play = p1_free_crash
                p1_free_crash = False
    
                    
            elif pygame.sprite.collide_rect(all_sprites.sprites()[0], all_sprites.sprites()[1]):
                crash.play()
    
                game_play = False

    
                    
            elif pygame.sprite.collide_rect(all_sprites.sprites()[0], all_sprites.sprites()[2]):
                if p1_free_crash == False:
                    p2_score += 1
                    crash.play()
    
                game_play = p1_free_crash
                p1_free_crash = False
                    
                 
                    
            elif pygame.sprite.collide_rect(all_sprites.sprites()[0], all_sprites.sprites()[3]):
                if p1_free_crash == False:
                    p2_score += 1
                    crash.play()
    
                game_play = p1_free_crash
                p1_free_crash = False
                 
                    
            elif pygame.sprite.collide_rect(all_sprites.sprites()[0], all_sprites.sprites()[4]):
                if p1_free_crash == False:
                    p2_score += 1
                    crash.play()
                
                game_play = p1_free_crash
                p1_free_crash = False
                                             
              
            if pygame.sprite.spritecollide(all_sprites.sprites()[1],tail_sprites, False):
                if p2_free_crash == False:
                    p1_score += 1
                    crash.play()

                game_play = p2_free_crash
                p2_free_crash = False
                 
                    
            elif pygame.sprite.spritecollide(all_sprites.sprites()[1],tail_sprites2, False):
                if p2_free_crash == False:
                    p1_score += 1
                    crash.play()
    
                game_play = p2_free_crash
                p2_free_crash = False
                 
                     
            elif pygame.sprite.collide_rect(all_sprites.sprites()[1], all_sprites.sprites()[2]):
                if p2_free_crash == False:
                    p1_score += 1
                    crash.play()
                
    
                game_play = p2_free_crash
                p2_free_crash = False
    
                                    
            elif pygame.sprite.collide_rect(all_sprites.sprites()[1], all_sprites.sprites()[3]):
                if p2_free_crash == False:
                    p1_score += 1
                    crash.play()
    
                game_play = p2_free_crash
                p2_free_crash = False
                     
                                    
            elif pygame.sprite.collide_rect(all_sprites.sprites()[1], all_sprites.sprites()[4]):
                if p2_free_crash == False:
                    p1_score += 1
                    crash.play()
    
                game_play = p2_free_crash
                p2_free_crash = False
            
             
            # constructs the scoreboard with an * beside the player with the power up  
            if p1_free_crash:
                message = "*Player 1: %i - %i :Player 2" %(p1_score, p2_score)
            
            if p2_free_crash:
                message = "Player 1: %i - %i :Player 2*" %(p1_score, p2_score)
            
                
            # constructs the score board for both players without the power up   
            if p1_free_crash == False and p2_free_crash == False:
                message = "Player 1: %i - %i :Player 2" %(p1_score, p2_score)
            
                
            # displays the appropriate scoreboard
            rendered_text = font.render(message, True, ((255, 255, 255)))
            
            screen.blit(background, (0, WINDOW_SIZE[1]*0.9))
            screen.blit(rendered_text, rendered_text_rect)

            pygame.display.update() 
            
          
            
        # after one of the players eaches a score of 3, it displays the appropriate
        # winner to the center of the screen, it is also the score rest condition
        # if the appropriate button is pressed
        else:
                
            if p1_score > p2_score and p1_score == 3:
                message = "PLAYER 1 WINS"
            
            elif p2_score > p1_score and p2_score == 3:
                message = "PLAYER 2 WINS"
            
            if message.__contains__("WINS"):
                font = pygame.font.SysFont("Verdana", 72)
                rendered_text = font.render(message, True, ((255, 255, 255)))
                
                rendered_text_rect = rendered_text.get_rect()
                rendered_text_rect.centerx = screen.get_rect().centerx
                rendered_text_rect.centery = screen.get_rect().centery
                
                screen.blit(rendered_text, rendered_text_rect)
                pygame.display.update()
            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    keep_going = False
                
                elif ev.type == pygame.KEYDOWN:
                    
                    # resets the scores to 0
                    if ev.key == pygame.K_SPACE:                        
                        
                        reset = True
                        game_play = False
                        
                        p1_score = 0
                        p2_score = 0
                            
                        reset = False
                            
                        font = pygame.font.SysFont("Courier New", 36)
                            
                        message = "Player 1: %i - %i :Player 2" %(p1_score, p2_score)
                        rendered_text = font.render(message, True, ((255, 255, 255)))
                            
                        rendered_text_rect = rendered_text.get_rect()
                        rendered_text_rect.centerx = screen.get_rect().centerx
                        rendered_text_rect.centery = WINDOW_SIZE[1] - ((WINDOW_SIZE[1] - GAME_SIZE[1])/2)
