a=input('Введите элементы 1-го списка через запятую: ' )
b=input('Введите элементы 2-го списка через запятую: ' )
a=a.split(',')
b=b.split(',')
a = list(map(int, a))
b = list(map(int, b))
a=set(a)
b=set(b)
c=a-b
print(list(c))