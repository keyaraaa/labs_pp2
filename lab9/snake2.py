import pygame, random
pygame.init()

# --- Настройки окна и игрового поля ---
W, H = 400, 400
TILE = 20
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# --- Начальные параметры ---
snake = [(100, 100)]
direction = (TILE, 0)  # начальное направление — вправо
score = level = 0
speed = 10
last_level_up = 0

# --- Параметры еды ---
food_weights = [1, 2, 3]
food = (0, 0)
food_value = 1
food_timer = 0
FOOD_LIFETIME = 3000  # миллисекунд (3 секунды)

# --- Создание новой еды вне тела змеи ---
def new_food():
    global food, food_value, food_timer
    while True:
        fx = random.randint(0, (W - TILE) // TILE) * TILE
        fy = random.randint(0, (H - TILE) // TILE) * TILE
        if (fx, fy) not in snake:
            food = (fx, fy)
            food_value = random.choice(food_weights)
            food_timer = pygame.time.get_ticks()  # время появления еды
            break

new_food()  # первая еда

# --- Игровой цикл ---
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    # --- Управление стрелками (запрещаем разворот на 180°) ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != (TILE, 0): direction = (-TILE, 0)
    if keys[pygame.K_RIGHT] and direction != (-TILE, 0): direction = (TILE, 0)
    if keys[pygame.K_UP] and direction != (0, TILE): direction = (0, -TILE)
    if keys[pygame.K_DOWN] and direction != (0, -TILE): direction = (0, TILE)

    # --- Перемещаем змею ---
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # --- Проверка на смерть (стена или сама в себя) ---
    if head[0] < 0 or head[0] >= W or head[1] < 0 or head[1] >= H or head in snake:
        break  # Game Over

    snake = [head] + snake

    # --- Проверка: еда съедена или исчезла ---
    now = pygame.time.get_ticks()
    if head == food:
        score += food_value
        new_food()
        # Повышение уровня каждые 5 очков
        if score - last_level_up >= 5:
            level += 1
            speed += 2
            last_level_up = score
    elif now - food_timer > FOOD_LIFETIME:
        new_food()  # если еда не съедена — исчезает и появляется новая
    else:
        snake.pop()  # не съел — хвост сокращается

    # --- Отрисовка игры ---
    sc.fill((255, 255, 255))

    # Змея — зелёные квадраты
    for s in snake:
        pygame.draw.rect(sc, (0, 200, 0), (*s, TILE, TILE))

    # Еда — красный квадрат
    pygame.draw.rect(sc, (255, 0, 0), (*food, TILE, TILE))

    # Текст: очки, уровень, значение еды
    sc.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 10))
    sc.blit(font.render(f"Level: {level}", True, (0, 0, 0)), (300, 10))
    sc.blit(font.render(f"Food: +{food_value}", True, (255, 0, 0)), (10, 30))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()