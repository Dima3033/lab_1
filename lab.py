num_1=int(input('ціна приставки'))
num_2=int(input('кількість приставок'))
num_3=int(input('знижка на приставку'))
num_4=int(input('1 сума всіх приставок \n 2 одна приставка \n '))
if num_4==1:
    s=num_1*num_2
    print(s)
elif num_4 == 2:
    s= num_1/100*num_3
    a = num_1 - s
    print(a)


