import random
import pygame
import Dijkstra_Algorithim


WINDOW_SIZE = (608, 750)
GAME_SIZE = (608, 672)
MOVEMENT_STEP = 32
SCARED_TIME = 40

    
pygame.font.init()

node_coordinates = Dijkstra_Algorithim.node_coordinates()

rev_node_coordinates = Dijkstra_Algorithim.rev_node_coordinates()





class Pacman(pygame.sprite.Sprite):
    '''Pacman starts in the middle of the screen automatically going to the left
    of the screen and uses the arrow keys'''
    
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()        
        self.rect.left = 288
        self.rect.top = 416
        self.direction = 'right'
        self.home_target= '35'
    
    
    def set_target(self, sprite):
        '''
        P.set_target(self, sprite_group) --> None
        Sets the target for the Ghosts as well as it will refresh the ghosts
        path to the new target.
        '''
        
        sprite.set_target(self.generate_target())
        sprite.set_refresh_path()
    
        
    def get_home_target(self):
        '''
        P.get_home_target(self) --> str
        Returns the home target for the ghosts.
        '''
        
        return self.home_target
    
    
    def set_home_target(self, sprite):
        '''
        P.set_home_target(self, sprite_group) --> None
        Sets the home target for the ghosts to go to after they have been eaten
        by Pacman
        '''
        
        sprite.set_target(self.get_home_target())
        
        
    def update(self, x, y, image):
        '''P.update(x, y, image) --> None
        Player 1's update method which takes the x-cordinate movement, 
        y-cordinate movement as well as the new image. It will moves the player 
        by x, y movements.'''
        
        if x > 0:
            self.direction = 'right'
        
        elif x < 0:
            self.direction = 'left'
            
        if y > 0:
            self.direction = 'down'
        
        elif y < 0:
            self.direction = 'up'
        
        self.rect.left += x
        self.rect.top += y     
            
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey(self.image.get_at((0,0)))
    
    
    def get_position(self):
        '''
        P.get_position(self) --> tuple
        Returns the tuple for Pacman's center x and y values
        '''
        
        node_x = (self.rect.centerx / MOVEMENT_STEP) + 1
        node_y = (self.rect.centery / MOVEMENT_STEP) + 1
        return (node_x, node_y)
    

    def get_node(self):
        '''
        P.get_node(self) --> str
        Returns the node of Pacman. If Pacman is in between two nodes, it will 
        return the node Pacman is moving towards.
        '''
        
        coordinates = self.get_position()
        node_x = coordinates[0]
        node_y = coordinates[1]
        node = ''
        
        if rev_node_coordinates.has_key(coordinates):    # gets the node Pacman is on
            node = rev_node_coordinates[coordinates]
            
        else:
            # if Pacman is in between two nodes, it wil get the closest one in the
            # direction Pacman is moving.
            
            
            # going right
            if self.direction == 'right':
                nearest = 10000
                
                for co in rev_node_coordinates:
                    if co[1] == node_y and co[0] > node_x:
                        if nearest > co[0]:
                            nearest = co[0]
                            
                node = rev_node_coordinates[(nearest, node_y)]
             
             
             #going left   
            elif self.direction == 'left':
                nearest = -1
                
                for co in rev_node_coordinates:
                    if co[1] == node_y and co[0] < node_x:
                        if nearest < co[0]:
                            nearest = co[0]
                            
                node = rev_node_coordinates[(nearest, node_y)]

            
            # going down    
            elif self.direction == 'down':
                nearest = 10000
                
                for co in rev_node_coordinates:
                    if co[0] == node_x and co[1] > node_y:
                        if nearest > co[1]:
                            nearest = co[1]
                            
                node = rev_node_coordinates[(node_x, nearest)]
            
                
            #going up   
            elif self.direction == 'up':
                nearest = -1
                
                for co in rev_node_coordinates:
                    if co[0] == node_x and co[1] < node_y:
                        if nearest < co[1]:
                            nearest = co[1]
                            
                node = rev_node_coordinates[(node_x, nearest)]     
     
        return node

    
    def generate_target(self):
        '''
        P.genereate_target(self) --> str
        Returns the target that is farthest from itself.
        '''
        
        my_node = self.get_node()

        target = Dijkstra_Algorithim.dijkstra(Dijkstra_Algorithim.graph(), my_node, my_node, False)
        return target




          
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




 
class Ghosts(pygame.sprite.Sprite):
    '''
    Creates the random generated ghost walk
    '''
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/original/blue_ghost - right.png').convert()
        self.image.set_colorkey(self.image.get_at((0,0)))
        
        self.rect = self.image.get_rect()        
        self.rect.left = x
        self.rect.top = y
        
        self.refresh_path = False
        self.path = []
        self.direction = ''
        
        self.target = ''
    
        
    def set_refresh_path(self):
        '''
        G.set_refresh_path(self) --> None
        Sets the refresh_path variable to True
        '''
        
        self.refresh_path = True
     
        
    def set_image(self, image):
        '''
        G.set_image(self, image) --> None
        Sets a new image for the ghost.
        '''
        
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey(self.image.get_at((0,0)))
        
    
    def update(self, scared):
        '''G.update() --> None
        Ghosts random update method. If Pacman has not given the ghost a new target
        the ghost will pick a target at random and move towards it.
        '''
        
        if scared:
            self.set_image("images/original/scared_ghost.png")
        
        
        # assigns a new path using dijkstra algorithim
        if  len(self.path) == 0 or self.refresh_path:
            self.refresh_path = False
            
            target_node = self.get_target()
            
            if len(target_node) == 0:
                
                target_node = self.get_random_node() # finds a random target node
        
                while self.get_node() == target_node:
                    target_node = self.get_random_node() # if the target node is equal to the node the ghosts in
                                                         # gets a new target node
            
            else:
                self.reset_target()  # resets the target node if the len is not zero
                
            self.path = Dijkstra_Algorithim.dijkstra(Dijkstra_Algorithim.graph(), self.get_node(), target_node)
        
        
        # gets the nodes where it needs to go    
        node_to_go = self.path[0]
        my_position = self.get_position()
        my_node = self.get_node()
        
        
        if node_coordinates[node_to_go] == my_position:
            self.path.remove(node_to_go)
        
        
        else:   
            # moves to the target area
            
            # moves right
            if node_coordinates[node_to_go][1] == my_position[1] and node_coordinates[node_to_go][0] > my_position[0]:
                self.rect.right += MOVEMENT_STEP
                self.direction = 'right'
                
                if scared == False:
                    self.set_image('images/original/blue_ghost - right.png')
                
            
            # moves left
            elif node_coordinates[node_to_go][1] == my_position[1]  and node_coordinates[node_to_go][0] < my_position[0] :
                self.rect.left += - MOVEMENT_STEP
                self.direction = 'left'
                
                if scared == False:
                    self.set_image('images/original/blue_ghost - left.png')
                
            # moves down
            if node_coordinates[node_to_go][0] == my_position[0]  and node_coordinates[node_to_go][1] > my_position[1]:
                self.rect.bottom += MOVEMENT_STEP
                self.direction = 'down'
                
                if scared == False:
                    self.set_image('images/original/blue_ghost - down.png')
            
            # moves up
            elif node_coordinates[node_to_go][0] == my_position[0]  and node_coordinates[node_to_go][1] < my_position[1]:
                self.rect.top += - MOVEMENT_STEP
                self.direction = 'up'
                
                if scared == False:
                    self.set_image('images/original/blue_ghost - up.png')
            
            
            #end of update
            
            
    def get_random_node(self):
        '''
        G.get_random_node(self) --> str
        Returns the a random node for a target.
        '''
        
        random_index = random.randint(1, len(node_coordinates))
        
        index = 0
        
        for random_node in node_coordinates:
            index += 1
            if index == random_index:
                break
        
        return random_node
     
    
    def get_position(self):
        '''
        G.get_position(self) --> tuple
        Returns the tuple for Ghost's center x and y values
        '''
         
        node_x = (self.rect.centerx / MOVEMENT_STEP) + 1
        node_y = (self.rect.centery / MOVEMENT_STEP) + 1
        return (node_x,node_y)
    
   
    def get_target(self):
        '''
        G.get_target(self) --> str
        Returns the target for the ghost
        '''
        
        return self.target
    
    
    def reset_target(self):
        '''
        G.reset_target(self) --> str
        Resets the target for the ghost of be empty
        '''
        self.target = ''
    
    
    def set_target(self, target):
        '''
        G.set_target(self, target) --> None
        Sets the new target for the ghost
        '''
        self.target = target
    
    
    def get_node(self):
        '''
        G.get_node(self) --> str
        Returns the node of Pacman. If Pacman is in between two nodes, it will 
        return the node Pacman is moving towards.
        '''
        
        coordinates = self.get_position()
        node_x = coordinates[0]
        node_y = coordinates[1]
        
        node = ''
        
        if rev_node_coordinates.has_key(coordinates): # gets the node the ghost is on
            node = rev_node_coordinates[coordinates]
            
        else:
            # if Pacman is in between two nodes, it wil get the closest one in the
            # direction Pacman is moving.
            
            
            # going right
            if self.direction == 'right':
                nearest = 10000
                
                for co in rev_node_coordinates:

                    if co[1] == node_y and co[0] > node_x:
                        if nearest > co[0]:
                            nearest = co[0]
                            
                node = rev_node_coordinates[(nearest, node_y)]
            
           
            # going left    
            elif self.direction == 'left':
                nearest = -1
                
                for co in rev_node_coordinates:

                    if co[1] == node_y and co[0] < node_x:
                        if nearest < co[0]:
                            nearest = co[0]
                            
                node = rev_node_coordinates[(nearest, node_y)]

            
            # going down
            elif self.direction == 'down':
                nearest = 10000
                
                for co in rev_node_coordinates:

                    if co[0] == node_x and co[1] > node_y:
                        if nearest > co[1]:
                            nearest = co[1]
                            
                node = rev_node_coordinates[(node_x, nearest)]
            
            
            # going up
            elif self.direction == 'up':
                nearest = -1
                
                for co in rev_node_coordinates:

                    if co[0] == node_x and co[1] < node_y:
                        if nearest < co[1]:
                            nearest = co[1]
                            
                node = rev_node_coordinates[(node_x, nearest)]    
        
        return node




 
