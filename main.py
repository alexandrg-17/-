from random import randint
from time import sleep
from helpser import *
from data import *

name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0

while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка
3 - Информация об игроке
4 - Информация о текущем противнике
5 - Показать инвентарь
6 - Магазин
7 - на завод!!!
8- узнать историю о персонаже
''')
    if action == '1':
        current_enemy = fight(current_enemy)
        if current_enemy == 3:
            break
    elif action == '2':
        training_type = input('''1 - тренировать атаку
2 - тренировать оборону
''')
        training(training_type)
    elif action == '3':
        display_player()
        print()
    elif action == '4':
        display_enemy(current_enemy)
        print()
    elif action == "5":
        display_inventory()
        print()
    elif action == "6":

        shop()
        print()
        print()
    elif action == "7":
        earn()
        print()
    elif action == "8":
        plot()
        print()