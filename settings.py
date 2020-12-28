import pygame

from spritesheet import SpriteSheet


class Settings:
	"""
	Holds all settings of game.
	"""


	def __init__(self, bolan_game):
		"""
		Initialize Settings class.
		"""
		self.bolan_game = bolan_game
		self.spritesheet = bolan_game.spritesheet

		# General settings
		self.screen_width = 1280
		self.screen_height = 600
		self.background_color = (255, 255, 255)
		self.display_caption = "Bolan.py"
		self.spritesheet_colorkey = (0, 0, 0)
		self.max_fps = 600


		# Title settings 
		self.title_font = pygame.font.Font(
			"game_assets/fonts/PressStart2P.ttf", 32)
		self.title_image = self.title_font.render(
			"B O L A N . P Y", True, (83, 83, 83))
		self.subtitle_font = pygame.font.Font(
			"game_assets/fonts/Fipps.otf", 16)
		self.subtitle_image = self.subtitle_font.render(
			"Press ENTER to Play", True, (83, 83, 83))


		# GameOverImages settings
		self.gameover_image = self.spritesheet.image_at(
			(1294, 29, 381, 21), self.spritesheet_colorkey)
		self.retry_image = self.spritesheet.image_at(
			(2, 2, 72, 64), self.spritesheet_colorkey)


		# Bolan settings
		self.bolan_x_position = 20
		self.bolan_y_position = 440

		self.bolan_run_images = self.spritesheet.load_strip(
			(1854, 2, 88, 94), 2, self.spritesheet_colorkey)
		self.bolan_duck_images = self.spritesheet.load_strip(
			(2206, 6, 118, 94), 2, self.spritesheet_colorkey)

		self.bolan_standing_image = self.spritesheet.image_at(
			(1678, 2, 88, 94), self.spritesheet_colorkey)
		self.bolan_dead_image = self.spritesheet.image_at(
			(2030, 2, 88, 94), self.spritesheet_colorkey)
		
		self.bolan_update_rate = 60 # Update Bolan's image every 60 ticks.


		# Pterodactyl settings
		self.pterodactyl_images = self.spritesheet.load_strip(
			(261, 2, 91, 80), 2, self.spritesheet_colorkey)

		# Update Pterodactyl's image every 150 ticks.
		self.pterodactyl_update_rate = 150

		# Heights at which the Pterodactyl can spawn.
		# 520: Jump, 460: Jump/Duck, 410: Run Under.
		self.pterodactyl_heights = [520, 460, 410]
		self.pterodactyl_min_score = 1000 # Starts spawning at 10,000 points.
		

		# Floor settings
		self.floor_rect = [2, 104, 2400, 26]
		self.floor_y = 500
		self.floor_speed = 1
		self.floor_image = self.spritesheet.image_at(
			self.floor_rect, self.spritesheet_colorkey)


		# Cactus settings
		self.cactus_small_images = self.spritesheet.load_strip(
			(447, 28, 34, 70), 6, self.spritesheet_colorkey)
		self.cactus_big_images = self.spritesheet.load_strip(
			(652, 2, 50, 100, 4), 4, self.spritesheet_colorkey)
		self.cactus_group_images = self.spritesheet.images_at([
			(481, 28, 68, 70), # Two small cacti.
			(549, 28, 102, 70), # Three small cacti.
			(802, 2, 150, 100), # Three big cacti, one small cactus.
			(702, 2, 100, 100), ], # Two big cacti.
			self.spritesheet_colorkey,
		)
		self.cactus_images = (
			self.cactus_small_images +
			self.cactus_big_images + 
			self.cactus_group_images 
		)


		# Cloud settings
		self.cloud_image = self.spritesheet.image_at(
			(166, 2, 92, 27), self.spritesheet_colorkey)
		self.cloud_x_range = range(100, 1180)
		self.cloud_y_range = range(75, 300)
		self.cloud_number = 6
