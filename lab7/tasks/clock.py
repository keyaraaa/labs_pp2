import pygame 
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("Mickey Clock")

leftarm = pygame.image.load("labs/lab7/images/leftarm.png")
rightarm = pygame.image.load("labs/lab7/images/rightarm.png")
mainclock = pygame.transform.scale(pygame.image.load("labs/lab7/images/clock.png"), (800, 600))

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = time.localtime()
    minute = (current_time.tm_min + 10) % 60
    second = current_time.tm_sec
    
    second_angle = -(second * 6)  
    minute_angle = -(minute * 6 + second / 10)  

    screen.blit(mainclock, (0, 0))

    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (41, 683)), second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip() 
    clock.tick(60) 

pygame.quit()