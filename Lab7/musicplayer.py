import pygame
import sys

pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("GUI Music Player")

background_color = (30, 30, 30)
button_color = (70, 130, 180)
text_color = (255, 255, 255)

font = pygame.font.Font(None, 36)

tracks = ['Kawtar - Ya Lalali (Sped Up).mp3', 'kalp kiriklari ( slowed  reverb).mp3']
current_track = 0

button_width, button_height = 150, 40
play_rect = pygame.Rect((screen_width // 2 - button_width // 2, 100), (button_width, button_height))
stop_rect = pygame.Rect((screen_width // 2 - button_width // 2, 150), (button_width, button_height))
next_rect = pygame.Rect((screen_width // 2 - button_width // 2, 200), (button_width, button_height))
prev_rect = pygame.Rect((screen_width // 2 - button_width // 2, 250), (button_width, button_height))


def play_music(track_number):
    pygame.mixer.music.load(tracks[track_number])
    pygame.mixer.music.play()

done = False
while not done:
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                pygame.mixer.music.pause()
            elif event.key == pygame.K_q:
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(1)
            elif event.key == pygame.K_e:
                current_track = (current_track + 1) % len(tracks)
                play_music(current_track)
            elif event.key == pygame.K_r:
                current_track = (current_track - 1) % len(tracks)
                play_music(current_track)

    pygame.display.flip()

pygame.quit()
