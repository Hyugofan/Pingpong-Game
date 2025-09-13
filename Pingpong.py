from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        ball.rect.x += speed_x
        ball.rect.y += speed_y

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

win_height = 600
win_width = 700

window = display.set_mode((win_width, win_height))
display.set_caption("The Smash")

background = transform.scale(image.load("C:/Users/ASUS/.vscode/extensions/algoritmika.algopython-20250624.103906.0/temp/Ping-pong/background.jpg"), (win_width, win_height))
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 35)
lose1 = font.render("Player 1 Lose!!!", True, (180, 0, 0))
lose2 = font.render("Player 2 Lose!!!", True, (180, 0, 0))

racket1 = Player("C:/Users/ASUS/.vscode/extensions/algoritmika.algopython-20250624.103906.0/temp/Ping-pong/racket.png", 30, 200, 25, 80, 10)
racket2 = Player("C:/Users/ASUS/.vscode/extensions/algoritmika.algopython-20250624.103906.0/temp/Ping-pong/racket.png", 620, 200, 25, 80, 10)
ball = GameSprite("C:/Users/ASUS/.vscode/extensions/algoritmika.algopython-20250624.103906.0/temp/Ping-pong/pingpong.png", 200, 200, 40, 40, 50)

speed_x = 3
speed_y = 3

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_r()
        racket2.update_l()
        ball.update()
        if sprite.collide_rect(racket1, ball):
            speed_x *= -1
            speed_y *= 1
        if sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height - 50:
            speed_y *= -1
        if ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game = True
        
    display.update()
    clock.tick(FPS)

