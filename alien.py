import pygame
import pgzrun
import random
import time

pygame.mixer.init()
pygame.mixer.music.load("fail-trumpet-242645.mp3")

HEIGHT = 500
WIDTH = 500

message = ""
alien = Actor("alien")
def draw():
    #screen.fill("medium aquamarine")
    screen.blit("space",(0,0))
    screen.draw.text(message,center= (250,30),fontsize= 30)
    alien.draw()

i = (50)
def position():
    alien.x = random.randint(50,WIDTH-50)
    alien.y = random.randint(50,HEIGHT-50)


def on_mouse_down(pos):
    global message
    if(alien.collidepoint(pos)):
        message = "good shot"
        position()
    else:
        message = "bad shot!"
        pygame.mixer.music.play()
position()


pgzrun.go()

   

