from spritesheet import SpriteSheet

import helpers

class Settings:
	"""
	Hold all settings of game.
	"""


	def __init__(self, bolan_game):
		"""
		Initialize Settings class.
		"""
		self.bolan_game = bolan_game

		# General settings
		self.screen_width = 1280
		self.screen_height = 600
		self.background_color = (255, 255, 255)
		self.display_caption = "Bolan.py"


		# Bolan settings
		self.bolan_x_position = 20
		self.bolan_y_position = 440

		self.bolan_run_images = helpers.get_sprites(
			self.bolan_game, 2, 1854, 2, 88, 94)
		self.bolan_duck_images = helpers.get_sprites(
			self.bolan_game, 2, 2206, 6, 118, 94)
		self.bolan_standing_image = self.bolan_game.spritesheet.image_at(
			(1678, 2, 88, 94), colorkey=(0, 0, 0))
		
		self.bolan_update_rate = 60 # Update Bolan's image every 60 ticks.


		# Floor settings
		self.floor_rect = [2, 104, 2400, 26]
		self.floor_y = 500
		self.floor_speed = 1
		self.floor_image = self.bolan_game.spritesheet.image_at(
			self.floor_rect, (0, 0, 0))


		# Cactus settings
		self.cactus_x_position = 1400
		self.cactus_y_position = 435

		self.cactus_small_images = helpers.get_sprites(
			self.bolan_game, 6, 443, 2, 35, 100,)
		self.cactus_big_images = helpers.get_sprites(
			self.bolan_game, 4, 652, 2, 50, 100)
		self.cactus_images = self.cactus_small_images + self.cactus_big_images