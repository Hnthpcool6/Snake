from re import S
import pygame
import os
from Define import *
from time import sleep
pygame.init()
screen = pygame.display.set_mode((720,640))
pygame.display.set_caption('Snake')
# icon = pygame.image.load('Images\icon.ico')
# pygame.display.set_icon(icon)
ruuning = True
clock = pygame.time.Clock()

snakes = [[5+2,5+0],[5+2,6+0],[5+2,7+0]]
direcrion = "right"

while running:
    clock.tick(60)
    screen.fill(BLACK)
    for i in range(20+1):

        pygame.draw.line(screen, WHITE, (60,i*30),(660,i*30))
        pygame.draw.line(screen, WHITE, (60+i*30,0),(60+i*30,600))
    pygame.draw.rect(screen, C_F, (FX*30, FY*30, 30,30))
    if eating:
        FX = random.randint(2,19)
        FY = random.randint(2,19)
        C_S = C_F
        C_F = (random.randint(100,200),random.randint(100,200),random.randint(100,200))
        eating = False
    if snakes[-1][0] == FX and snakes[-1][1] == FY:
        if direcrion == "right":
            snakes.append([snakes[-1][0]+1,snakes[-1][1]])

        sleep(0.1)
        if direcrion == "left":
            snakes.append([snakes[-1][0]-1,snakes[-1][1]])

        if direcrion == "up":
            snakes.append([snakes[-1][0],snakes[-1][1]-1])

        if direcrion == "down":
            snakes.append([snakes[-1][0],snakes[-1][1]+1])
        eating = True
    
    if snakes[-1][0] ==1  or snakes[-1][1] <0 or snakes[-1][0] ==22  or snakes[-1][1] ==21:
        running = False
    for snake in snakes:
        pygame.draw.rect(screen, C_S, (snake[0]*30, snake[1]*30, 30,30))
    if direcrion == "right":
        snakes.append([snakes[-1][0]+1,snakes[-1][1]])
        snakes.pop(0)
        sleep(0.1)
    if direcrion == "left":
        snakes.append([snakes[-1][0]-1,snakes[-1][1]])
        snakes.pop(0)
        sleep(0.1)
    if direcrion == "up":
        snakes.append([snakes[-1][0],snakes[-1][1]-1])
        snakes.pop(0)
        sleep(0.1)
    if direcrion == "down":
        snakes.append([snakes[-1][0],snakes[-1][1]+1])
        snakes.pop(0)
        sleep(0.1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ruuning = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direcrion != "down":
                direcrion = "up"
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direcrion != "right":
                direcrion = "left"
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direcrion != "up":
                direcrion = "down"
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direcrion != "left":
                direcrion = "right"



    pygame.display.flip()
pygame.quit()

