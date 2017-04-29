#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @文件名(file): snake.py
import pygame
import random
import os
from os import _exit as exit

SCORE = 0
LEVEL = 1
PAUSE = False
border = 5

POS_x0, POS_y0 = 15, 15
G_width, G_height = 400, 450
snake = ''
food = ''
font = ''

class Snake:
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    def __init__(self):
        self.direction = self.__class__.RIGHT              #初始方向
        self.pos = [(20,30),(19,30),(18,30),(17,30)]       #初始位置，游戏区域80*90
        self.length = len(self.pos)                        #初始长度
        self.speed = LEVEL*2.0                             #初始速度
        self.place = 0
        self.moved = 1

    def move(self,t=1.0):
        self.place += self.speed*t
        if int(self.place) < 1:
            return
        self.place -= 1
        self.moved = 1
        i = self.length - 1
        while i > 0:
            pos = (int(self.pos[i-1][0]), int(self.pos[i-1][1]))
            self.pos[i] = pos
            i -= 1
        if self.direction == self.__class__.LEFT:
            pos = (self.pos[0][0]-1, self.pos[0][1])
            self.pos[0] = pos
        elif self.direction == self.__class__.RIGHT:
            pos = (self.pos[0][0]+1, self.pos[0][1])
            self.pos[0] = pos
        elif self.direction == self.__class__.UP:
            pos = (self.pos[0][0], self.pos[0][1]-1)
            self.pos[0] = pos
        elif self.direction == self.__class__.DOWN:
            pos = (self.pos[0][0], self.pos[0][1]+1)
            self.pos[0] = pos

    def draw(self, sc, RGB=(255,0,0)):
        for pos in self.pos:
            sc.fill(RGB, (POS_x0+int(pos[0])*border, POS_y0+int(pos[1])*border, border,border))

    def judge(self, food):
        global SCORE, LEVEL
        if self.pos[0] in self.pos[1:] or self.pos[0][0] < 0 or self.pos[0][0] > 79 or self.pos[0][1] < 0 or self.pos[0][1] > 89:
            if os.path.exists('simkai.ttf'):
                font = pygame.font.Font('simkai.ttf',80)
            else:
                font = pygame.font.SysFont("宋体", 80)
            game_info = font.render(u'GAME OVER',True,(255,255,0))
            self.draw(screen)
            screen.blit(game_info,(40,160))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit(0)
                    if event.type == pygame.KEYDOWN:
                           #按ESC键退出
                        if event.key == pygame.K_ESCAPE:
                            exit(0)
        if self.pos[0] == food:
            Food.Count = 0
            self.pos.append(self.pos[-1])
            self.length += 1
            SCORE += 1
            if SCORE == 20:
                LEVEL += 1
            if os.path.exists('simkai.ttf'):
                font = pygame.font.Font('simkai.ttf',40)
            else:
                font = pygame.font.SysFont("宋体", 40)
            if len(str(SCORE)) < 2:
                scoreStr = ' '+str(SCORE)
            else:
                scoreStr = str(SCORE)
            game_info = font.render(scoreStr,True,(255,255,0),(0,0,0))
            screen.blit(game_info,(490,60))
            if len(str(LEVEL)) < 2:
                levelStr = ' '+str(LEVEL)
            else:
                levelStr = str(LEVEL)
            game_info = font.render(levelStr,True,(255,255,0),(0,0,0))
            screen.blit(game_info,(490,140))
            
class Food:
    Count = 0
    def __init__(self, (x, y)):
        self.pos = (x, y)
    def draw(self, sc, RGB=(0,0,255)):
        sc.fill(RGB, (POS_x0+self.pos[0]*border, POS_y0+self.pos[1]*border, border,border))
#游戏说明
def run():
    if os.path.exists('simkai.ttf'):
        font = pygame.font.Font('simkai.ttf',35)
    else:
        font = pygame.font.SysFont("宋体", 35)
    game_info = font.render(u'贪吃蛇',True,(0,255,255))
    screen.blit(game_info,(260,40))
    game_info = font.render(u'游戏说明:',True,(255,255,255))
    screen.blit(game_info,(100,100))
    game_info = font.render(u'1、使用方向进行操作。',True,(255,255,255))
    screen.blit(game_info,(130,150))
    game_info = font.render(u'2、按ESC键退出。',True,(255,255,255))
    screen.blit(game_info,(130,200))
    game_info = font.render(u'3、按P键暂停/继续。',True,(255,255,255))
    screen.blit(game_info,(130,250))
    game_info = font.render(u'>>按回车键开始游戏<<',True,(255,255,255))
    screen.blit(game_info,(260,330))
    pygame.display.update()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:    #ESC键退出
                exit(0)
            if event.key == pygame.K_RETURN:    #回车键开始
                break

