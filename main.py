import pygame, sys
pygame.init()

screen = pygame.display.set_mode((1280, 600)) 
pygame.display.set_caption("Bolan.py")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()