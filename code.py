import pygame


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.image.load('data/gameover.png')
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0

    def update(self):
        self.rect.x += 4


pygame.init()
all_sprites = pygame.sprite.Group()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 255))
game_over = GameOver()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game_over.rect.x < 0:
        all_sprites.update()
    screen.fill((0, 0, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(50)
