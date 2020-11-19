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
		self.default_x = self.settings.bolan_x_position
		self.default_y = self.settings.bolan_y_position
		self.x = self.default_x
		self.y = self.default_y

		# Image attributes
		self.image_frame = 0
		self.image_index = 0
		self.run_images = self.settings.bolan_run_images
		self.duck_images = self.settings.bolan_duck_images
		self.images = self.run_images
		self.image = self.run_images[self.image_index]

		# Movement attributes
		self.gravity = 1
		self.is_jump = False
		self.is_duck = False
		self.jump_speed = 1.25 

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
		if self.y < self.default_y:
			self.image = self.settings.bolan_standing_image
		else:
			if self.image_index >= len(self.images):
				self.image_index = 0
			self.image = self.images[self.image_index]


	def _player_control(self):
		"""
		Changes what Bolan does based on user input.
		"""
		if self.is_jump and not self.is_duck:
			self._jump()
		elif self.is_duck and self.y >= self.default_y:
			self._duck()
		else:
			self.images = self.run_images
			self._implement_gravity()


	def _implement_gravity(self):
		"""
		Brings Bolan's y-position he's above default y.
		"""
		if self.y < self.default_y:
			self.y += self.gravity


	def _jump(self):
		"""
		Makes Bolan jump.
		"""
		if self.y > 250:
			self.y -= self.jump_speed
		else:
			self.is_jump = False


	def _duck(self):
		"""
		Makes Bolan duck.
		"""
		self.images = self.duck_images


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
	Represents a single Cactus.
	"""


	def __init__(self, bolan_game, x):
		"""
		Initialize Cactus class attributes.
		"""
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings

		self.images = self.settings.cactus_images
		self.image = random.choice(self.images)

		self.x = x
		self.y = self.settings.cactus_y_position


	def update(self):
		"""
		Updates the Cactus object.
		"""
		if self.x <= -204:
			self.x = 2100
			self.image = random.choice(self.images)
		self.x -= 1


class Cacti:
	"""
	Represents the cacti that procedurally generate at fixed intervals.
	"""


	def __init__(self, bolan_game):
		"""
		Initialize Cacti class attributes.
		"""
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings

		self.cacti = [
			Cactus(bolan_game, 1400),
			Cactus(bolan_game, 2100),
			Cactus(bolan_game, 2800),
		]


	def update(self):
		"""
		Update each cactus in the self.cacti iterable.
		"""
		for cactus in self.cacti:
			cactus.update()


	def blitme(self):
		"""
		Blit the cacti onto the screen.
		"""
		for cactus in self.cacti:
			self.bolan_game.screen.blit(cactus.image, (cactus.x, cactus.y))