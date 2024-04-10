import pygame

pygame.init()

screen_width, screen_height = 900, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Moving Ball')

ball_radius = 25

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
background = green

x = 50
y = 50

done = True

while done:
    pygame.display.update()
    screen.fill((230, 230, 230))
    # pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            background = blue
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            x += 10
            # background = green
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            x -= 10
            # background = green
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            y += 10
            # background = green
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            y -= 10
            # background = green

    #pygame.draw.rect(screen, background, pygame.Rect(x, y, 50, 50))
    pygame.draw.circle(screen, background, (x, y), ball_radius)
    pygame.display.update()
    # pygame.draw.circle(screen, background, (100, 100), 30)

print("Finished")