def startGame():
    global snake, font
    screen.fill((0,0,0),(0,0, 640,480))
    #游戏区域

    pygame.draw.rect(screen,(255,255,255), (10,10, 410,460), 5)
    pygame.draw.rect(screen, (255,255,255), (440,10, 175,305), 5)
    pygame.draw.rect(screen, (255,255,255), (440,350, 175,115), 5)
    #作者信息
    if os.path.exists('simkai.ttf'):
        font = pygame.font.Font('simkai.ttf',13)
    else:
        font = pygame.font.SysFont("宋体", 13)
    author_info = font.render(u'姓名：梁飞',True,(255,0,0))
    screen.blit(author_info,(450,360))
    author_info = font.render(u'学号：16126161',True,(255,0,0))
    screen.blit(author_info,(450,380))
    author_info = font.render(u'姓名：揭杰',True,(255,0,0))
    screen.blit(author_info,(450,400))
    author_info = font.render(u'学号：346202141',True,(255,0,0))
    screen.blit(author_info,(450,420))
    # author_info = font.render(u'ICQ：wosuopu@gmail.com',True,(255,0,0))
    # screen.blit(author_info,(450,440))
    #游戏信息
    if os.path.exists('simkai.ttf'):
        font = pygame.font.Font('simkai.ttf',40)
        font1 = pygame.font.Font("simkai.ttf", 30)
    else:
        font = pygame.font.SysFont("宋体", 40)
        font1=pygame.font.SysFont("宋体",30)
    game_info = font.render('SCORE:',True,(255,0,0))
    screen.blit(game_info,(450,20))
    game_info = font.render('LEVEL:',True,(255,0,0))
    screen.blit(game_info,(450,100))
    game_info = font.render('STATUS:',True,(255,0,0))
    screen.blit(game_info,(450,180))
    if len(str(SCORE)) < 2:
        scoreStr = ' '+str(SCORE)
    else:
        scoreStr = str(SCORE)
    game_info = font.render(scoreStr,True,(255,255,0),(0,0,0))
    screen.blit(game_info,(490,60))
    if len(str(LEVEL)) < 2:
        levelStr = ' '+str(LEVEL)
    else:
        levelStr = str(LEVEL)
    game_info = font.render(levelStr,True,(255,255,0),(0,0,0))
    screen.blit(game_info,(490,140))
    game_info = font1.render(u'运行中...',True,(255,255,0),(0,0,0))
    screen.blit(game_info,(460,220))
    
    snake = Snake()
    snake.draw(screen)

def Key_input():
    while True:
        while Food.Count == 0:
            pos = (random.randint(0,79), (random.randint(0,89)))
            if pos in snake.pos:
                continue
            else:
                Food.Count = 1
                food = Food(pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                #按ESC键退出
                if event.key == pygame.K_ESCAPE:
                    exit(0)
                #p键暂停
                if event.key == pygame.K_p:
                    PAUSE = not PAUSE
                    if PAUSE:
                        game_info = font.render(u'已暂停',True,(255,255,0),(0,0,0))
                        screen.blit(game_info,(460,220))
                        pygame.display.update()
                        while True:
                            event = pygame.event.wait()
                            if event.type == pygame.QUIT:
                                exit(0)
                            if event.type == pygame.KEYDOWN:
                                #按ESC键退出
                                if event.key == pygame.K_ESCAPE:
                                    exit(0)
                                #p键继续
                                if event.key == pygame.K_p:
                                    PAUSE = not PAUSE
                                    break
                        game_info = font.render(u'运行中',True,(255,255,0),(0,0,0))
                        screen.blit(game_info,(460,220))
                        time_passed_seconds = clock.tick(30)
                if event.key == pygame.K_UP and snake.direction != Snake.DOWN and snake.moved:          #向上
                    snake.direction = Snake.UP
                    #snake.move(1)
                    snake.moved = 0
                    break
                elif event.key == pygame.K_DOWN and snake.direction != Snake.UP and snake.moved:        #向下
                    snake.direction = Snake.DOWN
                    #snake.move(1)
                    snake.moved = 0
                    break
                elif event.key == pygame.K_LEFT and snake.direction != Snake.RIGHT and snake.moved:     #向左
                    snake.direction = Snake.LEFT
                    s#nake.move(1)
                    snake.moved = 0
                    break
                elif event.key == pygame.K_RIGHT and snake.direction != Snake.LEFT and snake.moved:     #向右
                    snake.direction = Snake.RIGHT
                   # snake.move(1)
                    snake.moved = 0
                    break

        time_passed_seconds = clock.tick(30)
        screen.fill((0,0,0), (POS_x0,POS_y0 ,G_width,G_height))
        food.draw(screen)
        snake.move(time_passed_seconds/1000.0)
        snake.judge(food.pos)
        snake.draw(screen)
        pygame.display.update()

if __name__=='__main__':
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    logo = pygame.image.load('logo.ico').convert_alpha()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("贪吃蛇")
    run()
    startGame()
    clock = pygame.time.Clock()
    Key_input()