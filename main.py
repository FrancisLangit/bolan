import pygame, sys
pygame.init()

screen = pygame.display.set_mode((1280, 600)) 
pygame.display.set_caption("Bolan.py")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()