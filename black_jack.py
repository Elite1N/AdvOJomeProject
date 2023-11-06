import pygame
import random
from load_all_image import load_images_from_folder
from unanimated_sprite import Sprite

class Black_jack():
	def __init__(self, screen):
		self.screen = screen
		self.show = False
		self.card_all = {}
		self.card_dealer = {}
		self.card_player = {}
		self.card_back = {
			"back": Sprite(50, 0, pygame.image.load(f"card/back.png").convert_alpha(), 1.4)
		}
		for a in load_images_from_folder("card", "back.png"):
			x = pygame.image.load(f"card/{a}").convert_alpha()
			self.card_all[a.replace(".png", "")] = Sprite(0, 0, x, 0.2)
		self.dealer_init()
		self.player_init()
		self.draw_all()

	def dealer_init(self):
		for i in random.sample(list(self.card_all.keys()), 2):
			self.card_all[i].updater((self.card_all[i].width-100) * len(self.card_dealer) + 50, 0)
			self.card_dealer[i] = self.card_all[i]
			self.card_all.pop(i)
		return 0

	def player_init(self):
		for i in random.sample(list(self.card_all.keys()), 2):
			self.card_all[i].updater((self.card_all[i].width-100) * len(self.card_player) + 50, 430)
			self.card_player[i] = self.card_all[i]
			self.card_all.pop(i)
		return 0
	
	def player_draw(self):
		i = random.choice(list(self.card_all.keys()))
		self.card_all[i].updater((self.card_all[i].width-100) * len(self.card_player) + 50, 430)
		self.card_player[i] = self.card_all[i]
		self.card_all.pop(i)
		self.draw_all()
		return 0
	
	def end_check_win(self):
		dealer_score = 0
		player_score = 0
		for i in self.card_dealer.keys():
			dealer_score += self.convert_score(i)
		for i in self.card_player.keys():
			player_score += self.convert_score(i)
		dealer_sub = abs(21-dealer_score)
		player_sub = abs(21-player_score)
		self.show = True
		
		if dealer_score > 21 and player_score <= 21:
			return 1
		elif dealer_score <= 21 and player_score > 21:
			return 0
		elif dealer_sub > player_sub:
			return 1
		elif dealer_sub == player_sub:
			return 2
		else:
			return 0


	def convert_score(self, x):
		try:
			x = int(x[0:2])
		except:
			try:
				x = int(x[0])
			except:
				if x == "A":
					x = 11
				else:
					x = 10
		return x
	
	def draw_all(self, x=False):
		for i in self.card_player.values():
			i.draw(self.screen)
		if not self.show:
			self.card_back["back"].draw(self.screen)
		else:
			self.card_dealer[list(self.card_dealer.keys())[0]].draw(self.screen)
		self.card_dealer[list(self.card_dealer.keys())[1]].draw(self.screen)
		pass


	def reset(self):
		self.card_dealer.clear()
		self.card_player.clear()
		