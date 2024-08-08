# 미로 찾기_재귀함수를 이용한 백트래킹

def dfs2(i, j, N):
    visited[i][j] = 1
    if maze[i][j] == 3:
        return 1
    else:
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            