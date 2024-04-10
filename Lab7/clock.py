import pygame
import datetime
from math import radians, sin, cos

pygame.init()

clock = pygame.time.Clock()
screen_width, screen_height = 800, 800
center_pic = (screen_width // 2, screen_height // 2)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Clock")

#Backgound
background_image = pygame.image.load('mickeyclock.png').convert()
background_rect = background_image.get_rect(center=(screen_width / 2, screen_height / 2))

#Eto esli netu pictures
hour_hand_lenght = screen_width // 4
minute_hand_lenght = screen_width // 3
second_hand_lenght= screen_width // 2.5
hand_width = 6

#etot code esli netu pictures
def draw_hand(angle, length, color):
    angle_rad = radians(angle)
    end_pos = (center_pic[0] + length * sin(angle_rad), center_pic[1] - length * cos(angle_rad))
    pygame.draw.line(screen, color, center_pic, end_pos, hand_width)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background_image, background_rect.topleft)

    now = datetime.datetime.now()
    minute_angle = (now.minute / 60) * 360
    second_angle = (now.second / 60) * 360
    hour_angle = ((now.hour % 12) / 12) * 360 + (now.minute / 60) * 30

    screen.blit(background_image, background_rect.topleft)

    # Draw the hands as lines
    draw_hand(hour_angle, hour_hand_lenght, (255, 0, 0))  #krasny hour hand
    draw_hand(minute_angle, minute_hand_lenght, (0, 255, 0))  #zeleny minute hand
    draw_hand(second_angle, second_hand_lenght, (0, 0, 255))  #sini second hand

    pygame.display.flip()
    clock.tick(60)
    

#Tut prosto pictures dlya strelok
#hand_image = pygame.image.load('mickey_hand.png').convert_alpha()

#etot code dlya togo esli est pictures
"""
def draw_hand(image, angle, scale, offset):
    new_width = int(image.get_width() * scale)
    new_height = int(image.get_height() * scale) 
    scaled_image = pygame.transform.scale(image, (new_width, new_height))

    rotated_image = pygame.transform.rotate(scaled_image, angle)
    new_rect = rotated_image.get_rect(center=CENTER + offset)
    screen.blit(rotated_image, new_rect.topleft)
    
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    SCREEN.blit(background_image, background_rect.topleft)

    now = datetime.datetime.now()
    minute_angle = (now.minute / 60) * 360
    second_angle = (now.second / 60) * 360
    hour_angle = ((now.hour % 12) / 12) * 360 + (now.minute / 60) * 30 

    draw_hand(hand_image, -minute_angle, 0.35, pygame.math.Vector2(0, 0))  
    draw_hand(hand_image, -second_angle, 0.4, pygame.math.Vector2(0, 0)) 
    draw_hand(hand_image, -hour_angle, 0.3, pygame.math.Vector2(0, 0)) 

    pygame.display.flip()
    clock.tick(60)  
"""
