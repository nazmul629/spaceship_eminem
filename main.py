import pygame
import random
from pygame.constants import KEYDOWN
from pygame.image import load
#   asdasda
pygame.init()

screen = pygame.display.set_mode((800,600))
# Background 
backgrund = pygame.image.load('background.png')

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

player_img =  pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

enemy_img =  pygame.image.load('enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 1.5
enemyY_change = 40

bullet_img =  pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = 'ready'


def player(x,y):
    screen.blit(player_img,(x,y))

def enemy(x,y):
    screen.blit(enemy_img,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img,(x+16,y+10))


running = True
while running:
    screen.fill((0,0,0))
    screen.blit(backgrund,(0,0))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4

            if event.key == pygame.K_RIGHT:
                playerX_change = 4

            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

# Pleayer Chacking The boundary od Spacesho[ sp it doesn't go out od voundarys

    playerX += playerX_change
    if playerX<=0:
        playerX = 0
    elif playerX>=756:
        playerX = 756


    # Enameys movement 

    enemyX += enemyX_change
    if enemyX <=0:
        enemyX_change = 1.5
        enemyY +=enemyY_change 
    elif enemyX>=756:
        enemyX_change = -1.5
        enemyY +=enemyY_change 

    # Bullet Movement 
    if bullet_state is "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change

       
 
 
    player(playerX,playerY)
    enemy(enemyX,enemyY) 
    pygame.display.update()
