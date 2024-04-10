import pygame
import sys
import datetime
from math import radians, sin, cos

pygame.init()

clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 800
CENTER = (WIDTH // 2, HEIGHT // 2)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

#Tut prosto pictures
#hand_image = pygame.image.load('mickey_hand.png').convert_alpha()

#Backgound
background_image = pygame.image.load('mickeyclock.png').convert()
background_rect = background_image.get_rect(center=(WIDTH / 2, HEIGHT / 2))

#Eto esli netu pictures
HOUR_HAND_LENGTH = WIDTH // 4
MINUTE_HAND_LENGTH = WIDTH // 3
SECOND_HAND_LENGTH = WIDTH // 2.5
HAND_WIDTH = 6

#etot code dlya togo esli est pictures
"""
def draw_hand(image, angle, scale, offset):
    new_width = int(image.get_width() * scale)
    new_height = int(image.get_height() * scale) 
    scaled_image = pygame.transform.scale(image, (new_width, new_height))

    rotated_image = pygame.transform.rotate(scaled_image, angle)
    new_rect = rotated_image.get_rect(center=CENTER + offset)
    SCREEN.blit(rotated_image, new_rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(background_image, background_rect.topleft)

    now = datetime.datetime.now()
    minute_angle = (now.minute / 60) * 360
    second_angle = (now.second / 60) * 360
    hour_angle = ((now.hour % 12) / 12) * 360 + (now.minute / 60) * 30 

    draw_hand(hand_image, -minute_angle, 0.35, pygame.math.Vector2(0, 0))  
    draw_hand(hand_image, -second_angle, 0.4, pygame.math.Vector2(0, 0)) 
    draw_hand(hand_image, -hour_angle, 0.3, pygame.math.Vector2(0, 0)) 

    pygame.display.flip()
    clock.tick(30)  
"""

#etot code esli netu pictures
def draw_hand(angle, length, color):
    angle_rad = radians(angle)
    end_pos = (CENTER[0] + length * sin(angle_rad), CENTER[1] - length * cos(angle_rad))
    pygame.draw.line(SCREEN, color, CENTER, end_pos, HAND_WIDTH)

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

    SCREEN.blit(background_image, background_rect.topleft)

    # Draw the hands as lines
    draw_hand(hour_angle, HOUR_HAND_LENGTH, (255, 0, 0))  #krasny hour hand
    draw_hand(minute_angle, MINUTE_HAND_LENGTH, (0, 255, 0))  #zeleny minute hand
    draw_hand(second_angle, SECOND_HAND_LENGTH, (0, 0, 255))  #sini second hand

    pygame.display.flip()
    clock.tick(60)