class Ghosts2(Ghosts):
    '''
    Creates the ghost class that will always go after Pacman unless Pacman eats
    the big dots. However once Pacman eats the big dots and collides with the 
    Ghosts2, Ghosts2 will not return to the ghost house immediately. It will go 
    there after if has finished its original path.
    '''
    
    def __init__(self, x, y):
        
        Ghosts.__init__(self, x, y)
        self.image = pygame.image.load("images/original/red_ghost - right.png").convert()
        self.image.set_colorkey(self.image.get_at((0,0)))
        
        self.rect = self.image.get_rect()        
        self.rect.left = x
        self.rect.top = y
        
        self.refresh_path = True       
        self.counter = 0
        self.path = []
        
        self.direction = ''
    
    
        
    def update(self, sprite, scared):
        '''G2.update(sprite) --> None
        Ghosts update method. It will always go after Pacman in every scenario
        except when Pacman eats the big dots.
        '''
        
        self.counter += 1

        # assigns a new path using dijkstra algorithim
        if len(self.path) == 0 or (self.counter %2 == 0 and self.refresh_path):
            self.counter = 0
            self.refresh_path = True
             
            forced_target = self.get_target()      # gets a new 'forced' target
            
            if len(forced_target) == 0:
                pacman_node = sprite.get_node()
            
            else:
                pacman_node = forced_target
                self.reset_target()               # resets the target
                self.refresh_path = False
                
                
            self.path = Dijkstra_Algorithim.dijkstra(Dijkstra_Algorithim.graph(), self.get_node(), pacman_node)
        
        if scared:   
            self.set_image("images/original/scared_ghost.png")
        
        # gets the nodes to where it needs to go
        node_to_go = self.path[0]
        my_position = self.get_position()
        my_node = self.get_node()
        
        
        if node_coordinates[node_to_go] == my_position:
            self.path.remove(node_to_go)
        
        
        else:   
            
            # moves right
            if node_coordinates[node_to_go][1] == my_position[1] and node_coordinates[node_to_go][0] > my_position[0]:
                self.rect.right += MOVEMENT_STEP
                self.direction = 'right'
                if scared == False:
                    self.set_image("images/original/red_ghost - right.png")
                    
                
            # moves left
            elif node_coordinates[node_to_go][1] == my_position[1]  and node_coordinates[node_to_go][0] < my_position[0] :
                self.rect.left += - MOVEMENT_STEP
                self.direction = 'left'
                if scared == False:
                    self.set_image("images/original/red_ghost - left.png")
                
            
            # moves down
            if node_coordinates[node_to_go][0] == my_position[0]  and node_coordinates[node_to_go][1] > my_position[1]:
                self.rect.bottom += MOVEMENT_STEP
                self.direction = 'down'
                if scared == False:
                    self.set_image("images/original/red_ghost - down.png")
            
            
            # moves up
            elif node_coordinates[node_to_go][0] == my_position[0]  and node_coordinates[node_to_go][1] < my_position[1]:
                self.rect.top += - MOVEMENT_STEP
                self.direction = 'up'
                if scared == False:
                    self.set_image("images/original/red_ghost - up.png")
        

            
    # end of the update method
    
        

        
