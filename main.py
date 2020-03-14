import pygame

#Inittialize pygame
pygame.init()
#Creating screen
screen = pygame.display.set_mode((800, 600))
#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Adding game icons

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
enemyImg = pygame.image.load('enemy.png')
bulletImg = pygame.image.load('bullet.png')

#functions

def player():
    screen.blit(playerImg, (playerX, playerY))


running = True
while running:
    #Making the game closeable
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Making the background black
    screen.fill((0, 0, 0))
    player()
    pygame.display.update()

