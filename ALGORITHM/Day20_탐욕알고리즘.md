### 알고리즘, 자료구조_완전 검색, 탐욕
알고리즘 20일차  
부분집합, 조합, 탐욕 알고리즘(greedy)
***
## 부분집합
집합에 포함된 원소 선택
1. 재귀 호출 이용 완전 탐색
   ```python
    arr = ['O', 'X']
    path = []
    name = ['MIN', 'CO', 'TIM']
    # path 출력 함수
    def print_name():
        print(path, end=' / ')
        print('{ ', end='')
        for i in range(3):                      # 원소의 개수
            if path[i] == 'O':
                print(name[i], end=' ')
        print('}')


    def run(lev):
        # 3개를 뽑았을 때 출력
        if lev == 3:                            # 출력할 타이밍
            print_name()
            return

        for i in range(2):                      # 후보군 3개 중
            path.append(arr[i])                 # 선택_경로 추가
            run(lev + 1)                        # 다음 lev고려
            path.pop()                          # 경로 삭제


    run(0)
   ```
2. 2진수, 비트연산 이용 방법  
    o,x 대신 0과 1을 이용하여 원소의 유무 표기
    1 << n = 부분집합의 개수(2**n개)
    ```python
    # 부분집합 구하기_바이너리, 비트 연산
    arr = ['A', 'B', 'C']
    n = len(arr)


    def get_sub(target):
        for i in range(n):
            if target & 0b1:
                print(arr[i], end='')
            target >>= 1


    for target in range(0, 1 << n):  # range(0, 8) # n개 원소, 부분집합 개수 1 << n
        print('{', end='')
        get_sub(target)
        print('}')
    ```
    응용
    ```python
    # 5명의 친구 중, 2명 이상의 친구들과 놀러가는 경우의 수?
    arr = ['A', 'B', 'C', 'D', 'E']
    n = len(arr)


    # 총 몇개의 bit가 1로 되어있는지 확인하는 함수
    def get_count(tar):
        cnt = 0
        for i in range(n):
            if tar & 0x1:           # 원소 존재하면 cnt +1
                cnt += 1
            tar >>= 1
        return cnt


    result = 0
    for tar in range(0, 1 << n):    # range(0, 8)
        if get_count(tar) >= 2:     # 원소가 2개 이상이라면,
            result += 1             # 경우의수 카운트
    print(result)
    ```
---
## 조합 combination
서로 다른 n개의 원소 중 r개를 순서 없이 고르기 : nCr  
```python
# combination 5개 중 3개의 조합 출력
arr = ['A', 'B', 'C', 'D', 'E']
path = []
n = 3


def run(lev, start):
    if lev == n:
        print(*path)                # 재귀 종료 조건, 원소들 출력
        return

    for i in range(start, 5):
        path.append(arr[i])         # 경로 추가
        run(lev + 1, i + 1)         # 재귀함수 호출 | 이미 뽑은 수, 이후의 원소들만 고려하면 됨
        path.pop()                  # 경로 삭제

run(0, 0)
```
```python
# 주사위 N개를 던져 나올 수 있는 모든 조합?
N = 3
path = []


def run(lev, start):
    if lev == N:                    # 3개가 채워짐 -> 출력
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        run(lev + 1, i)             # 중복이 가능함, 1~6이내로 순회 돌도록!
        path.pop()


run(0, 1)   
```
***
## 탐욕 Greedy
현재 기준으로 가장 좋아보이는 선택지로 결정  

#### greedy 선택 조건
1. 각 단계의 선택이 이후 선택에 영향 x
2. 각 단계의 최선의 선택 -> 전체 문제의 최선의 해

### Greedy 문제 예시 
```python
# 동전선택
coin_list = [500, 100, 50, 10]
target = 1730
cnt = 0

for coin in coin_list:
    possible_cnt = target // coin  # 사용 가능한 동전의 수로 나눔 (ex) 500원이라면 3개 가능)
    
    cnt += possible_cnt  # 동전의 수를 정답에 추가
    target -= coin * possible_cnt  # 동전 금액 만큼 빼준다.

print(cnt)

###########################################################################
# 회의실 배정
T = int(input())            # 회의 요청 건수
li = []
for _ in range(T):  
    li.append(list(map(int, input().split())))

# 1. 끝나는 시간 / 2. 빨리 시작하는 시간 순서대로 정렬되어야 한다.
li.sort(key=lambda x: (x[1], x[0])) 

cnt = 0
end = -1
for meeting in li:
    # 끝나는 시간보다 크거나 같다 == 회의가 시작할 수 있다.
    # 즉, 회의가 시작할 수 있다면
    # 1. 정답에 1 추가
    # 2. 끝나는 시간 초기화
    if meeting[0] >= end:
        cnt += 1
        end = meeting[1]

print(cnt)
###########################################################################
# 부분집합의 원소의 합이 0인 경우의 수
numbers = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
cnt = 0  # 총 몇가지인지 계산
path = []


def recur(now, total):
    global cnt
    if now == 10:
        return

    if total + numbers[now] == 0:
        print(path + [numbers[now]])
        cnt += 1

    # 현재 수를 사용하지 않는 경우
    recur(now + 1, total)

    # 현재 수를 사용하는 경우: 경로에 추가, 누적합에 계산
    path.append(numbers[now])
    recur(now + 1, total + numbers[now])
    path.pop()


recur(0, 0)
print(f'총 {cnt}가지')
###########################################################################
#fractional knapsack
n = 3
target = 30  # Knapsack KG
things = [(5, 50), (10, 60), (20, 140)]  # (Kg, Price)

# (Price / Kg) 기준으로 내림차순 sort
things.sort(key=lambda x: (x[1] / x[0]), reverse=True)
# sort 결과 = [(5, 50), (20, 140), (10, 60)]
print(things)

total = 0
for kg, price in things:
    per_price = price / kg

    # 만약 가방에 남은 용량이 얼마되지 않는다면,
    # 물건을 잘라 가방에 넣고 끝낸다.
    if target < kg:
        total += target * per_price
        break

    total += price
    target -= kg

print(int(total))
```
---
### 참고: 대표적인 문제해결 기법
1. 완전탐색 (Brute-Force) : 답이 될 수 있는 모든 경우 시도
2. Greedy : 결정시에 가장 좋아보이는 선택지로 결정
3. DP : 과거의 데이터를 이용, 현재의 데이터 만들어내기
4. 분할정복 : 큰 문제를 작은 문제로 나누어 해결
***
