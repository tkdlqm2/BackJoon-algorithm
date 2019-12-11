#1260 번의 DFS 개념을 적용하면 풀기 쉬웠음.

# @param : 시작점
# @param : 그래프
# @param : 방문 확인 리스트

def DFS(V,graph,check_array):
    if check_array[V] == 1:
        return
    else:
        check_array[V] = 1
        stack = []
        for i in range(0,len(graph[V])):
            if graph[V][i] == 0:
                continue
            else:
                stack.append(i)

        for i in range(0,len(stack)):
            DFS(stack[i],graph,check_array)


N = int(input())
graph = [[0] * (N+1) for _ in range(N+1)]
check_array = [0] * (N+1)
n = int(input())

for i in range(0,n):
    index1,index2 = map(int,input().split())
    graph[index1][index2] = 1
    graph[index2][index1] = 1


DFS(1,graph,check_array)

# 방문 처리를 1로 했고, 1번 컴퓨터 자신을 빼야함.
print(check_array.count(1)-1)
