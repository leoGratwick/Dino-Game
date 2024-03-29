#import pygame
import pygame, sys
import math
from pygame import VIDEORESIZE, K_f, K_ESCAPE
import button
import random



#gihub link http://codingwithruss.com/pygame/shooter/music.html


pygame.init()
pygame.font.init() # you have to call this at the start,
                   # if you want to use fonts.

myfont = pygame.font.SysFont('Comic Sans MS', 30)
printList =[]
print(pygame.font.get_fonts())
# game variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 0.75
rightclick = False
TILESIZE = 40


#COLOURS

RED = (200, 20, 50)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
LIGHTGREEN = (50,150,50)
BLACK = (0, 0, 0)
PINK = (235, 65, 54)
LIGHTBLUE = (70,70, 200)

# player variables
moving_right = False
moving_left = False
jump = False


# set framerate
clock = pygame.time.Clock()
FPS = 60

monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Dino Game')
fullscreen = False
bgscroll = 0

# load images
# buttons
start_button = pygame.image.load('start_btn.png')
exit_button = pygame.image.load('exit_btn.png')

# player and enemy animations
player_img = [[pygame.image.load("player/idle0.png"), pygame.image.load("player/idle1.png"), pygame.image.load("player/idle2.png"), pygame.image.load("player/idle3.png")],
          [pygame.image.load("player/run0.png"), pygame.image.load("player/run1.png"), pygame.image.load("player/run2.png"), pygame.image.load("player/run3.png"), pygame.image.load("player/run4.png"),
           pygame.image.load("player/run5.png")], [pygame.image.load("player/jump0 .png")], [pygame.image.load("player/kick0.png"), pygame.image.load("player/kick1.png"), pygame.image.load("player/kick2.png")],
          [pygame.image.load("player/hurt0.png"), pygame.image.load("player/hurt1.png"), pygame.image.load("player/hurt2.png"), pygame.image.load("player/hurt3.png")],
          [pygame.image.load("player/tile017.png"), pygame.image.load("player/tile018.png"), pygame.image.load("player/tile019.png"), pygame.image.load("player/tile019.png"), pygame.image.load("player/tile020.png"),
           pygame.image.load("player/tile021.png"), pygame.image.load("player/tile022.png"), pygame.image.load("player/tile023.png")]]

enemy2_img = [[pygame.image.load("enemy/idle0.png"), pygame.image.load("enemy/idle1.png"), pygame.image.load("enemy/idle2.png"), pygame.image.load("enemy/idle3.png")],
          [pygame.image.load("enemy/run0.png"), pygame.image.load("enemy/run1.png"), pygame.image.load("enemy/run2.png"), pygame.image.load("enemy/run3.png"), pygame.image.load("enemy/run4.png"),
           pygame.image.load("enemy/run5.png")], [pygame.image.load("enemy/jump0.png")], [pygame.image.load("enemy/kick0.png"), pygame.image.load("enemy/kick1.png"), pygame.image.load("enemy/kick2.png")],
          [pygame.image.load("enemy/hurt0.png"), pygame.image.load("enemy/hurt1.png"), pygame.image.load("enemy/hurt2.png"), pygame.image.load("enemy/hurt3.png")], [pygame.image.load("enemy/tile017.png"),
            pygame.image.load("enemy/tile018.png"), pygame.image.load("enemy/tile019.png"), pygame.image.load("enemy/tile019.png"), pygame.image.load("enemy/tile020.png"),
           pygame.image.load("enemy/tile021.png"), pygame.image.load("enemy/tile022.png"), pygame.image.load("enemy/tile023.png")]]

enemy3_img = [[pygame.image.load("enemy2/tile000.png"), pygame.image.load("enemy2/tile001.png"), pygame.image.load("enemy2/tile002.png"), pygame.image.load("enemy2/tile003.png")],
          [pygame.image.load("enemy2/tile004.png"), pygame.image.load("enemy2/tile005.png"), pygame.image.load("enemy2/tile006.png"), pygame.image.load("enemy2/tile007.png"), pygame.image.load("enemy2/tile008.png"),
           pygame.image.load("enemy2/tile009.png")], [pygame.image.load("enemy2/tile010.png")], [pygame.image.load("enemy2/tile010.png"), pygame.image.load("enemy2/tile011.png"), pygame.image.load("enemy2/tile012.png")],
          [pygame.image.load("enemy2/tile013.png"), pygame.image.load("enemy2/tile014.png"), pygame.image.load("enemy2/tile015.png"), pygame.image.load("enemy2/tile016.png")], [pygame.image.load("enemy2/tile017.png"),
            pygame.image.load("enemy2/tile018.png"), pygame.image.load("enemy2/tile019.png"), pygame.image.load("enemy2/tile019.png"), pygame.image.load("enemy2/tile020.png"),
           pygame.image.load("enemy2/tile021.png"), pygame.image.load("enemy2/tile022.png"), pygame.image.load("enemy2/tile023.png")]]

