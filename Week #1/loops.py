# lst = [1,2,-4,5,-10]
# for item in lst:
#     print(item * 2)


number = int(input())
num_1 = 1
num_2 = 1
for item in range(number):
    c = num_2
    num_2 = num_1 + num_2
    num_1 = c 

print(num_2)
