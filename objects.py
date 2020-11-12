import pygame

import itertools


class Bolan:
	"""
	Represents Bolan, the T-Rex that the player plays as.
	"""
	

	def __init__(self, bolan_game):
		"""
		Initalize Bolan class attributes.
		"""
		self.bolan_game = bolan_game

		self.x = self.bolan_game.settings.bolan_x 
		self.y = self.bolan_game.settings.bolan_y 
		self.width = self.bolan_game.settings.bolan_width 
		self.height = self.bolan_game.settings.bolan_height	
		
		self.image_frame = 0
		self.image_index = 0
		self.images = self.images()
		self.image = self.images[self.image_index]
		self.rect = self.image.get_rect()

		self.is_jump = False
		self.jump_count = 10
		self.jump_frame = 0


	def images(self):
		"""
		Returns sprites of Bolan from spritesheet.
		"""
		rects = list()
		x = 1854
		for i in range(2):
			rects.append([x, 2, self.width, self.height])
			x += self.width
		return self.bolan_game.spritesheet.images_at(rects, (0, 0, 0))


	def update(self):
		"""
		Updates the object.
		"""
		self._update_image()
		self._update_position()


	def _update_image(self):
		"""
		Updates the image of Bolan.
		"""
		# Slow down animation. 
		self.image_frame += 1
		if self.image_frame == 60: 
			self.image_frame = 0
			self.image_index += 1

		# Animate Bolan running.
		if self.image_index >= len(self.images):
			self.image_index = 0
		self.image = self.images[self.image_index]


	def _update_position(self):
		"""
		Updates the position of Bolan on the screen.
		"""	
		if self.is_jump:
			# Keep Bolan's legs steady when he jumps.
			self.image = self.bolan_game.settings.bolan_image_standing

			# Only update Bolan's y every 15 frames.
			self.jump_frame += 1
			if self.jump_frame % 15 == 0: 
				self._jump()


	def _jump(self):
		"""
		Makes Bolan jump.
		"""
		if self.jump_count >= -10:
			self.y -= (self.jump_count * abs(self.jump_count)) * 0.45
			self.jump_count -= 1
		else:
			self.jump_count = 10
			self.is_jump = False


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
		self.image = self.bolan_game.spritesheet.image_at(
			self.bolan_game.settings.floor_rect, (0, 0, 0))
		self.rect = self.image.get_rect()

		self.x_1 = 0
		self.x_2 = self.rect.width
		self.y = self.bolan_game.settings.floor_y

		self.speed = self.bolan_game.settings.floor_speed


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