enemy_img = [[pygame.image.load("enemy3/tile000.png"), pygame.image.load("enemy3/tile001.png"), pygame.image.load("enemy3/tile002.png"), pygame.image.load("enemy3/tile003.png")],
          [pygame.image.load("enemy3/tile004.png"), pygame.image.load("enemy3/tile005.png"), pygame.image.load("enemy3/tile006.png"), pygame.image.load("enemy3/tile007.png"), pygame.image.load("enemy3/tile008.png"),
           pygame.image.load("enemy3/tile009.png")], [pygame.image.load("enemy3/tile010.png")], [pygame.image.load("enemy3/tile010.png"), pygame.image.load("enemy3/tile011.png"), pygame.image.load("enemy3/tile012.png")],
          [pygame.image.load("enemy3/tile013.png"), pygame.image.load("enemy3/tile014.png"), pygame.image.load("enemy3/tile015.png"), pygame.image.load("enemy3/tile016.png")], [pygame.image.load("enemy3/tile017.png"),
            pygame.image.load("enemy3/tile018.png"), pygame.image.load("enemy3/tile019.png"), pygame.image.load("enemy3/tile019.png"), pygame.image.load("enemy3/tile020.png"),
           pygame.image.load("enemy3/tile021.png"), pygame.image.load("enemy3/tile022.png"), pygame.image.load("enemy3/tile023.png")]]

magic_balls = [pygame.image.load("items/tile1.png"), pygame.image.load("items/tile2.png"),pygame.image.load("items/tile3.png")] #green red blue

heart_img = pygame.image.load("items/heart.png")

chest_img = pygame.image.load("items/tile009.png")

tile_img = [pygame.image.load("Final tiles/1.png"), pygame.image.load("Final tiles/2.png"),pygame.image.load("Final tiles/3.png"),pygame.image.load("Final tiles/4.png"),pygame.image.load("Final tiles/5.png"),
            pygame.image.load("Final tiles/6.png"), pygame.image.load("Final tiles/7.png"), pygame.image.load("Final tiles/8.png")]

bg_img = [pygame.image.load("Backgroundimage - Copy.png"), pygame.image.load("Backgroundimage - Copy - Copy.png")]


# level

