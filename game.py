import pygame

pygame.init()



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







class Character(pygame.sprite.Sprite):

    def __init__(self, char_type, x, y, vel, bullet):
        self.index = 0
        self.char_type = char_type
        self.vel = vel

        self.img_list = []
        self.frame_index = 0
        self.state = 0
        self.update_time = pygame.time.get_ticks()

        self.shoot_timer = 0
        self.bullet = bullet
        self.initial_bullet = bullet

        img_state = ['idle', 'run', 'jump', 'dead']
        for state in img_state:
            images = []
            num_of_img = len(os.listdir(f'img/{self.char_type}/{state}'))

            for num in range(num_of_img):
                img = pygame.image.load(f'img/{self.char_type}/{state}/{num}.png').convert_alpha()
                img = pygame.transform.scale(img, (40, 80)).convert_alpha()
                images.append(img)
            self.img_list.append(images)
        self.image = self.img_list[self.state][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.jump_vel = 0
        self.jump = False
        self.direction = 1
        self.flip = False
        self.jumping = True

        self.alive = True
        self.health = 100
        self.max_health = self.health
        self.health_timer = 0
        self.decrease = False

        self.mask = pygame.mask.from_surface(self.image)
        self.move_timer = 0
        self.stop = False

    def character_state(self):
        change_time = 100
        self.image = self.img_list[self.state][self.frame_index]

        if pygame.time.get_ticks() - self.update_time > 100:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.img_list[self.state]):
            if self.state == 3:
                self.frame_index = len(self.img_list[self.state]) - 1
            else:
                self.frame_index = 0

    def check_state(self, new_state):
        if new_state != self.state:
            self.state = new_state
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def shoot(self):
        if self.shoot_timer == 0 and self.bullet > 0:
            self.shoot_timer = 20
            ammo = Ammo(self.rect.centerx + (self.rect.size[0] * self.direction), self.rect.centery,
                        self.direction)
            ammo_group.add(ammo)

            self.bullet -= 1

    def update(self):
        self.character_state()
        self.death()

        if self.shoot_timer > 0:
            self.shoot_timer -= 1

    def move(self, turn_left, turn_right):
        camera_scroll = 0
        change_x = 0
        change_y = 0

        # turning
        if turn_right:
            change_x = self.vel
            self.flip = False
            self.direction = 1
        elif turn_left:
            change_x = -self.vel
            self.flip = True
            self.direction = -1

        # falling

        if self.jump == True and self.jumping == False:
            self.jump_vel = -19
            self.jump = False
            self.jumping = True

        self.jump_vel += 1
        if self.jump_vel > 10:
            self.jump_vel
        change_y += self.jump_vel

        for objects in world.collision_tiles:
            # getting rect by[1]
            if objects[1].colliderect(self.rect.x + change_x, self.rect.y, self.width, self.height):
                change_x = 0

                if self.char_type == 'enemy':
                    self.direction *= -1
                    self.move_timer = 0

            if objects[1].colliderect(self.rect.x, self.rect.y + change_y, self.width, self.height):
                if self.jump_vel < 0:
                    self.jump_vel = 0
                    change_y = objects[1].bottom - self.rect.top

                elif self.jump_vel >= 0:
                    self.jump_vel = 0
                    self.jumping = False
                    change_y = objects[1].top - self.rect.bottom


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

pygame.display.update()