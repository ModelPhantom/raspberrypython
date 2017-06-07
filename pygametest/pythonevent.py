import pygame
from pygame.locals import *

import random
from time import sleep

running=True

width,height=640,640
radius=0
mouseX,mouseY=0,0

pygame.init()
screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)

screen.fill(pygame.Color(255,255,255))

fps=pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type==MOUSEMOTION:
            mouseX,mouseY=event.pos
        if event.type==MOUSEBUTTONDOWN:
            screen.fill(pygame.Color(255,255,255))
            radius=(abs(width/2-mouseX)+abs(height/2-mouseY))/2+1
            pygame.draw.circle(screen,pygame.Color(255,0,0),(mouseX,mouseY),radius,1)
            pygame.display.update()
            fps.tick(30)
        if event.type==pygame.KEYDOWN:
            running=False
pygame.quit()
