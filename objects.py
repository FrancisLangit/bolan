import pygame, random


class Title:
	"""
	Text that appears on screen at the beginning of the game.
	"""


	def __init__(self, bolan_game):
		"""
		Initialize MainMenu class attributes.
		"""
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings

		self.title_image = self.settings.title_image
		self.title_rect = self.title_image.get_rect(
			center=self.bolan_game.screen_rect.center)
		self.title_rect.y -= 75

		self.subtitle_image = self.settings.subtitle_image
		self.subtitle_rect = self.subtitle_image.get_rect(
			center=self.bolan_game.screen_rect.center)
		self.subtitle_frame = 0


	def _blit_subtitle(self):
		"""
		Blits the subtitle with a blinking animation.
		"""
		self.subtitle_frame += 1
		if self.subtitle_frame < 400:
			self.bolan_game.screen.blit(self.subtitle_image, self.subtitle_rect)
		elif self.subtitle_frame < 800:
			pass
		else:
			self.subtitle_frame = 0


	def blitme(self):
		"""
		Blits the object onto the screen.
		"""
		self._blit_subtitle()	
		self.bolan_game.screen.blit(self.title_image, self.title_rect)




class GameOverImages:
	"""
	Images that appear on screen when the game is over.
	"""


	def __init__(self, bolan_game):
		"""
		Initialize object attributes.
		"""
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings

		self.gameover_image = self.settings.gameover_image
		self.gameover_rect = self.gameover_image.get_rect(
			center=self.bolan_game.screen_rect.center)
		self.gameover_rect.y -= 30

		self.retry_image = self.settings.retry_image
		self.retry_rect = self.retry_image.get_rect(
			center=self.bolan_game.screen_rect.center)
		self.retry_rect.y += 50


	def blitme(self):
		"""
		Blits the object onto the screen.
		"""
		self.bolan_game.screen.blit(self.gameover_image, self.gameover_rect)
		self.bolan_game.screen.blit(self.retry_image, self.retry_rect)





class Scoreboard:
	"""
	Displays the score of the player. Increments as time passes.
	"""


	def __init__(self, bolan_game):
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings

		self.score = 0
		self.font = pygame.font.Font("game_assets/fonts/PressStart2P.ttf", 20)
		with open("game_assets/highscore.txt", 'r') as highscore:
			self.highscore = int(highscore.read())

		# Render images.
		self.render_score_image()
		self.render_highscore_image()


	def render_score_image(self):
		"""
		Turns the score into a rendered image.
		"""
		self.score_image = self.font.render(
			str(self.score), False, (83, 83, 83))
		self.score_rect = self.score_image.get_rect(
			topright=self.bolan_game.screen_rect.topright)
		self.score_rect = (self.score_rect.x - 30, self.score_rect.y + 30)


	def render_highscore_image(self):
		"""
		Turns the highscore into a rendered image.
		"""
		self.highscore_image = self.font.render(
			f"HI {str(self.highscore)}", False, (83, 83, 83))
		self.highscore_rect = self.highscore_image.get_rect(
			topleft=self.bolan_game.screen_rect.topleft)
		self.highscore_rect = (
			self.highscore_rect.x + 30, self.highscore_rect.y + 30)


	def check_highscore(self):
		if self.score > self.highscore:
			self.highscore = self.score
			self.render_highscore_image()


	def update(self):
		"""
		Updates the score.
		"""
		if not self.bolan_game.is_gameover:
			self.score += 1
		self.render_score_image()
		self.check_highscore()


	def blitme(self):
		"""
		Blits the scoreboard onto the screen.
		"""
		self.bolan_game.screen.blit(self.score_image, self.score_rect)
		self.bolan_game.screen.blit(self.highscore_image, self.highscore_rect)




class Cloud:
	"""
	Represents a singular decorative cloud.
	"""


	def __init__(self, bolan_game, x, y):
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings

		self.image = self.settings.cloud_image
		self.rect = self.image.get_rect()

		self.x = x
		self.y = y		


	def update(self):
		"""
		Updates the x-position of the cloud.
		"""
		if self.x <= -self.rect.width:
			self.x = self.settings.screen_width + self.rect.width
		self.x -= 0.1




class Clouds:
	"""
	Represents the decorative clouds in the sky.
	"""


	def __init__(self, bolan_game):
		"""
		Initialize Cloud attributes.
		"""
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings
		self.clouds = [
			Cloud(
				bolan_game, 
				random.choice(self.settings.cloud_x_range), # Randomize x-position between specific range.
				random.choice(self.settings.cloud_y_range), # Randomize y-poistion between specific range.
			) 
			for i in range(self.settings.cloud_number) # Spawn a specific number of clouds.
		]


	def update(self):
		"""
		Updates the cloud objects in self.clouds.
		"""
		for cloud in self.clouds:
			cloud.update()


	def blitme(self):
		"""
		Blits the cloud onto the screen.
		"""
		for cloud in self.clouds:
			self.bolan_game.screen.blit(cloud.image, (cloud.x, cloud.y))




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




