# Helper functions.


def get_sprites(bolan_game, number, x, y, width, height):
	"""
	Returns a list of images from the spritesheet.
	"""
	rects = list()
	for i in range(number):
		rects.append([x, y, width, height])
		x += width
	return bolan_game.spritesheet.images_at(rects, (0, 0, 0))
