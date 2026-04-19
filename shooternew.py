from pgzrun import*
from random import*

WIDTH = 800
HEIGHT = 800

bee = Actor("bee_2")
shooter = Actor("shooter")

bees = []
bullets = []

bee_count = randint(1,10)
level = 5
ac_level = 0

is_game_over = False
score = 0

def thingi():
    global bee_count
    for i in range(bee_count):
        bees.append(Actor("bee_2"))
        bees[-1].x = randint(50,750)
        bees[-1].y = -1000
       
shooter.y = 750
shooter.x = 400

thingi()

def draw():
    global i
    screen.fill("blue")
    for i in bees:
        i.draw()
    for b in bullets:
        b.draw()
    shooter.draw()
    if is_game_over == True:
        screen.fill("light blue")
        screen.draw.text("GAME OVER",center= (400,400),fontsize= 110)
    if score == bee_count:
        screen.draw.text("you win",center= (400,400),fontsize= 110)
    
def update():
    global is_game_over,score,bullets,bee_count,level,ac_level
    if keyboard.right:
        shooter.x += 10
    if keyboard.left:
        shooter.x -= 10
    if keyboard.space:
         bullets.append(Actor("bullet"))
         bullets[-1].x = shooter.x
         bullets[-1].y = shooter.y
    for b in bullets:
        b.y -= 10
    for k in bees:
        for b in bullets[:]:
            if b.colliderect(k):
                bullets.remove(b)                  
                bees.remove(k)
                score += 1
                break
        
    for j in bees:
        j.y += randint(1,10)
        if j.y >= 750:
            is_game_over = True
    if score == bee_count:
        ac_level += 1
        level += 5
        score = 0
        bee_count = randint(level,20 + level)
        thingi()

go()