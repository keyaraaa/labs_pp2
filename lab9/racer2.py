import pygame, random
pygame.init()

# Размеры окна
W, H = 400, 600
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

# Загрузка картинок
road = pygame.image.load("labs/lab8/images/road.png")
player = pygame.image.load("labs/lab8/images/player.png")
enemy = pygame.transform.rotate(pygame.image.load("labs/lab8/images/enemy.png"), 180)
coin = pygame.image.load("labs/lab8/images/coin.png")

# Позиции игрока и врага
px, py = 150, 480
ex, ey = 100, -100

# Позиция монеты и её "вес" (сколько очков даёт)
cx, cy = 200, -100
coin_weights = [1, 2, 3]
coin_value = random.choice(coin_weights)

# Счёт и скорость врага
score = 0
enemy_speed = 5

run = True
while run:
    # Отображение фона
    sc.blit(pygame.transform.scale(road, (W, H)), (0, 0))

    # Обработка выхода
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    # Движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and px > 0: px -= 5
    if keys[pygame.K_RIGHT] and px < W - 100: px += 5

    # Движение врага и монеты вниз
    ey += enemy_speed
    cy += 4

    # Если враг или монета вышли за экран — создаём заново
    if ey > H:
        ey = -100
        ex = random.randint(0, W - 100)
    if cy > H:
        cy = -100
        cx = random.randint(0, W - 30)
        coin_value = random.choice(coin_weights)

    # Столкновение с врагом — игра окончена
    if pygame.Rect(px, py, 100, 100).colliderect((ex, ey, 50, 100)):
        sc.blit(font.render("GAME OVER", True, (255, 0, 0)), (150, 250))
        pygame.display.flip()
        pygame.time.delay(2000)
        break

    # Подбор монеты — увеличиваем счёт
    if pygame.Rect(px, py, 100, 100).colliderect((cx, cy, 30, 30)):
        score += coin_value
        cy = -100
        cx = random.randint(0, W - 30)
        coin_value = random.choice(coin_weights)

        # Каждые 10 очков — враг быстрее
        if score % 10 == 0:
            enemy_speed += 1

    # Отображение игрока, врага и монеты
    sc.blit(pygame.transform.scale(player, (100, 100)), (px, py))
    sc.blit(pygame.transform.scale(enemy, (50, 100)), (ex, ey))
    sc.blit(pygame.transform.scale(coin, (30, 30)), (cx, cy))

    # Показ счёта и веса монеты
    sc.blit(font.render(f"Coins: {score}", True, (255, 255, 255)), (10, 10))
    sc.blit(font.render(f"Coin value: {coin_value}", True, (255, 255, 255)), (10, 40))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

pygame.quit()