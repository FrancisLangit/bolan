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
		"""
		pygame.init()
		self.clock = pygame.time.Clock()
		self.spritesheet = SpriteSheet('game_assets/images/spritesheet.png')
		self.settings = Settings(self)

		self.screen = pygame.display.set_mode((
			self.settings.screen_width,
			self.settings.screen_height,
		))
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption(self.settings.display_caption)

		# Track gamestate.
		self.is_play = False
		self.is_gameover = False

		# Game objects.
		self.title = objects.Title(self)
		self.gameover_images = objects.GameOverImages(self)
		self.scoreboard = objects.Scoreboard(self)
		self.floor = objects.Floor(self)
		self.clouds = objects.Clouds(self)
		self.bolan = objects.Bolan(self)
		self.obstacles = objects.Obstacles(self)


	def run(self):
		"""
		Start the game's main loop.
		"""
		while True:
			self.clock.tick(self.settings.max_fps)
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

			elif event.type == pygame.MOUSEBUTTONDOWN:
				self._check_retry_button(pygame.mouse.get_pos())


	def _check_keydown_events(self, event):
		"""
		Checks keydown events.
		"""
		if event.key in (pygame.K_q, pygame.K_ESCAPE):
			self._exit_program()
		elif self.is_play:
			self._check_keydown_play_events(event)
		elif self.is_gameover:
			if event.key in (pygame.K_RETURN, pygame.K_r):
				self._reset_game()
		else:
			if event.key == pygame.K_RETURN:
				self.is_play = True


	def _check_keydown_play_events(self, event):
		"""
		Keydown events when is_play is True.
		"""
		if (event.key in (pygame.K_SPACE, pygame.K_UP)) and (
			self.bolan.rect.y >= self.bolan.default_y):
			self.bolan.is_jump = True
		if event.key == pygame.K_DOWN:
			self.bolan.is_duck = True


	def _check_keyup_events(self, event):
		"""
		Checks keyup events.
		"""
		if event.key == pygame.K_DOWN:
			self.bolan.is_duck = False


	def _check_retry_button(self, mouse_position):
		"""
		Checks if the user clicks the mousebutton within the retry button.
		"""
		if self.gameover_images.retry_rect.collidepoint(mouse_position):
			self._reset_game()
			

	def _reset_game(self):
		"""
		Resets the game to its settings upon startup.
		"""
		self.is_play = True
		self.is_gameover = False
		self.bolan.rect.y = self.bolan.default_y
		self.scoreboard.score = 0
		self.obstacles._reset_positions()


	def _exit_program(self):
		"""
		Saves the highscore and exits the program.
		"""
		with open("game_assets/highscore.txt", 'w') as highscore:
			highscore.write(str(self.scoreboard.highscore))
		sys.exit()


	def _update_screen(self):
		"""
		Update display of game.
		"""
		self.screen.fill((255, 255, 255))

		self._check_collisions()
		self._update_objects()
		self._blit_objects()

		pygame.display.flip()


	def _check_collisions(self):
		"""
		Respond to collisions between Bolan and an obstacles.
		"""
		if pygame.sprite.spritecollide(
			self.bolan, 
			self.obstacles.obstacles,
			False, 
			pygame.sprite.collide_mask):
				self.is_play = False
				self.is_gameover = True
				self.bolan.image = self.settings.bolan_dead_image


	def _update_objects(self):
		"""
		Updates the game objects.
		"""
		self.clouds.update()
		if self.is_play:
			self.floor.update()
			self.bolan.update()
			self.obstacles.update()
			self.scoreboard.update()


	def _blit_objects(self):
		"""
		Blits the game objects onto the screen.
		"""
		self.clouds.blitme()
		self.floor.blitme()
		self.bolan.blitme()
		self.obstacles.blitme()
		self._blit_text()
		self.scoreboard.blitme()


	def _blit_text(self):
		if not self.is_play and not self.is_gameover:
			self.title.blitme()
		elif self.is_gameover:
			self.gameover_images.blitme()


if __name__ == '__main__':
	bolan_game = BolanGame()
	bolan_game.run()
