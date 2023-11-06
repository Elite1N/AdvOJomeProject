import pygame
pygame.init()
class Text():
    def __init__(self, x, y, size, color,whattosay,screen):
        self.x = x 
        self.y = y
        self.size = size
        self.color = color
        self.whattosay = whattosay
        self.text = None
        self.textRect = None
        self.screen = screen
        
    def draw(self):
        self.text = pygame.font.Font('freesansbold.ttf', self.size)
        self.text = self.text.render(self.whattosay, True, self.color)
        self.textRect =  self.text.get_rect()
        self.textRect.center = (self.x, self.y)
        
        self.screen.blit(self.text, self.textRect)
        

    
        
