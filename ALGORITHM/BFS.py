# 1. 기본
def BFS(Graph, start):          # 그래프 Graph, 탐색 시작점 start
    visited_arr = [False] * (n+1) # visited arr 모두 false로 초기화, n은 정점의 개수
    queue = [start]               # 큐 생성, 시작점 start를 큐에 삽입
    # 시작점 start 방문
    while queue:                  # 큐가 비어있지 않은 경우 = 더 방문할 정점이 있음
        go = queue.pop(0)           # 큐의 첫번째 원소로 이동
        if not visited_arr[go]:     # 다음 방문할 정점인 go가 방문하지 않은 정점이라면,
            visited_arr[go] = True    # 방문 도장
            visit(go)                 # 방문한 노드에서 할 일
        for i in Graph[go]:       # go와 연결된 정점 중
            if not visited_arr[i]:
                queue.append(i)       # 방문하지 않았던 정점을 큐에 추가(나중에 이동 예정)

####################################################################################
# 2. 인접행렬 구하고, 이동
# 라이브 강의 진행 코드 (인접 리스트)
'''
input.txt
7 8 
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 
################################
output
1 2 3 4 5 7 6
'''

def bfs(start, V):                       # 시작정점 s, 마지막 정점 V
    visited_arr = [0] * (V + 1)          # 방문 여부 표기할 visited_arr 생성
    que = [start]                        # 큐 생성, 시작 정점 enQueue
    visited_arr[start] = True            # 시작점 방문표시
    
    while que:                           # 큐에 정점이 남아있으면 front != rear
        go = que.pop(0)                  # 다음 이동할 정점 pop = deQueue
        print(go)                        # 방문한 정점에서 할일
        for elem in adj_l[go]:           # 인접한 정점 중 인큐되지 않은 정점 elem가 있으면
            if visited_arr[elem] == False: # enQueue한 적 없음
                que.append(elem)         # 인접 원소가 enQueue되었음을 표시
                visited_arr[elem] = visited_arr[go] + 1


V, E = map(int, input().split())         # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))

# 인접리스트 -------------------------
adj_l = [[] for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)  # 방향이 없는 경우

# 함수 호출
bfs(1, V)

####################################################################################

"""
라이브 강의 진행 코드 (인접행렬)
"""
# def bfs(s, V):  # 시작정점 s, 마지막 정점 V
#     visited = [0] * (V + 1)  # visited 생성
#     q = []  # 큐 생성
#     q.append(s)  # 시작점 인큐
#     visited[s] = 1  # 시작점 방문표시
#     while q:  # 큐가 비어있지 않은 동안 반복
#         t = q.pop(0)  # 디큐
#         print(t)  # 방문한 정점 출력
#         for w in range(1, V + 1):  # 모든 노드에 대해
#             # 현재 노드와 연결되어 있고, 아직 방문하지 않은 노드라면
#             if adj_m[t][w] == 1 and visited[w] == 0:
#                 q.append(w)  # w 인큐, 인큐 되었음을 표시
#                 visited[w] = visited[t] + 1
#     # print(visited)


# V, E = map(int, input().split())  # 1번부터 V번 정점, E개의 간선
# arr = list(map(int, input().split()))  # 간성 정보

# # 인접행렬
# adj_m = [[0] * (V + 1) for _ in range(V + 1)]

# for i in range(E):
#     v1, v2 = arr[i * 2], arr[i * 2 + 1]
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1  # 방향이 없는 경우

# bfs(1, V)