#считать 5 чисел в список
#вывести их квадраты

lst = []
for i in range(5):
    n = int(input())
    lst.append(n)

print()


for i in lst:
    print(i**2)