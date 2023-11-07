#5.	Реализовать модуль, содержащий функцию нахождения в массиве целых чисел
#   разности индексов максимального и минимального элементов.

import find_difference

n = input("Enter the size of the array: ")
while True: #проверка числа n
    try:
        n = int(n)
        break
    except:
        n = input('Enter correct size of the array:  ')

arr = []
for i in range(n):
    x = input('Enter element: ')
    while True: #проверка каждого нового введенного элемента
        try:
            x = int(x)
            break
        except:
            x = input('Enter correct previous element:  ')
    arr.append(x)

print(find_difference.difference(arr))