"""
    ui
"""
from bll import GameCoreController
from mode01 import Direction
import os

class GameConsoleView:
    """
    控制台视图
    """
    def __init__(self):
        #创建核心类对象
        self.__controller=GameCoreController()

    def start(self):
        """
            游戏开始
        :return: 
        """
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__print_map()

    def __print_map(self):
        """
            打印界面
        :return: 
        """
        #清空控制台
        # os.system("clear")
        # print("----------------------")
        for r in range(len(self.__controller.map)):
            for c in range(len(self.__controller.map[r])):
                print(self.__controller.map[r][c],end="\t")
            print()

    def update(self):
        """
            更新（游戏逻辑）
        :return: 
        """
        while True:
            self.__move_map()
            #if 界面发生变化
            if self.__controller.is_change:
                self.__controller.generate_new_number()
                self.__print_map()
                if self.__controller.is_game_over():
                    print("游戏结束")
                    break

    def __move_map(self):
        dir=input("请输入移动方向（wsad）")
        if dir == "w":
            self.__controller.move(Direction.up)
        if dir == "a":
            self.__controller.move(Direction.left)
        if dir == "d":
            self.__controller.move(Direction.right)
        if dir == "s":
            self.__controller.move(Direction.down)

