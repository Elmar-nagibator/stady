import time
import random
import os
import sys
hp = 100
endurance = 100


# текст будет медлено выходить
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

#текст будет удаляться
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def player():
    global hp, endurance
    print(f"❤️  HP: {hp}/100  | ⚡  Выносливость: {endurance}/100")
    print("=" * 55)
    

clear_screen()

slow_print("Вы — обычный человек, который возвращался домой поздно вечером после тяжелого дня.\n"
        "Зайдя в старый лифт или оступившись на тёмной лестнице, вы на секунду ощутили\n"
        "странное чувство невесомости, будто провалились сквозь текстуры реальности (Noclip).\n"
        "Реальный мир мгновенно исчез...\n\n"
        "Вы очнулись на холодном ковре под раздражающий, непрерывный гул люминесцентных ламп.\n"
        "Вокруг — бесконечный лабиринт из старых жёлтых обоев. Это Закулисье (Backrooms).\n"
        "Ваша цель — пройти через 10 искажённых пространств, сохранить разум и выжить.")
print("\nНажмите Enter, чтобы сделать первый шаг...")

input()
clear_screen()

def monstr():
    global hp, endurance
    slow_print('дорогой мой ты слышиш шаги и тебе не по себе ты можешь \n' 
    ' продолжать путь или сбежать но помни каждый твой шаг можен стать фотальным')
    answer = input('что ты будеш делать дорогой мой? \n (продолжать путь - 1\n сбежать - 2)')
    if answer == '1':
        slow_print('боже мой какой же ты тупой теперь ты видишь перед собой и он видит тебя в далеке' )
        slow_print('беги что есть силенок  а то тебе кишки выпотрашат')
        random_monstr = random.randint(1, 3)
        asw_monstr = input('ты можesh бежать или спрятаться \n (бежать - 1\n спрятаться - 2 \n драться с ним раз на раз - 3)')
        if asw_monstr == '3':
            slow_print('ваахаххахахахахахааха')
            slow_print('ваахаххахахахахахааха')
            slow_print('ваахаххахахахахахааха')
            slow_print('капец ты конечно безумец')
            slow_print('к твоему счастью ты умер быстро и безболезненно')
            slow_print('прощяй малой')
            sys.exit()
            clear_screen()
        elif random_monstr == 1 and asw_monstr == '1':
            slow_print('ты смог убежать от него но он тебя догнал и ты умер')
            sys.exit()
            clear_screen()
        elif random_monstr == 2 and asw_monstr == '2':
            slow_print('думал что спрячишься не тут то было \n не умеешь ты в прятки играть вахахах пока')
            sys.exit()
        elif random_monstr == 1 and asw_monstr == '2':
                    slow_print('думал что спрячишься не тут то было \n не умеешь ты в прятки играть вахахах пока')
                    sys.exit()
        elif random_monstr == 3 and asw_monstr == '2':
                    slow_print('ух ты да ты умеешь прятаться молодец ты вижил')
        elif random_monstr == 2 and asw_monstr == '1':
            slow_print('ты смог убежать от него но он тебя догнал и ты умер')
            sys.exit()
        elif random_monstr == 3 and asw_monstr == '1':
            slow_print('ты смог убежать молодец человек маленькие ножки')
            endurance -= 20
        input('нажми Enter чтобы продолжить путь')
        clear_screen()

while True:
    print("\n--- УРОВЕНЬ 1: ЖЕЛТЫЕ КОРИДОРЫ ---")
    print("1. Пойти вперёд")
    print("2. Пойти вправо")
    print("3. Пойти влево")
    print("4. Пойти назад")
    input_choice = input("\nВаш выбор (1-4): ").strip()
    clear_screen()
    slow_print('')
    player()
    random_event = random.randint(1,10)
    print()
    if random_event == 1 or random_event == 8:
        slow_print('вы до сих пор шляитесь по коридору мдаааа')
        if endurance < 95:
            endurance += 5
        print('нажмите Enter чтобы продолжить путь')
        input()
        clear_screen()
    elif random_event == 3:
        slow_print('вы нашли бутылку воды и выпили ее')
        if endurance < 90:
            endurance += 10   
        elif endurance < 95:
            endurance += 5

        if hp < 90:
            hp += 10
        elif hp < 95:
            hp += 5 
        print('нажмите Enter чтобы продолжить путь')
        input()
        clear_screen()
    elif random_event == 4 or random_event == 5:
        slow_print('Вам начинает казаться, что выхода нет...')
        endurance -= 5
        print('нажмите Enter чтобы продолжить путь')
        input()
        clear_screen()
    elif random_event == 7 or random_event == 9:
            slow_print('ты забрел не туда и в тебя кинули палку и ты упал на пол')
            hp -= 5
            print('нажмите Enter чтобы продолжить путь')
            input()
            clear_screen()
    elif random_event == 2 or random_event == 7 or random_event == 10:
        monstr()
    elif random_event == 6:
        slow_print('о боже мой вы нашли дверь я уж думал что так и \n подохнеш на первом этаже молодец')
        print('нажмите Enter чтобы открыть дверь')
        input()
        clear_screen()
        break
slow_print('поздравляю тебя мой непутевый друг ты смог пройти первый уровень')
player()
print('нажмите Enter чтобы продолжить путь')
input()
clear_screen()

    




