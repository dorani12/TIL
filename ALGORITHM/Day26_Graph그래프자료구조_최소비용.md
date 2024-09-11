### 알고리즘, 자료구조_Graph
알고리즘 26일차  
최소비용 신장 트리(MST)_Prim, Kruskal 알고리즘 | 최단 경로_Dijkstra
***
## 최소비용 신장 트리 MST
- 1. 신장 트리 : 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
- 2. 두 정점 사이의 최소 비용의 경로 찾기
---
### Prim 알고리즘
[내용 추가 예정...]
```python
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

from heapq import heappush, heappop

def prim(start):
    heap = list()
    MST = [0] * (V)

    # 최소 비용 합계
    sum_weight = 0

    # 힙에서 관리해야 할 데이터
    # 가중치, 정점 정보
    heappush(heap, (0, start))

    while heap:
        weight, v = heappop(heap)
        
        # 이미 방문한 지점이면 통과
        if MST[v]:
            continue

        # 방문 처리
        MST[v] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈수 있는 노드를 보면서
        for next in range(V):
            # 갈 수 없는 지점이면 continue
            if graph[v][next] == 0:
                continue

            # 이미 방문한 지점이면 continue
            if MST[next]:
                continue

            heappush(heap, (graph[v][next], next))

    return sum_weight


V, E = map(int, input().split())
graph = [[0] * (V) for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w  # 가중치가 있는 무방향 그래프

result = prim(0)
print(f'최소 비용 = {result}')
```

## Kruskal 알고리즘


구현 by.  

```python
V, E = map(int, input().split())    # V 마지막 정점, 0~V번 정점. 개수 (V+1)개
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([u, v, w])
edge.sort(key=lambda x : x[2])
parents = [i for i in range(V)]       # 대표원소 배열


def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    # 더 작은 루트노트에 합친가
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# MST의 간선수 N = 정점 수 - 1
cnt = 0     # 선택한 edge의 수
total = 0   # MST 가중치의 합
print(edge)
for u, v, w in edge:
    print(u, v, w)
    # 다른 집합이라면
    if find_set(u) != find_set(v):
        cnt += 1
        union(u, v)
        total += w
        if cnt == V:  # MST 구성이 끝나면
            break
print(f'최소 비용 = {total}')
```
***
## 최단 경로_Dijkstra

```python
'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

import heapq

INF = int(1e9)  # 무한을 의미하는 값으로 10억

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호
start = 0
# 인접리스트 만들기
graph = [[] for i in range(n)]
# 누적거리를 저장할 테이블 - INF 로 저장
distance = [INF] * n

# 간선 정보를 입력
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])


def dijkstra(start):
    pq = []
    # 시작 노드 최단 거리는 0
    # heapq 에 리스트로 저장할 때는 맨 앞의 데이터를 기준으로 정렬된다.
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    # 우선순위 큐가 빌 때 까지 반복
    while pq:
        # 가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # 현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            # 다음 노드를 가는 데 더 많은 비용이 드는 경우
            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


# 다익스트라 알고리즘 실행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(n):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("INF", end=' ')
    else:
        print(distance[i], end=' ')
```
***