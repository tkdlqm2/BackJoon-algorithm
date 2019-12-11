
# DFS
# @param : 시작노드
# @param : 그래프
# @param : 방문 완료 노드 리스트

def DFS(V,graph,check_array):

    # 방문된 노드는 종료
    if check_array[V] == 1:
        return


    else:

        # 방문한 노드 print, 방문 처리
        print(V,end=" ")
        check_array[V] = 1

        # 방문한 노드의 인접 노드들을 stack에 담음
        stack = []
        for i in range(0,len(graph[V])):
            if graph[V][i] == 0:
                continue
            else:
                stack.append(i)

        # 인접노드들을 대상으로 DFS 수행.
        for i in range(0,len(stack)):
            DFS(stack[i],graph,check_array)

# BFS
# @param : 시작노드
# @param : 그래프

def BFS(V,graph):

    que = [V]
    foot_prints = [V]
    while que:
        start = que.pop(0)

        # 방문한 노드의 인접노드들은 que에 담음.
        for i in range(0,len(graph[start])):
            if graph[start][i] and i not in foot_prints:
                foot_prints += [i]
                que += [i]
    return foot_prints


N, M, V = map(int,input().split())
check_array = [0] * (N+1)

graph = [[0] * (N+1) for _ in range(0,N+1)]

for i in range(0,M):
    index,mapping_index = map(int,input().split())
    graph[index][mapping_index] = 1
    graph[mapping_index][index] = 1


DFS(V,graph,check_array)
print()
print(*BFS(V,graph))
