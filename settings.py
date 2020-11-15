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
		self.bolan_game_x = 20
		self.bolan_game_y = 430

		self.bolan_standing_width = 88
		self.bolan_standing_height = 94
		self.bolan_standing_spritesheet_x = 1854 
		self.bolan_standing_spritesheet_y = 2 

		self.bolan_ducking_width = 118
		self.bolan_ducking_height = 60
		self.bolan_ducking_y = 470
		self.bolan_ducking_spritesheet_x = 2206
		self.bolan_ducking_spritesheet_y = 36
		self.bolan_image_standing = self.bolan_game.spritesheet.image_at(
			(1678, 2, self.bolan_standing_width, self.bolan_standing_height), 
			colorkey=(0, 0, 0))
		self.bolan_update_rate = 60 # Update Bolan's image every 60 ticks.


		# Floor settings
		self.floor_rect = [2, 104, 2400, 26]
		self.floor_y = 500
		self.floor_speed = 1
		self.floor_image = self.bolan_game.spritesheet.image_at(
			self.floor_rect, (0, 0, 0))


		# Cactus settings
		self.cactus_game_x = 1000
		self.cactus_game_y = 445
		self.cactus_images = helpers.get_sprites(
			self.bolan_game,
			6,
			443,
			2, 
			35, 
			70,
		)