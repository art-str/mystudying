x = float(input('Vvedite chislo: '))
if x >= 100:
    y = 20
    z = 40
    print (y)
    print (z)

a = float(input('Vvedite chislo: '))
if a <= 10:
    b = 0
    c = 1
    print(b)
    print(c)

a = float(input('Vvedite chislo: '))
if a <= 10:
    b = 0
    print (b)
else:
    b = 99
    print (b)


amount1 = float(input('Vvedite chislo 1: '))
amount2 = float(input('Vvedite chislo 2: '))
if amount1>10 and amount2<100:
    if amount1>amount2:
        print(amount1)
    else:
        print(amount2)

speed = int(input('Vvedite vashu skorost\': '))
if speed >= 24 and speed <= 56:
    print('Skorost\' normalnaja!')
else:
    print('Skorost\' avariynaja!')

points = float(input('Vvedite chislo: '))
if points <= 9 or points >= 51:
    print('Nedopustimie tochki!')
else:
    print('Dopustimie tochki')

# 1 This programm shows days of week


day = int(input('Vvedite chislo:): '))

if day == 1:
    print('Today is monday:(')
elif day == 2:
    print('Today is tuesday!')
elif day == 3:
    print('So it is wednsday!')
elif day == 4:
    print('yea, it is thursday already!')
elif day == 5:
    print('The week coms to end: it is friday!')
elif day == 6:
    print('Yea? weekend! It is saurday!:)')
elif day == 7:
    print('you go at work tomorrow:(')
else:
    if day < 1 or day > 7:
        print('X3 wich day is today!')

# 2 Эта программа сравнивает площади прямоугольников
shirina_pru1 = float(input('Vvedite shirine prjamougolnika1: '))
dlina_pru1 = float(input('Vvedite dlinu prjamougolnika 1: '))
ploshjad1 = shirina_pru1 * dlina_pru1
shirina_pru2 = float(input('Vvedite shirinu vtorogo prjamougolnika: '))
dlina_pru2 = float(input('Vvedite dlinu 2go prjamougolnika: '))
ploshjad2 = shirina_pru2 * dlina_pru2
if ploshjad1 > ploshjad2:
    print('Pervii prjamougolnik bol\'she vtorogo')
elif ploshjad2 > ploshjad1:
    print('Vtoroy prjamougolnik bol\'she pervogo')
else:
    print('Ugolniki ravni')

#N3 Классификатор возраста
AGE_1 = 1
AGE_2 = 13
AGE_3 = 20
age = float(input('Vvedite vash vozrast: '))
if age <= AGE_1:
    print('Tak eto mlodenec!')
elif age < AGE_2:
    print('Eto rebenok')
elif age < AGE_3:
    print('Vi pdrostok')
else:
    print('Vi vzrosliy')

# 4Классификатор римских цифр

chislo = int(input('Vvedite chislo: '))
if chislo == 1:
    print('Eto rimskaja I')
elif chislo == 2:
    print('Eto rimskaja II')
elif chislo == 3:
    print('Rimskaja III')
elif chislo == 4:
    print('A eto rimskaja IV')
elif chislo == 5:
    print('Eto rimskaja V')
elif chislo == 6:
    print('Eto rimskay VI')
elif chislo == 7:
    print('Vot rimskaja VII')
elif chislo == 8:
    print('Eto rimskaja VIII')
elif chislo == 9:
    print('Eto rimskaja IX')
elif chislo == 10:
    print('Eto rimskaja X')
else:
    if chislo < 1 or chislo > 10:
        print('IT is error')

# 5 Programma vichisljaet ves
massa = float(input('Vvedite vashu massu: '))
ves = massa * 9.8
if ves > 500:
    print('Vashe telo slishkom tjazholoe!')
elif ves < 100:
    print('Vashe telo slishkom legkoe!')
else:
    print('vse ok!')

