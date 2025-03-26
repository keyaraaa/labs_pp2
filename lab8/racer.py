import pygame, random
pygame.init()

W, H = 400, 600
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28) 

# Загрузка и масштабирование
road = pygame.transform.scale(pygame.image.load("labs/lab8/images/road.png"), (W, H))
player = pygame.transform.scale(pygame.image.load("labs/lab8/images/player.png"), (100, 100)) 
enemy = pygame.transform.scale(
    pygame.transform.rotate(pygame.image.load("labs/lab8/images/enemy.png"), 180), (50, 100)
)
coin = pygame.transform.scale(pygame.image.load("labs/lab8/images/coin.png"), (30, 30))

# Позиции
px, py = W // 2 - 25, H - 110
ex, ey = random.randint(50, W - 50), -100
cx, cy = random.randint(50, W - 50), -100
score = 0

run = True
while run:
    sc.blit(road, (0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and px > 0: px -= 5
    if keys[pygame.K_RIGHT] and px < W - 50: px += 5

    ey += 5
    cy += 4
    if ey > H: ey, ex = -100, random.randint(50, W - 50)
    if cy > H: cy, cx = -100, random.randint(50, W - 50)

    # 💥 Столкновение с врагом
    if pygame.Rect(px, py, 50, 100).colliderect(pygame.Rect(ex, ey, 50, 100)):
        # Показать Game Over и счёт
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        score_text = font.render(f"Coins collected: {score}", True, (255, 255, 255))
        sc.blit(game_over_text, (W // 2 - game_over_text.get_width() // 2, H // 2 - 30))
        sc.blit(score_text, (W // 2 - score_text.get_width() // 2, H // 2 + 10))
        pygame.display.flip()
        pygame.time.delay(2500)
        run = False

    # 💰 Подбор монеты
    if pygame.Rect(px, py, 50, 100).colliderect(pygame.Rect(cx, cy, 30, 30)):
        score += 1
        cy, cx = -100, random.randint(50, W - 50)

    # Отрисовка
    sc.blit(player, (px, py))
    sc.blit(enemy, (ex, ey))
    sc.blit(coin, (cx, cy))
    sc.blit(font.render(f"Coins: {score}", True, (255, 255, 255)), (W - 130, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()