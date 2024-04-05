from pygame import *
from random import randint
font.init()
font1 = font.Font(None, 36)
img_rocket = "rocket.png"
img_ball = "ball.png"
img_back = "background.png"
lost = 0
score = 0
win = False
lose = False
speed_x = 3
speed_y = 3
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

win_width = 700
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

rocket1 = Rocket1(img_rocket, 100, 200, 75, 150, 6)
rocket2 = Rocket2(img_rocket, 600, 200, 75, 150, 6)
ball = Ball(img_ball, 350, 250, 60, 60, 5)

right_score = 0
left_score = 0
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        window.blit(background, (0,0))
        rocket1.update()
        rocket2.update()
        rocket1.reset()
        rocket2.reset()
        if ball.rect.x <= 0:
            right_score += 1
            ball.rect.x, ball.rect.y = 350, 250
        right_txt = font1.render('Счёт правого игрока: ' + str(right_score), True, (180, 0, 0))
        window.blit(right_txt, (20, 60))   
        if ball.rect.x >= win_width:
            left_score += 1
            ball.rect.x, ball.rect.y = 350, 250
        left_txt = font1.render('Счёт левого игрока: ' + str(left_score), True, (180, 0, 0))
        window.blit(left_txt, (20, 30))
        if right_score >= 10:
            win_right = font1.render('Правый игрок выиграл!', True, (randint(0, 255), randint(0, 255), randint(0, 255)))
            window.blit(win_right, (250, 250))
        if left_score >= 10:
            win_left = font1.render('Левый игрок выиграл!', True, (randint(0, 255), randint(0, 255), randint(0, 255)))
            window.blit(win_left, (250, 250))
        ball.reset()
        display.update()
        time.delay(20)