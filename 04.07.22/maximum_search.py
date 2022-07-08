#поиск максимума в списке
lst = []
for i in range(10):
    n = int(input())
    lst.append(n)


maximum = lst[0]
for i in range(10):
    if lst[i] > maximum:
        maximum = lst[i]

print(maximum)