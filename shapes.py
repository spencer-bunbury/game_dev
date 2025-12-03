import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    r = 255
    g = 0
    b = randint(128,255)

    width = WIDTH
    height = HEIGHT-200

    for i in range(26):
        rectangle = Rect((0,0),(width,height))
        rectangle.center= 150,150
        screen.draw.rect(rectangle,(r,g,b))
        width -= 10
        height += 10
        r -= 10
        g += 10


pgzrun.go()