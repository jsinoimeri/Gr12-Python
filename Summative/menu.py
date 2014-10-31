import Jacman_original
import Jacman_timeTrial
import pygame

import keyboard_typing
import database
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.font.init()

WINDOW_SIZE = (700, 700)

data_base = database.Database()



def main():
    '''
    main() --> None
    Allows the user to interact with the two different modes through a menu.
    After the game has finished, another window will open up allowing the user
    to enter their name. Press Enter to submit the name. Highscores will then be
    displayed onto the screen.
    '''
    
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("JACMAN - JETON SINOIMERI")
        
    background = pygame.image.load("images/menu/menu.png").convert()
        
    screen.blit(background, (0,0))
    
    keep_going = True
    
    # main menu screen
    while keep_going:
        
        for ev in pygame.event.get():
            
            mouse_pos = pygame.mouse.get_pos()
            
            if ev.type == pygame.QUIT:
                keep_going = False
            
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[0] >= 208 and mouse_pos[0] <= 491:
                    
                    # the menu which allows the user to play
                    if mouse_pos[1] >= 430 and mouse_pos[1] <= 503:
                        
                        start = True
    
                        start_menu = pygame.image.load("images/menu/start_menu.png").convert()
                        screen.blit(start_menu, (0,0))
                        
                        pygame.display.update()
                        
                        while start:
                            for ev in pygame.event.get():
                                mouse_pos = pygame.mouse.get_pos()
                                
                                
                                if ev.type == pygame.QUIT:
                                    start = False
                                    keep_going = False
                                
                                
                                elif ev.type == pygame.MOUSEBUTTONDOWN:
                                    if mouse_pos[0] >= 208 and mouse_pos[0] <= 491:
                                        
                                        # play the original game
                                        if mouse_pos[1] >= 354 and mouse_pos[1] <= 427:
                                            game = Jacman_original.main()
                                            
                                            if game[1] == False:
                                                keyboard_input = keyboard_typing.main()
                                                
                                                if keyboard_input[1] == False:
                                                    start = False
                                                    data_base.insert("Original", keyboard_input[0], game[0])
                                            
                                            
                                            pygame.time.delay(2000)
                                            screen.blit(background, (0,0))

                                            
                                        # play the time trial game
                                        elif mouse_pos[1] >= 468 and mouse_pos[1] <= 540:
                                            
                                            game = Jacman_timeTrial.main()
                                            
                                            if game[1] == False:
                                                keyboard_input = keyboard_typing.main()
                                                
                                                if keyboard_input[1] == False:
                                                    start = False
                                                    data_base.insert("Original", keyboard_input[0], game[0])
                                            
                                            
                                            pygame.time.delay(2000)
                                            screen.blit(background, (0,0))
                                        
                                            
                                        # go back to the main menu
                                        elif mouse_pos[1] >= 576 and mouse_pos[1] <= 650:
                                            
                                            start = False
                                            background = pygame.image.load("images/menu/menu.png").convert()
        
                                            screen.blit(background, (0,0))
                    
                    
                    # quits the all game
                    elif mouse_pos[1] >= 544 and mouse_pos[1] <= 616:
                        keep_going = False
        
                        
        pygame.display.update()
               
             
if __name__ == "__main__":
    main()
