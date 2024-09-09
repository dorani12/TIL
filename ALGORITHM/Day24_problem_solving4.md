### 알고리즘
알고리즘 24일차  
SWEA 문제풀이4_A형 대비  
***
- 20551 : 증가하는 사탕 수열 
  ```python
  '''
  세 개의 상자 | 첫 번째 상자에는 사탕 A개, 두 번째 상자에는 사탕 B개, 세 번째 상자에는 사탕 C개 | 사탕의 개수가 순증가
  모든 상자에 1개 이상의 사탕
  [출력] 세현이가 조건을 만족시킬 수 있는지 판단하고, 만족시킬 수 있다면 최소 몇 개의 사탕을 먹어야 하는지 구하는 프로그램
  #############################################################

  '''
  # C와 비교하여 1이 작도록 B 먹어치우기, 다음 A
  T = int(input())

  for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    if B < 2 or C < 3:        # 예외 경우
      print(f'#{tc} -1')

    eat = 0                   # 먹은 사탕의 개수
    if B >= C:
      eat += B - (C - 1)
      B = C - 1

    if A >= B:
      eat += A - (B - 1)
      A = B - 1
    print(f'#{tc}', eat)
  ```

---
- 12741 : 두 전구
  ```python
  '''
  두 개의 전구 X와 Y
  전구 X는 관찰 시작 경과 후 A초에서부터 관찰 시작 경과 후 B초까지에만 켜져 있었다. 전구 Y는 관찰 시작 경과 후 C초에서부터 관찰 시작 경과 후 D초까지에만 켜져 있었다.
  [출력] 두 전구를 관찰하던 100초 중 두 전구가 동시에 켜져 있던 시간은 몇 초?
  #############################################################
  testcase 개수가 5만개 -> input(), output()을 매우 많이 반복해서 발생하는 시간초과의 문제도 해결해야함 
  '''
  T = int(input())
  result_list = list()
  for tc in range(T):
    A, B, C, D = map(int, input().split())

    # 나중에 켜진 전구의 시간이 시작점
    start = max(A, C)
    # 먼저 꺼진 전구의 시간이 끝점
    end = min(B, D)

    result = end - start
    if result < 0:
      result = 0

    result_list.append(result)

  for index, result in enumerate(result_list):  
    print(f'{index+1}', result[index])
  ```
---
- 5656 : 벽돌깨기
  ```python
  '''
  구슬은 N번만 쏠 수 있고, 벽돌들의 정보는 아래와 같이 W x H 배열
  ① 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있다.
  ② 벽돌은 숫자 1 ~ 9 로 표현되며, 구슬이 명중한 벽돌은 상하좌우로 ( 벽돌에 적힌 숫자 - 1 ) 칸 만큼 같이 제거된다.
  ③ 제거되는 범위 내에 있는 벽돌은 동시에 제거
  ④ 빈 공간이 있을 경우 벽돌은 밑으로 떨어지게 된다.
  [입력] 첫 번째 줄에는 N, W, H | 다음 H 줄에 걸쳐 벽돌들의 정보가 1 줄에 W 개씩 
  [출력] 남은 벽돌의 개수를 구하라!
  #############################################################
  완전탐색_모든 열을 돌며 어디를 터뜨려야 최대로 터지는지 확인, 델타 탐색, 재귀_구슬을 N번 떨어뜨려야함
  현재 남은 벽돌의 수를 확인, 0개면 함수 종료
  '''
  dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
  def shoot(level, remains, now_arr):
    global min_blocks

    # 기저조건_구슬 모두 발사 || 남은 벽돌이 0
    if level == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return                                # 탈출 조건
    
    for col in arr:
      # 한 열씩 구슬을 떨어뜨리기_arr를 복사후 쏘고난뒤 결과 공유 포함 재귀
      copy_arr = [row[:] for row in now_arr]
      # 1. 맨 위에 벽돌 찾기
      row = -1                                # 벽돌이 없는 경우
      for r in range(H):
        if copy_arr[r][col]:                  # 가장 위에 있는 벽돌을 만나면
          row = r
          break
      # 2. 연쇄적으로 벽돌 깨기                 
      li = [(row, col, copy_arr[row][col])]   # 다음에 깨질 벽돌의 정보(위치, power) 저장해야 연쇄적으로 터뜨려짐
      now_remains = remains -1                # 현재 남은 벽돌 -1
      copy_arr[row][col] = 0

      while li:
        r, c, p = li.pop()
        for k in range(1, p)                  # 벽돌에 적힌 수 = power만큼 주변을 깨뜨림
          for i in range(4):                  # 상하좌우
            nr, nc = r + (dy[i]*k), c + (dx[i]*k)

            if nr < 0 or nr >= H or nc < 0 or nc >= W: continue
            if copy_arr[nr][nc] == 0: continue # 범위 벗어나거나, 벽돌이 없는 경우

            li.append((nr, nc, copy_arr[nr][nc]))
            now_remains -= 1                  # 현재 남은 벽돌 -1
            copy_arr[nr][nc] = 0
      # 3. 중력 적용
      for c in range(W):
        idx = H - 1                           # 벽돌이 있으면 무조건 swap
        for r in range(H-1, -1, -1):
          if copy_arr[r][c]:
            copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
            idx -= 1
    shoot(level + 1, now_remains, copy_arr)

  T = int(input())
  for tc in range(1, T+1):
      N, W, H = map(int, input().split())
      arr = [list(map(int, input().split())) for _ in range(H)]
      min_blocks, blocks = 1e9, 0

      for row in arr:
        for el in row:
          if el:
            blocks += 1
      
      shoot(1, blocks, arr)                   # 함수 호출

      print(f'#{tc}', min_blocks)
  ```
---
- 4008 : 숫자 만들기
  ```python
  '''
  N개의 숫자가 적혀 있는 게임 판이 있고, +, -, x, / 의 연산자 카드를 숫자 사이에 끼워 넣기
  수식을 계산할 때 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
  수식을 완성할 때 각 연산자 카드를 모두 사용해야 한다.
  [입력] 숫자의 개수 N | '+', '-', '*', '/' 순서대로 연산자 카드의 개수 | 수식에 들어가는 N 개의 숫자
  [출력] 그 결과가 최대가 되는 수식과 최소가 되는 수식을 찾고, 두 값의 차이를 출력
  #############################################################
  '''
  def cal(oper1, oper2, oper_idx):
    if oper_idx == 0:
      return oper1 + oper2

    if oper_idx == 1:
      return oper1 - oper2

    if oper_idx == 2:
      return oper1 * oper2

    if oper_idx == 3:               # 음수인 경우도 고려 필요
      if oper1 < 0:
        return -(abs(oper1) // oper2)
      return oper1 // oper2

  def dfs(level, total):        # 1. 첫번째 숫자부터 마지막 연산자를 사용할 때까지 | 연산 결과 값 전달
    global max_result, min_result

    if level == N:
      min_result = min(min_result, total)
      max_result = max(max_result, total)

    for i in range(4):
      if opers[i] == 0: continue    # 연산자 별로 사용횟수 남아있으면 연산, 결과값 전달
      
      opers[i] -= 1
      dfs(level+1, cal(total, numbers[level], i))
      opers[i] += 1

  T = int(input())
  for tc in range(1, T+1):
    N = int(input())
    opers = list(map(int, input().split()))          
    numbers = list(map(int, input().split()))
    max_result, min_result = 1e9, -1e9
    
    dfs(1, 0)
    
    print(f'#{tc}', max_result - min_result)
  ```
***