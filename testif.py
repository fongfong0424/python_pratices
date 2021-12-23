#!/usr/bin/python


import random

def game():
    player = int(input("石头剪刀布游戏\n0:石头\n1:剪刀\n2:布"))
    computer = random.randint(0, 2)
    if (player == 0 and computer == 2) or (player == 1 and computer == 3) or (player == 2 and computer == 0):
        print("电脑出：%s\nYou Win!" % computer)
    elif (player == 0 and computer != 2) or (player == 1 and computer != 3) or (player == 2 and computer != 0):
        print(f"电脑出：{computer}\nSorry" )
    elif computer != (0,2):
        print("输入错误！")

if __name__ == '__main__':
    game()