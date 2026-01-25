import pgzrun
import pygame
from random import randint 

WIDTH = 500
HEIGHT = 500

game_over = False
score = 0

bumblebee = Actor("bee")
bumblebee.pos = (250,250)


flower = Actor("flower")
flower.pos = randint(50,450),randint(50,450)

def draw():
    screen.blit("scenary",(0,0))
    screen.draw.text("score = "+str(score),center= (250,30),fontsize= 30)
    if game_over == True:
        screen.fill("medium aquamarine")
        screen.draw.text("game over \n",str(score), center=(250,250),fontsize= 90)
    bumblebee.draw()
    flower.draw()

def timer():
    global game_over
    game_over = True
    

            
def place_Flower():
    flower.pos = randint(50,450),randint(50,450)

def update():
    global score

    if keyboard.left and bumblebee.x >50:
        bumblebee.x -= 30
    if keyboard.right and bumblebee.x <450:
        bumblebee.x += 30
    if keyboard.up and bumblebee.y >50:
        bumblebee.y -= 30
    if keyboard.down and bumblebee.y <450:
        bumblebee.y += 30
    if bumblebee.colliderect(flower) == True:
        place_Flower()
        score += 1
    if game_over == True
clock.schedule(timer,20.0)
pgzrun.go()