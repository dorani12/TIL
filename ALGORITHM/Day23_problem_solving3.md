### 알고리즘
알고리즘 23일차  
SWEA 문제풀이3_A형 대비  
***
- 1861: 정사각형 방  
  ```python
  '''
  N2개의 방이 N×N형태 | 위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.
  상하좌우에 있는 다른 방으로 이동할 수 있다. 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
  처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램

  [출력] 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지를 공백으로 구분하여 출력한다 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력
  #############################################################

  '''
  # 접근 방법1_DFS
  # 접근 방법2_1차원 배열_상하좌우 중 이동가능? -> 1로 표기, 연속된 1의 길이를 출력
  # (1~n**2까지 무조건 들어가게 되니까 해당 값에서 이동 가능한지 아닌지만 탐색하면 됨)
  T = int(input())

  for tc in range(1, T+1):
    N = int(input())                            # 방의 개수
    arr = [list(map(int, input().split()))for _ in range()]     # 방에 적힌 숫자들
    visited = [0]*(N * N + 1)                   # 다른 방으로 이동 가능한지 1로 체크

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
            
                if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                if arr[nx][ny] == arr[i][j] + 1:
                    visited[i][j] = 1           # 전체 배열을 순회하며 인접한 방의 숫자가 현재 숫자보다 1 크면 1차원 리스트에 1저장
                    break                       # 같은 숫자는 존재 x, 1을 체크했으면 다른 방향 필요 x
    cnt = max_cnt = start = 0                   
    for i in range(N*N, -1, -1):
        if visited[i]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                start = i + 1                   # 초기화 이슈 발생 -> 뒤에서부터 탐색하는게 유리
                cnt = 0
    print(f'#{tc}', {start}, {max_cnt+1})
  ```

---
- 1486: 장훈이의 높은 선반
  ```python
  '''
  탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.
  탑의 높이가 B 이상인 경우 선반 위의 물건을 사용할 수 있는데 탑의 높이가 높을수록 더 위험하므로 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑?!
  [입력] 두 정수 N, B(1 ≤ N ≤ 20, 1 ≤ B ≤ S) | 높이가 B인 선반, N명의 점원
  S는 두 번째 줄에서 주어지는 점원들 키의 합이다.
  두 번째 줄에는 N개의 정수가 공백으로 구분되어 주어지며, 각 정수는 각 점원의 키 Hi (1 ≤ Hi ≤ 10,000)

  [출력] 만들 수 있는 높이가 B 이상인 탑 중에서 탑의 높이와 B의 차이가 가장 작은 것을 출력
  #############################################################
  탈출조건의 순서에 따라서 답이 안나올 수도 있음
  '''
  # 부분집합의 합이 B인 부분집합의 원소의 개수를 구하시오
  def recur(cnt, sum_height):
    global ans
    if sum_height >= B:                                     # 기저 조건 가지치기_합이 B를 넘어서면 고려x
        ans = min(ans, sum_height)
        return

    if cnt == N:                                            # 탈출조건_모든 점원의 키 고려했는가?
        return

    recur(cnt+1, sum_height + heights[cnt])                 # cnt번 점원을 탑에 고려
    recur(cnt+1, sum_height)                                # 고려X

  T = int(input())
  for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))               # 각 점원의 키
    ans = 1e9                                               # 일단 큰 값

    recur(0, 0)
    print(f'{tc}', ans-B)
  ```
---
- 2819: 격자판의 숫자 이어 붙이기
  ```python
  '''
  4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9 사이의 숫자
  동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수 | 재방문 가능
  [입력] 4개의 줄에 걸쳐서, 각 줄마다 4개의 정수로 격자판의 정보
  [출력] 격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램
  #############################################################

  '''
  dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
  def dfs(x, y, path):
    if len(path) == 7:
        result.add(path)
        return                  # 탈출 조건
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4: continue
        dfs(nx, ny, path + arr[nx][ny])      # 경로를 추가하며 이동

  T = int(input())
  for tc in range(1, T+1):
      arr = [list(map(int, input().split())) for _ in range(4)]
      result = set()

      for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

      print(f'#{tc}', len(result))
  ```
---
- 1952 : 수영장
  ```python
  '''
  가장 적은 비용으로 수영장을 이용할 수 있는 방법
  각 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때, 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 그 비용을 정답으로 출력하는 프로그램
  [입력]  1일 이용권의 요금, 1달 이용권의 요금, 3달 이용권의 요금, 1년 이용권의 요금 \n  1월부터 12월까지의 이용 계획
  [출력] 이용 계획대로 수영장을 이용하는 경우 중 가장 적게 지출하는 비용
  #############################################################
  '''
  def dfs(month, sum_cost):
    global ans                                      # 시작점 1월, 12월이 탈출 조건
    if month > 12:
        ans = min(ans, sum_cost)
        return
    # 트리로 4가지 경우를 선택한다고 고려
    dfs(month + 1, sum_cost + (days[month]*cost[0]))# 1일권 구매, 다음 탐색은 1달로
    dfs(month + 1, sum_cost + cost[1])# 1달권 구매, 다음 탐색은 3달로
    dfs(month + 3, sum_cost + cost[2])# 3달권 구매, 다음 탐색은 1년으로
    dfs(month + 12, sum_cost + cost[3])# 1년권 구매
                                                    
  T = int(input())
  for tc in range(1, T+1):
    cost = list(map(int, input().split()))          # 1일, 1달, 3달, 1년 이용권의 이용 요금
    days = [0]+list(map(int, input().split()))
    ans = 1e9
    dfs(1, 0)
    print(f'#{tc}', ans)
  ```
***