import pgzrun
from random import randint
from time import time

WIDTH = 750
HEIGHT = 750

sattellites = []
lines = []
next_satellite = 0

start_time = 0
total_time = 0
end_time = 0

def create_satellites():
    global start_time
    for i in range(8):
        satellite = Actor("sat")
        satellite.pos = randint(50,700), randint(50,700)
        sattellites.append(satellite)
    start_time = time()

def draw():
    global total_time
    screen.blit("space2",(0,0))
    number = 1
    for i in sattellites:
        screen.draw.text(str(number),(i.pos[0],i.pos[1] + 15))
        number += 1
        i.draw()
    if next_satellite < 8:
        total_time = time()-start_time
        screen.draw.text(str(round(total_time)),(375,45), fontsize= 90)
def update():
    pass
create_satellites()
pgzrun.go()




