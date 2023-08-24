import pygame
from random import randint

pygame.init()

FPS = 60
window = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
# background = pygame.image.load("galaxy.jpg")
# background = pygame.transform.scale(background, (700, 500))

# fire_snd = pygame.mixer.Sound("fire.ogg")

class GameSprite():
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.transform.scale(image, (w, h))
    def paint(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, x, y, w, h, image, speed, go_up, go_down):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.go_up = go_up
        self.go_down = go_down

    def move(self):
        k = pygame.key.get_pressed()
        if k[self.go_up]:
            self.rect.y += self.speed
        if k[self.go_down]:
            self.rect.y -= self.speed

player_img = pygame.image.load("raket.jpg")    
player1 = Player(10, 10, 20, 40, player_img, 4, pygame.K_w, pygame.K_s)
game = True
finish = False

while game:

    if not finish:
        window.fill((200, 10, 50))
        player1.paint()
        player1.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    clock.tick(FPS)
    pygame.display.update()
