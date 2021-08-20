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

font = pygame.font.SysFont('commissars', 30)
screen = pygame.display.set_mode((width, height))
bullet_img = pygame.image.load('img/bullet .png').convert_alpha()
box_img = pygame.image.load('img/box.png').convert_alpha()

images = []





