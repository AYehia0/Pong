import pygame
import sys


# Every pygame must have init()
pygame.init()

screen_width, screen_height = 900, 600
mid_pos_x, mid_pos_y = screen_width //2 , screen_height//2     # Not in the middle but close ,as shapes are rects 
clk = pygame.time.Clock()
fps = 60 
screen = pygame.display.set_mode((screen_width, screen_height))

# Setting the caption aka title 
pygame.display.set_caption('GamePong')

# char basic dims
ball_width, ball_height = 20,20
players_width, players_height = 10, 100
margin = 15

# Game char rects
ball = pygame.Rect(mid_pos_x-ball_width//2, mid_pos_y-ball_height//2, ball_width, ball_height)
player_right = pygame.Rect(screen_width-margin , screen_height-players_height//2 ,players_width, players_height)
player_left = pygame.Rect(margin , screen_height-players_height//2 ,players_width, players_height)

# Main loop
while True:
    # checking for events 
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # updating vars
    pygame.display.flip()
    clk.tick(fps)