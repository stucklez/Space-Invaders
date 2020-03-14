import pygame
import random
import math

from pygame import mixer
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
mixer.music.load('background.wav')
mixer.music.play(-1)

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change= []
enemyY_change= []
num_of_enemies = 6

for i in range (6):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(0, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

game_over_font = pygame.font.Font('freesansbold.ttf', 64)
#functions
def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))
def enemy (x,y, i):
    screen.blit(enemyImg[i], (x, y))


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

def game_over_text():
    game_over = game_over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over, (200,250))

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
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
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

    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            enemy_sound = mixer.Sound('explosion.wav')
            enemy_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(0, 150)

        enemy(enemyX[i], enemyY[i], i)

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

