import pygame

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Paint Advanced")

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
command_width = 150 

screen.fill(colors['white'])
pygame.display.update()

font = pygame.font.Font(None, 24)

def draw_line(screen, start_pos, end_pos, color, width=5):
    pygame.draw.line(screen, color, start_pos, end_pos, width)

def draw_rect(screen, start_pos, end_pos, color):
    rect = pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
    pygame.draw.rect(screen, color, rect, 5)

def draw_circle(screen, start_pos, end_pos, color):
    center = start_pos
    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
    pygame.draw.circle(screen, color, center, radius, 5)

def draw_square(screen, start_pos, end_pos, color):
    length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
    rect = pygame.Rect(start_pos[0], start_pos[1], length, length)
    pygame.draw.rect(screen, color, rect, 5)

def draw_right_triangle(screen, start_pos, end_pos, color):
    vertices = [start_pos, (end_pos[0], start_pos[1]), end_pos]
    pygame.draw.polygon(screen, color, vertices, 5)

def draw_equilateral_triangle(screen, start_pos, end_pos, color):
    length = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
    height = int(length * (3 ** 0.5) / 2)
    vertices = [start_pos, (start_pos[0] + length, start_pos[1]), (start_pos[0] + length // 2, start_pos[1] - height)]
    pygame.draw.polygon(screen, color, vertices, 5)

def draw_diamond(screen, start_pos, end_pos, color):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    mid_x, mid_y = start_pos[0] + dx // 2, start_pos[1] + dy // 2
    vertices = [(mid_x, start_pos[1]), (end_pos[0], mid_y), (mid_x, end_pos[1]), (start_pos[0], mid_y)]
    pygame.draw.polygon(screen, color, vertices, 5)

def draw_commands():
    commands = [
        "C: Clear",
        "R: Red",
        "B: Blue",
        "Y: Yellow",
        "K: Black",
        "E: Erase",
        "D: Draw line",
        "S: Square",
        "T: Right Triangle",
        "Q: Equilateral Triangle",
        "M: Diamond"
    ]
    y = 20
    for command in commands:
        text = font.render(command, True, colors['black'], colors['white'])
        screen.blit(text, (5, y))
        y += 20

done = False

while not done:
    draw_commands()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > command_width:
                drawing = True
                last_pos = event.pos
                start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode in ['rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'diamond']:
                end_pos = event.pos
                if mode == 'rectangle':
                    draw_rect(screen, start_pos, end_pos, current_color)
                elif mode == 'circle':
                    draw_circle(screen, start_pos, end_pos, current_color)
                elif mode == 'square':
                    draw_square(screen, start_pos, end_pos, current_color)
                elif mode == 'right_triangle':
                    draw_right_triangle(screen, start_pos, end_pos, current_color)
                elif mode == 'equilateral_triangle':
                    draw_equilateral_triangle(screen, start_pos, end_pos, current_color)
                elif mode == 'diamond':
                    draw_diamond(screen, start_pos, end_pos, current_color)
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == 'draw' and event.pos[0] > command_width:
                mouse_position = pygame.mouse.get_pos()
                if last_pos is not None:
                    draw_line(screen, last_pos, mouse_position, current_color)
                last_pos = mouse_position
            elif mode == 'erase' and event.pos[0] > command_width:
                mouse_position = pygame.mouse.get_pos()
                pygame.draw.circle(screen, colors['white'], mouse_position, 10)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill(colors['white'])
            elif event.key == pygame.K_r:
                current_color = colors['red']
            elif event.key == pygame.K_b:
                current_color = colors['blue']
            elif event.key == pygame.K_y:
                current_color = colors['yellow']
            elif event.key == pygame.K_k:
                current_color = colors['black']
            elif event.key == pygame.K_e:
                mode = 'erase'
            elif event.key == pygame.K_d:
                mode = 'draw'
            elif event.key == pygame.K_s:
                mode = 'square'
            elif event.key == pygame.K_t:
                mode = 'right_triangle'
            elif event.key == pygame.K_q:
                mode = 'equilateral_triangle'
            elif event.key == pygame.K_m:
                mode = 'diamond'

    pygame.display.update()
