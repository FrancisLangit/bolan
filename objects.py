import pygame


class Bolan:
	"""Represents Bolan, the T-Rex that the player plays as."""
	

	def __init__(self, bolan_game):
		"""Initalize Bolan class attributes."""
		self.bolan_game = bolan_game
		self.image = self.bolan_game.spritesheet.image_at(
			(1678, 2, 88, 94), (0, 0, 0))


	def blitme(self):
		"""Blit Bolan onto the screen."""
		self.bolan_game.screen.blit(self.image, (0, 0))


class Floor:
	"""Represents the desert floor that Bolan runs on."""


	def __init__(self, bolan_game):
		"""Initalize Floor class attributes."""
		self.bolan_game = bolan_game
		self.image = self.bolan_game.spritesheet.image_at(
			(2, 104, 2400, 26), (0, 0, 0))
		self.rect = self.image.get_rect()

		self.x_1 = 0
		self.y_1 = 500

		self.x_2 = self.rect.width
		self.y_2 = 500

		self.speed = 1


	def update(self):
		"""Updates the coordinates of the object."""
		self.x_1 -= self.speed
		self.x_2 -= self.speed
		if self.x_1 <= -self.rect.width:
			self.x_1 = self.rect.width
		if self.x_2 <= -self.rect.width:
			self.x_2 = self.rect.width


	def blitme(self):
		"""Blits the floor onto the screen."""
		self.bolan_game.screen.blit(self.image, (self.x_1, self.y_1))
		self.bolan_game.screen.blit(self.image, (self.x_2, self.y_2))