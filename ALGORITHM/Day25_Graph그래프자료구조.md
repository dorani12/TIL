### 알고리즘, 자료구조_Graph
알고리즘 25일차  
Graph, BFS, DFS, 서로소 집합
***
## 그래프
### 그래프 종류와 용어
- 무향 그래프 (방향 X)
- 유향 그래프 (지하철, 도로, 팔로우 같이 방향 O)
- 가중치 그래프 (무향, 유향 둘다 가능)
- 사이클이 없는 방향 그래프
---
- 완전 그래프 vs 부분 그래프: 정점들에 대해 가능한 모든 간선 O, X
- 인접 : 간선으로 연결된 정점들 -> 인접해있다
- 경로 : 간선을 순서대로 나열
- 단순경로 vs 사이클 : 한 정점을 한 번만 지나는 경우 vs 시작한 정점에서 끝나는 경로
---
### 그래프 표현
- 인접 행렬 :  2차원 배열에 간선 정보 저장_연결되지 않은 정보도 파악 가능
- 인접 리스트 : 해당 정점으로 나가는 간선의 정보 저장
- 연결 리스트
***

## DFS
문제: A로부터 시작 한명의 친구에게 소식 전달 가능, 최대 몇명의 친구가 소식을 전달 받을지?  
    :or 동시에 전달 가능할 때, 가장 늦게 받는 사람은 누구 일지?  

구현 by.  
- 재귀 
- 반복
```python
import sys
sys.stdin = open("graph.txt", "r")
###
def dfs(node):                      # 1번부터 갈 수 있는 모든 정점을 방문하면 종료
    print(node, end=' ')            # 현재 노드 출력

    # 갈 수 있는 = 연결된 노드들을 탐색
    for next_node in graph[node]:   # in graph[node][::-1]으로 하면 큰 수부터 탐색
        if visited[next_node]:      # 이미 방문한 경우 통과
            continue

        visited[next_node] = 1      # 방문 여부 체크 후, 다음 정점으로 재귀
        dfs(next_node)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 인접리스트로 인접정점 정보 저장, 0번 인덱스 제외
visited = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)              # 양방향 그래프이므로, 시작점과 끝점을 바꿔가면서 저장
    graph[e].append(s)

visited[1] = 1                      # 출발지 방문 처리, 함수 호출
dfs(1)
```
---
## BFS
인접한 모든 정점들을 차례대로 방문한 후에, 그다음 자식노드 방문   

```python
def bfs(node):
    q = [node]                      # 선입선출 구조인 Queue 처럼 활용, 다음에 처리할 데이터 후보군이 저장됨

    while q:
        now = q.pop(0)              # Queue에 저장된 값이 없을 때까지 = 갈 수 있는 곳이 없을 때까지

        print(now, end=' ')         # 현재 노드, 가장 앞의 노드 출력

        for next_node in graph[now]:# 현재 정점에서 인접한 정점들 확인
            if visited[next_node]:
                continue            # 이미 확인 한 경우는 통과

            visited[next_node] = 1
            q.append(next_node)     # queue에 다음에 방문할 노드 저장


N, M = map(int, input().split())    # bfs dfs 모두 인접리스트 만드는건 동일
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited[1] = 1
bfs(1)
```
***
## 서로소 집합 Disjoint Sets
교집합이 없는 집합, 상호배타  
연결리스트, 트리 등을 이용해 표현 가능  
대표자(representative)를 이용해 각 집합을 구분  

### 상호배타 집합연산  
- Make-set(x) : x라는 원소를 가지는 집합 생성
- Find-set(x) : x를 가지는 집합을 찾아 대표자 return
- Union(x, y) : x와 y를 포함하는 두 집합을 하나로 묶기  

```python
def make_set(n):
    p = [i for i in range(n)]   # 각 원소의 부모를 자신으로 초기화
    return p


def find(x):
    if parents[x] == x:         # x 자기자신이 x를 바라본다 => 대표자를 찾음
        return x

    return find(parents[x])


def union(x, y):
    root_x = find(x)            # x, y 집합의 대표자를 찾기
    root_y = find(y)

    if root_x == root_y:        # 이미 같은 집합이면 끝
        return

    # 다른 집합이라면 더 작은 루트노트에 합친다.
    if root_x < root_y:
        parents[y] = root_x
    else:
        parents[x] = root_y


# 예제 사용법
n = 7  # 원소의 개수
parents = make_set(n)

union(1, 3)
union(2, 3)
union(5, 6)

print(parents)                  # 대표자의 수 = 집합의 개수
print('find_set(6) = ', find(6))

target_x = 2
target_y = 3

# 원소 1과 원소 2가 같은 집합에 속해 있는지 확인
if find(target_x) == find(target_y):
    print(f"원소 {target_x}과 원소 {target_y}는 같은 집합에 속해 있습니다.")
else:
    print(f"원소 {target_x}과 원소 {target_y}는 다른 집합에 속해 있습니다.")
```

### 편향 -> 문제점 해결 by. path compression, rank
```python
def find(x):
    # 원소의 부모가 자기자신이다 == 자기가 그 그룹의 대표자
    if parents[x] == x:
        return x

    # 경로 압축 (path compression)을 통해 부모를 루트로 설정
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:  # 이미 같은 집합이면 끝
        return

    # # rank를 비교하여 더 작은 트리를 큰 트리 밑에 병합
    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    elif ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y
    else:
        # rank가 같으면 한쪽을 다른 쪽 아래로 병합하고 rank를 증가시킴
        parents[root_y] = root_x
        ranks[root_x] += 1
```

***