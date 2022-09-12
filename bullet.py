import pygame
from random import randint
class Bullet:
    def __init__(self,x,y,change,img,amount,width,height):
        self.x = []
        self.y = []
        self.change = []
        self.img = []
        self.amount = amount
        self.width = width
        self.height = height
        for i in range(self.amount):
            self.img.append(pygame.image.load(img))
            self.x.append(x)
            self.y.append(y) 
            self.change.append(change)
        
    def bullet_fire(self):
        for i in range (self.amount):
            self.y[i] += self.change[i]
        if(self.y[i] <= 7):
                laser = pygame.mixer.Sound("data/laser.wav")
                laser.set_volume(0.2)
                laser.play()
    def check_bullet_boundary (self):
        for i in range(self.amount):
            if self.y[i] >= 557:
                self.y[i] = 0
                self.x[i] = randint(40,750)