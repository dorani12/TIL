### 알고리즘, 자료구조_Stack 스택
알고리즘 8일차  
memoization, DP, DFS  
***
### Memoization
이전 계산 값을 메모리에 저장  
=> 매번 다시 계산하지 않아서 실행속도가 빠르도록 함  

시간복잡도 O(n)으로 감소  
*기존 피보나치수열 연산의 시간복잡도 O(n**2)*  
- 예제
  ```python
  # memo를 위한 배열 할당, 모두 0으로 초기화
  # memo[0]을 0으로, memo[1]은 1로 초기화

  def fibo1(n):
    global memo
    if n >= 2 and memo[n] == 0:
      memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

  def fibo(n):  # 기존의 방식
    if n < 2:
      return n
    else:
      return fibo(n-1) + fibo(n-2)

  n = 900
  memo = [0] * (n+1)
  memo[0] = 0
  memo[1] = 1
  print(fibo1(n))
  print(fibo(n))
  ```
---
### DP 동적 계획
dynamic programming: 최적화 문제 해결 알고리즘  
입력 크기가 작은 부분문제 해결 후, 그 해를 이용해 큰 크기의 부분문제 해결   
 
- 예제 (피보나치 수열) f[0], f[1] 부터 구한 후 그 값을 이용해 그 이후의 값 연산  
  ```python
  def fibo2(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
      f[i] = f[i-1] + f[i-2]

    return f[n]
  ```
---
### DFS 깊이 우선 탐색
depth first search || BFS: breadth 너비 우선 탐색  
노드 = 정점, 엣지 =  간선  
- 정점의 갈 수 있는 곳까지 깊이 탐색   
-> 더이상 못갈 경우, 마지막에 만났던 갈림길로 복귀  
-> 또 갈 수 있는 곳까지 깊게 탐색(화살표 부분 반복)   

- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색 반복  
  = 후입선출 구조의 스택 사용  
  갈림길의 정점을 stack에 저장  

*기술 면접에서 설명할 수 있을 정도로 개념을 설명할 줄 알아야함!*

---

- 예제: DFS   
  ```python
  # N = 정점의 개수
  def DFS(v):
    visited = [False] * N # visited stack 모두 false로 초기화
    stack = []  # 현위치, 방문 안 끝난 stack 초기화
    # 시작점 v 방문
    visited[v] = True
    while True: 
      if visited[w] == 0:  # v의 인접 정점 중 방문 안한 정점 w가 있는 경우
        stack.append(v) # push(v)
        v = w
        visited[w] = True
        break
      else:  # 더이상 방문할 곳이 없음
        if len(stack[]) != 0:  # stack이 비어있지 않음
          v = stack.pop()
        else:
          break
  ```
- 예제: 인접 list, 행렬 구하기
  ```python
  # 정점의 개수와 정점들간으 관계 주어졌을 때
  # DFS로 탐색하기 & 방문 순서
  ''' 
  input data 
  1  # testcase
  7 8  # 정점의 개수 7, 정점 쌍의 개수 8
  1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
  '''
  def DFS(s, V):            # 시작 정점 s, 정점개수 V
    visited = [0]*(V+1)     # 방문한 정점을 표시할 리스트
    stack = []              # 스택 생성 (현 위치, 방문 안 끝난 정점)
    visited[s] = 1          # 시작 정점 방문 표시
    v = s
    while True:
      for w in adjl[v]:     # v에 인접하고, 방문 안한 w가 있으면..
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
  ```
- 예제: DFS 모든 과정
  ```python
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
  ```
  - 예제: 재귀함수
  ```python
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
  ```
***