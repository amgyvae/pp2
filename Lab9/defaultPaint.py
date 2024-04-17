import pygame

pygame.init()

screen_width, screen_height = 1600, 1200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Paint")

colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0)
}
current_color = colors['black']

drawing = False
last_pos = None
mode = 'draw'

screen.fill(colors['white'])
pygame.display.update()

def draw_line(screen, start_pos, end_pos, color, width=5):
    pygame.draw.line(screen, color, start_pos, end_pos, width)

def draw_rect(screen, start_pos, end_pos, color):
    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
    pygame.draw.rect(screen, color, rect, 5)

def draw_circle(screen, start_pos, end_pos, color):
    center = start_pos
    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
    pygame.draw.circle(screen, color, center, radius, 5)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode in ['rectangle', 'circle']:
                end_pos = event.pos
                if mode == 'rectangle':
                    draw_rect(screen, start_pos, end_pos, current_color)
                elif mode == 'circle':
                    draw_circle(screen, start_pos, end_pos, current_color)
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == 'draw':
                mouse_position = pygame.mouse.get_pos()
                if last_pos is not None:
                    draw_line(screen, last_pos, mouse_position, current_color)
                last_pos = mouse_position
            elif mode == 'erase':
                mouse_position = pygame.mouse.get_pos()
                pygame.draw.circle(screen, colors['white'], mouse_position, 10)

        if event.type is pygame.KEYDOWN:
            if event.key is pygame.K_c:
                screen.fill(colors['white'])
            elif event.key is pygame.K_r:
                current_color = colors['red']
            elif event.key is pygame.K_b:
                current_color = colors['blue']
            elif event.key is pygame.K_y:
                current_color = colors['yellow']
            elif event.key is pygame.K_k:
                current_color = colors['black']
            elif event.key is pygame.K_e:
                mode = 'erase'
            elif event.key is pygame.K_d:
                mode = 'draw'
            elif event.key is pygame.K_s:
                mode = 'rectangle'
            elif event.key is pygame.K_o:
                mode = 'circle'

    pygame.display.update()
