import pygame, sys

import objects

from settings import Settings
from spritesheet import SpriteSheet


class BolanGame:
	""" 
	Overall class to manage game assets and behavior.
	"""


	def __init__(self):
		"""
		Initialize the game
.		"""
		pygame.init()
		self.spritesheet = SpriteSheet('images/spritesheet.png')
		self.settings = Settings(self)

		self.screen = pygame.display.set_mode((
			self.settings.screen_width,
			self.settings.screen_height,
		))
		self.screen_rect = self.screen.get_rect()

		self.bolan = objects.Bolan(self)
		self.floor = objects.Floor(self)
		self.cactus = objects.Cactus(self)

		pygame.display.set_caption(self.settings.display_caption)


	def run(self):
		"""
		Start the game's main loop.
		"""
		while True:
			self._check_events()
			self._update_screen()


	def _check_events(self):
		"""
		Track events and user input.
		"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key in (pygame.K_q, pygame.K_ESCAPE):
					sys.exit()	
				if event.key == pygame.K_SPACE and not self.bolan.is_duck:
					self.bolan.is_jump = True
				if event.key == pygame.K_DOWN:
					self.bolan.is_duck = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					self.bolan.is_duck = False


	def _update_screen(self):
		"""
		Update display of game.
		"""
		self.screen.fill((255, 255, 255))

		self._update_objects()

		self.floor.blitme()
		self.bolan.blitme()
		self.cactus.blitme()

		pygame.display.flip()


	def _update_objects(self):
		self.floor.update()
		self.bolan.update()
		self.cactus.update()


if __name__ == '__main__':
	bolan_game = BolanGame()
	bolan_game.run()