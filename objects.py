import random

import pygame

import helpers



class Bolan:
	"""
	Represents Bolan, the T-Rex that the player plays as.
	"""
	

	def __init__(self, bolan_game):
		"""
		Initalize Bolan class attributes.
		"""
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings

		# In-game coordinates and dimensions
		self.default_x = self.settings.bolan_game_x
		self.default_y = self.settings.bolan_game_y
		self.x = self.default_x
		self.y = self.default_y

		self.standing_width = self.settings.bolan_standing_width 
		self.standing_height = self.settings.bolan_standing_height
		self.standing_y = self.settings.bolan_game_y

		self.ducking_width = self.settings.bolan_ducking_width
		self.ducking_height = self.settings.bolan_ducking_height
		self.ducking_y = self.settings.bolan_ducking_y

		# Spritesheet coordinates and dimensions
		self.standing_spritesheet_x = self.settings.bolan_standing_spritesheet_x
		self.standing_spritesheet_y = self.settings.bolan_standing_spritesheet_y
		self.ducking_spritesheet_x = self.settings.bolan_ducking_spritesheet_x
		self.ducking_spritesheet_y = self.settings.bolan_ducking_spritesheet_y

		# Jump attributes
		self.is_jump = False
		self.jump_count = 10
		self.jump_frame = 0

		# Duck attributes 
		self.is_duck = False

		# Image attributes
		self.image_frame = 0
		self.image_index = 0
		self.default_images = helpers.get_sprites(
			self.bolan_game,
			2, 
			self.standing_spritesheet_x, 
			self.standing_spritesheet_y, 
			self.standing_width, 
			self.standing_height,
		)
		self.images = self.default_images
		self.image = self.images[self.image_index]
		self.rect = self.image.get_rect()


	def update(self):
		"""
		Updates Bolan.
		"""
		self._increment_animation()
		self._update_sprite(self.image_frame, self.image_index)
		self._player_control()


	def _increment_animation(self):
		"""
		Defines the rate at which Bolan's images change.
		"""
		self.image_frame += 1
		if self.image_frame == self.settings.bolan_update_rate: 
			self.image_frame = 0
			self.image_index += 1


	def _update_sprite(self, image_frame, image_index):
		"""
		Changes Bolan's sprite.
		"""
		if self.image_index >= len(self.images):
			self.image_index = 0
		self.image = self.images[self.image_index]


	def _player_control(self):
		"""
		Changes what Bolan does based on user input.
		"""
		if self.is_jump:
			self._jump()
		elif self.is_duck:
			self._duck()
		else:
			self.images = self.default_images
			self.y = self.standing_y


	def _jump(self):
		"""
		Makes Bolan jump.
		"""
		# Update Bolan's image.
		self.image = self.settings.bolan_image_standing

		# Only update Bolan's y every 12 frames.
		self.jump_frame += 1
		if self.jump_frame % 15 == 0: 
			if self.jump_count >= -10:
				self.y -= (self.jump_count * abs(self.jump_count)) * 0.5
				self.jump_count -= 1
			else:
				self.jump_count = 10
				self.is_jump = False


	def _duck(self):
		"""
		Makes Bolan duck.
		"""
		self.images = helpers.get_sprites(
			self.bolan_game,
			2, 
			self.ducking_spritesheet_x, 
			self.ducking_spritesheet_y, 
			self.ducking_width, 
			self.ducking_height
		)
		self.y = self.ducking_y


	def blitme(self):
		"""
		Blit Bolan onto the screen.
		"""
		self.bolan_game.screen.blit(self.image, (self.x, self.y))


class Floor:
	"""
	Represents the desert floor that Bolan runs on.
	"""


	def __init__(self, bolan_game):
		"""
		Initalize Floor class attributes.
		"""
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings

		self.image = self.settings.floor_image
		self.rect = self.image.get_rect()

		self.x_1 = 0
		self.x_2 = self.rect.width
		self.y = self.settings.floor_y

		self.speed = self.settings.floor_speed


	def update(self):
		"""
		Updates the floor object.
		"""
		self.x_1 -= self.speed
		self.x_2 -= self.speed
		if self.x_1 <= -self.rect.width:
			self.x_1 = self.rect.width
		if self.x_2 <= -self.rect.width:
			self.x_2 = self.rect.width


	def blitme(self):
		"""
		Blits the floor onto the screen.
		"""
		self.bolan_game.screen.blit(self.image, (self.x_1, self.y))
		self.bolan_game.screen.blit(self.image, (self.x_2, self.y))


class Cactus:
	"""
	Represents the Cactus obstacles that Bolan must jump over.
	"""


	def __init__(self, bolan_game):
		"""
		Initialize Cactus class attributes.
		"""
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings

		self.x = self.settings.cactus_game_x
		self.y = self.settings.cactus_game_y

		self.images = self.settings.cactus_images
		self.image = random.choice(self.images)


	def update(self):
		"""
		Updates the Cactus object.
		"""
		if self.x <= -1000:
			self.x = self.settings.cactus_game_x
			self.image = random.choice(self.images)

		self.x -= 1


	def blitme(self):
		"""
		Blits the Cactus onto the screen.
		"""
		self.bolan_game.screen.blit(self.image, (self.x, self.y))
