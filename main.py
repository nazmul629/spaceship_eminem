import pygame
import random
from pygame.constants import KEYDOWN
from pygame.image import load
 
pygame.init()

screen = pygame.display.set_mode((800,600))
# Background 
backgrund = pygame.image.load('background.png')

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

player_img =  pygame.image.load('player.png')
PlayerX = 370
playerY = 480
PlayerX_change = 0

enemy_img =  pygame.image.load('enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 1.5
enemyY_change = 40


def player(x,y):
    screen.blit(player_img,(x,y))

def enemy(x,y):
    screen.blit(enemy_img,(x,y))


running = True
while running:
    screen.fill((0,0,0))
    screen.blit(backgrund,(0,0))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_change = -4

            if event.key == pygame.K_RIGHT:
                PlayerX_change = 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0

# Pleayer Chacking The boundary od Spacesho[ sp it doesn't go out od voundarys

    PlayerX += PlayerX_change
    if PlayerX<=0:
        PlayerX = 0
    elif PlayerX>=756:
        PlayerX = 756


    # Enams movement 

    enemyX += enemyX_change
    if enemyX <=0:
        enemyX_change = 1.5
        enemyY +=enemyY_change 
    elif enemyX>=756:
        enemyX_change = -1.5
        enemyY +=enemyY_change 

 
    player(PlayerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
