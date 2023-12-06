#2. Дана действительная матрица размером n х m, все элементы которой различны.
#   В каждой строке выбирается элемент с наименьшим значением.
#   Если число четное, то заменяется нулем, нечетное - единицей. Вывести на экран новую матрицу.






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
        while 1:
            x = input('Enter element: ')
            while True:
                try:
                    x = float(x)
                    break
                except:
                    x = input('Enter correct element:  ')
            if any(x in r for r in mas):
                print("The value is already there, enter another one: ")
            else:
                break
        row.append(x)
    mas.append(row)
print(mas)

mas2 = mas
for i in range(n):
    min_el = min(mas2[i])
    for idx, val in enumerate(mas2[i]):
#Функция enumerate() применяется для прохода по значениям коллекции,
#при этом предоставляется информация о номере каждого элемента.
        if val == min_el and int(min_el) == min_el:
            mas2[i][idx] = min_el % 2
print(mas2)