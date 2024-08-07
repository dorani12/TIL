# 인접 행렬 구하기
node = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']  # 0번 인덱스는 생각하지 않음
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 5
# A B   C   D   E   F       G 
'''
인접 행렬(adjacency matrix)
- n*n 크기의 정사각형 행렬
- 노드들 간의 연결 관계를 행렬로 표현한 것
- 무방향 그래프
    -> 정점 i와 j 사이에 간선이 있다면 matrix[i][j] = maxtrix[j][i] = 1, 없으면 0
'''

# # 일단 손코딩 
# # 이중 리스트 크기는 정점+1*정점+1 : 0은 무시
# # 간선을 표기 matrix[i][j] = maxtrix[j][i] = 1
# matrix = [
#     #   A  B  C  D  E  F  G
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0, 0, 0, 0], # A
#     [0, 1, 0, 0, 1, 1, 0, 0], # B
#     [0, 1, 0, 0, 0, 1, 0, 0], # C
#     [0, 0, 1, 0, 0, 0, 1, 0], # D
#     [0, 0, 1, 1, 0, 0, 1, 0], # E
#     [0, 0, 0, 0, 1, 1, 0, 1], # F
#     [0, 0, 0, 0, 0, 0, 1, 0]  # G
# ]

def DFS(s, V):                          # 시작 정점 s, 정점의 개수 V
    stack = [s]                         # 스택의 시작 정점 push/# 현위치, 방문 안 끝난 정점을 넣을 stack
    visited = [0] * (V + 1)             # 방문 여부를 체크하는 리스트, 0번 인덱스는 무시

    # stack이 빌 때까지 DFS 진행
    while stack:
        current = stack.pop()           # 현재 조사할 노드

        # 방문x 노드0
        if visited[current] == 0:       # 방문하지 않은 노드라면
            visited[current] = 1        # 방문 했음 표시
            print(node[current])        # 방문한 노드 출력

            # 다음 노드들을 stack에 추가
            # for next in range(1, V+1): 큰 번호 우선 탐색, V부터 1까지 역순으로 확인
            for next in range(V, 0, -1): # 후입선출(먼저 갈 노드를 나중에 넣기), 작은번호 우선 탐색
                # 간선이 현재 정점과 연결되어 있음 & 방문하지 않았음
                if adj_matrix[current][next] == 1 and visited[next] == 0:
                    stack.append(next)    # stack에 push 
# 인접 행렬 만들기
# v : 노드의 개수
# E : 간선의 개수
V, E = map(int, input().split())

adj_matrix = [[0] * (V+1) for _ in range(V+1)] # 0번째 인덱스는 무시 -> V+1

data = list(map(int, input().split()))  # 노드별 간선 정보
# 간선 정보를 넣기: 간선의 개수만큼 반복
for n in range(E):
    i, j = data[2*n], data[2*n+1]
    adj_matrix[i][j] = 1
    adj_matrix[j][i] = 1

DFS(1, 7)

##############################################################################
# 정점의 개수와 정점들간의 관계 주어졌을 때
# DFS로 탐색하기 & 방문 순서
# 인접 list 구하는 방식
''' 
input data 
1  # testcase
7 8  # 정점의 개수 7, 정점 쌍의 개수 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def DFS(s, V):            # 시작 정점 s, 정점개수 V
    visited = [0]*(V+1)     # 방문한 정점을 표시할 리스트
    stack = []              # 스택 생성 (현 위치)
    visited[s] = 1          # 시작 정점 방문 표시
    v = s
    while True:
        for w in adjL[v]:     # v에 인접하고, 방문 안한 w가 있으면..
            if visited[w] == 0:
                stack.append(v)   # 현재 정점 push, push(v)
                v = w             # w에 방문
                print(v)
                visited[w] = True # w에 방문 표시
                break             # 남은 갈림길로 가는거 x, v부터 다시 탐색
        else:                 # 남은 인접정점 x, break 없이 반복문 모두 실행시
            if stack:           # 이전 갈림길을 stack에서 꺼내기
                v = stack.pop()
            else:               # 되돌아갈 곳이 없으면, 남은 갈림길이 없음 => 탐색 종료
                break             # while True:

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  # 정점의 개수, 쌍의 개수 
    adjL = [[] for _ in range(V+1)]   # 인접한 원소를 저장할 리스트
    arr = list(map(int, input().split()))
    for i in range(E):
        V1, V2 = arr[i*2], arr[i*2+1]
        adjL[V2].append(V1)
        adjL[V1].append(V2)

##############################################################################
# DFS 모든 과정
'''
input data
7 8  # 정점의 개수 7, 노드 = 정점 연결된 쌍의 개수 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def DFS(start):
    stack = [start]                 # 시작 지점을 현재 방문한 정점, 갈림길이 남았던 정점을 담을 스택
    visited = [0] * (V + 1)         # 방문 여부 확인할 리스트

    while stack:                    # stack에 값이 있는 동안만 반복
        current = stack.pop()       # 현재 조사할 노드

        if visited[current] == 0:   # 방문하지 않은 노드만 생각
            visited[current] = 1    # 방문 도장 찍기
            print(current, end = ' ') # 출력

            for next in range(V, 0, -1):  # 역순으로 넣기 = 작은 수 부터 방문
                # 인접 list에서 연결되고, 방문하지 않음 -> stack에 넣기
                if matrix[current][next] == 1 and visited[next] == 0:
                    stack.append(next)


V, E = map(int, input().split())  # 정점, 노드의 개수
data = list(map(int, input().split()))  # 노드별 간선 정보

# 인접행렬 생성
# 빈 도화지
matrix = [[0] * (V+1) for _ in range(V+1)]
for n in range(E):
    i, j = data[2*n], data[2*n+1]
    matrix[i][j] = 1
    matrix[j][i] = 1

DFS(1)

##############################################################################
# DFS 마지막 방법: 재귀
'''
input data
7 8  # 정점의 개수 7, 노드 = 정점 연결된 쌍의 개수 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def DFS(start):
    visited[start] = 1          # 방문 도장 찍기
    print(start, end = ' ')     # 방문 노드 출력

    for next in range(1, V+1):  # 다음 조사 가능 노드 찾기, 방향 상관 없음
        # 인접 list에서 연결되고, 방문하지 않음 -> stack에 넣기
        if matrix[start][next] == 1 and visited[next] == 0:
            DFS(next)            # 재귀함수 호출

V, E = map(int, input().split())  # 정점, 노드의 개수
data = list(map(int, input().split()))  # 노드별 간선 정보

# 인접행렬 생성
# 빈 도화지
matrix = [[0] * (V+1) for _ in range(V+1)]
for n in range(E):
    i, j = data[2*n], data[2*n+1]
    matrix[i][j] = 1
    matrix[j][i] = 1

visited = [0] * (V + 1)         # 방문 여부_초기화되지 않도록 밖으로 이동
DFS(1)

'''
cf) 재귀함수 종료조건
현재 노드에서 방문 가능한 노드 없음

# 동작과정
1. DFS(1) 호출
2. 1번 노드(정점) 방문 표시 및 출력
3. 1번 노드의 인접 노드 중 방문 x인 2번 노드 발견
4. DFS(2)
5. 2번 노드 방문 표시 및 출력
6. 2번 노드의 인접 노드 중 방문 x인 4번 노드 발견
7. DFS(4)
8. ...
9. 마지막 노드에서 더 이상 방문할 인접 노드가 없음
10. 이전 호출로 돌아가며 남은 인접 노드 확인
11. 모든 노드 방문 완료 시 전체 DFS 가 종료
'''