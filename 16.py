
number = int(input('Vvedite cifru: ' ))
if number == 1:
    print('odin')
elif number == 2:
    print('Dva')
elif number == 3:
    print('Tri')
else:
    print('HZ')

speed = float(input('VVedite vashu skorost\': '))
if speed > 0 and speed < 200:
    print('U vas dopustimaja skorost\'!')
    print('mi vas pozdravliaem!')
else:
    print('sorry, but all bad!')

speed = float(input('Vvedite vashu skorost\': '))
if speed <= 50 or speed >= 100:
    print('It\'s very bad!')
else:
    print('It is soo good!')

if score >= A_score:
    print('Ваш уровень - А.')
else:
    if score >= B_score:
        print('Ваш уровень - В . ')
    else:
        if score >= C_score:
            print('Ваш уровень - С.')
        else:
            if score >= D_score:
                print('Ваш уровень - D.')
            else:
                print('Ваш уровень - F.')



