'''eda_1 = float(input('Укажите стоимость 1го блюда: '))
eda_2 = float(input('Укажите стоимость 2го блюда: '))
eda_3 = float(input('Укажите стоимость 3го блюда: '))
eda_4 = float(input('Укажите стоимость 3го блюда: '))
eda_5 = float(input('Укажите стоимость 3го блюда: '))
учеба


eda_vsego = eda_1+eda_2+eda_3+eda_4+eda_5
chai = eda_vsego*0.18
nalog = (eda_vsego+chai)*0.07
itogo = eda_vsego+chai+nalog
print('Сумма заказа составила: ', f'{eda_vsego:.2f}', ' гривен')
print('Сумма чаевых состовляет: ', f'{chai:.2f}', 'гривен')
print('Налог на покупки: ', f'{nalog:.2f}', 'гривен')
print('Итого с Вас: ', f'{itogo:.2f}', 'гривен')'''
kolvo_blud = int(input('Укажите кол-во блюд: '))
eda_vsego = 0
for count in range(kolvo_blud):
    eda_1 = float(input('Укажите стоимость блюда: '))
    eda_vsego += eda_1

chai = eda_vsego*0.18
nalog = eda_vsego *0.07
itogo = eda_vsego+chai+nalog
print('Сумма заказа составила: ', f'{eda_vsego:.2f}', ' гривен')
print('Сумма чаевых состовляет: ', f'{chai:.2f}', 'гривен')
print('Налог на покупки: ', f'{nalog:.2f}', 'гривен')
print('Итого с Вас: ', f'{itogo:.2f}', 'гривен')











