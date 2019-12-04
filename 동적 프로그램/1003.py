# 컨셉1 : 동적 프로그래밍으로 접근 -> 버퍼 메모리제이션
# 컨셉2 : 0 의 갯수는 1의 갯수의 그 전 배열의 개수 즉, 10의 1의 개수가 fibo(10) 이면, 0의 개수는 fibo(9)임

def fibo(n,array):
    if n == 0:
        return 0
    if (n == 1) | (n == 2):
        array[n] = 1
        return array[n]
    else:
        if array[n-1] != 0:
            array[n] = array[n-1]
        else:
            array[n] = fibo(n-1, array)
        if array[n-2] != 0:
            array[n] += array[n-2]
        else:
            array[n] += fibo(n-2,array)
    return array[n]


testCase = int(input())

for i in range(0,testCase):
    number = int(input())
    array = [0] * (number+1)
    array[0] = 0
    if number == 0:
        print("1 0")
    else:
        print(fibo(number-1,array), fibo(number,array))