# 6 Programma "Магические даты"
den = int(input('Vvedite chislo mesjaca: '))
mes = int(input('Vvedite mesjac: '))
god = int(input('Vvedite god (poslednie 2 cifri): '))
magia = den * mes
if magia == god:
    print('Введенная дата является магической!:)')
else:
    print('К сожалению дата не магическая:(')

#7 Цветовой миксер
KRASNIY = 'красный'
SINIY = 'синий'
ZHELTIY = 'желтый'
cvet1 = input('Vvedite 1y osnovnoy cvet: ')
cvet2 = input('Vvedite 2y osnovnoy cvet: ')
if cvet1 == KRASNIY and cvet2 == SINIY:
    print('Tak poluchitsja fioletoviy;) ')
elif cvet1 == KRASNIY and cvet2 == ZHELTIY:
    print('A eto orangheviy')
elif cvet1 == SINIY and cvet2 == ZHELTIY:
    print('Vot eto zeleniy:)')
elif cvet1 == SINIY and cvet2 == KRASNIY:
    print('Tak poluchitsja fioletoviy;) ')
elif cvet1 == ZHELTIY and cvet2 == KRASNIY:
    print('A eto orangheviy')
elif cvet1 == ZHELTIY and cvet2 == SINIY:
    print('Vot eto zeleniy:)')
else:
    print('Drugie cveta ja ne smescivayu:(...')

#8 Калькулятор сосисок
SOSISKI_UPAKOVKA = 10
BULOCHKA_UPAKOVKA = 8
kol_chelovek = int(input('Vvedite kolichestvo chelovek: '))
kol_hotdogov = int(input('Vvedite kolichestvo hotgov na cheloveka: '))
kol_up_sosisok = kol_chelovek * kol_hotdogov
kol_up_bul = kol_chelovek * kol_hotdogov
if kol_chelovek == 0 and kol_hotdogov == 0:
    print('Vam ne nuzhno ni sosisok ni bulochek!')
else:
    if kol_up_sosisok % 10 == 0:
        min_col_up_sosisok = kol_up_sosisok // SOSISKI_UPAKOVKA
        print('Vam nuzhno minimum', f'{min_col_up_sosisok}', 'upakovok sosisok')
        ostatok_sosisok = (min_col_up_sosisok * SOSISKI_UPAKOVKA) - kol_up_sosisok
        print('Vash ostatok sosikok', ostatok_sosisok, 'shtuk')

    else:
        kol_up_sosisok = kol_chelovek * kol_hotdogov
        kol_sosisok = kol_up_sosisok * SOSISKI_UPAKOVKA
        min_col_up_sosisok = kol_up_sosisok // SOSISKI_UPAKOVKA + 1
        ostatok_sosisok = (min_col_up_sosisok * SOSISKI_UPAKOVKA) - kol_up_sosisok
        print('Vam nuzhno minimum', f'{min_col_up_sosisok}', 'upakovok sosisok')
        print('Vash ostatok sosikok', ostatok_sosisok, 'shtuk')

if  kol_up_bul % 8 == 0:
    min_col_up_bulochek = kol_up_bul // BULOCHKA_UPAKOVKA
    print('Vam nuzhno minimum', f'{min_col_up_bulochek}', 'upakovok bulochek')
    ostatok_bulochek = (min_col_up_bulochek * BULOCHKA_UPAKOVKA) - kol_up_bul
    print('Vash ostatok bulochek', ostatok_bulochek, 'shtuk')
else:
    kol_up_bul = kol_chelovek * kol_hotdogov
    kol_bulochek = kol_up_bul * BULOCHKA_UPAKOVKA
    min_col_up_bulochek = kol_up_bul // BULOCHKA_UPAKOVKA + 1
    ostatok_bulochek = (min_col_up_bulochek * BULOCHKA_UPAKOVKA) - kol_up_bul
    print('Vam nuzhno minimum', f'{min_col_up_bulochek}', 'upakovok bulochek')
    print('Vash ostatok bulochek', ostatok_bulochek, 'shtuk')

