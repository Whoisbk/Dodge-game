import pygame
from pygame import mixer
import os
import player
import random
import math
from block import Walls
pygame.font.init()
mixer.init()
pygame.init()


SCREEN_WIDTH = 400 
SCREEN_HEIGHT = 600

MAX_WALLS = 5#NUMBER OF WALLS ON SCREEN

WIN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("SKY PEA")

FPS = 60

score = 0
fade_counter = 0
game_over = False
health = 3

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE =(0,0,255)
RED =(255,0,0)
#FONT
font = pygame.font.SysFont("Lucida Sans",30)

def draw_win():
    WIN.fill((255,255,0))
    pygame.draw.rect(WIN,RED,(0,0,SCREEN_WIDTH,40))


def draw_text(text,x,y,font,color):
    txt = font.render(text,True,color)
    WIN.blit(txt,(x,y))



#INSTANCES
player = player.Player(200,500,WIN)
blocks = Walls(200,400,WIN,40,BLACK)

life_w = 20
life_x = random.randint(0,SCREEN_WIDTH-life_w)
life_y = blocks.rect.y - random.randint(80,150)
life = Walls(life_x,life_y,WIN,life_w,RED)

life= Walls(life_x,life_y,WIN,life_w,RED)

block_list = []
block_list.append(blocks)

life_blocks = []
life_blocks.append(life)

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    if game_over!= True:

        draw_win() #DRAW WINDOW
        #DRAW PLAYER
        player.draw()
        player.move()

        #DRAW BLOCKS
        if len(block_list) < MAX_WALLS:
            block_w = random.randint(90,150)
            block_x = random.randint(0,SCREEN_WIDTH-block_w)
            block_y = blocks.rect.y - random.randint(90,100)
            blocks = Walls( block_x,block_y,WIN,block_w,BLACK)
            block_list.append(blocks)
        
        for block in block_list:
            block.draw()
            block.update()
            if block.rect.top > SCREEN_HEIGHT + 10:
                block_list.remove(block)
            if block.rect.colliderect(player.rect):
                block_list.remove(block)
                health -= 1

            if score >= 9:
                block.speed = 6.5
            elif score >= 6:
                block.speed = 5.5
            elif score >= 3:
                block.speed = 3.5

        
        #DRAW SCORE BLOCK
        if len(life_blocks) < 1:
            life_w = 20
            life_x = random.randint(0,SCREEN_WIDTH-life_w)
            life_y = blocks.rect.y - random.randint(80,150)
            life = Walls(life_x,life_y,WIN,life_w,RED)
            life_blocks.append(life)
            
        for life in life_blocks:
            life.draw()
            life.update()
            if life.rect.top > SCREEN_HEIGHT or life.rect.colliderect(player.rect) :
                life_blocks.remove(life)
            if life.rect.colliderect(player.rect):
                score += 1
                print(score)
        
        draw_text(str(score),SCREEN_WIDTH/2,1,font,WHITE)
        draw_text(f'x{health}',5,1,font,WHITE)
        #CHECK GAME OVER
        if health == 0:
            game_over = True
    else:
        if fade_counter < 300:
            fade_counter += 5
            pygame.draw.rect(WIN,BLUE,(0,0,SCREEN_WIDTH,fade_counter))
            pygame.draw.rect(WIN,RED,(0,SCREEN_HEIGHT-fade_counter,SCREEN_WIDTH,fade_counter))
        else:
            draw_text(f"GAME OVER!",SCREEN_WIDTH//2-80,SCREEN_HEIGHT//2 -60,font,WHITE)
            draw_text(f"SCORE:{score}",SCREEN_WIDTH//2-60,SCREEN_HEIGHT//2,font,WHITE)
            draw_text('PRESS SPACE TO PLAY ',SCREEN_WIDTH//2 -150,SCREEN_HEIGHT-90,font,WHITE)
            
            #RESET GAME
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_SPACE]:
                game_over = False
                score = 0
                fade_counter = 0
                health = 3
                player.rect.center = (200,400)
                block_list.clear()
                life_blocks.clear()


    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    pygame.display.update()


pygame.quit()

