from spritesheet import SpriteSheet


class Settings:
	"""
	Hold all settings of game.
	"""


	def __init__(self):
		"""
		Initialize Settings class.
		"""


		# General settings
		self.screen_width = 1280
		self.screen_height = 600
		self.background_color = (255, 255, 255)
		self.display_caption = "Bolan.py"
		self.spritesheet = SpriteSheet('images/spritesheet.png')


		# Bolan settings
		self.bolan_x = 20
		self.bolan_y = 430
		self.bolan_width = 88
		self.bolan_height = 94		
		self.bolan_image_standing = self.spritesheet.image_at(
			(1678, 2, self.bolan_width, self.bolan_height), colorkey=(0, 0, 0))


		# Floor settings
		self.floor_rect = [2, 104, 2400, 26]
		self.floor_y = 500
		self.floor_speed = 1

