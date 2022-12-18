# Алгоритмический тренажер
# 1
num = float(input('Введите число: '))
def times_ten(num):
    result = num * 10
    print('Результат: ', result, 'вот такое число')

times_ten(num)

# 2
quantity = 12
def show_value(quantity):
    print ("Проверка квантити, Кторая равна: ", quantity)

show_value(quantity)

# 3
Взгляните на приведенный ниже заголовок функции:
def my_function(а, b, с):
Теперь взгляните на приведенный ниже вызов функции myfunction:
my_function(3, 2, 1)
Какое значение будет присвоено а, когда этот вызов исполнится? Какое значение будет
присвоено Ь? Какое значение будет присвоено с?
a = 3,b = 2, c = 1

# 4 Что покажет приведенная ниже программа?
def main():
 х = 1
 у = 3.4
 print(х, у)
 change_us(х, у)
 print(х, у)
 def change_us(а, b):
 а = 0
 Ь = 0
 print(а, Ь)
 main()
Ответ: 1 сначала покажет значение 1 и 3.4
2. Покажет значение х = 0 у = 0
3. снова покажет 1 и 3.4

# 5 Взгляните на приведенное ниже определение функции:
 def my_function(а, b, с):
 d = (а + с) / b
 print(d)
 • Напишите инструкцию, которая вызывает эту функцию и применяет именованные
  аргументы для передачи 2 в а , 4 в b и 6 в с.
my_function(2, 4, 6)
 • Какое значение будет показано, когда исполнится вызов функции
2

# 6 код случайных чисел
import random
number = random.randint(1, 100)
print(number)

# 7 Приведенная ниже инструкция вызывает функцию half, возвращающую значение,
# которое вдвое меньше аргумента. (Допустим, что переменная number ссылается на
# вещественное значение с типом float.) Напишите код для этой функции.
result = half(number)
number = float(input('Введите число: '))
def half(number):
    result = number/2
    return result
result = half(number)
print (result)

# 8 Программа содержит приведенное ниже определение функции:
def cube(num):
return num * num * num
Напишите инструкцию, которая передает значение 4 в эту функцию и присваивает
возвращаемое ею значение переменной result.
num = 4
def cube(num):
    return num * num * num
rezult = cube(num)
print(rezult)

# 9 Напишите функцию Напишите функцию times ten, которая принимает number в качестве аргумента. Когда
функция вызывается, она должна возвращать значение ее аргумента, умноженное на 10

num = float(input('Введите число: '))
def times_ten(num):
    return num * 10
rezult = times_ten(num)
print(rezult)

# 10 Напишите функцию get first name, которая просит пользователя ввести свое имя и его же возвращает.
name = input('Введите свое имя: ')
def get_name(name):
    return name
name_1 = get_name(name)
print('Ваше имя...ваше имя', name_1, 'от такое')

# Упражнения по программированию
# 1 Конвертор километров
KOOFICIENT = 0.6214
km = float(input('Введите расстояние в километрах: '))
mp = km * KOOFICIENT
print('Расстояние в милях составит: ', f'{mp:.1f}')

# 2 Модернизация программы
def pokupka():
    pokup_ka = float(input('Введите стоимость Вашей покупки: '))
    print('Стоимость Вашей покупки: ', pokup_ka, 'грн')
    federalniy_nalog = fednalog(pokup_ka)
    regionalniy_nalog = regnalog(pokup_ka)
    ob_nalog = obwiynalog(federalniy_nalog, regionalniy_nalog)
    obwaysumma(pokup_ka, ob_nalog)

def fednalog(num):
    fed_nalog = num*0.05
    print('Федеральный налог с покупки составил: ', f'{fed_nalog:.2f}', 'грн')
    return fed_nalog
def regnalog(num):
    reg_nalog = num*0.025
    print('Региональный налог состовляет: ', f'{reg_nalog:.2f}', 'грн')
    return reg_nalog
def obwiynalog(num1, num2):
    obwiy_nalog = num1 + num2
    print('Общий налог состовляет: ', f'{obwiy_nalog:.2f}', 'грн')
    return obwiy_nalog
def obwaysumma(num1, num2):
    obway_summa = num1 + num2
    print('Общая сумма расходов состовляет: ', f'{obway_summa:.2f}', 'грн')

pokupka()

