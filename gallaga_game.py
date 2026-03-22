from pgzrun import*
from random import*

WIDTH = 800
HEIGHT = 800

bee = Actor("bee_2")
shooter = Actor("shooter")

bees = []
for i in range(4):
        bees.append(bee)
        bees[-1].x = randint(50,750)
        bees[-1].y = 50
       

shooter.y = 750
shooter.x = 400
def draw():
    screen.fill("blue")
    for i in bees:
        i.draw()
    shooter.draw()
    
def update():
    if keyboard.right:
        shooter.x += 10
    if keyboard.left:
        shooter.x -= 10
    
go()
