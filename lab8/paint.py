import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
screen.fill(WHITE)

# Переменные
drawing = False
start_pos = None
last_pos = None
color = (0, 0, 0)
tool = "pen"
font = pygame.font.SysFont("Arial", 18)

# Простая палитра
colors = [(0, 0, 0), (255, 0, 0), (0, 128, 0), (0, 0, 255)]

running = True
while running:
    # Верхняя панель
    screen.fill(WHITE, (0, 0, 600, 50))
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, 600, 50))
    text = font.render("[1] Pen  [2] Rect  [3] Circle  [4] Eraser", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Цвета
    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (400 + i*40, 10, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Инструменты
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: tool = "pen"
            elif event.key == pygame.K_2: tool = "rect"
            elif event.key == pygame.K_3: tool = "circle"
            elif event.key == pygame.K_4: tool = "eraser"

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Цвет
            if y < 50 and x >= 400:
                index = (x - 400) // 40
                if 0 <= index < len(colors):
                    color = colors[index]
            else:
                drawing = True
                start_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pygame.mouse.get_pos()
            if tool == "rect":
                x1, y1 = start_pos
                x2, y2 = end_pos
                pygame.draw.rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
            elif tool == "circle":
                dx = end_pos[0] - start_pos[0]
                dy = end_pos[1] - start_pos[1]
                radius = int((dx**2 + dy**2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

    # Перо
    if drawing and tool == "pen":
        mouse_pos = pygame.mouse.get_pos()
        if last_pos:
            pygame.draw.line(screen, color, last_pos, mouse_pos, 2)
        last_pos = mouse_pos
    else:
        last_pos = None

    # Ластик
    if drawing and tool == "eraser":
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, WHITE, mouse_pos, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()