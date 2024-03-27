#!/usr/bin/python
# coding=utf-8
import pygame
import random

pygame.init()

# 设置窗口大小
width, height = 800, 600
win = pygame.display.set_mode((width, height))
# 加载背景音乐
# pygame.mixer.music.load(''
#                         '.mp3')
#
# # 播放背景音乐（-1表示循环播放）
# pygame.mixer.music.play(-1)
pygame.display.set_caption("贪吃蛇游戏")

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 蛇和食物的大小
block_size = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)


# 绘制蛇
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])


# 游戏循环
def gameLoop():
    game_over = False
    game_close = False

    x1, y1 = width / 2, height / 2

    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    foodx, foody = round(random.randrange(0, width - block_size) / 10.0) * 10.0, round(
        random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close is True:
            win.fill(white)
            message("你输了， 按 Q 退出或C 重新开始 ！".encode(encoding="utf-8"), red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        win.fill(white)
        pygame.draw.rect(win, green, [foodx, foody, block_size, block_size])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = round(random.randrange(0, width - block_size) / 10.0) * 10.0, round(
                random.randrange(0, height - block_size) / 10.0) * 10.0
            length_of_snake += 1

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
