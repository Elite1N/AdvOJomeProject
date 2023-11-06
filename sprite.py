import pygame

class Sprite():
	def __init__(self, x, y, image, scale, health = 100):
		
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.health = health
		
		

	def draw(self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))

	def receive_damage(self,damage = 10):
		self.health -= damage