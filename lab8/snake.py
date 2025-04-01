import pygame, random
pygame.init()

# --- Настройки ---
W, H = 400, 400
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# --- Начальные значения ---
snake = [(100, 100)]
dir = (20, 0)
food = (random.randint(0, 19) * 20, random.randint(0, 19) * 20)
score = level = 0
speed = 10
last_score_level = 0

# --- Генерация еды вне змеи ---
def new_food():
    while True:
        f = (random.randint(0, 19) * 20, random.randint(0, 19) * 20)
        if f not in snake:
            return f

# --- Главный игровой цикл ---
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    # Управление
    k = pygame.key.get_pressed()
    if k[pygame.K_LEFT] and dir != (20, 0): dir = (-20, 0)
    if k[pygame.K_RIGHT] and dir != (-20, 0): dir = (20, 0)
    if k[pygame.K_UP] and dir != (0, 20): dir = (0, -20)
    if k[pygame.K_DOWN] and dir != (0, -20): dir = (0, 20)

    # Перемещение змейки
    head = (snake[0][0] + dir[0], snake[0][1] + dir[1])
    
    # Проверка на столкновение
    if head[0] < 0 or head[0] >= W or head[1] < 0 or head[1] >= H or head in snake:
        break

    snake = [head] + snake

    # Поедание еды
    if head == food:
        score += 1
        food = new_food()
        if score - last_score_level >= 4:
            level += 1
            speed += 2
            last_score_level = score
    else:
        snake.pop()

    # Рисование
    sc.fill((255, 255, 255))
    for s in snake:
        pygame.draw.rect(sc, (0, 255, 0), (*s, 20, 20))
    pygame.draw.rect(sc, (255, 0, 0), (*food, 20, 20))
    sc.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 10))
    sc.blit(font.render(f"Level: {level}", True, (0, 0, 0)), (300, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()