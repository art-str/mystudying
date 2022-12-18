BAS_HOURS = 40
MULTIPLIKATOR = 1.5

hours = int(input('Введите количество отработанных часов: '))
stavka = float(input('Введите почасовую оплату: '))

if hours > BAS_HOURS:
    over_hours = hours - BAS_HOURS
    over_pay = over_hours * stavka * MULTIPLIKATOR
    oplata = hours * stavka + over_pay

else:
    oplata = hours * stavka

print('Ваша зарплата составила: ', f'{oplata:.2f}', "гривен")