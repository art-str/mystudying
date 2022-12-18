# Задание 1
product = 0
while product < 100:
    chislo = float(input('Vvedite chislo: '))
    product = chislo*10
print('poka')

# Задание 2
keep = 'д'
while keep == 'д' or keep == 'Д':
    chislo_1 = float(input('Vvedite 1e chislo: '))
    chislo_2 = float(input('Vvedite 2e chislo: '))
    summa = chislo_1+chislo_2
    print('Summa chisel sostovljaet: ', summa)
    keep=input('Xotite prodolzhit6 dal6she? '+'Esli da vvedite"д": ')
print('kak xotite))')

# Задание 3
for number in range(0,1001,10):
    print(number)

# Задание 4
MAX = 10
total = 0
for x in range(MAX):
    chislo = float(input('Vvedite chiclo: '))
    total += chislo
    print('Seychas summa takaja: ', total)

print('Summa chisel sostavljaet: ', total)

# Задание 5
START_CHISLO = 1
END_CHISLO = 31
STEP = 1
total = 0
for number in range(START_CHISLO, END_CHISLO, STEP):
        itog = number/(END_CHISLO-number)
        total += itog
print('Summa vichesleniy: ', f'{total:.2f}')

# Задание 6
x += 1
x *= 2
x /= 10
x -= 100

# Задание 7
for strok in range(10):
    for stolb in range(15):
        print('#', end='')
    print()

# Задание 8
udostoveritsja = 'д'
while udostoveritsja == 'д' or udostoveritsja == 'Д':
    prodazhi = float(input('Vvedite summu prodazh: '))
    while prodazhi <= 0:
        print('Oshibka takogo ne mozhet bit6')
        prodazhi = float(input('Vvedite summu prodazh: '))

    procent = prodazhi * 0.07
    print('Vash dohod sostavil: ', f'{procent:.2f}')
    udostoveritsja = input('Hotite eche 1 poschitat6? Esli da vvedite "д": ')

# Задание 9
chislo = float(input('Vvedite chislo ot 0 do 100: '))
while chislo < 0 or chislo > 100:
    print('Kak to vi ne pravilno menja ponjali...')
    chislo = float(input('Vvedite chislo ot 0 do 100: '))
print('okay')

# Упражнения по программированию
# 1 Сборщик ошибок

MAX_DAY = 5
total_error = 0
for spisok in range (MAX_DAY):
    error = int(input('Введите количество ошибок за день: '))
    total_error += error
print("Общее количество ошибок за 5 дней составляет: ", total_error, 'ошибок(ки)')

# 2 Сожженные калории
START_TIME = 10
END_TIME = 31
STEP = 5
KALORII_MINUTA = 4.2
print('Время\tКалории')
print('-------------------')
for kalorii in range (START_TIME, END_TIME, STEP):
    sozhen_kalor = kalorii * KALORII_MINUTA
    print(f'{kalorii}\t{sozhen_kalor:.1f}')
print('Это таблица соотшения времени и сожженных калорий!:)')

# 3 Анализ бюджета
bjudzhet = float(input('Введите сумму выделеного вам бюджета: '))
kolichestvo_rashodov = int(input('Введите количество статей расходов: '))
total_rashod = 0
for rashod in range (kolichestvo_rashodov):
    rashod = float(input('Ведите сумму расходов по каждой статье: '))
    total_rashod += rashod
print('Сумма расходов составила: ', f'{total_rashod:.1f}')
if total_rashod < bjudzhet:
    economija = bjudzhet - total_rashod
    print('Вы сэкономили бюджет на сумму: ', f'{economija:.1f}')
elif total_rashod > bjudzhet:
    pererashod = total_rashod - bjudzhet
    print('Перерасход бюджета составил: ', f'{pererashod:.1f}')
else:
    total_rashod = bjudzhet
    print('У вас нет ни экономии ни перерасхода')

# 4 Пройденное расстояние
speed = float(input('С какой скоростью двигалось транспортное средство(км/час)? '))
time = int(input('Сколько часов двигалось транспортное средство? '))
print('Время\tРасстояние')
print('--------------------')
for ras in range (1,time+1):
    rasstojanie = speed * ras
    print(f'{ras} \t {rasstojanie}')

