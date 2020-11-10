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
		Initialize the game.
		"""
		pygame.init()
		self.settings = Settings()
		self.spritesheet = SpriteSheet('images/spritesheet.png')

		self.screen = pygame.display.set_mode((
			self.settings.screen_width,
			self.settings.screen_height,
		))

		self.bolan = objects.Bolan(self)
		self.desert_floor = objects.DesertFloor(self)

		pygame.display.set_caption("Bolan")


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


	def _update_screen(self):
		"""
		Update display of game.
		"""
		self.screen.fill((255, 255, 255))

		# self.bolan.blitme()
		self.desert_floor.blitme()
		self.desert_floor.x -= 1

		pygame.display.flip()


if __name__ == '__main__':
	bolan_game = BolanGame()
	bolan_game.run()