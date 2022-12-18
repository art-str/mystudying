tov1 = float(input('Введите стоимость товара1: '))
tov2 = float(input('Введите стоимость 2го товара: '))
tov3 = float(input('Введите стоимость вашего 3го товара: '))
tov4 = float(input("Стоимость 4го товара: "))
tov5 = float(input('А теперь и ваш 5й товар: '))
stoim = tov1+tov2+tov3+tov4+tov5
nalog = stoim * 0.07
itog_summa = stoim + nalog
print('Стоимость купленных товаров составила: ', f'{stoim:.1f}')
print('Налог на данные товары состовил: ', f'{nalog:.2f}')
print('Итого к оплате: ', f'{itog_summa:.2f}')

n=9
fact=1
for i in range(2,n+1):
    fact=fact*i
    print("The factorial of ",n," is: ",fact)
