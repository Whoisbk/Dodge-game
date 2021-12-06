import pygame
import os

WHITE = (255,255,255)
GRAVITY = 0.5
class Player():
    

    def __init__(self,x,y,WIN):
        self.width = 25
        self.height = 25
        self.WIN = WIN
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = (x,y)
        self.vel_y = 0
        self.speed = 5
        self.clicked = False
        

    def draw(self):
        pygame.draw.rect(self.WIN,WHITE,self.rect)

    def move(self):
        dx = 0
        dy = 0

        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_a]:
            dx -= self.speed
        if key_pressed[pygame.K_d]:
            dx += self.speed

        if self.rect.left + dx <= 0:
            dx = 0 - self.rect.left

        if self.rect.right + dx > 400:
            dx = 400 - self.rect.right
            
        self.rect.x += dx
        self.rect.y += dy


        

