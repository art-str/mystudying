osnov_summa = float(input('Введи те вашу сумму депозита: '))
proc = float(input('Введите вашу процентную ставку: '))
procent = proc / 100
chastota = int(input('Как часто вам начисляются проценты: '))
kolich_let = float(input('На сколько лет вы поланируете внести депозит: '))

itog_summa = osnov_summa * (1 + procent / chastota) ** (chastota * kolich_let)

print('Сумма денег, которая будет у вас на счету составит после заданных лет состави ', f'{itog_summa:.2f}', '$')