# 9 Koleso cvetov
chislo = int(input('Vvedite chislo ot 0 do 36: '))
if chislo == 0:
    print('Eto zeleniy!')
elif chislo==1 or chislo==3 or chislo==5 or chislo==7 or chislo==9:
    print('Eto krasniy!!!')
elif chislo == 2 or chislo == 4 or chislo == 6 or chislo == 8 or chislo == 10:
    print ('Bingo - cherniy!')
elif chislo == 11 or chislo == 13 or chislo == 15 or chislo == 17:
    print('Cherniy')
elif chislo == 12 or chislo == 14 or chislo == 16 or chislo == 18:
    print ('Snova krasniy')
elif chislo == 19 or chislo == 21 or chislo == 23 or chislo == 25 or chislo == 27:
    print('Eto krasniy')
elif chislo == 20 or chislo == 22 or chislo == 24 or chislo == 26 or chislo == 28:
    print('Cherniy cherniy')
elif chislo == 29 or chislo == 31 or chislo == 33 or chislo == 35:
    print('Cherniy cvet')
elif chislo == 30 or chislo == 32 or chislo == 34 or chislo == 36:
    print ('Krasniy')
else:
    if chislo < 0 or chislo > 36:
        print ('Error, i know not this number')

# 9 Колесо цветов
karman = int(input('Vvedite chislo ot 0 do 36: '))
if karman == 0:
    print('Eto zeleniy!')
elif karman >= 1 and karman <= 10:
    if karman % 2 == 0:
        print('Это черный')
    else:
        karman % 2 != 0
        print('это красный')
elif karman >= 11 and karman <= 18:
    if karman % 2 == 0:
        print('Это красный')
    else:
        karman % 2 != 0
        print('это черный')
elif karman >=19 and karman <= 28:
    if karman % 2 == 0:
        print ('Это черный карман')
    else:
        karman % 2 != 0
        print('Это красненький карманчик:)')
elif karman >=29 and karman <= 36:
    if karman % 2 == 0:
        print ('Это красный  карман')
    else:
        karman % 2 != 0
        print('Это черненький карманчик:)')
else:
    print('это число не относится ни к какому карману')

# 10 Igra v moneti
KOPEEK_5 = 0.05
KOPEEK_10 = 0.10
KOPEEK_50 = 0.50
moneti_5 = int(input('Vvedite kolichestvo monet nominalom 5 kopeek: '))
moneti_10 = int(input('Vvedite kolichestvo monet nominalom 10 kopeek: '))
moneti_50 = int(input('Vvedite kolichestvo monet nominalom 50 kopeek: '))
summa_monet_5 = KOPEEK_5 * moneti_5
summa_monet_10 = KOPEEK_10 * moneti_10
summa_monet_50 = KOPEEK_50 * moneti_50
summa_monet = summa_monet_5 + summa_monet_10 + summa_monet_50
if summa_monet < 1 or summa_monet > 1:
    print('''Summa monet ne rovnjaetsa 1 grivne' 
'Vi proigrali!''')
else:
    print('Pozdrovljaem - vi vigrali!')

# 11 Ochki knizhnogo kluba

kolichestvo_knig = int(input('Vvedite kolichestvo knig, kotorie vi kupili: '))
if kolichestvo_knig == 0 or kolichestvo_knig == 1:
    print('Vi poluchili 0 balov v etom mesjace')
elif kolichestvo_knig >= 2 and kolichestvo_knig < 4:
    print('Vi poluchili 5 balov')
elif kolichestvo_knig >= 4 and kolichestvo_knig < 6:
    print('Vi poluchili 15 balov v etom mesjace')
elif kolichestvo_knig >= 6 and kolichestvo_knig < 8:
    print('Vam nachisleno 30 balov')
else:
    print('Vi molodec - dlja vas 60 balov!:)')

# 12 Realizacija PO
SKIDKA_10 = 0.1
SKIDKA_20 = 0.2
SKIDKA_30 = 0.3
SKIDKA_40 = 0.4
STOIMOST6 = 99
kolichestvo_paketov = int(input('Vvedite kolichestvo paketov, kotorie vi preobrili: '))
if kolichestvo_paketov < 10:
    print('K sozhaleniju u vas net skidki')
