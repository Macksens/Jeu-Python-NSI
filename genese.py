import sys
import pygame

class GENTIL:
    def __init__(self, nom, color, widht, height):
        self.nom = nom
        self.color = color
        self.widht = widht
        self.height = height
        self.image = pygame.Surface([widht, height])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.rect(self.image, color, [0, 0, widht, height])
        self.rect = self.image.get_rect()
        
    def moveUp(self, pixels):
        self.rect.y = self.rect.y - pixels
        if self.rect.y < 0:
            self.rect.y = 0
    
    def moveDown(self, pixels):
        self.rect.y = self.rect.y + pixels
        if self.rect.y > 400:
            self.rect.y = 400
