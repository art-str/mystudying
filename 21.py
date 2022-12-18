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