# 5 Средняя толщина слоя дождевых осадков
years = int(input('Введите количество лет:  '))
obwee_kol_osadkov = 0
for d in range (years):
    for vnut in range (12):
        osadki = float(input(f'Введите количество осадков, в мм {vnut+1}: '))
        obwee_kol_mes = years*12
        obwee_kol_osadkov += osadki
        sred_tolwina_osadkov = obwee_kol_osadkov/obwee_kol_mes
print('Общее количество месяцев: ', obwee_kol_mes)
print('Общее количество осадков: ', obwee_kol_osadkov, 'mm')
print('Среднее толщина осадков: ', sred_tolwina_osadkov, 'mm' )


# 6 Таблица соответствие между градусами Цельсия и Фаренгейта
START_TEM = 0
END_TEMP = 21
STEP = 1
print('Celsi\tFaringete')
print('------------------')
for c in range(START_TEM, END_TEMP, STEP):
    far = 9/5*c + 32
    print(f'{c}\t{far:.1f}')

# 7 Мелкая монета для зарплаты
START_KOPEEK = 0.01
KOLICHESTVO_DNEY = int(input('Введите количество отработанных дней: '))
print('№ Дня\tЗарплата в копейках')
print('---------------------------')
for dn in range (1,3,1):
    total_zp = 0
    zp = dn*START_KOPEEK
    print(f'{dn} \t {zp}')

for dn in range (3,KOLICHESTVO_DNEY+1):
    zp_1 = dn*START_KOPEEK*2
    total_zp = total_zp+zp+zp_1
    print(f'{dn} \t {zp_1:.2f}')
print('Заработная плата состовляет: ', f'{total_zp:.2f}', 'гривен')

# 8 Сумма чисел
chislo = float(input('Введите число: '))
total = 0
while chislo >= 0:
    total += chislo
    chislo = float(input('Введите число: '))

print(total)
print('good by')

# 9 ровень океана
GODA = 25
uroven6 = 1.6
print('Год \t Уровень подъема океана, mm')
print('===============================')
for years in range(1, GODA+1):
    uroven_v_god = years*uroven6
    print(f'{years} \t {uroven_v_god:.2f}', 'mm')

print('Так повышается уровень океана в год')

# 10 Рост платы за обучение
stoim_obuch_v_god = 29000
procent = 0.03
print('Схема оплаты за обучение в течении 5 лет')
print('№ Года \t Стоимость обучения')
print('=============================')
print(f'{1} \t {stoim_obuch_v_god}')
for god in range (2, 6, 1):
    stoim_obuch_v_god = stoim_obuch_v_god*1.03
    print(f'{god} \t {stoim_obuch_v_god:.2f}')

print('Так выглядит схема оплаты за обучение')

# 11 Потеря массы
print('Эта таблица показывает насколько \n'
'уменьшается ваш вес каждый месяц \n'
'при использовании грфика по сжиганию калорий')
ves = float(input('Введите ваш текущий вес (кг): '))
print("Месяц \t Ожидаемый вес через месяц" )
print('======================================')
for mes in range (1,7):
    ves = ves - 1.5
    print(f'{mes}\t{ves:.1f}',"кг")

print('Такой вес у вас будет после каждого месяца использования нашей методики!')

# 12 Вычисление факториала числа
chislo = int(input('Введите целое положительное число: '))
fact=1
for fac in range(2,chislo+1):
    fact = fact*fac
print('Факториал числа, которое вы ввели:',chislo,'- состовляет:',fact)

# 13 Популяция
start_kolichestvo = float(input('Введите стартовое количество особей: '))
sut_uvel = float(input("Введите процент увеличения популяции: "))
kol_dney = int(input('Введите количество дней для размножения: '))
procent = (sut_uvel/100)+1
print('День \t Популяция')
print('_-_-_-_-_-_-_-_-_-_')
print(f'{1} \t {start_kolichestvo} ')
for dn in range (2, kol_dney+1):
    start_kolichestvo = start_kolichestvo * procent
    print(f'{dn} \t {start_kolichestvo:.2f}')

# 14 Звездочки
rows = 7
for r in range (rows):
    for c in range(7-r):
        print('*',end='')
    print()


# 15 Решетки
steps = 6
for r in range(steps):
    print('#' + r * ' ' + '#')

