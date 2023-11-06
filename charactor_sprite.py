import pygame

class Sprite():
	def __init__(self, x, y, image, scale, health = 100):
		
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.x, self.y = x, y
		self.health = health
		
		

	def draw(self, surface):
		surface.blit(self.image, (self.x, self.y))

	def receive_damage(self,damage = 10):
		self.health -= damage
		if self.health < 0:
			self.health = 0
		return damage
	
	def receive_health(self,heal = 5):
		self.health += heal
		if self.health > 100:
			self.health = 100
		return heal


	def info():
		return 10

	def animate():
		pass