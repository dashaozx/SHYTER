from pygame import*
from random import randint
from time import time as time_count
font.init()
window = display.set_mode()
background = transform.scale(image.load('mlechnyj_put.jpg'), window.get_size()
)
class GameSprite (sprite.Sprite):
    def __init__(self, x,y,height, width, filename):
        super().__init__()
        self.image = image.load(filename)
        self.image = transform.scale(self.image, (height, width))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
    
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def move(self):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_d]:
            self.rect.x -= 5
        if pressed_keys[K_a]:
            self.rect.x += 5

    
    #def move(self):         
      #  pressed_keys = key.get_pressed()
     #   if pressed_keys[K_w]:
       #     self.hitbox.y -= 2
      #  if pressed_keys[K_s]:
      #      self.hitbox.y += 2
      #  if pressed_keys[K_d]:
       #     self.hitbox.x += 2
      #  if pressed_keys[K_a]:
        #    self.hitbox.x -= 2

    #def is_touch(self, sprite):
     #   return self.hitbox.colliderect(sprite.hitbox)
    def update(self):
        self.rect.y += 1
        if self.rect.y > window.get_height():
            self.kill()

    def print(self):
        font.Font()
        my_font = font.Font(None, 50)
        text = my_font.render("Счет", True, (106,90,205))
        window.blit(text, (60, 85))

    def schetchik(self):
        font.Font()
        my_font = font.Font(None, 50)
        schet_text = my_font.render(str(schet), True, (106,90,205))
        window.blit(schet_text, (100, 150))

    def defeat(self):
        font.Font()
        my_font = font.Font(None, 50)
        text = my_font.render("Проигрыш", True, (139, 0, 0))
        window.blit(text, (450, 450))


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= 5
        if self.rect.y < 0:
            self.kill()
    #def last_bullet(self):
     #   last_shot_time = time.time()
      #  if (time.time() - last_shot_time) >= 0.5:
       #     last_shot_time = time.time() 


            
rocket = GameSprite(500, 500, 150, 100, "rockets.png")
enemies = sprite.Group()
bullets = sprite.Group()

schet = 0
clock = time.Clock()
game = True 
last_bullet = time_count()
run = True
while game:
    for e in event.get():
        if e.type == QUIT or(e.type == KEYDOWN and e.key == K_ESCAPE):
            game = False
    if run == True:
        while len(enemies) < 7:
            x = randint(0, window.get_height() - 100)
            Ovni = GameSprite(x, 0, 200, 150, "ovni.png")
            enemies.add(Ovni)
        pressed_keys = key.get_pressed()
        if pressed_keys[K_SPACE] and time_count() - last_bullet > 0.5:
            last_bullet = time_count()
            bullet = Bullet(rocket.rect.x + 100, rocket.rect.y, 40, 25, "bullet.png" )
            bullets.add(bullet)
        dead_ufo = sprite.groupcollide(bullets, enemies, True, True)
        if len(dead_ufo) > 0:
            schet += len(dead_ufo)
        window.blit(background, (0,0))
        if  Ovni.rect.y > rocket.rect.y:
            rocket.defeat()
            run = False
        rocket.print()
        rocket.schetchik()
        enemies.update()
        enemies.draw(window)
        bullets.update()
        bullets.draw(window)
        rocket.move()
        rocket.draw()
        Ovni.draw()
    display.update() 
    clock.tick(60) 