elif kolichestvo_paketov >= 10 and kolichestvo_paketov <= 19:
    skidka = SKIDKA_10 * STOIMOST6
    stoimost6 = (STOIMOST6 - skidka)*kolichestvo_paketov
    print('Vasha skidka sostovljaet', skidka, '$')
    print('Stoimost6 vashei pokupki sostavljaet', stoimost6, '$')
elif kolichestvo_paketov >= 20 and kolichestvo_paketov <= 49:
    skidka = SKIDKA_20 * STOIMOST6
    stoimost6 = (STOIMOST6 - skidka)*kolichestvo_paketov
    print('Vasha skidka sostovljaet', skidka, '$')
    print('Stoimost6 vashei pokupki sostavljaet', stoimost6, '$')
elif kolichestvo_paketov >= 50 and kolichestvo_paketov <= 99:
    skidka = SKIDKA_30 * STOIMOST6
    stoimost6 = (STOIMOST6 - skidka)*kolichestvo_paketov
    print('Vasha skidka sostovljaet', skidka, '$')
    print('Stoimost6 vashei pokupki sostavljaet', stoimost6, '$')
else:
    skidka = SKIDKA_40 * STOIMOST6
    stoimost6 = (STOIMOST6 - skidka)*kolichestvo_paketov
    print('Vasha skidka sostovljaet', skidka, '$')
    print('Stoimost6 vashei pokupki sostavljaet', stoimost6, '$')

# 13 Stoimost6 dostavki
VES_200 = 150
VES_600 = 300
VES_1000 = 400
VES_SVISHE_1000 = 475
massa_paketa = float(input('Vvedite ves vashei posilki v grammah: '))
if massa_paketa <= 200:
    plata_za_dostavku = massa_paketa * VES_200 / 100
    print('Oplata za dostavku sostavit: ', f'{plata_za_dostavku:,.2f}', 'griven')
elif massa_paketa > 200 and massa_paketa <= 600:
    plata_za_dostavku = massa_paketa * VES_600 / 100
    print('Oplata za dostavku sostavit: ', f'{plata_za_dostavku:,.2f}', 'griven')
elif massa_paketa > 600 and massa_paketa <= 1000:
    plata_za_dostavku = massa_paketa * VES_1000 / 100
    print('Oplata za dostavku sostavit: ', f'{plata_za_dostavku:,.2f}', 'griven')
else:
    plata_za_dostavku = massa_paketa * VES_SVISHE_1000 / 100
    print('Oplata za dostavku sostavit: ', f'{plata_za_dostavku:,.2f}', 'griven', 'Da mi dorogaja companija')

# 14 Индекс массы тела

massa = float(input('Введите Ваш вес в килограммах: '))
rost = float(input('Введите ваш рост в метрах: '))
imt = massa / (rost**2)
print('Ваш индекс массы тела: ', imt)
if imt >= 18.5 and imt <= 25.0:
    print('У вас оптимальный индекс массы тела!:)')
elif imt < 18.5:
    print('Вы веситите ниже нормы')
else:
    print('Ваш вес больше нормы')

