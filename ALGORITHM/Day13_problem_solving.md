### 알고리즘
알고리즘 13일차  
SWEA 문제풀이  
***
- 6485: 삼성시의 버스노선   
  ```python
  '''
  버스 정류장 1에서 5,000까지 번호/버스 노선은 N개, i번째 버스 노선은 번호가 Ai이상이고, Bi이하인 모든 정류장만을 다님
  P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지?
  
  [입력] 테스트 케이스의 수 T /n 하나의 정수 N ( 1 ≤ N ≤ 500 ) /n
  다음 N개의 줄의 i번째 줄에는 두 정수 Ai, Bi ( 1 ≤ Ai ≤ Bi ≤ 5,000 )
  다음 줄에는 하나의 정수 P ( 1 ≤ P ≤ 500 ) /n 다음 P개의 줄의 j번째 줄에는 하나의 정수 Cj ( 1 ≤ Cj ≤ 5,000 )
  [출력] 한 줄에 P개의 정수를 공백 하나로 구분하여 출력한다. j번째 정수는 Cj번 버스 정류장을 지나는 버스 노선의 개수여야 한다.
  '''
  T = int(input())
  for tc in range(1, T+1):
    N = int(input())        # 노선의 개수
    counts = [0] * 5001     # 5000번 정류장까지, 버스 대수 저장
    
    # N개의 노선 정보를 읽을 때마다 처리
    for _ in range(N):
      A, B = map(int, input().split())  # 버스노선 시작점 Ai => 종점 Bi
      for i in range(A, B+1):
        counts[i] += 1

    P = int(input())        # 버스 정류장의 개수
    bus_arr = [int(input()) for _ in range(P)]
    print(f'#{tc}', end=' ')
    for j in bus_arr:
      print(counts[j], end=' ')
    print()
  ```

---
- 9490: 풍선팡
  ```python
   '''
  꽃가루가 들어있는 풍선이 M개씩 N개의 줄
  어떤 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임
  NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력
  
  [입력] 첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M, 이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수
  [출력] #과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력
  '''
  dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
  T = int(input())
  for tc in range(1, T+1):
    N, M = map(int, input().split())        # 행과 열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 풍선별 꽃가루의 수
    
    max_v = 0                               # 꽃가루의 최대 합계
    for i in range(N):                      # 터트려 볼 풍선의 위치
      for j in range(M):
        cnt = arr[i][j]                     # 터트린 풍선에서 나올 꽃가루 개수
        
        # 주변 풍선의 꽃가루 수
        for k in range(4):                  # 확인할 방향
          for l in range(1, arr[i][j]+1):   # 주변 방향으로 추가로 터지는 풍선과의 거리
            nx = i + dx[k]*l
            ny = j + dy[k]*j
            if 0 <= nx < N and 0 <= ny < M:
              cnt += arr[nx][ny]            # 주변의 풍선에서 나오는 꽃가루 추가
        if max_v < cnt:                     # for k에서 모든 꽃가루가 더해짐
          max_v = cnt
    print(f'#{tc}', max_v)
  ```
---
- 4615: 오셀로 게임
  ```python
   '''
  오셀로: 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임
  자신이 놓을 돌과 자신의 돌 사이(가로,세로,대각선)에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고, 그 때의 상대편의 돌은 자신의 돌
  만약 돌을 놓을 곳이 없다면 상대편 플레이어가 다시 돌을 놓는다.
  보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고 그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리
  
  [입력] 각 테스트 케이스의 첫 번째 줄에는 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.
  그 다음 M줄에는 돌을 놓을 위치와 돌의 색이 주어진다. 돌의 색이 1이면 흑돌, 2이면 백돌이다. 만약 3 2 1이 입력된다면 (3, 2) 위치에 흑돌을 놓음
  [출력] 각 테스트 케이스마다 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력

  '''
  def play_game(i, j, bw, N):
    board[i][j] = bw                    # 지정된 위치에, 돌 놓기
    for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:  # 대각선을 포함한 상하좌우
      ni, nj = i + di, j + dj
      tmp = []                          # 뒤집을 돌의 인덱스 저장
      while 0 <= ni < N and 0<= nj < N and board[ni][nj] == op[bw]:   # 범위내에 존재, 반대 색 돌인경우
        tmp.append((ni, nj))            # 뒤집을 돌 저장
        ni, nj = ni + di, nj + dj       # 현재 방향으로 계속 이동
      if  0 <= ni < N and 0<= nj < N and board[ni][nj] == bw:         # 중단의 이유가 같은 색 만남
        for p, q in tmp:
          board[p][q] = bw              # 게임 규칙대로 색 뒤집기

  
  B, W = 1, 2                           # 흑돌 1, 백돌 2
  op = [2, 1]                           # 반대 색 돌 정보
  T = int(input())
  for tc in range(1, T+1):
    N, M = map(int, input().split())    # 보드 한 변의 길이 N, 돌을 놓는 횟수 M
    play = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)] # N * N 보드 준비, 0 -> N-1 인덱스 사용
    
    # 중심부에 돌 배치
    board[N//2 - 1][N//2 - 1] = W
    board[N//2 - 1][N//2] = B
    board[N//2][N//2 - 1] = B
    board[N//2][N//2] = W
    
    # 돌 놓기
    for col, row, bw in play:
      play_game(row-1, col-1, bw, N)        # 게임 진행

    bl_cnt = wh_cnt = 0
    for i in range(N):
      for j in range(N):
        if board[i][j] == B:
          bl_cnt += 1
        else:
          wh_cnt += 1

    print(f'#{tc}', bl_cnt, wh_cnt)

  ```
---
- 11315: 오목판정
  ```python
   '''
  N X N 크기의 판이 있다. 판의 각 칸에는 돌이 있거나 없을 수 있다. 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정
  
  [입력] 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(5 ≤ N ≤ 20)
  다음 N개의 줄의 각 줄에는 길이 N인 문자열| 각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미
  [출력] 각 테스트 케이스 마다 돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력
  '''
  di, dj = [0, 1, 1, 1], [1, 1, 0, -1]    # 반대방향에서 체크가능하므로 절반만 확인
  def play_game(N):
    for i in range(N):
      for j in range(N):
        for k in range(4):
          cnt = 0
          ni, nj = i, j     # 돌인지 확인할 위치
          while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
            cnt += 1
            if cnt == 5:
              return 'YES'
            ni += di[k]
            nj += dj[k]
    return 'NO'             # 모든 자리 i, j에서 5개 연속을 찾는걸 실패
  
  T = int(input())
  for tc in range(1, T+1):
    N = int(input())    # 오목판의 크기
    arr = [input() for _ in range(N)]
    ans = play_game(N)
    
    print(f'#{tc}', ans)
  ```
***