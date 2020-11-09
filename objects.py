import pygame

class Bolan:
	"""Represents Bolan, the T-Rex that the player plays as."""
	

	def __init__(self, bolan_game):
		self.bolan_game = bolan_game
		self.rect = (1678, 2, 88, 94)
		self.image = self.bolan_game.spritesheet.image_at(self.rect)
