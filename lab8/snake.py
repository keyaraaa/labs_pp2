import pygame, random
pygame.init()
W, H = 400, 400
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

snake = [(100, 100)]
dir = (20, 0)
food = (random.randint(0, 19)*20, random.randint(0, 19)*20)
score = level = 0
speed = 10

def new_food():
    while True:
        f = (random.randint(0, 19)*20, random.randint(0, 19)*20)
        if f not in snake: return f

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False
    k = pygame.key.get_pressed()
    if k[pygame.K_LEFT] and dir != (20,0): dir = (-20,0)
    if k[pygame.K_RIGHT] and dir != (-20,0): dir = (20,0)
    if k[pygame.K_UP] and dir != (0,20): dir = (0,-20)
    if k[pygame.K_DOWN] and dir != (0,-20): dir = (0,20)
    
    head = (snake[0][0]+dir[0], snake[0][1]+dir[1])
    if head[0]<0 or head[0]>=W or head[1]<0 or head[1]>=H or head in snake:
        break
    snake = [head] + snake
    if head == food:
        score += 1
        food = new_food()
        if score % 4 == 0: level += 1; speed += 2
    else: snake.pop()

    sc.fill((255,255,255))
    for s in snake: pygame.draw.rect(sc, (0,255,0), (*s,20,20))
    pygame.draw.rect(sc, (255,0,0), (*food,20,20))
    sc.blit(font.render(f"Score:{score}",1,(0,0,0)), (10,10))
    sc.blit(font.render(f"Level:{level}",1,(0,0,0)), (300,10))
    pygame.display.flip()
    clock.tick(speed)
pygame.quit()