# 15 Калькулятор времени
total_seconds = float(input('Введите количество секунд: '))
seconds = total_seconds % 60
minutes = (total_seconds // 60) % 60
hours = total_seconds // 3600
days = total_seconds // 86400
if total_seconds < 60:
    print('Это', total_seconds, 'сукунд')
elif total_seconds >= 60 and total_seconds < 3600:
    print(minutes, 'минут')
    print('и', seconds, "секунд")
elif total_seconds >= 3600 and total_seconds < 86400:
    print('Это', hours, 'часа(ов)')
    print(minutes, 'минут')
    print('и', seconds, "секунд")
else:
    print('Так получается', days, 'день(дней)')
    print('Это', hours, 'часов')
    print(minutes, 'минут(ы)')
    print('и', seconds, "секунд")

# 16 дни в феврале
god = int(input('Введите год: '))
if god % 100 == 0:
    if god % 400 != 0:
        if god % 4 == 0:
            print('Год не высокосный')
if god % 100 == 0:
    if god % 400 == 0:
        print('Год высокосный')

elif god % 100 != 0:
    if god % 4 == 0:
        print('Год высокосный')

    else:
        print('Год не высококосный')

# 17 Проверка качества WI FI
otvet = 'да'
otvet = 'нет'
print('Перезагрузите компьютер и\nпопробуйте подключиться')
otvet = input('Исправили проблему: ')
if otvet == 'да':
    print('Мы рады вам помочь')
elif otvet == 'нет':
    print('Перезагрузите маршрутизатор и попробуйте подключиться')
    otvet = input('Исправили проблему: ')
    if otvet == 'да':
        print('Мы рады вам помочь')
    elif otvet == 'нет':
        print('Убедитесь, что кабели между маршрутизатором и\nмодемом прочно соеденены')
        otvet = input('Исправили проблему: ')
        if otvet == 'да':
            print('Мы рады вам помочь')
        elif otvet == 'нет':
            print('Переместите маршрутизатор в другое место')
            otvet = input('Исправили проблему: ')
            if otvet == 'да':
                print('Мы рады вам помочь')
            elif otvet == 'нет':
                print('Возьмите новый маршрутизатор')
                print('Мы рады вам помочь')

# 18 Селектор ресторанов

spisok_1_vse_da = '"Кафе за углом"\n"Кухня шеф повара"'
spisok_2_1_da = '"Центральная пиццерия"\n"Кафе! за углом"\n"Блюда от итал мамы"\n"Кухня шеф-повара"'
spisok_3_2_da = '"К!афе за углом"\n"Кухня шеф-повара"'
spisok_4_3_da = '"Центральная пиццерия"\n"Кафе за углом"\n"Кухня шеф-повара"'
spisok_5_1_i_2_da = '"Ка!фе за углом"\n"Кухня шеф-повара"'
spisok_6_1_i_3_da = '"Центральная пиццерия"\n"Кафе з-а углом"\n"Кухня шеф_повара"'
spisok_6_2_i_3_da = '"Кафе за углом"\n"Кафе Ш Еф-повара"'
spisok_6_vse_net = '"Изысканная кухня от Джо"'
otvet_1 = input('Будет ли на ужине вегатарианец: ')
otvet_2 = input('Будет ли на ужине веганец: ')
otvet_3 = input('Будет ли на ужине приверженец безглютеновской еды: ')
if otvet_1 == 'да' and otvet_2 == 'да' and otvet_3 == 'да':
    print('Вам подойдет:', spisok_1_vse_da)
elif otvet_1 == 'да' and otvet_2 == 'нет' and otvet_3 == 'нет':
    print('Вам подойдет: ', spisok_2_1_da)
elif otvet_1 == 'нет' and otvet_2 == 'да' and otvet_3 == 'нет':
    print('Вам подойдет: ', spisok_3_2_da)
elif otvet_1 == 'нет' and otvet_2 == 'нет' and otvet_3 == 'да':
    print('Вам подойдет: ', spisok_4_3_da)
elif otvet_1 == 'да' and otvet_2 == 'да' and otvet_3 == 'нет':
    print('Вам подходит: ', spisok_5_1_i_2_da)
elif otvet_1 == 'да' and otvet_2 == 'нет' and otvet_3 == 'да':
    print('Вам подходит: ', spisok_6_1_i_3_da)
elif otvet_1 == 'нет' and otvet_2 == 'да' and otvet_3 == 'да':
    print('Ваш вариант: ', spisok_6_2_i_3_da)
else:
    otvet_1 == 'нет' and otvet_2 == 'нет' and otvet_3 == 'нет'
    print('Вам подойдет: ', spisok_6_vse_net)


