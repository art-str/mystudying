akcii = 2000
akcii_pokupka = akcii*40
komis_pokupka = akcii_pokupka*0.03
akcii_prod = akcii*42.75
komis_prod = akcii_prod*0.03
ostatok = akcii_prod - akcii_pokupka - (komis_prod+komis_pokupka)
print('Джо заплатил за акции: ', akcii_pokupka, '\n'
      'Комиссия брокера составила: ', komis_pokupka, '\n'
      'Джо продал акции на сумму: ', akcii_prod, '\n'
      'Комиссия брокера за продажу акции составила: ', komis_prod, '\n'
      'Остаток денег у Джо составил: ', ostatok, '$.')