import pygame, sys

import objects

from settings import Settings
from spritesheet import SpriteSheet


class BolanGame:
	""" 
	Overall class to manage game ass`ets and behavior.
	"""


	def __init__(self):
		"""
		Initialize the game
		"""
		pygame.init()
		self.spritesheet = SpriteSheet('images/spritesheet.png')
		self.settings = Settings(self)

		self.screen = pygame.display.set_mode((
			self.settings.screen_width,
			self.settings.screen_height,
		))
		self.screen_rect = self.screen.get_rect()

		self.floor = objects.Floor(self)
		self.clouds = objects.Clouds(self)
		self.bolan = objects.Bolan(self)
		self.cacti = objects.Cacti(self)

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
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)


	def _check_keydown_events(self, event):
		"""
		Checks keydown events.
		"""
		if event.key in (pygame.K_q, pygame.K_ESCAPE):
			sys.exit()	
		if event.key == pygame.K_SPACE and (
			self.bolan.y >= self.bolan.default_y):
			self.bolan.is_jump = True
		if event.key == pygame.K_DOWN:
			self.bolan.is_duck = True


	def _check_keyup_events(self, event):
		"""
		Checks keyup events.
		"""
		if event.key == pygame.K_DOWN:
			self.bolan.is_duck = False


	def _update_screen(self):
		"""
		Update display of game.
		"""
		self.screen.fill((255, 255, 255))

		self._update_objects()
		self._blit_objects()

		pygame.display.flip()


	def _update_objects(self):
		"""
		Updates the game objects.
		"""
		self.floor.update()
		self.clouds.update()
		self.bolan.update()
		self.cacti.update()


	def _blit_objects(self):
		"""
		Blits the game objects onto the screen.
		"""
		self.floor.blitme()
		self.clouds.blitme()
		self.bolan.blitme()
		self.cacti.blitme()


if __name__ == '__main__':
	bolan_game = BolanGame()
	bolan_game.run()