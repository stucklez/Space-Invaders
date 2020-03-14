import pygame
import random
import math

#Inittialize pygame
pygame.init()
#Creating screen
screen = pygame.display.set_mode((800, 600))
#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Adding game icons
backgroundImg = pygame.image.load('background.png')
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(0, 150)
enemyX_change = 4
enemyY_change = 40

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

score = 0
#functions
def enemy (x,y):
    screen.blit(enemyImg, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    if math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))) < 27:
        return True
    else:
        return False

running = True
while running:
    # Making the background black
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))

    #Making the game closeable
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_d:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"


    if isCollision(enemyX, enemyY, bulletX, bulletY):
        bulletY = 480
        bullet_state = "ready"
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