class Bolan:
	"""
	Represents Bolan, the T-Rex that the player plays as.
	"""
	

	def __init__(self, bolan_game):
		"""
		Initalize Bolan class attributes.
		"""
		super().__init__()
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings
		self.is_bolan = True

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
		self.image = self.settings.bolan_standing_image
		self.rect = self.image.get_rect(topleft=(self.x, self.y))
		self.mask = pygame.mask.from_surface(self.image)

		# Movement attributes
		self.gravity = 1
		self.is_jump = False
		self.is_duck = False
		self.jump_speed = 1


	def update(self):
		"""
		Updates Bolan.
		"""
		self._increment_animation(self.settings.bolan_update_rate)
		self._update_sprite(self.image_frame, self.image_index, True)
		self._player_control()


	def _increment_animation(self, update_rate):
		"""
		Defines the rate at which Bolan's images change.
		"""
		self.image_frame += 1
		if self.image_frame == update_rate: 
			self.image_frame = 0
			self.image_index += 1


	def _update_sprite(self, image_frame, image_index, is_bolan=False):
		"""
		Updates Bolan's sprite.
		"""
		self.mask = pygame.mask.from_surface(self.image)
		if self.rect.y < self.default_y and is_bolan:
			self.image = self.settings.bolan_standing_image
		else:
			self._animate()


	def _animate(self):
		"""
		Animates Bolan.
		"""
		if self.image_index >= len(self.images):
			self.image_index = 0
		self.image = self.images[self.image_index]


	def _player_control(self):
		"""
		Changes what Bolan does based on user input.
		"""
		if self.is_jump and not self.is_duck:
			self._jump()
		elif self.is_duck and self.rect.y >= self.default_y:
			self._duck()
		else:
			self.images = self.run_images
			self._implement_gravity()


	def _implement_gravity(self):
		"""
		Brings Bolan's y-position down if he's above default_y.
		"""
		if self.rect.y < self.default_y:
			self.rect.y += self.gravity


	def _jump(self):
		"""
		Makes Bolan jump.
		"""
		if self.rect.y > 220:
			self.rect.y -= self.jump_speed
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
		# pygame.draw.rect(self.bolan_game.screen, (0, 0, 0),  self.rect)
		self.bolan_game.screen.blit(self.image, self.rect)





class Obstacle(Bolan):
	"""
	Represents a single Obstacle.
	"""


	def __init__(self, bolan_game, x):
		"""
		Initialize Obstacle class attributes.
		"""
		super().__init__(bolan_game)
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings
		self.x = x

		# Image attributes
		self.pterodactyl_image_frame = 0
		self.pterodactyl_image_index = 0
		self.images_pterodactyl = self.settings.pterodactyl_images
		self.images_cacti = self.settings.cactus_images

		self._initialize_image_attributes()


	def _initialize_image_attributes(self):
		"""
		Reinitializes image attibutes that are continually redefined.
		"""
		self.is_Cactus = True
		self._check_pterodactyl_min_score()
		self._choose_obstacle()
		self.image = random.choice(self.images)
		self.rect = self.image.get_rect(midbottom=(self.x, self.y))
		self.mask = pygame.mask.from_surface(self.image)


	def _check_pterodactyl_min_score(self):
		"""
		Allows game to start spawning Pterodactyls if score is equal to or
		above 10,000 points.
		"""
		if self.bolan_game.scoreboard.score > self.settings.pterodactyl_min_score:
			self.is_Cactus = random.choice([True, False])


	def _choose_obstacle(self):
		"""
		Randomly chooses whether to spawn a Cactus or Pterodactyl obstacle. 
		"""
		if self.is_Cactus:
			self.images = self.images_cacti
			self.y = 530
		else:
			self.images = self.images_pterodactyl
			self.y = random.choice(self.settings.pterodactyl_heights)

			
	def update(self):
		"""
		Updates the Obstacle object.
		"""
		if not self.is_Cactus:
			self._animate_pterodactyl()
		if self.rect.x <= -204:
			self._initialize_image_attributes()
			self.rect.x = self.settings.screen_width + 204
		self.rect.x -= 1


	def _animate_pterodactyl(self):
		"""
		Animates a Pterodactyl.
		"""
		self._increment_animation(self.settings.pterodactyl_update_rate)
		self._update_sprite(
			self.pterodactyl_image_frame, self.pterodactyl_image_index)




class Obstacles:
	"""
	Represents the obstacles that procedurally generate at fixed intervals.
	"""


	def __init__(self, bolan_game):
		"""
		Initialize Obstacles class attributes.
		"""
		self.bolan_game = bolan_game
		self.settings = bolan_game.settings
		self.obstacles = [
			Obstacle(bolan_game, x) for x in range(1400, 2800, 700)]


	def update(self):
		"""
		Update each obstacle in the self.obstacles iterable.
		"""
		for obstacle in self.obstacles:
			obstacle.update()


	def _reset_positions(self):
		x_offset = 700
		for obstacle in self.obstacles:
			obstacle.rect.x = self.settings.screen_width + 204 + x_offset
			obstacle._initialize_image_attributes()
			x_offset += 700


	def blitme(self):
		"""
		Blit the obstacles onto the screen.
		"""
		for obstacle in self.obstacles:
			self.bolan_game.screen.blit(obstacle.image, obstacle.rect)

