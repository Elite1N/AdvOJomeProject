import pygame
from pygame import mixer
pygame.init()
mixer.music.load("sfx/song.wav")
mixer.music.set_volume(0.5)
mixer.music.play(-1)
click_sound = pygame.mixer.Sound("sfx/mouse_click.mp3")


#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		#action = False
		#get mouse position
		pos = pygame.mouse.get_pos()
		
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				click_sound.play()
				self.clicked = True
				return True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		
		#draw button on screen
		surface.blit(self.image, self.rect.topleft)
		
		#return action
