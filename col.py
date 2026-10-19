
import time
import os

heart = 3
level = 0


def player():
    global heart
    print(f"❤️  HP: {heart}/3")
    print("=" * 55)


def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# Текст будет удаляться
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


otvet = [
    "молодец, следующая задача👍",
    "Вы не решили задачу и потеряли 1 жизнь💔",
    "Вы потеряли все жизни. Игра окончена.😫",
    "не расстраивайтесь, попробуйте снова😉",
    "Вы решили задачу и можете продолжать путь🙂",
    "Вы решили все задачи и переходите на следующий уровень!👏"
]


play = [
    {
        "floor": 1,
        "name": "Вы попадаете в старую прихожую с пыльным зеркалом.🪞 \nНа стене мелом выведена надпись. (Вам нужно решить задачи)",
        "exercise_1": "73 + 54 = ?",
        "exercise_2": "130 - 55 = ?",
        "exercise_3": "12 * 7 = ?",
        "answer_1": "127",
        "answer_2": "75",
        "answer_3": "84"
    },
    {
        "floor": 2,
        "name": "Вы очутились в кабинете информатики. Перед вами лишь один компьютер🖥️, задумывались стать программистом? Самое время!",
        "exercise_1": "На мониторе выведено \n x = 5 \n y = 4\nprint(5*x+y*2)\nчто выведет этот код?",
        "answer_1": "33",
        "exercise_2": "numbers = [2, 51, 6, 29, 41, 38] \nprint(numbers[3])\n что выведет этот код?",
        "exercise_3": "x = 12\nprint(f'мне {x} лет' )\n что выведет этот код?",
        "answer_2": "29",
        "answer_3": "мне 12 лет"
    },
    {
        "floor": 3,
        "name": "Вы попали в детский сад💒, на стене написаны загадки, ответьте на них, чтобы пройти дальше",
        "exercise_1": "я существую благодаря свету, но свет меня убивает, что я?",
        "exercise_2": "Что идет, не двигаясь с места, бежит без ног и утекает, хотя не является водой?",
        "exercise_3": "Я рождаюсь и молчу, я существую и молчу, когда я умираю, я реву, что я?",
        "answer_1": "тень",
        "answer_2": "время",
        "answer_3": "снег"
    },
    {
        "floor": 4,
        "name": "Детский сад окончен, пора в школу🏫, а именно, в кабинет русского языка",
        "exercise_1": "Пр..хожий д..лг.. см..трел на кр..сивый в..д..пад.",
        "exercise_2": "З..водск..я ф..брик.. отпр..вил.. т..в..ры н.. скл..д.",
        "exercise_3": "Д..к..е х..щн..к.. т..хо брод..л.. в д..кой глуш.. .",
        "answer_1": "7",
        "answer_2": "9",
        "answer_3": "10"
    },
    {
        "floor": 5,
        "name": "Огромный зал с массивной золотой дверью. Это последний шаг к выходу",
        "col": "это программа кто хочет отсюда выбраться. Начнем игру!!!",
        "exercise_1": "Какая планета Солнечной системы известна своими яркими и огромными кольцами? \n А) Марс \n Б) Юпитер \n В) Сатурн \n Г) Нептун",
        "answer_1": "в",
        "exercise_2": "Сколько игроков одной команды одновременно находится на поле в классическом футболе? \n А) 9 \n Б) 10 \n В) 11 \n Г) 12",
        "answer_2": "в",
        "exercise_3": "Какая еда является любимым лакомством кота Гарфилда из одноимённого комикса и мультфильма? \n А) Жареная рыба \n Б) Пицца \n В) Лазанья \n Г) Бургеры",
        "answer_3": "в"
    }
]


def papilus(floor, name, exercise_1, exercise_2, exercise_3,
            answer_1, answer_2, answer_3, col=""):

    global heart, level

    slow_print(
        'Здравствуй путник, пройди пять СЛОЖНЕЙШИХ уровней \n и будь свободен, но помни: жизни ограничены')

    player()

    slow_print(name)

    slow_print(exercise_1)
    otv = input('Введите ответ: ')

    if otv == answer_1:
        slow_print(otvet[0])
    else:
        slow_print(otvet[1])
        heart -= 1

    if heart <= 0:
        player()
        slow_print(otvet[2])
        return

    clear_screen()





    player()
    slow_print(exercise_2)
    otv = input('Введите ответ: ')

    if otv == answer_2:
        slow_print(otvet[0])
    else:
        slow_print(otvet[1])
        heart -= 1

    if heart <= 0:
        player()
        slow_print(otvet[2])
        return

    clear_screen()




    player()

    slow_print(exercise_3)
    otv = input('Введите ответ: ')

    if otv == answer_3:
        slow_print(otvet[5])
        clear_screen()

        level += 1

    else:
        slow_print(otvet[1])
        heart -= 1

        if heart <= 0:
            player()
            slow_print(otvet[2])
            return

        player()
        slow_print(otvet[3])


while level < len(play) and heart > 0:

    if level == 0:
        papilus(**play[0])
    elif level == 1:
        papilus(**play[1])
    elif level == 2:
        papilus(**play[2])
    elif level == 3:
        papilus(**play[3])
    elif level == 4:
        papilus(**play[4])

    if heart <= 0:
        break

if level == 5 and heart > 0:
    slow_print('Вы прошли все уровни и теперь свободны, поздравляю!!!')
elif heart <= 0:
    slow_print('Попробуйте запустить игру заново!')
