import random

KAMEN = 1
NOZHNICI = 2
BUMAGA = 3
def play():
    vibor_komp = random.randint(KAMEN,BUMAGA)
    vibor_1 = 'камень'
    vibor_2 = 'ножницы'
    vibor_3 = 'бумага'
    vibor_chel = input('Напишите, что Вы выбираете: ')
    if vibor_komp == KAMEN:
        print('Компьютер выбрал Камень')
    elif vibor_komp == NOZHNICI:
        print('Компьютер выбрал Ножницы')
    else:
        print('Компьютер выбрал Бумагу')
    if vibor_komp == KAMEN and vibor_chel == vibor_2:
        print('Увы, компьютер победил!')
    elif vibor_komp == KAMEN and vibor_chel == vibor_3:
        print('Поздравляем Вы выиграли!:))')
    elif vibor_komp == NOZHNICI and vibor_chel == vibor_1:
        print('Поздравляем Вы выиграли!:))')
    elif vibor_komp == NOZHNICI and vibor_chel == vibor_3:
        print('Увы, Компьютер победил!')
    elif vibor_komp == BUMAGA and vibor_chel == vibor_1:
        print('Увы, Компьютер победил!')
    elif vibor_komp == BUMAGA and vibor_chel == vibor_2:
        print('Поздравляем Вы выиграли!:))')
    else:
        print('У вас с компьютером ничья!')
        print("Нужно сыграть еще раз!:")
        play()
    print('Сыграем еще раз?:)')
    otvet = int(input('Введите 1, если хотите сыграть еще раз: '))
    if otvet == 1:
        play()
    else:
        print('Жаль, всего наилучшего!:)')
play()









