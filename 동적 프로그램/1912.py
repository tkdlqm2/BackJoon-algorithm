import sys

n = int(sys.stdin.readline())
list = []
list = (input().split(' '))
max = -2147483648
sum = 0
count = 0
k = 1

for i in range(0,len(list)):

    tmp =int(list[i])
    if tmp > max:
        max = tmp

    sum += tmp
    if (sum > 0):
        if max < sum:
            max = sum

    else:
        sum = 0;


print(max)