#1. Упорядочить по возрастанию элементы каждой строки матрицы размером n х m.

print('Enter size of matrix: ')
n = input('Enter n: ')
while True:
    try:
        n = int(n)
        break
    except:
        n = input('Enter correct n:  ')
m = input('Enter m: ')
while True:
    try:
        m = int(m)
        break
    except:
        m = input('Enter correct m:  ')

mas = []
i = 0
j = 0
for i in range(n):
    row = []
    print('Enter new row')
    for j in range(m):
        x = input('Enter element: ')
        while True:
            try:
                x = int(x)
                break
            except:
                x = input('Enter correct element:  ')
        row.append(x)
    mas.append(sorted(row))
print(mas)