def main():
    '''
    main() --> int and bool
    Returns the score and the boolean value of the main game loop
    '''
    
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("JACMAN: Original - JETON SINOIMERI")
    
    background = pygame.image.load("images/original/Map.png").convert()
    
    
    x = MOVEMENT_STEP
    y = 0
    image = "images/original/pacman - right.png"


    score = 0
    lives = 3
    
    
    all_sprites = pygame.sprite.OrderedUpdates()
    points_sprites = pygame.sprite.OrderedUpdates()
    points_sprites2 = pygame.sprite.OrderedUpdates()
    
    
    all_sprites.add(Pacman(image), Ghosts(288, 288), Ghosts2(320, 288))
    
    # adds dots to the field
    for vert in range (0, GAME_SIZE[1] - MOVEMENT_STEP, MOVEMENT_STEP):
        for horiz in range(MOVEMENT_STEP, GAME_SIZE[0] - MOVEMENT_STEP, MOVEMENT_STEP):
            
            if background.get_at((horiz, vert)) == (0, 0, 0):
                
                if horiz == MOVEMENT_STEP and vert == 3 * MOVEMENT_STEP or horiz == GAME_SIZE[0] - 2 * MOVEMENT_STEP and vert == 3 * MOVEMENT_STEP or horiz == MOVEMENT_STEP and vert == GAME_SIZE[1] - 4 * MOVEMENT_STEP or horiz == GAME_SIZE[0] - 2 * MOVEMENT_STEP and vert == GAME_SIZE[1] - 4 * MOVEMENT_STEP:
                    points_sprites2.add(Points("images/original/big dot.png", horiz, vert))
                
                else:
                    points_sprites.add(Points("images/original/little dot.png", horiz, vert))
       
    
    direction = "right"
    
    clock = pygame.time.Clock()
    keep_going = True
    game_play = True
    
    
    # countdown to start of game
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
    
    message = "score: %i        lives: %i" %(score, lives)
    rendered_text = font.render(message, True, ((255, 255, 255)))
            
            
    screen.blit(rendered_text, (32, WINDOW_SIZE[1]*0.9))    
    
    eaten = False
    scared = False
    
    
    # main game loop
    while keep_going:
        counter = 0
        
        # reset the game
        if lives > 0 and game_play == False:
            
            game_play = True
            
            x = MOVEMENT_STEP
            y = 0
        
            image = "images/original/pacman - right.png"
    
            score = 0

            all_sprites = pygame.sprite.OrderedUpdates()
            points_sprites = pygame.sprite.OrderedUpdates()
            points_sprites2 = pygame.sprite.OrderedUpdates()
            
            all_sprites.add(Pacman(image), Ghosts(288, 288), Ghosts2(320, 288))
            
            for vert in range (0, GAME_SIZE[1] - MOVEMENT_STEP, MOVEMENT_STEP):
                for horiz in range(MOVEMENT_STEP, GAME_SIZE[0] - MOVEMENT_STEP, MOVEMENT_STEP):
                    
                    if background.get_at((horiz, vert)) == (0, 0, 0):
                        
                        if horiz == MOVEMENT_STEP and vert == 3 * MOVEMENT_STEP or horiz == GAME_SIZE[0] - 2 * MOVEMENT_STEP and vert == 3 * MOVEMENT_STEP or horiz == MOVEMENT_STEP and vert == GAME_SIZE[1] - 4 * MOVEMENT_STEP or horiz == GAME_SIZE[0] - 2 * MOVEMENT_STEP and vert == GAME_SIZE[1] - 4 * MOVEMENT_STEP:
                            
                            points_sprites2.add(Points("images/original/big dot.png", horiz, vert))
                        
                        else:
                            points_sprites.add(Points("images/original/little dot.png", horiz, vert))
               
            
            direction = "right"
            
            clock = pygame.time.Clock()

            
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
            
            message = "score: %i" %(score)
            rendered_text = font.render(message, True, ((255, 255, 255)))
                    
            screen.blit(pygame.Surface((608, 75)), (0, 675))         
            screen.blit(rendered_text, (32, WINDOW_SIZE[1]*0.9))    
            
            pygame.display.update()
            
            eaten = False
            scared = False
            
            
        # secondary game loop    
        while game_play == True and lives > 0:
        
            clock.tick(6)
                
            # event handling
            for ev in pygame.event.get():
                
                if ev.type == pygame.QUIT:
                    game_play = False
                    keep_going = False
                
                
                if ev.type == pygame.KEYDOWN:
                    
                    # up movement
                    if ev.key == pygame.K_UP and direction != "up":
                        
                        if background.get_at((all_sprites.sprites()[0].rect.midtop[0], all_sprites.sprites()[0].rect.midtop[1] - 1)) != (0, 0, 255) and background.get_at((all_sprites.sprites()[0].rect.midtop[0], all_sprites.sprites()[0].rect.midtop[1] - 1)) != (1, 1, 1):
                            
                            image = "images/original/pacman - up.png"
                            y = - MOVEMENT_STEP
                            x = 0
    
                    # down movement    
                    elif ev.key == pygame.K_DOWN and direction != "down":
                        
                        if background.get_at((all_sprites.sprites()[0].rect.midbottom[0], all_sprites.sprites()[0].rect.midbottom[1] + 1)) != (0, 0, 255) and background.get_at((all_sprites.sprites()[0].rect.midbottom[0], all_sprites.sprites()[0].rect.midbottom[1] + 1)) != (1, 1, 1):
                            
                            image = "images/original/pacman - down.png"    
                            y = MOVEMENT_STEP
                            x = 0
                            
                    # right movement    
                    elif ev.key == pygame.K_RIGHT and direction != "right":
                        
                        if all_sprites.sprites()[0].rect.midright[0] + 1 >= GAME_SIZE[0] or background.get_at((all_sprites.sprites()[0].rect.midright[0] + 1, all_sprites.sprites()[0].rect.midright[1])) != (0, 0, 255):
                            
                            image = "images/original/pacman - right.png"    
                            y = 0
                            x = MOVEMENT_STEP
                        
                    # left movement    
                    elif ev.key == pygame.K_LEFT and direction != "left":
                        
                        if all_sprites.sprites()[0].rect.midleft[0] - 1 <= 0 or background.get_at((all_sprites.sprites()[0].rect.midleft[0] - 1 , all_sprites.sprites()[0].rect.midleft[1])) != (0, 0, 255):
                            
                            image = "images/original/pacman - left.png"    
                            y = 0
                            x = - MOVEMENT_STEP
    
            
            
            # border controls
            
            if image == "images/original/pacman - right.png":
                if all_sprites.sprites()[0].rect.midright[0] + 1 >= GAME_SIZE[0]:
                    
                    all_sprites.sprites()[0].rect.right = 0
                    all_sprites.sprites()[0].rect.top = all_sprites.sprites()[0].rect.top
                
                else:
                    if background.get_at((all_sprites.sprites()[0].rect.midright[0] + 1, all_sprites.sprites()[0].rect.midright[1])) == (0, 0, 255):
                        
                        x = 0
                        y = 0
                
                direction = "right"
                
            
            elif image == "images/original/pacman - left.png":
                
                if all_sprites.sprites()[0].rect.midleft[0] - 1 <= 0:
                    
                    all_sprites.sprites()[0].rect.left = GAME_SIZE[0]
                    all_sprites.sprites()[0].rect.top = all_sprites.sprites()[0].rect.top
                
                else:
                    if background.get_at((all_sprites.sprites()[0].rect.midleft[0] - 1 , all_sprites.sprites()[0].rect.midleft[1])) == (0, 0, 255):
                        
                        x = 0
                        y = 0
                
                direction = "left"
            
            
            elif image == "images/original/pacman - down.png":
                
                if all_sprites.sprites()[0].rect.midbottom[0] + 1 >= GAME_SIZE[1]:
                    
                    x = 0
                    y = 0
                
                else:
                    if background.get_at((all_sprites.sprites()[0].rect.midbottom[0], all_sprites.sprites()[0].rect.midbottom[1] + 1)) == (0, 0, 255):
                       
                        x = 0
                        y = 0
                
                direction = "down"
    
            
            elif image == "images/original/pacman - up.png":
                if all_sprites.sprites()[0].rect.midtop[1] - 1 <= 0:
                    
                    x = 0
                    y = 0
                
                else:
                    if background.get_at((all_sprites.sprites()[0].rect.midtop[0], all_sprites.sprites()[0].rect.midtop[1] - 1)) == (0, 0, 255):
                       
                        x = 0
                        y = 0
                
                direction = "up"
        
            
            # sprite collide
            if pygame.sprite.spritecollide(all_sprites.sprites()[0], points_sprites, False):          
                score += 10
                points_sprites.remove(pygame.sprite.spritecollide(all_sprites.sprites()[0], points_sprites, False))
            
            elif pygame.sprite.spritecollide(all_sprites.sprites()[0], points_sprites2, False):          
                score += 30
                points_sprites2.remove(pygame.sprite.spritecollide(all_sprites.sprites()[0], points_sprites2, False))
                for i in range(1, len(all_sprites.sprites())):
                    all_sprites.sprites()[0].set_target(all_sprites.sprites()[i])
                
                eaten = True
                scared = True
                
            if eaten:
                counter += 1
            
            # after eating the big dots collision handling
            if counter > 0 and counter < SCARED_TIME:
                if pygame.sprite.collide_rect(all_sprites.sprites()[0], all_sprites.sprites()[1]):
                    all_sprites.sprites()[0].set_home_target((all_sprites.sprites()[1]))
                    score += 200
                        
                
                if pygame.sprite.collide_rect(all_sprites.sprites()[0], all_sprites.sprites()[2]):
                    all_sprites.sprites()[0].set_home_target((all_sprites.sprites()[2]))
                    score += 200
                    
            
            # resets the counter to 0, and the boolean values to False
            if counter == SCARED_TIME:
                counter = 0
                eaten = False
                scared = False
            

            # if there are no more dots left  
            if len(points_sprites.sprites()) == 0:
                game_play = False
             
            # drawing to screen     
            points_sprites.clear(screen, background)
            points_sprites.draw(screen)
           
            points_sprites2.clear(screen, background)
            points_sprites2.draw(screen)
            
            all_sprites.clear(screen, background)
            all_sprites.sprites()[0].update(x, y, image)

            all_sprites.sprites()[1].update(scared)
            all_sprites.sprites()[2].update(all_sprites.sprites()[0], scared)
            
            all_sprites.draw(screen)

            
            # collision after time has run out
            if scared == False and eaten == False:    
                if pygame.sprite.collide_rect(all_sprites.sprites()[0], all_sprites.sprites()[1]):
                    lives -= 1
                    game_play = False

                    
                if pygame.sprite.collide_rect(all_sprites.sprites()[0], all_sprites.sprites()[2]):
                    lives -= 1
                    game_play = False


            
            message = "score: %i        lives: %i" %(score, lives)
            rendered_text = font.render(message, True, ((255, 255, 255)))
            
            screen.blit(pygame.Surface((608, 75)), (0, 675))    
                
            screen.blit(rendered_text, (32, WINDOW_SIZE[1]*0.9))
            
            
            pygame.display.update()

        
        if game_play == False and lives == 0:
            
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
    