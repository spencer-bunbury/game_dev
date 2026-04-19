import pgzrun
from random import randint
from random import choice

WIDTH = 800
HEIGHT = 500


bomb = Actor("bomb")
fruit = Actor("fruit")
shoot = Actor("bullet")

i = True
j = True

thingi = ("bomb","fruit")
game_over = False

score = 0
bullets = [] 

def draw():
    global game_over,score
    screen.blit("scenary",(0,0))
    if game_over == False:
        what = choice(thingi)
        if what == bomb:
            bomb.x = randint(50,750)
            bomb.y = randint(200,450)
            bomb.draw()
        if what == fruit:
            fruit.x = randint(50,750)
            fruit.y = randint(200,450)
            fruit.draw()
        for k in bullets:
            k.draw()
    if shoot.colliderect(bomb):
        game_over = True
    if game_over == True:
        screen.draw.text("GAME OVER",center= (400,250),fontsize= 110)
    if shoot.colliderect(fruit):
        score += 1
        


def update():
    global game_over
    shoot.y -= 10
    if shoot.colliderect(bomb):
        i = False
        game_over = True
    if shoot.colliderect(fruit):
        i = False
        game_over = False
    if keyboard.space:
        bullets.append(Actor("shoot"))
        bullets[-1].x = shoot.x
        bullets[-1].y = shoot.y
    if keyboard.right:
        shoot.x += 10
    if keyboard.left:
        shoot.x -= 10    
    

pgzrun.go()