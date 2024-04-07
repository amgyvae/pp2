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

def draw_buttons():
    pygame.draw.rect(screen, button_color, play_rect)
    pygame.draw.rect(screen, button_color, stop_rect)
    pygame.draw.rect(screen, button_color, next_rect)
    pygame.draw.rect(screen, button_color, prev_rect)

    play_text = font.render("Play/Pause", True, text_color)
    screen.blit(play_text, play_rect.move(10, 5))

    stop_text = font.render("Stop", True, text_color)
    screen.blit(stop_text, stop_rect.move(50, 5))

    next_text = font.render("Next", True, text_color)
    screen.blit(next_text, next_rect.move(50, 5))

    prev_text = font.render("Previous", True, text_color)
    screen.blit(prev_text, prev_rect.move(30, 5))

running = True
while running:
    screen.fill(background_color)

    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif stop_rect.collidepoint(event.pos):
                pygame.mixer.music.stop()
            elif next_rect.collidepoint(event.pos):
                current_track = (current_track + 1) % len(tracks)
                play_music(current_track)
            elif prev_rect.collidepoint(event.pos):
                current_track = (current_track - 1) % len(tracks)
                play_music(current_track)

    pygame.display.flip()

pygame.quit()

