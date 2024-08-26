# SWEA D2 20739 2024.08.26
# 알고리즘 문제풀이 2 : 고대 유적2

'''
사진의 해상도는 NxM, 구조물이 있는 곳은 1, 빈 땅은 0 | 교차하거나 만나는 것처럼 보이는 구조물은 서로 다른 깊이에 묻힌 것이므로 직선인 구조만 고려
구조물의 최소 크기는 1x2
[입력] 첫 줄에 사진 데이터의 개수, 다음 줄부터 사진 데이터 별로 첫 줄에 N과 M, 이후 N개의 줄에 M개씩의 데이터

[출력] 각 구역 별로 가장 긴 구조물의 길이?
#############################################################

'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0                                   # 가장 긴 구조물 길이
    
    # i행에서 가로 구조물 길이 확인
    for i in range(N):                          
        cnt = 0                                 # 구조물 길이_행별로 순회 할 때마다 초기화
        for j in range(M):
            if arr[i][j]:                       # 구조물이면
                cnt += 1                        # 길이 1m증가
                if max_v < cnt:                 # 가로 구조물의 최대 길이 찾기
                    max_v = cnt
                # max_v = max(max_v, cnt)
            else:
                cnt = 0
    
    # j열에서 세로 구조물 길이 확인
    for j in range(M):                          
        cnt = 0 
        for i in range(N):
            if arr[i][j]:                       # 구조물인 경우
                cnt += 1
                if max_v < cnt:                 # 가로 구조물의 최대 길이 찾기
                    max_v = cnt
            else:
                cnt = 0
    
    if max_v == 1:                              # 노이즈인 경우
        max_v = 0
    print(f'#{tc} {max_v}')