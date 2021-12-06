import pygame

BLACK = (0,0,0)

class Walls():
    def __init__(self,x,y,WIN,width,color):
        self.width = width
        self.height = 30
        self.WIN = WIN
        self.color = color
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = (x,y)
        self.speed = 3

    def draw(self):
        pygame.draw.rect(self.WIN,self.color,self.rect)

    def update(self):
        self.rect.y += self.speed
    

        


        

