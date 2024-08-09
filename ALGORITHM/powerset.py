# 부분집합 구하기
# 백트래킹 활용

def construct_candidates(arr, k, n, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(arr, k):
    for i in range(k):
        if arr[i]:
            print(num[i], end = ' ')
    print()

def backtrack(arr, k, n):  # 주어진 배열 arr, 결정할 원소 k, 원소 개수 n
    c = [0] * MAXCANDIDATES 

    if k == n:
        process_solution(arr, k)  # 완성인 경우 -> 원하는 작업 실행
    else:
        ncandidates = construct_candidates(arr, k, n, c)
        for i in range(ncandidates):
            arr[k] = c[i]
            backtrack(arr, k+1, n)

MAXCANDIDATES = 2
NMAX = 4
arr= [0] * NMAX
num = [1, 2, 3, 4]
backtrack(arr, 0, 4)
'''
# 부분집합 출력
1 2 3 4 
1 2 3 
1 2 4
1 2
1 3 4
1 3
1 4
1
2 3 4
2 3
2 4
2
3 4
3
4
    (공집합)
'''


################################################################
# 방법 3 with. 부분집합의 합
def f(i, K):    # bit[i]를 결정하는 함수
    if i == K:  # 모든 원소에 대해 결정됨 => 완성
        s = 0
        for j in range(K):
            if bit[j]:      # bit[j]가 0이 아니면
                print(a[j], end=' ')
                s += a[j]   # 부분집합의 합을 구하는 변수 s
        print(' : ', s)
    else:
        # bit[i] = 1
        # f(i+1, k)
        # bit[i] = 0
        # f(i+1, k)
        for j in [1, 0]:
            bit[i] = j
            f(i+1, K)

N = 3
a = [1, 2, 3]
bit = [0] * N
f(0, 3)
################################################################
# 방법 4 가지치기 with. 부분집합의 합

def f(i, k, s, t):
    global cnt
    if i == k:  # 모든 원소 고려
        if s > t:
            print(bit)
            cnt += 1
        elif s == t:    # 남은 원소를 고려할 필요 없음
            cnt += 1    # 경우의 수 추가
            return
        else:
            bit[i] = 1
            f(i + 1, k, s + A[i], t)    # A[i] 포함
            bit[i] = 0
            f(i + 1, k, s , t)    # A[i] 미포함

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # [i for i in range(1, N+1)]
N = 10

cnt = 0
f()