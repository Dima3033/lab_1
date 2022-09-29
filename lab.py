h = int(input('Введіть кількість годин:'))
if h>=0  and h<6:
    print('Good night!')
elif h>=6 and h<13:
    print('Good Morning!')
elif h>=13 and h<17:
    print('Good day!')
elif h>=17 and h<23:
    print('Good Evening!')