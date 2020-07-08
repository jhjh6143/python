import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Setting()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#指定窗口像素
    pygame.display.set_caption("（外星人入侵）Alien Invasion")#标题名称

    #创建储存游戏统计信息的实例，并创建记分牌
    stats=GameStats(ai_settings)

    #创建Play按钮
    play_button=Button(ai_settings,screen,'Play')

    #创造一艘飞船
    ship=Ship(ai_settings,screen)
    #创建一个用于储存子弹的编组
    bullets=Group()
    #创建一个外星人的编组 
    aliens=Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #创建一个用于储存游戏统计信息的实例
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
        #设置背景色,每次循环时都绘制屏幕颜色
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
run_game()