# 3 Стоимость страховки
STRAH_PROCENT = 0.8
def strahovka ():
    stoim_nedvizh = float(input('Введите стоимость Вашей недвижимости: '))
    print('При цене', stoim_nedvizh, 'долларов, сумма страховки составит')
    stoim_strahovki = cenastrahovki(stoim_nedvizh)
    print(f'{stoim_strahovki:.2f}', 'долляров')
def cenastrahovki (num):
    return num*STRAH_PROCENT

strahovka()

# Расход на автомобиль
def avtorashodi():
    print('Сейчас мы посчитаем Вашиа расходы на Ваш автомобиль в месяц и год!:))')
    rashodavto()
    print('Теперь Вы видите как дорого Вам обхадится Ваш автомобиль;) ')
def rashodavto():
    kolich_rashodov = int(input('Введите количество Ваших расходов на автомобиль: '))
    total_rashod = 0
    print('Укажите Ваши расходы: \nплатеж по кредиту,\nстраховка, бензин\nмашинное масло\n'
         'шины,\nтехобслуживание')
    for c in range(kolich_rashodov):
        rashod = float(input('Введите сумму затрат(в гривнах): '))
        total_rashod += rashod
    god_stoim = total_rashod*12
    print('Общая стоимость Ваших расходов в месяц состовляет: ' f'{total_rashod:.2f}', "гривен")
    print('Стоимость Ваших расходов составит: 'f'{god_stoim:.2f}', "гривен")

avtorashodi()

# 5 Налог на недвижимость
KOOFICIENT = 0.6
stoim_nedvizhemosti = float(input('Введите стоимость Вашей недвижимости: '))
ocenochn_stoimost = stoim_nedvizhemosti*KOOFICIENT
nalog_na_imuch = ocenochn_stoimost/100*0.72
print('Оценочная стоимость Вашего имущества составит: ',f'{ocenochn_stoimost:.2f}', "далларов")
print('Налог на Вашу недвигу будет: ',f'{nalog_na_imuch:.2f}', "долларов")

# 6 Калории за счет жиров
ZHIRI = 9
UGLEVODI = 4
def raschet_kaloriy ():
    print('Сейчас мы попробуем расчитать Ваше потребление колорий в день и в месяц')
    zhiri = float(input('Введите ваше потребление жиров в день(в граммах): '))
    uglevodi = float(input('Введите ваше потребление углеводов в день(в граммах): '))
    kol_zhirov = vashi_zhiri(zhiri)
    kol_uglevodov = vashi_uglevodi(uglevodi)
    kolich_dney = int(input('Введите количество дней в этом месяце: '))
    zhiri_v_mesjac = kol_zhirov*kolich_dney
    uglevodi_v_mesjac = kol_uglevodov*kolich_dney
    print('В месяц вы поглащаете', f'{zhiri_v_mesjac:.1f}', 'калорий по жирам')
    print('И', f'{uglevodi_v_mesjac:.1f}','калорий по углеводам')
    print('Хорошего Вам дня:)')

def vashi_zhiri(num):
    zhiri_vashi = num*ZHIRI
    print('В день вы потребляете', f'{zhiri_vashi:.1f}', 'калорий по жирам:)')
    print('Нужно уточнить у диетолога: много это или мало')
    return zhiri_vashi

def vashi_uglevodi(num):
    uglevodi_vashi = num*UGLEVODI
    print('Ваше потребление калорий по углеводам состовляет: ', f'{uglevodi_vashi:.1f}', 'в день')
    print('Уточните у диетолога нормально это или нет')
    return uglevodi_vashi
raschet_kaloriy()

# 7 Сидячие места на стадионе
A = 20
B = 15
C = 10
ticketsA = int(input('Укажите сколько было продано билетов класса А: '))
ticketsB = int(input('Сколько было продано билетов класса Б: '))
ticketsC = int(input('Введите количество проданных билетов класса С: '))
print('Блилетов класса А продано на сумму', f'{ticketsA*A:.1f}', 'долларов')
print('Билетики класса Б продали на сумму', f'{ticketsB*B:.1f}', 'вечно зеленых')
print('Билетов класса С продали на сумму', f'{ticketsC*C:.1f}', 'американской валюты')
print('Общий доход от продажи билетов составил:', f'{(ticketsA*A)+(ticketsB*B)+(ticketsC*C):.1f}', 'долларов USA')


# 8 Оценщик малярных работ
METR2_KRASKA = 0.5
METR2_CHAS = 0.8
PLATA = 200
KRASKA_UPAKOVKA = 5

def kraska (num):
    return num*METR2_KRASKA
