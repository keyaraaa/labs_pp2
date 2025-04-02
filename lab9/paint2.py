import pygame
pygame.init()

# --- Настройки окна и цветов ---
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen.fill(WHITE)

# --- Переменные ---
drawing = False
start_pos = None
last_pos = None
color = BLACK
tool = "pen"
font = pygame.font.SysFont("Arial", 18)

# --- Палитра цветов ---
colors = [(0, 0, 0), (255, 0, 0), (0, 128, 0), (0, 0, 255)]

run = True
while run:
    # --- Панель инструментов (увеличена до 90px по высоте) ---
    screen.fill(WHITE, (0, 0, 600, 90))
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, 600, 90))

    # --- Первая строка инструментов ---
    text1 = font.render("[1] Pen  [2] Rect  [3] Circle  [4] Eraser", True, BLACK)
    screen.blit(text1, (10, 10))

    # --- Вторая строка инструментов ---
    text2 = font.render("[5] Square  [6] R-Triangle  [7] E-Triangle  [8] Rhombus", True, BLACK)
    screen.blit(text2, (10, 30))

    # --- Рисуем палитру ниже текста, на y = 55 ---
    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (400 + i*40, 55, 30, 30))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        # --- Выбор инструмента по цифрам ---
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_1: tool = "pen"
            elif e.key == pygame.K_2: tool = "rect"
            elif e.key == pygame.K_3: tool = "circle"
            elif e.key == pygame.K_4: tool = "eraser"
            elif e.key == pygame.K_5: tool = "square"
            elif e.key == pygame.K_6: tool = "rtriangle"
            elif e.key == pygame.K_7: tool = "etriangle"
            elif e.key == pygame.K_8: tool = "rhombus"

        # --- Нажатие мыши ---
        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Проверка на выбор цвета
            if 55 <= y <= 85 and x >= 400:
                index = (x - 400) // 40
                if 0 <= index < len(colors):
                    color = colors[index]
            else:
                drawing = True
                start_pos = pygame.mouse.get_pos()

        # --- Отпускание мыши: рисуем выбранную фигуру ---
        if e.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pygame.mouse.get_pos()
            x1, y1 = start_pos
            x2, y2 = end_pos

            if tool == "rect":
                pygame.draw.rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)

            elif tool == "circle":
                radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

            elif tool == "square":
                side = min(abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, color, (x1, y1, side, side), 2)

            elif tool == "rtriangle":
                points = [start_pos, (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, color, points, 2)

            elif tool == "etriangle":
                side = min(abs(x2 - x1), abs(y2 - y1))
                height = (3 ** 0.5 / 2) * side
                points = [(x1, y1), (x1 + side, y1), (x1 + side / 2, y1 - height)]
                pygame.draw.polygon(screen, color, points, 2)

            elif tool == "rhombus":
                mid_x = (x1 + x2) // 2
                mid_y = (y1 + y2) // 2
                dx = abs(x2 - x1) // 2
                dy = abs(y2 - y1) // 2
                points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
                pygame.draw.polygon(screen, color, points, 2)

    # --- Рисование пером ---
    if drawing and tool == "pen":
        mouse_pos = pygame.mouse.get_pos()
        if last_pos:
            pygame.draw.line(screen, color, last_pos, mouse_pos, 2)
        last_pos = mouse_pos
    else:
        last_pos = None

    # --- Ластик — белый круг ---
    if drawing and tool == "eraser":
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, WHITE, mouse_pos, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()