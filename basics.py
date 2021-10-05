import pygame
pygame.mixer.init()


pygame.display.init()
pygame.font.init()

tile_types = 33
width = 800
height = 640
level = 0
rows = 16
columns = 150
tile_size = height // rows
scroll_width = 200
camera_scroll = 0
bg_scroll = 0

coin_score = 0
bullet = 20
font = pygame.font.SysFont('commissars', 30)

screen = pygame.display.set_mode((width, height))

images = []
for i in range(tile_types):
    img = pygame.image.load(f'img/tile/{i}.png')
    img = pygame.transform.scale(img, (tile_size, tile_size))
    images.append(img)