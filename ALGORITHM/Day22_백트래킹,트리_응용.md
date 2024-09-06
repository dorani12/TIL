### 알고리즘, 자료구조_분할 정복
알고리즘 22일차  
백트래킹, 그래프_트리 응용
***
## 백트래킹
여러 옵션 중 한개 선택 -> 정답을 찾을 수 있는지 계속 탐색해나가기  
실패하면 해당 선택지 x(가지치기, prunning), 최근의 분기점에서 다른 선택지 선택   

1.  상태 공간 트리의 깊이 우선 검색 실시
2.  각 노드가 유망한지 점검
3.  해당 노드가 유망하지 않으면, 부모노드로 돌아가 다시 검색

<-> 깊이 우선 탐색: 모든 경로 추적, 경우의 수 너무 많음   

### N-Queen
체스에서 퀸 -> 상하좌우, 대각선까지 8가지 방향으로 이동 가능  
퀸들을 배치할 때, 서로 위협하지 않도록 n개의 퀸들을 장기판에 배치하기  

```python
def check(row, col):
    # 현재 열에 퀸이 있는지 확인
    for i in range(row):
        if visited[i][col] == 1:
            return False

    # 왼쪽 대각선 확인
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # 오른쪽 대각선 확인
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if visited[i][j] == 1:
            return False
        i -= 1
        j += 1

    # # 왼쪽 대각선 확인
    # for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
    #     if visited[i][j] == 1:
    #         return False
    #
    # # 오른쪽 대각선 확인
    # for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
    #     if visited[i][j] == 1:
    #         return False

    return True


def dfs(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        if check(row, col):
            visited[row][col] = 1
            dfs(row + 1)
            visited[row][col] = 0  # Backtracking


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    dfs(0)
    print(f'#{tc} {cnt}')
```

### 부분집합
1~10까지의 수를 원소로 가지는 집합의 powerset 중 원소의 합이 10인 부분집합 모두 출력
```python
# 1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
# 단, 순서에 따른 중복을 제거하세요
arr = [i for i in range(1, 11)]
visited = []


# 버전1
def dfs(level, sum, idx):
    # 가지치기 : 합이 10이면 종료
    if sum == 10:
        print(*visited)
        return

    # 가지치기 : 10이상의 숫자면 볼 필요 없음
    if sum > 10:
        return

    for i in range(idx, len(arr)):
        # 가지치기 : 이미 사용한 숫자라면 생략
        if arr[i] in visited:
            continue

        visited.append(arr[i])
        dfs(level + 1, sum + arr[i], i)
        visited.pop()


# 버전2
# 트리 구조처럼 사용하면 훨씬 쉽고 빠르다
def dfs2(level, sum):
    if sum > 10:
        return

    if sum == 10:
        print(*visited)
        return

    # 모두 선택하지 않으면 합이 10이 넘지 못하므로
    # 기저조건 추가
    if level == len(arr):
        return

    # 선택하는 경우
    visited.append(arr[level])
    dfs2(level + 1, sum + arr[level])
    visited.pop()

    # 현재 숫자를 선택하지 않는 경우
    dfs2(level + 1, sum)


# dfs(0, 0, 0)
dfs2(0, 0)
```
***
## 트리
- 사이클이 없는, 무향 연결 그래프  
- 두 노드 사이에 유일한 경로가 존재
- 계층 구조: 각 노드는 최대 하나의 부모노드만 가진다
- 각 노드는 자식 노드가 없거나 하나 이상 존재 가능
- 1:n 관계
- 부모 노드가 없다 -> 루트 노드

### 트리 용어 정리
- 노드(node) = 정점(vertax)
- 간선(edge)
- 차수 degree
  - 노드의 차수 = 노드에 연결된 자식 노드의 수
  - 트리의 차수 = 트리에 있는 노드의 차수 중에 가장 큰 값
  - 단말 노드(리프 노드) = 차수가 0인 노드, 자식 노드가 없는 노드
- 높이: 루트에서 노드에 이르는 간선의 수 | 최댓값이 트리의 높이

[트리 종류, 탐색 등 복습]  
트리는 리스트로 생각하면 삭제가 어려움 -> 리스트로 구현 금지!, 연결리스트, 딕셔너리 형태로 구현해보기  
힙
```python
from heapq import heappush, heappop

arr = [20, 15, 19, 4, 13, 11]

# 최소힙
min_heap = []

for el in arr:
    heappush(min_heap, el)

print(min_heap)  # [4, 13, 11, 20, 15, 19] 출력

while len(min_heap) > 0:
    print(heappop(min_heap), end=' ')

print()

# 최대힙
max_heap = []
for el in arr:
    heappush(max_heap, -el)

print(max_heap)  # [-20, -15, -19, -4, -13, -11] 출력

while len(max_heap) > 0:
    print(-heappop(max_heap), end=' ')
```
***