def chasi (num):
    kol_chasov = num*METR2_CHAS
    print("На покраску Вашей стены потребуется ", f'{kol_chasov:.2f}', 'часов')
    return kol_chasov
def stoimostkraski  (num1,num2):
    stoim_kraski = num1*num2
    print('Общее количество краски будет стоить: ', f'{stoim_kraski:.2f}', 'гривен')
    return stoim_kraski
def cena_raboti (num1,num2):
    cena_rabot = num1*num2
    print('Стоимость работы по покраске стены составит: ', f'{cena_rabot:.2f}', 'гривен')
    return cena_rabot
def obwajastoimost (num1, num2):
    zatrati = num1 + num2
    print('Общие затраты с учетом краски и материала оставят: ', f'{zatrati:.2f}', 'наших, украинских гривен:)')
    return zatrati

def proshet_rabot():
    print('Программа посчитает все Ваши расходы на покраску стен')
    ploschjad_steni = float(input('Укажите площать поверхности, которую Вам нужно покрасить: '))
    cena_emkosti = float(input('Введите стоимость 5-ти литровой канистры краски: '))
    kolichestvo_kraski = kraska(ploschjad_steni)
    if kolichestvo_kraski % 5 == 0:
        kol_upakov_kraski = kolichestvo_kraski//KRASKA_UPAKOVKA
        print('Вам понадобится: ', kol_upakov_kraski, 'упаковки краски')
    else:
        kol_upakov_kraski = kolichestvo_kraski//KRASKA_UPAKOVKA+1
        print('Вам нужно: ', kol_upakov_kraski, 'упаковок краски')
    kolichestvo_chasov = chasi(ploschjad_steni)
    stoimost_kraski = stoimostkraski(cena_emkosti, kol_upakov_kraski)
    stoimost_raboti = cena_raboti(kolichestvo_chasov, PLATA)
    obwaja_stoimost_rabot = obwajastoimost(stoimost_raboti,stoimost_kraski)
proshet_rabot()

# 9 Месячный налог с продаж
FED_NALOG = 0.05
MUNICIP_NALOG = 0.025
def federal(num):
    return num * FED_NALOG
def municipal(num):
    return num*MUNICIP_NALOG
def mesjachniy_nalog ():
    prodazhi = float(input('Укажите сумму продаж предприятия за прошлый месяц: '))
    fed_nal = federal(prodazhi)
    mun_nal = municipal(prodazhi)
    obwiy_nal = fed_nal + mun_nal
    print('Федеральный налог за прошлый месяц составит', f'{fed_nal:.2f}','гривен')
    print('Муниципальный налог за прошлый месяц составит', f'{mun_nal:.2f}', 'гривен')
    print('Общая сумма налогов за предидущий месяц составляет', f'{obwiy_nal:.2f}', 'гривен')
mesjachniy_nalog()

# 10 Футы и дюймы
DYM = 12
def feet_to_inches(num):
    return num * DYM
futi = float(input('Введите количество футов: '))
dymi = feet_to_inches(futi)
print(futi, 'футов - это', dymi, "дюймов")

# 11 Математический тест
import random
def mat_test():
    again = 'д'
    while again == 'д' or again == 'Д':
        for c in range(2):
            number1 = random.randint(1,1000)
            number2 = random.randint(1,1000)
        summa = number1+number2
        print('Пожалуйста дайте ответ. Какой будет сумма:',
          number1, "+",
          number2)
        otvet = float(input('Введите ваш ответ: '))

        if otvet == summa:
            print('Это правильный ответ. Поздравляем!')
        else:
            print('К сожалению это не правильный ответ.')
        again = input('Попробуете снова? Укажите ответ: ')
mat_test()


num1 = float(input('Введите число 1: '))
num2 = float(input('Введите число 2: '))
def max():
    if num1 > num2:
        print(num1, 'больше', num2)
        return num1
    else:
        print(num2, 'больше', num1)
        return num2
max()

# 13 Высота падения
G = 9.8
def falling_distance():
    for t in range(1,11):
        d = 1/2*G*(t**2)
        print('При падении предмета', t, 'секунду, тело пролетит', f'{d:.2f}', 'метров')
    return d
falling_distance()

# 14 Кинетическая энергия
m = float(input('Введите массу тела, пожалуйста (в кг): '))
v = float(input('Укажите скорость тела (в м/с): '))
def kinetic_energy(num1,num2):
    return 1/2*num1*(num2**2)
kinetic=kinetic_energy(m,v)
print('Кинетическая энергия тела, при таких данных составит: ', f'{kinetic:.1f}', 'джоулей')

