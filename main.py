import pygame
import sys


# Every pygame must have init()
pygame.init()

# Screen dims
screen_width, screen_height = 900, 600
mid_pos_x, mid_pos_y = screen_width //2 , screen_height//2     # Not in the middle but close ,as shapes are rects 

# Colours 
bg_col = pygame.Color('grey12')
white_col = (255,255,255)

# Clock
clk = pygame.time.Clock()
fps = 60 

# Screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Setting the caption aka title 
pygame.display.set_caption('GamePong')

# char basic dims
ball_width, ball_height = 20,20
players_width, players_height = 10, 100
margin = 15

# Game char rects
ball = pygame.Rect(mid_pos_x-ball_width//2, mid_pos_y-ball_height//2, ball_width, ball_height)
player_right = pygame.Rect(screen_width-margin , screen_height//2 - players_height//2 ,players_width, players_height)
player_left = pygame.Rect(margin//2 ,screen_height//2 - players_height//2 ,players_width, players_height)

# ball speeds
ball_speed_x, ball_speed_y = 9,9

# Main loop
while True:
    # checking for events 
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    # Moving the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # checking for bouncing ball
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    #drawing 
    screen.fill(bg_col)
    pygame.draw.rect(screen, white_col, player_left) # surface , color , object to draw
    pygame.draw.rect(screen, white_col, player_right) # surface , color , object to draw
    pygame.draw.ellipse(screen, white_col, ball)
    pygame.draw.line(screen, white_col, (mid_pos_x,0), (mid_pos_x, screen_height))
    
    # updating vars
    pygame.display.flip()
    clk.tick(fps)