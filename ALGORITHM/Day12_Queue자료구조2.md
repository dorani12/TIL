### 알고리즘, 자료구조_Queue 큐
알고리즘 12일차  
BFS  
***
### BFS 너비 우선 탐색
BFS: breadth 너비 우선 탐색 || DFS: 깊이 depth first search 
노드 = 정점, 엣지 =  간선  
- 정점의 인접 정점 차례대로 방문

- 방문 했던 정점의 인접 정점을 차례로 방문하는 너비 우선 탐색 반복  
  = 선입선출 구조의 큐 사용  
  한 정점에서의 인접 정점을 Queue에 저장 후 pop(0)하면서 이동,  
  이동을 하면서 인접 정점 저장 & 이동 반복

*기술 면접에서 설명할 수 있을 정도로 개념을 설명할 줄 알아야함!*

---
- 예제: BFS   
  ```python
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
  ```
- 예제: 인접 list, 행렬 구하기
  ```python
  # 2. 인접행렬 구하고, 이동
  # 라이브 강의 진행 코드 (인접 리스트)
  '''input.txt
  7 8 
  1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 
  ******
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
  ```
- 예제 : visited_arr 활용 예제
  ```python
    """
  1. BFS(너비 우선 탐색) 개념:
    - BFS는 그래프나 트리를 탐색하는 알고리즘
    - 시작 노드에서 가까운 노드부터 차례대로 탐색
    - 같은 레벨의 모든 노드를 탐색한 후 다음 레벨로 넘어감

  2. 큐(Queue) 사용:
    - BFS는 큐 자료구조를 사용하여 구현
    - 큐는 선입선출(FIFO) 방식으로 동작
    - 탐색할 노드를 큐에 넣고, 순서대로 꺼내며 탐색

  3. 방문 체크:
    - 이미 방문한 노드를 다시 방문하지 않도록 방문 여부를 체크
    - `visited` 리스트를 사용하여 각 노드의 방문 상태를 관리

  4. 인접 노드 탐색:
    - 현재 노드와 연결된 모든 인접 노드를 확인
    - 방문하지 않은 인접 노드를 큐에 추가

  5. 그래프 표현:
    - 이 코드에서는 인접 행렬을 사용하여 그래프를 표현
    - `G[i][j] = 1`은 노드 i와 j가 연결되어 있음을 의미

  6. 탐색 순서:
    - 시작 노드부터 가까운 순서대로 노드를 탐색
    - 결과적으로 시작 노드로부터의 거리 순으로 노드를 방문

  7. 구현 과정:
    - 시작 노드를 큐에 넣고 방문 표시를 
    - 큐가 빌 때까지 다음 과정을 반복:
      a) 큐에서 노드를 하나 꺼낸다.
      b) 꺼낸 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 넣고 방문 표시를 한다.
  """
  '''
  input.txt
  7 8 
  1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 
  ################################
  output
  1 2 3 4 5 7 6
  '''
  def BFS(start):
      queue = [start]  # 탐색할 노드를 저장하는 큐
      print(start, end=' ')  # 시작 노드 출력
      visited[start] = 1  # 시작 노드 방문 표시

      while queue:  # 큐가 비어있지 않은 동안 반복
          current = queue.pop(0)  # 큐에서 노드를 하나 꺼냄
          for next_node in range(1, V + 1):  # 모든 노드에 대해
              # 현재 노드와 연결되어 있고, 아직 방문하지 않은 노드라면
              if G[current][next_node] == 1 and visited[next_node] == 0:
                  queue.append(next_node)  # 큐에 추가
                  visited[next_node] = 1  # 방문 표시
                  print(next_node, end=' ')  # 노드 출력


  # 노드 수(V)와 간선 수(E) 입력
  V, E = map(int, input().split())

  # 간선 정보 입력
  edge_info = list(map(int, input().split()))

  # 그래프 초기화 (인접 행렬)
  G = [[0] * (V + 1) for _ in range(V + 1)]

  # 방문 여부를 체크할 리스트 초기화
  visited = [0 for _ in range(V + 1)]

  # 간선 정보를 바탕으로 그래프(인접 행렬) 구성
  for i in range(0, len(edge_info), 2):
      n1, n2 = edge_info[i], edge_info[i + 1]
      G[n1][n2] = G[n2][n1] = 1  # 무방향 그래프이므로 양방향 연결

  # 그래프 확인
  # pprint(G)

  # BFS 실행 (시작 노드: 1)
  BFS(1)
  ```
***