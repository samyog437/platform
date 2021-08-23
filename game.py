import pygame

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
fps = 60
keys = pygame.key.get_pressed()

turn_left = False
turn_right = False

font = pygame.font.SysFont("comicsansms", 20)
fon2 = pygame.font.SysFont("comicsansms", 30)

pygame.display.set_caption("Runnin")

sun_img = pygame.image.load('img/sun.png')
sun_img = pygame.transform.scale(sun_img, (tile_size, tile_size))
bg_img = pygame.image.load('img/sky.png').convert_alpha()
bg_img = pygame.transform.scale(bg_img, (width, height))
pine1_img = pygame.image.load('img/pine1.png').convert_alpha()
pine2_img = pygame.image.load('img/pine2.png').convert_alpha()
mountain_img = pygame.image.load('img/mountain.png').convert_alpha()
sky_img = pygame.image.load('img/sky_cloud.png').convert_alpha()

restart_img = pygame.image.load('img/restart_btn.png').convert_alpha()
exit_img = pygame.image.load('img/exit_btn.png').convert_alpha()
start_img = pygame.image.load('img/start_btn.png').convert_alpha()
save_img = pygame.image.load('img/save_btn.png').convert_alpha()

score_coin_img = pygame.image.load('img/tile/32.png').convert_alpha()
coin_img = pygame.transform.scale(score_coin_img, (25, 25))

bullet_count = pygame.transform.scale(bullet_img, (25, 25))

nameActive = False
newName = ""
user = ""

passActive = False
newPass = ""
passw = ""
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def restart():
    ammo_group.empty()
    danger_group.empty()
    decoration_group.empty()
    treasure_group.empty()
    exit_group.empty()
    enemy_group.empty()

    data = []
    for row in range(rows):
        r = [-1] * columns
        data.append(r)
    return data


def draw_bg():
    s_width = sky_img.get_width()
    for x in range(5):
        screen.blit(bg_img, ((x * width) - bg_scroll * 0.5, 0))
        screen.blit(mountain_img, ((x * s_width) - bg_scroll * 0.6, height - mountain_img.get_height() - 300))
        screen.blit(pine1_img, ((x * s_width) - bg_scroll * 0.7, height - pine1_img.get_height() - 150))
        screen.blit(pine2_img, ((x * s_width) - bg_scroll * 0.8, height - pine2_img.get_height()))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
pygame.display.update()