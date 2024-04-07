import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ball')

white = (255, 255, 255)
red = (255, 0, 0)

ball_radius = 25
ball_x, ball_y = screen_width // 2, screen_height // 2  
move_distance = 20 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - move_distance - ball_radius > 0:
                ball_y -= move_distance
            elif event.key == pygame.K_DOWN and ball_y + move_distance + ball_radius < screen_height:
                ball_y += move_distance
            elif event.key == pygame.K_LEFT and ball_x - move_distance - ball_radius > 0:
                ball_x -= move_distance
            elif event.key == pygame.K_RIGHT and ball_x + move_distance + ball_radius < screen_width:
                ball_x += move_distance

    screen.fill(white)

    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

pygame.quit()
sys.exit()

