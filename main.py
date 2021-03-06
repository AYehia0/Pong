import pygame
import sys
import random

def draw():
    #drawing 
    screen.fill(bg_col)
    pygame.draw.rect(screen, white_col, player_left) # surface , color , object to draw
    pygame.draw.rect(screen, white_col, player_right) # surface , color , object to draw
    pygame.draw.ellipse(screen, white_col, ball)
    pygame.draw.line(screen, white_col, (mid_pos_x,0), (mid_pos_x, screen_height))

def draw_text(surf, text, size, x, y, w_color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, w_color )
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def move_ball(ball, ball_speed_x, ball_speed_y):
    """Moving the ball"""
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # checking for bouncing ball
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    # checking collssion : collidrect is the simplest
    if ball.colliderect(player_right) or ball.colliderect(player_left):
        ball_speed_x *= -1
        # reversing the y axis makes the ball goes the opp side 45 deg 
        #ball_speed_y *= -1
    return ball, ball_speed_x, ball_speed_y

def check_player_bound(player):
    """ Check for the walls to bounce the ball"""

    # checking boundries
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if player.top <= 0:
        player.top = 0
    
    return player

def move_player(player, player_speed):
    """ Moving the player """
    player.y += player_speed

    #checking boundaries
    player = check_player_bound(player)

    return player

def move_opponent(player, player_speed, ball):
    """Moving an opponent"""
    if player.bottom > ball.y:
        player.bottom -= player_speed
    if player.top < ball.y:
        player.top += player_speed

    #checking boundaries
    player = check_player_bound(player)

    return player

def game_over(ball, ball_speed_x, ball_speed_y):
    """ Resets the ball after a win """
    ball.center = (screen_width//2, screen_height//2) 
    ball_speed_x *= random.choice([-1,1])
    ball_speed_y *= random.choice([-1,1])

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
font_name = pygame.font.match_font('arial')
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

# player speed 
p_speed = 0
o_speed = 6


# Scores 
p_score = 0
o_score = 0

# Main loop
while True:

    # checking for events 
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p_speed -= 9
            if event.key == pygame.K_DOWN:
                p_speed += 9

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                p_speed += 9
            if event.key == pygame.K_DOWN:
                p_speed -= 9

  
    if ball.left <= 0:
        o_score += 1
        game_over(ball, ball_speed_x, ball_speed_y)
    if ball.right >= screen_width:
        p_score += 1
        game_over(ball, ball_speed_x, ball_speed_y)

    print(f"Score:  {p_score},{o_score}")
    # Moving the ball, and updating 
    ball, ball_speed_x, ball_speed_y = move_ball(ball, ball_speed_x, ball_speed_y)
    player_left = move_player(player_left, p_speed)
    player_right = move_opponent(player_right, o_speed, ball)
    
    #drawing 
    draw()
    draw_text(screen,f"{p_score}:{o_score}", 50, screen_width//2 , 20, white_col)
    # updating vars
    pygame.display.flip()
    clk.tick(fps)