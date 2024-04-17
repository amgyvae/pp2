import pygame
import random

pygame.init()

display_width = 900
display_height = 400

screen = pygame.display.set_mode((display_width, display_height))
icon = pygame.image.load("icons/icons8-game-16.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Snake")

done = False

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
background = white

x = 50
y = 50

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [display_width / 9, display_height / 4])

def show_score(number):
    score = font_style.render("Your score: " + str(number), True, black)
    screen.blit(score, [0, 0])

def gameSnake():

    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    lenght_of_snake = 1

    food_width = random.randint(5, 15)
    food_height = random.randint(5, 15)
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
    food_time_limit = 5000
    last_food_time = pygame.time.get_ticks()


    while not game_over:

        while game_close:
            screen.fill(white)
            message("Looser, r - repeat, c - close", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameSnake()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
          
        x1 += x1_change
        y1 += y1_change
        screen.fill(green)

        if pygame.time.get_ticks() - last_food_time > food_time_limit:
            foodx = round(random.randrange(0, display_width - food_width) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - food_height) / 10.0) * 10.0
            food_width = random.randint(5, 15)
            food_height = random.randint(5, 15)
            last_food_time = pygame.time.get_ticks()
      
        pygame.draw.rect(screen, red, [foodx, foody, food_width, food_height])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > lenght_of_snake:
            del snake_List[0]

        our_snake(snake_block, snake_List)
        show_score(lenght_of_snake - 1)

        if x1 >= foodx and x1 <= foodx + food_width and y1 >= foody and y1 <= foody + food_height:
            foodx = round(random.randrange(0, display_width - food_width) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - food_height) / 10.0) * 10.0
            food_width = random.randint(5, 15)
            food_height = random.randint(5, 15)
            lenght_of_snake += 1
            last_food_time = pygame.time.get_ticks()

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameSnake()

'''
        time on lecture
        
        pygame.display.update()
        screen.fill((0, 0, 0))
        #pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                background = blue
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                x += 10
                #background = green
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                x -= 10
                # background = green
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                y += 10
                # background = green
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                y -= 10
                # background = green

        pygame.draw.rect(screen, background, pygame.Rect(x, y, 50, 50))
        pygame.display.update()
        screen.fill((0, 0, 0))
        #pygame.draw.circle(screen, background, (100, 100), 30)
        

    print("Finished")
'''

