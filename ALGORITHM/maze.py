# # 미로 찾기_재귀함수를 이용한 백트래킹

# def dfs2(i, j, N):
#     visited[i][j] = 1
#     if maze[i][j] == 3:
#         return 1
#     else:
#         for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
#             ni, nj = i+di, j+dj
            

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

