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
		self.bolan_standing_width = 88
		self.bolan_standing_height = 94		
		self.bolan_image_standing = self.spritesheet.image_at(
			(1678, 2, self.bolan_standing_width, self.bolan_standing_height), 
			colorkey=(0, 0, 0)
		)
		self.bolan_image_ducking = self.spritesheet.image_at(
			(2206, 34, 118, 62), colorkey=(0, 0, 0))


		# Floor settings
		self.floor_rect = [2, 104, 2400, 26]
		self.floor_y = 500
		self.floor_speed = 1.5
		self.floor_image = self.spritesheet.image_at(
			self.floor_rect, (0, 0, 0))

