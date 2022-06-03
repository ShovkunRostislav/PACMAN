from pygame import *
from random import *

animCount = 0

class GameSprite(sprite.Sprite):
    def __init__(player, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        player.image = transform.scale(image.load(player_image), (size_x, size_y))
        player.speed = player_speed
        player.rect = player.image.get_rect()
        player.rect.x = player_x
        player.rect.y = player_y
    def show(player):
        window.blit(player.image, (player.rect.x, player.rect.y))
class Hero(GameSprite):
    def update(player):
        print('fff')
class Enemy(GameSprite):
    def move(self):
        # move in random directions.
        self.x, self.y = 0, 0
        self.movex, self.movey = 0, 0
        self.movex = randint(-1,1)
        self.movey = randint(-1,1)
        self.x += self.movex
        self.y += self.movey
class Wall(sprite.Sprite):
    def __init__(player, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        player.color1 = color1
        player.color2 = color2
        player.color3 = color3
        player.width = wall_width
        player.height = wall_height
        player.image = Surface((player.width, player.height))
        player.image.fill((color1, color2, color3))
        player.rect = player.image.get_rect()
        player.rect.x = wall_x
        player.rect.y = wall_y
    def draw_wall(player):
        window.blit(player.image, (player.rect.x, player.rect.y))

win_height = 700
win_width = 700
window = display.set_mode((win_width, win_height))
display.set_caption('Pacman Game')
clock = time.Clock()

player = Hero('Pacman_HD.png', 15, 308, 15, 15, 2)
back = transform.scale(image.load('Pacman-Background.png'), (win_height, win_width))
ghost = Enemy('ghost1.png', 350, 320, 15, 20, 2)

w1 = Wall(30,144,255, 0, 0, 700, 30)
w2 = Wall(30,144,255, 0, 20, 30, 210)
w3 = Wall(30,144,255, 0, 200, 145, 30)
w4 = Wall(30,144,255, 115, 200, 30, 95)
w5 = Wall(30,144,255, 0, 270, 145, 30)
w7 = Wall(30,144,255, 670, 20, 30, 210)
w8 = Wall(30,144,255, 556, 200, 145, 30)
w9 = Wall(30,144,255, 556, 200, 30, 95)
w10 = Wall(30,144,255, 556, 270, 150, 30)
w11 = Wall(30,144,255, 335, 0, 30, 95)
w12 = Wall(30,144,255, 187, 70, 110, 30)
w13 = Wall(30,144,255, 406, 70, 110, 30)
w14 = Wall(30,144,255, 187, 470, 110, 30)
w15 = Wall(30,144,255, 406, 470, 110, 30)
w16 = Wall(30,144,255, 190, 335, 30, 95)
w17 = Wall(30,144,255, 485, 335, 30, 95)
w18 = Wall(30,144,255, 0, 670, 700, 30)
w19 = Wall(30,144,255, 0, 400, 30, 280)
w20 = Wall(30,144,255, 0, 400, 145, 30)
w21 = Wall(30,144,255, 115, 340, 30, 70)
w22 = Wall(30,144,255, 0, 334, 145, 30)
w23 = Wall(30,144,255, 670, 400, 30, 280)
w24 = Wall(30,144,255, 556, 340, 30, 70)
w25 = Wall(30,144,255, 556, 334, 145, 30)
w26 = Wall(30,144,255, 556, 400, 150, 30)
w27 = Wall(30,144,255, 16, 530, 60, 30)
w28 = Wall(30,144,255, 624, 530, 60, 30)
w29 = Wall(30,144,255, 260, 340, 180, 30)
w30 = Wall(30,144,255, 260, 135, 180, 30)
w31 = Wall(30,144,255, 260, 530, 180, 30)
w32 = Wall(30,144,255, 260, 400, 180, 30)
w33 = Wall(30,144,255, 190, 135, 30, 160)
w34 = Wall(30,144,255, 335, 135, 30, 95)
w35 = Wall(30,144,255, 335, 405, 30, 95)
w36 = Wall(30,144,255, 335, 542, 30, 95)
w37 = Wall(30,144,255, 190, 535, 30, 95)
w38 = Wall(30,144,255, 485, 535, 30, 95)
w39 = Wall(30,144,255, 485, 135, 30, 160)
w40 = Wall(30,144,255, 75, 70, 70, 30)
w41 = Wall(30,144,255, 75, 133, 70, 30)
w42 = Wall(30,144,255, 555, 70, 70, 30)
w43 = Wall(30,144,255, 555, 133, 70, 30)
w44 = Wall(30,144,255, 555, 470, 70, 30)
w45 = Wall(30,144,255, 75, 470, 70, 30)
w46 = Wall(30,144,255, 115, 470, 30, 95)
w47 = Wall(30,144,255, 555, 470, 30, 95)
w48 = Wall(30,144,255, 75, 600, 220, 30)
w49 = Wall(30,144,255, 405, 600, 220, 30)
w50 = Wall(30,144,255, 215, 200, 85, 30)
w51 = Wall(30,144,255, 405, 200, 85, 30)
w52 = Wall(30,144,255, 260, 270, 70, 30)
w53 = Wall(30,144,255, 370, 270, 70, 30)
w54 = Wall(30,144,255, 260, 275, 30, 95)
w55 = Wall(30,144,255, 410, 275, 30, 95)

walls = sprite.Group()
pacman_group = sprite.Group()

walls.add(w1)
walls.add(w2)
walls.add(w3)
walls.add(w4)
walls.add(w5)
walls.add(w7)
walls.add(w8)
walls.add(w9)
walls.add(w10)
walls.add(w11)
walls.add(w12)
walls.add(w13)
walls.add(w14)
walls.add(w15)
walls.add(w16)
walls.add(w17)
walls.add(w18)
walls.add(w19)
walls.add(w20)
walls.add(w21)
walls.add(w22)
walls.add(w23)
walls.add(w24)
walls.add(w25)
walls.add(w26)
walls.add(w27)
walls.add(w28)
walls.add(w29)
walls.add(w30)
walls.add(w31)
walls.add(w32)
walls.add(w33)
walls.add(w34)
walls.add(w35)
walls.add(w36)
walls.add(w37)
walls.add(w38)
walls.add(w39)
walls.add(w40)
walls.add(w41)
walls.add(w42)
walls.add(w43)
walls.add(w44)
walls.add(w45)
walls.add(w46)
walls.add(w47)
walls.add(w48)
walls.add(w49)
walls.add(w50)
walls.add(w51)
walls.add(w52)
walls.add(w53)
walls.add(w54)
walls.add(w55)

finish = False
game = True

count = 0

while game:
    for e in event.get():
            if e.type == QUIT:
                exit()
    side = 'None'
    keyPressed = key.get_pressed()
    if keyPressed[K_LEFT] and player.rect.x > 5:
        player.rect.x -= player.speed
        if sprite.spritecollide(player, walls, False):
            side = 'Right'
        if side == 'Right':
            print(side)
            player.rect.x += 2
    if keyPressed[K_RIGHT] and player.rect.x < win_width - 40:
        player.rect.x += player.speed
        if sprite.spritecollide(player, walls, False):
            side = 'Left'
        if side == 'Left':
            print(side)
            player.rect.x -= 2
    if keyPressed[K_UP] and player.rect.y > 5:
        player.rect.y -= player.speed
        if sprite.spritecollide(player, walls, False):
            side = 'Down'
        if side == 'Down':
            print(side)
            player.rect.y += 2
    if keyPressed[K_DOWN] and player.rect.y < win_height - 40:
        player.rect.y += player.speed
        if sprite.spritecollide(player, walls, False):
            side = 'Up'
        if side == 'Up':
            print(side)
            player.rect.y -= 2
    if player.rect.x == 660 and 300 < player.rect.y < 330:
        player.rect.x , player.rect.y = 10 , 308
    if player.rect.x == 13 and 300 < player.rect.y < 330:
            player.rect.x , player.rect.y = 660 , 308
    if finish != True:
        window.fill((0,0,0))
        walls.draw(window)
        player.show()
        ghost.show()
        ghost.move() #-- метод движения по случ. направлениям
    display.update()
    clock.tick(60)