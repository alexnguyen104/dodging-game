from typing import Tuple
from bullet import Bullet
from ufo import Ufo
import pygame
from random import randint
import sys
import time

pygame.init()
fpsclock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
#caption,icon
pygame.display.set_icon(pygame.image.load("data/ufo1.png"))
pygame.display.set_caption("Dodging")
#background
background = pygame.transform.scale(pygame.image.load("data/background.jpg"),(800,600))   
#asteroid line
asteroid_img = pygame.transform.scale(pygame.image.load("data/asteroid.png"),(50,50))
def asteroid_draw():
    for i in range(0,20):
        screen.blit(asteroid_img,(i*40,395))
        
#player
player = Ufo(368,500,7,"data/ufo1.png",57,40)
def draw_player(x,y):
    player_img = pygame.transform.scale(pygame.image.load(player.img),(player.width,player.height))
    screen.blit(player_img,(x,y))
#bullet
bullet = Bullet(randint(40,750),0,7,"data/bullet.png",10,16,43)

def collision(bullet_x,bullet_y,bullet_w,bullet_h,player_x,player_y,player_w,player_h):
    if(bullet_y+bullet_h >= player_y) and bullet_y<(player_y+player_h):
        if(bullet_x+bullet_w >= player_x) and (bullet_x<player_x):
            return True
        elif(bullet_x <=(player_x + player_w)) and ((bullet_x + bullet_w) >=(player_x + player_w)):
            return True
        elif(bullet_x + bullet_w) <= (player_x + player_w) and (bullet_x + bullet_w) >= player_x:
            return True
    else:
        return False

BLACK = (0,0,0)
WHITE = (255,255,255)
title = True
t0 =0

def show_time():
    global tl
    if title == False:
        t1 = time.time()
        tl = int(t1 - t0)
        time_font = pygame.font.Font("data/ARCADE_N.TTF",20)
        time_text = time_font.render("Time:"+ str(tl),True,WHITE)
        screen.blit(time_text,(10,150))

def cheat_mode():
    pygame.draw.circle(screen,(52, 229, 235),(player.x+27,player.y+21),50,2)
    cheat_font = pygame.font.Font("data/ARCADE_N.TTF",20)
    cheat_text = cheat_font.render("Cheat Mode:on",True,WHITE)
    screen.blit(cheat_text,(14,190))
state = 0
#title screen
def title_screen():
    
    running = True
    while running:
        screen.blit(background,(0,0))
        show_time()
        #title
        title_font = pygame.font.Font("data/JMH Cthulhumbus Arcade.ttf",120)
        title_text = title_font.render("Dodging",True,(77, 2, 163))
        title_text1 = title_font.render("Dodging",True,WHITE)
        screen.blit(title_text,(152,205))
        screen.blit(title_text,(152,200))
        screen.blit(title_text1,(152,195))
        screen.blit(pygame.transform.scale(pygame.image.load("data/ufo1.png"),(60,45)),(615,175))
        #press to play game
        tick = pygame.time.get_ticks()
        flicker = int(tick/800%60)
        if flicker % 2 == 0:
            replay_font = pygame.font.Font("data/ARCADECLASSIC.TTF",45)
            replay_text = replay_font.render("press any key  to  play",True,WHITE)
            screen.blit(replay_text,(155,400))
        author_font = pygame.font.Font("data/ARCADECLASSIC.TTF",25)
        author_text = author_font.render("by Nguyen Nguyen",True,(255,255,255))
        screen.blit(author_text,(20,550))
        #event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                global title
                title= False
                start = pygame.mixer.Sound("data/startgame.wav")
                start.set_volume(0.3)
                start.play()
                running = False
                global state
                global t0
                state = 1 
                t0 = time.time()
        pygame.display.update()

def over_screen():
    over_run = True
    while over_run:
        screen.blit(background,(0,0))
        #GAME OVER
        font = pygame.font.Font("data/ARCADECLASSIC.TTF",150)
        over_text = font.render("GAME OVER",True,(255,255,255))
        screen.blit(over_text,(65,125))
        #SURVIVAL TIME
        stime_font = pygame.font.Font("data/ARCADE_N.TTF",20)
        stime_text = stime_font.render("Survival Time:" + str(tl),True,(255,255,255))
        stime_font1 = pygame.font.Font("data/ARCADE_N.TTF",20)
        stime_text1 = stime_font1.render("Survival Time:" + str(tl),True,(77, 2, 163))
        screen.blit(stime_text1,(100,304))
        screen.blit(stime_text,(100,300))
        #REPLAY
        tick1 = pygame.time.get_ticks()
        flicker1 = int(tick1/800%60)
        if flicker1 % 2==0:
            replay_font = pygame.font.Font("data/ARCADECLASSIC.TTF",50)
            replay_text = replay_font.render("press enter  to  play again",True,WHITE)
            screen.blit(replay_text,(84,400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = pygame.mixer.Sound("data/startgame.wav")
                    start.set_volume(0.3)
                    start.play()
                    over_run = False
                    global state
                    state = 0
                    global t0
                    t0 = time.time()
                    global title
                    title= True
                
        pygame.display.update()
#game loop
while True:
    pygame.mixer.music.load("data/Electronic Fantasy.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    if state == 0:
        title_screen()
    if state == 2:
        over_screen()
    if state == 1:
        pygame.mixer.music.stop()
    #on screen background
    screen.blit(background,(0,0))
    #line
    asteroid_draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    cheated = 0
    #player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        player.y += player.change
    if keys[pygame.K_UP]:
        player.y -= player.change 
    if keys[pygame.K_LEFT]:
        player.x -= player.change
    if keys[pygame.K_RIGHT]:
        player.x += player.change 
    if keys[pygame.K_k]:
        cheat_mode() 
        cheated = "active"
    #boundary
    player.check_player_boundary()
    #bullet movement
    
    #bullet boundary
    bullet.check_bullet_boundary()
    bullet.bullet_fire()
    for i in range(bullet.amount):
        screen.blit(bullet.img[i],(bullet.x[i],bullet.y[i]))
    # bullet_draw(bullet.x,bullet.y)
    for i in range (bullet.amount):
        is_collision = collision(bullet.x[i],bullet.y[i],bullet.width,bullet.height,player.x,player.y,player.width,player.height)
        if (is_collision):
            for j in range(bullet.amount):
                bullet.y[j] = 2000
            explosion = pygame.mixer.Sound("data/explosion.wav")
            explosion.set_volume(0.2)
            explosion.play()
            state = 2
            if (cheated == "active"):
                state = 1
                explosion.stop()
    #BIG UFO
    screen.blit(pygame.transform.scale(pygame.image.load("data/enemy.png"),(800,200)),(0,0))
    #time
    show_time()
    draw_player(player.x,player.y)
    pygame.display.update()
    fpsclock.tick(60)
