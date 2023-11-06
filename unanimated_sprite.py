import pygame

class Sprite():
	def __init__(self, x, y, image, scale):
		self.width = int(image.get_width() * scale)
		self.height = int(image.get_height() * scale)
		self.image = pygame.transform.scale(image, (self.width, self.height))
		self.x, self.y = x, y

	def draw(self, surface):
		surface.blit(self.image, (self.x, self.y))
		return

	def updater(self, x, y):
		self.x, self.y = x, y
		return