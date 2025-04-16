import pygame, psycopg2, random
from datetime import datetime

# Вход игрока
username = input("Имя игрока: ")

conn = psycopg2.connect(host="localhost", database="phonebook", user="keyara", password="")
cur = conn.cursor()

cur.execute("SELECT id, level FROM game_user WHERE username = %s", (username,))
user = cur.fetchone()
if user:
    user_id, level = user
    print(f"Добро пожаловать, {username}! Текущий уровень: {level}")
else:
    cur.execute("INSERT INTO game_user (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    level = 1
    print(f"Создан новый пользователь {username} с уровнем {level}")
conn.commit()

# Pygame init
pygame.init()
w, h = 400, 300
win = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

x, y = w//2, h//2
dx, dy = 0, 0
size = 10
food = [random.randrange(0, w, size), random.randrange(0, h, size)]
snake = [[x, y]]
score = 0

snake_speed = 5 + level * 2
paused = False
font = pygame.font.SysFont(None, 30)

def draw_text(text, x, y, color=(0,0,0)):
    t = font.render(text, True, color)
    win.blit(t, (x, y))

run = True
while run:
    pygame.time.delay(40)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT: dx, dy = -size, 0
            if e.key == pygame.K_RIGHT: dx, dy = size, 0
            if e.key == pygame.K_UP: dx, dy = 0, -size
            if e.key == pygame.K_DOWN: dx, dy = 0, size
            if e.key == pygame.K_p:
                paused = not paused
                if paused:
                    cur.execute("INSERT INTO user_score (user_id, score, timestamp) VALUES (%s, %s, %s)", (user_id, score, datetime.now()))
                    cur.execute("UPDATE game_user SET level = %s WHERE id = %s", (level, user_id))
                    conn.commit()
                    print(f"Пауза. Счёт {score}, уровень {level} сохранены.")

    if paused:
        win.fill((255,255,255))
        draw_text("ПАУЗА - нажми P чтобы продолжить", 50, 130, (200,0,0))
        pygame.display.update()
        continue

    x += dx
    y += dy
    snake.append([x, y])
    if len(snake) > score + 1:
        snake.pop(0)

    if [x, y] == food:
        score += 1
        food = [random.randrange(0, w, size), random.randrange(0, h, size)]
        if score % 5 == 0:
            level += 1
            snake_speed = 5 + level * 2

    if x < 0 or x >= w or y < 0 or y >= h or [x, y] in snake[:-1]:
        break

    win.fill((255,255,255))
    pygame.draw.rect(win, (0,255,0), (*food, size, size))
    for s in snake:
        pygame.draw.rect(win, (0,0,0), (*s, size, size))
    draw_text(f"Счёт: {score}  |  Уровень: {level}", 10, 10)
    pygame.display.update()
    clock.tick(snake_speed)

# Финал
cur.execute("UPDATE game_user SET level = %s WHERE id = %s", (level, user_id))
cur.execute("INSERT INTO user_score (user_id, score) VALUES (%s, %s)", (user_id, score))
conn.commit()
cur.close()
conn.close()
pygame.quit()
print(f"Игра окончена. Счёт: {score}, Уровень: {level}")