import pygame
from plane_sprites import *

pygame.init()
# 游戏开始
screen = pygame.display.set_mode((480, 700))
# 创建游戏屏幕
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# 创建背景图
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 500))
# 创建飞机
pygame.display.update()
# 游戏刷新
clock = pygame.time.Clock()
hero_rect = pygame.Rect(150, 300, 102, 126)
enemy = GameSprite("./images/enemy1.png")
enemy_group = pygame.sprite.Group(enemy)
i = 0
while True:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出")
            pygame.quit()
            exit()
    hero_rect.y = 50
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

pygame.quit()
