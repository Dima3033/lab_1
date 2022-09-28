sec = int(input("sec->"))
end = 86400
between = end - sec
min = 0
h = 0
print(f'Your time: Hours {int(sec/3600)} Minutes {int((sec%3600)/60)} Seconds {int((sec%3600)%60)}')
if between > 0:
    h = int(between/3600)
    min = int((between % 3600)/60)
    sec = int((between % 3600) % 60)
    print(f'Left time to midnight: {h}:{min}:{sec}')
else:
    print('Erorr!')