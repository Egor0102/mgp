import random
import time
from helpers import *
from data import *

name = input('Введи своё имя, школьник: ')
player['name'] = name
current_enemy = 0

while True:
    action = input('''Выбери действие:
1 - На урок
2 - Тренировка
3 - Информация об школьнике
4 - Информация о текущем учителе
5 - Показать инвентарь
6 - Магазин
7 - Пойти поиграть в карты
''')
    if action == '1':
        current_enemy = fight(current_enemy)
        if current_enemy == 4:
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
    elif action == "7":
        earn()
        print()   
    print()