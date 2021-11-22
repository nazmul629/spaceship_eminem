import pygame
import random
import math
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

# Multiple Enemy
enemy_img =[]
enemyX = []
enemyY =[]
enemyX_change= []
enemyY_change = []
num_of_enemy= 6
for i in range(num_of_enemy):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1.5)
    enemyY_change.append(40)

bullet_img =  pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = 'ready'

# Score
score_value = 0 
font = pygame.font.Font('freesansbold.ttf',50)
textX=14
textY=14

def show_score(x,y):
    score = font.render("Score: "+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def player(x,y):
    screen.blit(player_img,(x,y))

def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img,(x+16,y+10))
def isCollision(enemyX,enemyY,bulletX,bulletY):

    distance = math.sqrt((math.pow(enemyX-bulletX,2)) +(math.pow(enemyY-bulletY,2)))
    if distance <30:
        return True
    else:
        return False    

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
                if bullet_state == 'ready':
                    bulletX = playerX
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
    for i in range(num_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 1.5
            enemyY[i] +=enemyY_change[i] 
        elif enemyX[i]>=736:
            enemyX_change[i] = -1.5
            enemyY[i] +=enemyY_change[i]

        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state= "ready"
            score_value +=1
            # print(score_value)
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i)

    # Bullet Movement 
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    #Collision 
  
 
 
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
