
import pygame

class Ammo(pygame.sprite.Sprite):
    score = 0

    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)  # inherit from sprite
        self.vel = 5
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        score = 0
        self.rect.x += (self.direction * self.vel) + camera_scroll

        if self.rect.right > width or self.rect.right < 0:
            self.kill()

        if pygame.sprite.spritecollide(player, ammo_group, False):
            if player.alive:
                player.health -= 20
                self.kill()

        if pygame.sprite.spritecollide(self, enemy_group, False):
            self.kill()

        collided_enemy = pygame.sprite.spritecollideany(self, enemy_group)
        if collided_enemy:
            enemy_audio.play()
            collided_enemy.kill()