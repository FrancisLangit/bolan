import pygame, sys


class Bolan:
	"""Overall class to manage game assets and behavior."""


	def __init__(self):
		"""Initialize the game."""
		pygame.init()

		self.screen = pygame.display.set_mode((1280, 600))
		pygame.display.set_caption("Bolan")


	def run(self):
		"""Start the game's main loop."""
		while True:
			self._check_events()
			self._update_screen()


	def _check_events(self):
		"""Track events and user input."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key in (pygame.K_q, pygame.K_ESCAPE):
					sys.exit()		


	def _update_screen(self):
		"""Update display of game."""
		self.screen.fill((255, 255, 255))
		pygame.display.flip()


bolan = Bolan()
bolan.run()