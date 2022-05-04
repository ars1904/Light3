a=int(input("Введите количество элементов: "))
list_1=[]
for i in range(a):
   list_1.append(int(input(f"Введите {i+1} элемент: ")))
list_1.sort()
print(f'Вывод:{list_1}')
