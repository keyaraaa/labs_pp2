import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
screen.fill(WHITE)

drawing = False
last_pos = None
color = (0, 0, 0)
tool = "pen"
font = pygame.font.SysFont("Arial", 18)

def draw_text(text, pos):
    img = font.render(text, True, (0, 0, 0))
    screen.blit(img, pos)

running = True
while running:
    screen.fill(WHITE, (0, 0, 600, 30))  # Панель сверху
    draw_text("[1] Pen  [2] Rect  [3] Circle  [4] Eraser  [C] Color", (10, 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Выбор инструмента
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = "pen"
            elif event.key == pygame.K_2:
                tool = "rect"
            elif event.key == pygame.K_3:
                tool = "circle"
            elif event.key == pygame.K_4:
                tool = "eraser"
            elif event.key == pygame.K_c:
                color = (pygame.Color("red"))  # Можно менять на random или циклом

        # Начало рисования
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pygame.mouse.get_pos()
            if tool == "rect":
                pygame.draw.rect(screen, color, pygame.Rect(
                    start_pos[0], start_pos[1],
                    end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]
                ), 2)
            elif tool == "circle":
                radius = int(((end_pos[0] - start_pos[0]) ** 2 +
                              (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

    # Инструмент "ручка"
    if drawing and tool == "pen":
        mouse_pos = pygame.mouse.get_pos()
        if last_pos:
            pygame.draw.line(screen, color, last_pos, mouse_pos, 3)
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