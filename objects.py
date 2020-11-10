import pygame

class Bolan:
	"""Represents Bolan, the T-Rex that the player plays as."""
	

	def __init__(self, bolan_game):
		self.bolan_game = bolan_game
		self.rect = (1678, 2, 88, 94)
		self.image = self.bolan_game.spritesheet.image_at(
			self.rect, (0, 0, 0))


	def blitme(self):
		self.bolan_game.screen.blit(self.image, (0, 0))


class DesertFloor:
	"""Represents the desert floor that Bolan runs on."""


	def __init__(self, bolan_game):
		self.bolan_game = bolan_game
		self.rect = (2, 104, 2400, 26)
		self.image = self.bolan_game.spritesheet.image_at(
			self.rect, (0, 0, 0))

		self.x = 0
		self.y = 500


	def blitme(self):
		self.bolan_game.screen.blit(self.image, (self.x, self.y))