# 15 Средний балл и его уровень
A = 90
B = 80
C = 70
D = 60
KOL_OCENOK = 5
def calc_average():
    print('Введите вашу 1, 2, 3, 4 и 5 оценку')
    total_bal = 0
    for c in range(KOL_OCENOK):
        bal=int(input('Введите оценку: '))
        total_bal+=bal
    return total_bal/KOL_OCENOK
def determine_grade():
    sred_bal = int(input('Введите Вашу среднюю оценку: '))
    if sred_bal >= A:
        print('Ваш уровень знаний отвечает уровню А')
    elif sred_bal >= B:
        print('Ваш уровень знаний соответствует оценке В')
    elif sred_bal >= C:
        print('Ваши знания отвечают уровню С')
    elif sred_bal >= D:
        print('Если у Вас такой балл, то это уровень D')
    else:
        print('Ваш уровень знаний отвечает оценке Е')
    return sred_bal
def exam():
    print('Прграмма расчитывает Ваш средний бал''\n'
    'И показывает уровень соответсвия Вашей оценки буквенной категории')
    sred_bal = calc_average()
    print('Ваша средняя оценка состовляет: ', sred_bal)
    uroven = determine_grade()
    print('Мы показали ваш средний бал и уровень оценки.')
exam()

# 16 Счетчик четных и не четных чисел
import random

def chisla ():
    total_a = 0
    total_b = 0

    for c in range(30):
        number = random.randint(1,30)
        print(number)
        if number % 2 == 0:
            total_a += 1
        else:
            total_b += 1
    print('Количество четных чисел составляет: ', total_a)
    print('Количество нечетных чисел составляет: ', total_b)
chisla()

# 17 Простые числа
def is_prime(number):
    if number == 1 or number == 2 or number == 3:
        return True
    elif number % 2 != 0 and number % 3 != 0 and number % 1 == 0 and number % number == 0:
        return True
    else:
        return False
    return False
again = 'д'
while again == 'д' or again == 'Д':
    print('Сейчас программа проверит является ли число простым или сложным')
    number = int(input('Введите число, которое Вы хотите проверить: '))
    if is_prime(number):
        print('Это число является простым:)) ')
    else:
        print('Такое число является сложным:))')
    again = input('Попробуем снова? Если нажмите "д" или "Д": ')

# 18 Список простых чисел
def is_prime(number):
    if number == 1 or number == 2 or number == 3:
        print(number)
    elif number % 2 != 0 and number % 3 != 0 and number % 1 == 0 and number % number == 0:
        print(number)

for c in range (1,101):
    c = is_prime(c)
print('На этом простые числа закончились')

# 19 Будущая стоимость
P = float(input('Укажите, какая сумма денег на данный момент находится на Вашем счете: '))
i = float(input('Введите процентную ставку в Вашем банке: '))
t = int(input('Укажите сколько месяцев деньги будут находиться на сберегательном счете: '))

def summa_v_bushem(num1,num2,num3):
    print('Сейчас мы посчитаем ваши доходы!')
    return num1*(1+num2/100)**num3
def glavnaya ():
    print('Эта программка посчитае количество денег, которые будут на вашем счете, через указанное время')
    print('Мы очень надеемся, что результаты оправдают ожидания!:)')
    budush_summa = summa_v_bushem(P,i,t)
    print('Вот такая сумма', f'{budush_summa:.2f}','гривен будет на вашем счете после', t, 'месяцев')
glavnaya()

# 20 Игра в угадываенгие случайного числа
import random

def ugadat_chislo():
    again = 'д'
    total_number = 0
    while again == 'д' or again == 'Д':
        print("Сейчас мы будем играть в угадывание чисел")
        print("Попробуем?:)")
        number = int(input('Введите число от 1 до 100: '))
        rand_number = random.randint(1,100)
        print('Вот число, которые выбрал компьютер: ', rand_number)

        if number > rand_number:
            print("К сожалению Вы не угадали - Вы выбрали слишком большое число:(")
            total_number += 1
        elif number < rand_number:
            print('Ваша попытка не увенчалась успехом - Вы вбрали слишком маленькое число ')
            total_number += 1
        else:
            print('Поздравляем, вы смогли угадать!:))')
            total_number += 1
            print("Вы угадали с", total_number, "раза!")
        print("Играем дальше ")
        again = input('Введите д или Д для продолжения: ')

ugadat_chislo()

# 21 Игра, "Камень, ножницы, бумага"
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




