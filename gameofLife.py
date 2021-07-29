import pygame as pg 
import time 
import numpy as np 
import os 
import grid
import random

os.environ["SDL_VIDEO_CENTERED"]='1' 

# RESOLUTION 
width, height = 1920, 1080
size = (width, height) 

pg.init() 
pg.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
fps = 60 

black = (0, 0, 0)
blue = (0, 121, 150) 
blue1 = (0, 14, 71) 
white = (255, 255, 255) 

scaler = 30 
offset = 1

Grid = grid.Grid(width,height, scaler, offset) 
Grid.random2d_array()

pause = False 
run = True 
while run: 
    clock.tick(fps) 
    screen.fill(black) 

    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            run = False 
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE: 
                run = False 
            if event.key == pg.K_SPACE:
                pause = not pause 

    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=pause)

    if pg.mouse.get_pressed()[0]:
        mouseX, mouseY = pg.mouse.get_pos() 
        Grid.HandleMouse(mouseX, mouseY)

    pg.display.update() 

    
pg.quit() 
            