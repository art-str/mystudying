r = float(input('Введите длину вашей грядки: '))
e = float(input('Введите размер концевых опор: '))
s = float(input('Введите расстояние между виноградными лозами: '))
kolich = (r-2*e)/s
print('Вы можете посадить: ', f'{kolich:.0f}', "лоз винограда!")