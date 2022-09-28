num_1=int(input('введіть діаметр -'))
x = 3.14
S = int(input('Виберіть операцію: \n 1 площа кола \n 2 периметр кола'))
if S == 1:
    p = (x*num_1*num_1)
if S == 2:
    p = (x*num_1*2)
print(f'p ={p}')