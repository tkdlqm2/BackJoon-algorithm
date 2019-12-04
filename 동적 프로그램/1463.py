# 컨셉 1: 동적프로그래밍을 활용하여 메모리 제이션을 통해 시간을 단축
# 컨셉 2: Input 값에 맞게 배열 선언
# 컨셉 3: 과정을 하나씩 진행하면서 조건에 만족하는 값을 도출.


import sys

N = int(sys.stdin.readline())
arr = [0] * (N+1)

arr[1] = 0

for i in range(2, N+1):

    arr[i] = arr[i - 1] + 1
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[int(i / 2)] + 1)
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[int(i / 3)] + 1)

print(arr[N])