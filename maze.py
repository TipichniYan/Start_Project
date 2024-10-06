from pygame import *


window = display.set_mode((700,500))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (700,500))
clock = time.Clock()

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(40,40))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Monster(GameSprite):
    diretion = 'left'
    def update(self):
        if self.rect.x < 470:
            self.diretion = 'right'
        if self.rect.x > 620:
            self.diretion = 'left'
        if self.diretion == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Enemy(GameSprite):
    diretion = 'down'
    def update(self):
        if self.rect.y < 200:
            self.diretion = 'up'
        if self.rect.y > 400:
            self.diretion = 'down'
        if self.diretion == 'down':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.image = Surface((wall_width, wall_height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        walls.add(self)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed   
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed   
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed   
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed   
font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN', True, (0,255,0))
lose = font.render('YOU LOSE', True, (255,0,0))
lol_2 = Enemy('cyborg.png',5, 400, 200)
player = Player('pacman.png', 6, 20, 400)
lol = Monster('hero.png',5, 500, 100)
gold = GameSprite('chery.png', 680, 600, 350)
walls = sprite.Group()
w1 = Wall(150,200,100,1,0,700, 10)
w2 = Wall(150,200,100,100,80,10, 500)
w3 = Wall(150,200,100,100,80,100, 10)
w4 = Wall(150,200,100,190,80,10, 500)
w5 = Wall(150,200,100,290,0,10, 300)
w6 = Wall(150,200,100,200,400,500, 10)
w7 = Wall(150,200,100,370,0,10, 300)
w8 = Wall(150,200,100,290,290,100, 10)
w9 = Wall(150,200,100,450,0,10, 300)
w9 = Wall(150,200,100,550,150,10, 250)
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))
        player.reset()
        player.update()
        lol.reset()
        lol.update()
        lol_2.reset()
        lol_2.update() 
        gold.reset()
        if sprite.collide_rect(player, gold):
            finish = True
            window.blit(win, (200,300))
            money.play()
        if sprite.spritecollide(player, walls, False) or sprite.collide_rect(player, lol) or sprite.collide_rect(player, lol_2):
            finish = True
            window.blit(lose, (200,300))
            kick.play()
    walls.draw(window)
    display.update()
    clock.tick(60)