from pygame import *
from random import randint
font.init()
f = font.SysFont(None, 96)
font2 = font.SysFont(None, 36)
img_rocket = "rocket.png"
img_ball = "ball.png"
img_back = "background.png"
lost = 0
score = 0
win = False
lose = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Rocket1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height:
            self.rect.y += self.speed
class Rocket2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_i] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_k] and self.rect.y < win_height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        if ball.collide(rocket1):
            self.rect.x += 123
            self.rect.y += randint(-5,5)
        #self.rect.y -= self.speed
        #global vic
rocket1 = Rocket1(img_rocket, 100, 200, 75, 150, 5)
rocket2 = Rocket2(img_rocket, 600, 200, 75, 150, 5)
ball = Ball(img_ball, 350, 250, 60, 60, 5)
win_width = 700
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
rocket1 = Rocket1(img_rocket, 100, 200, 75, 150, 5)
rocket2 = Rocket2(img_rocket, 600, 200, 75, 150, 5)
ball = Ball(img_ball, 350, 250, 60, 60, 5)

finish = False
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        #if e.type == KEYDOWN:
        #    if e.key == K_SPACE:
        #       ship.fire()
    if not finish:
        window.blit(background, (0,0))
        rocket1.update()
        rocket2.update()
        rocket1.reset()
        rocket2.reset()
        #ball.update()
        ball.reset()
        display.update()
        time.delay(50)