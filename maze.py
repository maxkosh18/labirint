from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super(). __init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#игровая сцена
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)

final = GameSprite('png-transparent-treasure-hunting-thepix-buried-treasure-gold-miscellaneous-game-gold-PhotoRoom.png-PhotoRoom.png', win_width - 470, win_height - 90, 0)
final1 = GameSprite('treasure.png', win_width - 270, win_height - 410, 0)
final2 = GameSprite('treasure.png', win_width - 580, win_height - 90, 0)
final3 = GameSprite('treasure.png', win_width - 300, win_height - 190, 0)
final4 = GameSprite('treasure.png', win_width - 470, win_height - 200, 0)
final5 = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
gold = GameSprite('kkeyka-PhotoRoom.png-PhotoRoom.png', win_width - 120, win_height - 330, 0)

w1 = Wall(255, 0, 0, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 470, 10)
w3 = Wall(255, 0, 0, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 200, 110, 10, 380)
w5 = Wall(255, 0, 0, 300, 20, 10, 150)
w6 = Wall(255, 0, 0, 400, 180, 10, 100)
w7 = Wall(154, 205, 50, 400, 385, 10, 100)
w8 = Wall(154, 205, 50, 210, 380, 100, 10)
w9 = Wall(154, 205, 50, 210, 280, 100, 10)
w10 = Wall(154, 205, 50, 300, 385, 10, 100)

life = 0
finish = False
game = True
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 45)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', False, (180, 0, 0))

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        life1 = font.render('Собрано монет: ' + str(life), 1, (255, 255, 25))
        window.blit(background,(0, 0))
        player.reset()
        player.update()
        monster.reset()
        monster.update()

        final.reset()
        final1.reset()
        final2.reset()
        final3.reset()
        final4.reset()
        final5.reset()
        gold.reset()
        
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        
        if sprite.collide_rect(player, final1):
            life = life + 1
            final1.rect.x = -100
        if sprite.collide_rect(player, final2):
            life = life + 1
            final2.rect.x = -100
        if sprite.collide_rect(player, final3):
            life = life + 1
            final3.rect.x = -100
        if sprite.collide_rect(player, final4):
            life = life + 1
            final4.rect.x = -100
        if sprite.collide_rect(player, final5):
            life = life + 1
            final5.rect.x = -100

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2)or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()

        if sprite.collide_rect(player, gold):
            gold.rect.x = -100
            w10.rect.x = -100

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()

    window.blit(life1, (400, 50))
    display.update()
    clock.tick(FPS)