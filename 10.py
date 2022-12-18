devushki = int(input('Сколько в группе девушек: '))
parni = int(input('Сколько в гуппе парней: '))
vsego = devushki + parni
devushki_proc = devushki/vsego
parni_proc = parni/vsego
print('В вашей группе: ', f'{devushki_proc:.0%}', 'девушек', '\n'
      "и", f'{parni_proc:.0%}', 'парней.')