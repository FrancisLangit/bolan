class Settings:
	"""Hold all settings of game."""


	def __init__(self):
		"""Initialize Settings class."""


		# General settings
		self.screen_width = 1280
		self.screen_height = 600
		self.background_color = (255, 255, 255)
		self.display_caption = "Bolan.py"
		self.spritesheet_filename = 'images/spritesheet.png'


		# Floor settings
		self.floor_rect = [2, 104, 2400, 26]
		self.floor_y = 500
		self.floor_speed = 1