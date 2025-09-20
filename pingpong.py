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
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_height = 600
win_width = 700

window = display.set_mode((win_width, win_height))
display.set_caption("The Smash")

background = transform.scale(image.load("C:/Users/ASUS/.vscode/extensions/algoritmika.algopython-20250918.133302.0/temp/pingpong/background (1).jpg"), (win_width, win_height))
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 35)
lose1 = font.render("Player 1 Lose!!!", True, (180, 0, 0))
lose2 = font.render("Player 2 Lose!!!", True, (180, 0, 0))

# variable score
score1 = 0  
score2 = 0  
max_score = 5  

racket1 = Player("C:/Users/ASUS/.vscode/extensions/algoritmika.algopython-20250918.133302.0/temp/pingpong/racket.png", 30, 200, 25, 80, 10)
racket2 = Player("C:/Users/ASUS/.vscode/extensions/algoritmika.algopython-20250918.133302.0/temp/pingpong/racket.png", 620, 200, 25, 80, 10)
ball = GameSprite("C:/Users/ASUS/.vscode/extensions/algoritmika.algopython-20250918.133302.0/temp/pingpong/pingpong.png", 200, 200, 40, 40, 50)


ball_size = 40  # ukuran awal bola
min_ball_size = 10  # ukuran bola paling kecil

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

        # menampilkan score
        score_text1 = font.render("Player 1: "+ str(score1), True, (255, 0, 0))
        score_text2 = font.render("Player 2: " + str(score2), True, (0, 0, 255))
        window.blit(score_text1, (100, 25))
        window.blit(score_text2, (win_width - 250, 25))

        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_r()
        racket2.update_l()
        ball.update()
        if sprite.collide_rect(racket1, ball):
            speed_x *= -1
            speed_y *= 1
            # meningkatkan kecepatan dan mengecilkan ukuran bola saat menyentuh raket 1
            if ball_size > min_ball_size:
                speed_x += 0.2  
                speed_y += 0.2
                ball_size -= 3  
                # Update gambar bola agar tidak error
                ball.image = transform.scale(image.load("C:/Users/ASUS/.vscode/extensions/algoritmika.algopython-20250918.133302.0/temp/pingpong/pingpong.png"), (ball_size, ball_size))
                ball.rect = ball.image.get_rect(center=ball.rect.center)  

        if sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
            # meningkatkan kecepatan dan mengecilkan ukuran bola saat menyentuh raket 2
            if ball_size > min_ball_size:
                speed_x += 0.2  
                speed_y += 0.2
                ball_size -= 3  
                # Update gambar bola agar tidak error
                ball.image = transform.scale(image.load("C:/Users/ASUS/.vscode/extensions/algoritmika.algopython-20250918.133302.0/temp/pingpong/pingpong.png"), (ball_size, ball_size))
                ball.rect = ball.image.get_rect(center=ball.rect.center) 
        if ball.rect.y > win_height - 50:
            speed_y *= -1
        if ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0: #kondsisi jika bola melewati raket 1
            score2 += 1
            # mengembalikan bola ketengah
            ball.rect.x = win_width // 2
            ball.rect.y = win_height // 2
            ball_size = 40  # mengembalikan ukuran bola
            speed_multiplier = 1.0  # mengembalikan kecepatan bola
            speed_x = 3  # bola mengarah ke kanan
            speed_y = 3
            # U
            ball.image = transform.scale(image.load("C:/Users/ASUS/.vscode/extensions/algoritmika.algopython-20250918.133302.0/temp/pingpong/pingpong.png"), (ball_size, ball_size))
            ball.rect = ball.image.get_rect(center=(ball.rect.x, ball.rect.y))

        if ball.rect.x > win_width: # kondisi jika bola melewati raket 2
            score1 += 1
            # menbgembalikan bola ketengah
            ball.rect.x = win_width // 2
            ball.rect.y = win_height // 2
            ball_size = 40  # mengembalikan ukuran bola
            speed_multiplier = 1.0  # mengembalikan kecepatan bola
            speed_x = -3  # bola mengarah kekiri
            speed_y = 3
            ball.image = transform.scale(image.load("C:/Users/ASUS/.vscode/extensions/algoritmika.algopython-20250918.133302.0/temp/pingpong/pingpong.png"), (ball_size, ball_size))
            ball.rect = ball.image.get_rect(center=(ball.rect.x, ball.rect.y))

        # kondisi menang
        if score1 >= max_score or score2 >= max_score:
            finish = True
            if score1 >= max_score:
                window.blit(lose2, (200, 200))  # Player 1 menang
            else:
                window.blit(lose1, (200, 200))  # Player 2 menang
        
    display.update()
    clock.tick(FPS)
