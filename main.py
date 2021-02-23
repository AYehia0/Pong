import pygame


# Every pygame must have init()
pygame.init()

screen_width, screen_height = 900, 600
clk = pygame.time.Clock()
fps = 60 
screen = pygame.display.set_mode((screen_width, screen_height))

# Setting the caption aka title 
pygame.display.set_caption('GamePong')


# Main loop
while True:
    # checking for events 
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()


    # updating vars
    pygame.display.flip()
    clk.tick(fps)