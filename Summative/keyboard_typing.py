import pygame

pygame.font.init()

WINDOW_SIZE = (700, 700)

def main():
    '''
    main() --> text and bool
    This fuction allows the user to type something and it will appear onto the 
    screen. The user can use any keys except the Enter/Return key unless they
    want to end the program.    
    '''
        
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("JACMAN - JETON SINOIMERI")
    
    background = pygame.image.load("images/menu/Textbox.png").convert()

    message = ""
    
    font = pygame.font.SysFont("Arial", 30)
    
    rendered_text = font.render(message, True, (0,0,0))
    
    clock = pygame.time.Clock()
    keep_going = True
    

    while keep_going:

        clock.tick(30)

        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                keepGoing = False
            
            elif ev.type == pygame.KEYDOWN:
                
                if ev.key == pygame.K_BACKSPACE and len(message) > 0:
                    message = message[:-1]
                
                
                elif ev.key != pygame.K_BACKSPACE and ev.key != pygame.K_RETURN and len(message) < 25:
                    message += ev.unicode
                
                
                elif ev.key == pygame.K_RETURN or len(message) == 25:
                    keep_going = False
                
                
                rendered_text = font.render(message, True, (0,0,0))
        
                
        rendered_rect = rendered_text.get_rect()
        rendered_rect.midleft = (232, 357)
        
        screen.blit(background, (0, 0))
        screen.blit(rendered_text, rendered_rect)
        
        pygame.display.update()
    
    
    return message, keep_going
    
    
if __name__ == "__main__":
    main()
