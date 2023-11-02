import pygame
import random

class Sprite():
	def __init__(self, color, x, y, height):
		self.x = x
		self.y = y	
		self.height = height
		self.rect_color = color
		




	def draw(self, screen,health,target_health):
		self.target_health = target_health
		self.health = health
		if self.target_health < self.health:
			self.health -= 1
			self.x_rand = random.randint( self.x-10, self.x+10 )
			self.y_rand = random.randint( self.y-10, self.y+10 )
			pygame.draw.rect(screen, self.rect_color, (self.x_rand, self.y_rand, self.health*7, self.height))
			return True
		else:
			pygame.draw.rect(screen, self.rect_color, (self.x, self.y, self.health*7, self.height))
		
