import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
ball_pos = [400, 300]

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    ball_pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 20
    ball_pos[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), ball_pos, 25)
    pygame.display.flip()
    pygame.time.delay(40)