test_level = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,1,2,2,2,2,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [2,2,2,2,2,8,8,8,8,8,8,8,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
              [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
              [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
              [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
              [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
              [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
              [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
              [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
              [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
              [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]]

test_level2 = [[0,0],[1,1]]
#background

def printcheck(item, message) :
    message = str(message)
    printList.append(message)
    if printList[printList.__len__() -2] != message :
        print(item, message)


def fill_bg():
    screen.fill(LIGHTBLUE)
    screen.blit(bg_img[1], (0,0))
    for i in range(4):
        screen.blit(bg_img[0], (i*bg_img[0].get_width() - bgscroll,0))

def gemcounter():
    #green gem counter
    #screen.blit(magic_balls[0], (SCREEN_WIDTH/3, SCREEN_HEIGHT/14))
    #Greennumber = myfont.render(str(player.gemnumber[0]), True, (0, 0, 0))
    #screen.blit(Greennumber, (SCREEN_WIDTH/3 + 2*(SCREEN_WIDTH/20), SCREEN_HEIGHT / 14))
    #red gem counter
    #screen.blit(magic_balls[1], (SCREEN_WIDTH / 3 + 4*(SCREEN_WIDTH/20), SCREEN_HEIGHT / 14))
    #Rednumber = myfont.render(str(player.gemnumber[1]), True, (0, 0, 0))
    #screen.blit(Rednumber, (SCREEN_WIDTH / 3 + 6 * (SCREEN_WIDTH / 20), SCREEN_HEIGHT / 14))
    # blue gem counter

    #screen.blit(magic_balls[2], (SCREEN_WIDTH / 3 + 8*(SCREEN_WIDTH/20), SCREEN_HEIGHT / 14))
    #Bluenumber = myfont.render(str(player.gemnumber[2]), True, (0, 0, 0))
    #screen.blit(Bluenumber, (SCREEN_WIDTH / 3 + 10 * (SCREEN_WIDTH / 20), SCREEN_HEIGHT / 14))





    screen.blit(magic_balls[0], (10, 60))
    Greennumber = myfont.render(str(player.gemnumber[0]), True, (0, 0, 0))
    screen.blit(Greennumber, (60,  60))
    # red gem counter
    screen.blit(magic_balls[1], (10, 110))
    Rednumber = myfont.render(str(player.gemnumber[1]), True, (0, 0, 0))
    screen.blit(Rednumber, ( 60, 110))
    # blue gem counter

    screen.blit(magic_balls[2], ( 10, 160))
    Bluenumber = myfont.render(str(player.gemnumber[2]), True, (0, 0, 0))
    screen.blit(Bluenumber, ( 60, 160))

def Attack_defence():
    attack = myfont.render('attack : ' + str(player.attacklevel), True, (0, 0, 0))
    screen.blit(attack, (SCREEN_WIDTH - 600,10))
    defence = myfont.render('defence : ' + str(player.defencelevel), True, (0, 0, 0))
    screen.blit(defence, (SCREEN_WIDTH- 400, 10))

def displaylevel():
    level = myfont.render('level : ' + str(player.level), True, (0, 0, 0))
    screen.blit(level, (SCREEN_WIDTH-170, 10))

def displayplayerstats():
    gemcounter()
    Attack_defence()
    displaylevel()

# character class
class Dino(pygame.sprite.Sprite):
    def __init__(self, x, y, char_type):
        pygame.sprite.Sprite.__init__(self)
        self.width = player_img[0][0].get_width()
        self.height = player_img[0][0].get_height()
        self.scale = 1
        self.image = pygame.transform.scale(player_img[0][0], (int(self.width * self.scale), int(self.height * self.scale))).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = 1
        self.char_type = char_type
        self.action = 0
        self.flip = False
        self.frame_index = 0
        self.vel_y = 0
        self.time = pygame.time.get_ticks()
        self.in_air = False
        self.alive = True
        self.animation_count =0
        self.jump = False
        self.attack = False
        self.shift = False
        self.level = 1
        self.lasttime = pygame.time.get_ticks()
        self.moving = False

        # assign dino health, speed, attack level and type depending on the on what type of enemy it is or player
        if char_type == player_img :
            self.health = 1500
            self.type = "player"
            self.attacklevel = 1
            self.speed = 3
        elif char_type == enemy2_img:
            self.health = 500
            self.type = "enemy"
            self.attacklevel = 0.5
            self.speed = 1

        elif char_type == enemy_img:
            self.health = 100
            self.type = "enemy"
            self.attacklevel = 0.2
            self.speed = 1

        elif char_type == enemy3_img:
            self.health = 300
            self.type = "enemy"
            self.attacklevel = 1
            self.speed = 2


        self.maxhealth = self.health
        self.ogspeed = self.speed

        self.gemnumber = [0, 0, 0]   # number of each colour gem in players inventory

        self.defencelevel = 1

        #enemy variables
        self.dropped = False
        self.vision = pygame.Rect(0, 0, 150, 50)
        self.enemyrange = [self.rect.x - 100, self.rect.x + 100]
        self.idling = False
        self.idletime = 0
        self.idlecount = 0
        self.collided = False




    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))


    def update(self):
        if self.check_alive():
            self.collision()
            self.update_animation()
            self.check_health()
            if self.type == "enemy":
                self.enemy_ai()

    def check_health(self):
        if self.health > self.maxhealth:
            self.maxhealth = self.health

    def action_update(self, newaction):
        if self.action != newaction:
            self.action = newaction
            #print(self.action)
            self.frame_index = 0

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.kill()
            gem = Magic_ball(self.rect.x, self.rect.y, 1)
            self.drops()
        return self.alive

    def drops(self):
        if self.type == "enemy" and not self.alive:

            if self.char_type == enemy2_img:
                gem = Magic_ball(self.rect.x + 50, self.rect.y, 2)
                ballgroup.add(gem)


            elif self.char_type == enemy_img:
                gem = Magic_ball(self.rect.x+50, self.rect.y, 1)
                ballgroup.add(gem)


            elif self.char_type == enemy3_img:
                gem = Magic_ball(self.rect.x+50, self.rect.y, 3)
                ballgroup.add(gem)

            if random.randint(1,10) == 1:
                heart = Heart(self.rect.x+100, self.rect.y)
                heartgroup.add(heart)




    def update_animation(self):
        self.animation_count += 1
        self.image = pygame.transform.scale(self.char_type[self.action][self.frame_index], (
        int(self.width * self.scale), int(self.height * self.scale))).convert_alpha()


        # check if enough time has passed since the last update
        if self.animation_count % 4 == 0 :
            self.animation_count = 0

            self.frame_index += 1

            # restart index if it is above the amount of images in the animation

            if self.frame_index >= len(self.char_type[self.action]) - 1 :
                # only allows you to do one kick at a time
                if self.action == 3 and self.type == "player":
                    self.attack = False
                self.frame_index = 0  # loops animation




    def move(self, moving_right, moving_left):
        dx = 0
        dy = 0

        if moving_left == True:
            self.flip = True
            self.direction = -1

        if moving_right == True:
            self.flip = False
            self.direction = 1



        dx += self.direction * self.speed

        # if player is jumping
        if self.jump == True and self.in_air == False:
            self.jump = False
            #self.vel_y = -math.sqrt(self.image.get_height()) #scales the dinos jump for fullscreen
            self.vel_y = -12


        # add gravity
        self.vel_y += GRAVITY
        dy += self.vel_y


        # collision with floor
        collum = (self.rect.x) // TILESIZE + 1
        print("collum: ", collum)
        print("floor: ", World.floorlist[collum])

        if self.rect.bottom + dy >= World.floorlist[collum] - TILESIZE:
            dy = 0

            self.in_air = False

        else:
            self.in_air = True



        if not moving_left and not moving_right:
            dx=0

        if self.rect.x   <= -5  and moving_left:
            dx= 0 #stops player running off the left side of screen

        if dx == 0:
            self.moving = False
        else:
            self.moving = True

        # update coordinates

        self.rect.x += dx
        self.rect.y += dy
        print("y pos top: ", self.rect.top, " y pos bottom: ", self.rect.bottom)
        #print(self.rect.x, self.rect.y)
       # print(self.rect)


    def attacking(self):
        # makes sure you cant spam leftclick to continually attack
        newtime = pygame.time.get_ticks()
        if newtime - self.lasttime > 200:
            self.attack = True
        self.lasttime = pygame.time.get_ticks()

    def collision(self):   # checks for collision between emenys anf player and if attacking di=ecide who takes damage
        damage = self.attacklevel * 7
        if self.type == "player":
            hurtchar = pygame.sprite.spritecollideany(self, enemygroup)

            if pygame.sprite.spritecollideany(self, enemygroup):
                if self.attack == True and hurtchar.check_alive():
                    hurtchar.health -= damage


        else:
            if pygame.sprite.collide_rect(self, player):
                if self.attack == True and player.check_alive():
                    player.health -= damage / self.defencelevel
                    self.collided = True
                else:
                    self.collided = False


    def usegem(self, colour, buff):
        if self.gemnumber[colour-1] > 0:
            if buff == "attack":
                if self.attacklevel + colour >= 10 :
                    self.attacklevel = 10
                else:
                    self.attacklevel += colour

            else:
                if self.defencelevel + colour >= 10:
                    self.defencelevel = 10
                else:
                    self.defencelevel += colour



            self.gemnumber[colour-1] -= 1 # the colour gem decreases by one after being used



    def enemy_ai(self):

        dx = 0
        direction = 1


        if self.direction == -1:
            self.flip = True

        if self.direction == 1:
            self.flip = False

        dx += self.speed * self.direction



        #print(player.rect, self.vision)
        if self.vision.colliderect(player.rect) and player.alive:

            self.action_update(3)
            self.attack = True
            self.attacking()
            #print("collided")
        elif self.idling:
            self.idlecount += 1
            self.action_update(0)  # idle
            if self.idlecount < self.idletime:
                dx = 0


            else:
                self.idling = False
                self.action_update(1)  # run
                self.idlecount = 0


        else:
            self.attack = False
            self.action_update(1)  # run
            if random.randint(1, 1200) % 100 == 1:
                self.idling = True
                self.idletime = random.randint(50,70)







        self.vision.center = (self.rect.centerx + 80 * self.direction, self.rect.centery + 10) #updates enemys vision rectangle
        #pygame.draw.rect(screen,BLACK, self.vision)








        if self.rect.x + dx < self.enemyrange[0] or self.rect.x +dx > self.enemyrange[1]:
            if self.attack :



                self.enemyrange[0] += dx
                self.enemyrange[1] += dx


            else:
                self.direction = -self.direction

        if pygame.sprite.collide_rect(self, player) and self.attack:
            dx = 0



        self.rect.x += dx







class Healthbar():
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health


    def draw(self,health):
        self.health = health

        #printcheck("health2 :",self.health)
        self.ratio = self.health / player.maxhealth

        # printcheck("ratio; ", ratio)
        # displays health bar
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(screen, RED, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, LIGHTGREEN, (self.x, self.y, 150 * self.ratio, 20))

    def update(self):
        self.ratio = self.health / player.maxhealth

class Magic_ball(pygame.sprite.Sprite):
    def __init__(self, x, y, colour):
        pygame.sprite.Sprite.__init__(self)
        self.colour = colour
        self.image = magic_balls[colour-1] # green1 red2 blue3
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.exist = True


    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        if pygame.sprite.collide_rect(self, player):

            player.gemnumber[self.colour-1] += 1
            self.kill()
            self.exist = False


class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = heart_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.exist = True


    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        if pygame.sprite.collide_rect(self, player):
            player.health += 500           # if the player walks over a heart player hea;th is increased by 50 and thn the heart is deleted
            self.kill()
            self.exist = False



class Chest(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = heart_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.image = chest_img
        self.exist = True
        self.items = []
        self.open = False
        self.itemnumber = random.randint(1, 3)          # random number of items from 1-3 in chest
        for i in range(self.itemnumber):
            self.items.append(random.randint(1,4)) # add random items to chest 1 green gem 2 red gem 3 blue gem 4 heart


    def update(self,rightclick):
        if pygame.sprite.collide_rect(self, player) and rightclick:# if player right clicks chest the contents are spawned in
            self.open = True
            for item in self.items:
                if item == 4:
                    heart = Heart(self.rect.x + random.randint(-300,300), self.rect.y) # spawns items in the chest within 300 pixels each side of the chest
                    heartgroup.add(heart)
                else:
                    gem = Magic_ball(self.rect.x + random.randint(-300,300),self.rect.y, item)
                    ballgroup.add(gem)

                self.kill()

    def draw(self):
        screen.blit(self.image, self.rect)





class world():
    def __init__(self):
        self.obstacle_list = []
        self.level_length = 0
        self.floorlist = []



    def sortdata(self, data):
        self.level_length = len(data[0])
        # iterate through each value in level data file
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile > 0:
                    img = tile_img[tile-1]
                    img = pygame.transform.scale(img, ( TILESIZE,TILESIZE))
                    img_rect = img.get_rect()
                    img_rect.x = x * TILESIZE
                    img_rect.y = y * TILESIZE
                    tile_data = (img, img_rect)
                    if tile > 0 and tile <= 8:

                        self.obstacle_list.append(tile_data)
                    elif tile == 9:
                        player = Dino(x * TILESIZE, y * TILESIZE, player_img)
                        health_bar = Healthbar(10, 20, player.health)
                    elif tile == 10:
                        enemy = Dino(x * TILESIZE, y * TILESIZE, enemy_img)
                        enemygroup.add(enemy)
                    elif tile == 11:
                        enemy = Dino(x * TILESIZE, y * TILESIZE, enemy2_img)
                        enemygroup.add(enemy)
                    elif tile == 12:
                        enemy = Dino(x * TILESIZE, y * TILESIZE, enemy3_img)
                        enemygroup.add(enemy)
                    elif tile == 13:
                        heart = Heart(x * TILESIZE, y * TILESIZE)
                        heartgroup.add(heart)
                    elif tile == 14:
                        chest = Chest(x * TILESIZE, y * TILESIZE)
                        chestgroup.add(chest)
                    elif tile == 15:
                        magicball = Magic_ball(x * TILESIZE, y * TILESIZE, 1)
                        ballgroup.add(magicball)
                    elif tile == 16:
                        magicball = Magic_ball(x * TILESIZE, y * TILESIZE, 2)
                        ballgroup.add(magicball)
                    elif tile == 17:
                        magicball = Magic_ball(x * TILESIZE, y * TILESIZE, 3)
                        ballgroup.add(magicball)

        for i in range(0, self.level_length-1):
            floorlevel = (len(data) + 2)* TILESIZE
            for j in range(len(data) - 1, -1, -1):

                if data[j][i] != 0 :
                    floorlevel = j * TILESIZE
            floorlevel += TILESIZE // 2
            self.floorlist.append(floorlevel)

        print(self.floorlist)





        #return player, health_bar

    def draw(self):
        #print(self.obstacle_list)
        for tile in self.obstacle_list:
            #tile[1][0] += screen_scroll
            screen.blit(tile[0], tile[1])
            #print("here")













#player, healthbar = world.process_data(world_data)

start = button.Button(start_button, 100, 300, 0.7)
exit = button.Button(exit_button, 400, 300, 0.7)
player = Dino( 200, 200, player_img)
enemy = Dino( 200, 272,  enemy_img)
enemy2 = Dino( 300, 272,  enemy2_img)
enemy3 = Dino( 400, 272,  enemy3_img)
healthbar = Healthbar(10, 20, player.health)

enemygroup = pygame.sprite.Group()
#enemygroup.add(enemy)
#enemygroup.add(enemy2)
#enemygroup.add(enemy3)
#green = Magic_ball(150,300,1)
#red = Magic_ball(100,300,2)
#blue = Magic_ball(50,300,3)
ballgroup = pygame.sprite.Group()
#ballgroup.add(blue)
#ballgroup.add(red)
heart = Heart(300,300)
heartgroup = pygame.sprite.Group()
heartgroup.add(heart)

chest = Chest( 300,300)
chestgroup = pygame.sprite.Group()
chestgroup.add(chest)



World = world()

World.sortdata(test_level)




run = True

while run:

    clock.tick(FPS)
    if player.moving:


        bgscroll += player.speed * player.direction * 0.1



    fill_bg()
    #if start.draw(screen):
       # print('START')
    #if exit.draw(screen):
       # run = False
    World.draw()
    player.update()
    player.draw()

    for enemy in enemygroup:
        enemy.update()
        enemy.draw()



    for ball in ballgroup:
        if ball.exist:
            ball.draw()
            ball.update()

    for heart in heartgroup:
        heart.update()
        heart.draw()

    for chest in chestgroup:
        chest.update(rightclick)
        chest.draw()



    healthbar.draw(player.health)
    displayplayerstats()

    player.scale = screen.get_width() / 300
    for enemy in enemygroup:
        enemy.scale = screen.get_width() / 300

    if player.alive:
        # putting kick first priorotise attacking meaning that the player has the kick animation if they attack while running or jumping
        if player.attack:
            player.action_update(3)  # kick
        elif player.in_air:
            player.action_update(2) #jump
        elif player.shift:
            player.action_update(5) # crouch
        elif moving_left or moving_right:
            player.action_update(1) # run


        else:
            player.action_update(0) #idle


        player.move(moving_right, moving_left)










    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            run = False

        # event handler for moving the player with keys
        if event.type == VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)



        if event.type == pygame.KEYDOWN:

            if event.key == K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
                player.scale = screen.get_width()/200

            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_d:
                moving_right = True



            if event.key == pygame.K_a:
                moving_left = True


            if event.key == pygame.K_SPACE:
                player.jump = True

            if event.key == pygame.K_s:
                player.shift = True
                player.speed += 2
                # makes speed faster when crouching

            if event.key == pygame.K_1 :
                player.usegem(1, "attack") # if player preses 1 it uses a green gem on the attack and increases the level by 1


            if event.key == pygame.K_2:
                player.usegem(2, "attack")


            if event.key == pygame.K_3:
                player.usegem(3, "attack")


            if event.key == pygame.K_4:
                player.usegem(1, "defense")


            if event.key == pygame.K_5:
                player.usegem(2, "defense")


            if event.key == pygame.K_6:
                player.usegem(3, "defense")




        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                player.attacking()

            if event.button == 3:
                rightclick = True
                printcheck("rightclick", rightclick)



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.type == pygame.K_SPACE:
                jump = False
            if event.key == pygame.K_s:
                player.shift = False
                player.speed = player.ogspeed
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                player.attack = False
            if event.button == 3:
                rightclick = False




#nina woz here



    pygame.display.update()


pygame.quit()
