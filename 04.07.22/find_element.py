#поиск индекса введенного числа
lst = []
for i in range(10):
    n = int(input())
    lst.append(n)

print('Введите число для поиска:')
n = int(input())

print()
for i in range(10):
    if lst[i] == n:
        print(i)


    


