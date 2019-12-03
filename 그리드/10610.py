
# 컨셉1 : 높은 수 정렬

Number = list(input())
answer = ''
buffer = []

Number.sort()
for i in range(0,len(Number)):
    answer += Number.pop()

answer = int(answer)

if answer%30 == 0:
    print(answer)
else:
    print(-1)
