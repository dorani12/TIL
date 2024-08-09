### 알고리즘, 자료구조_Stack 스택
알고리즘 10일차  
백트래킹(부분집합, 순열)  
***
### 백트래킹   
해를 찾는 도중 '막힘' -> 되돌아가서 다시 해 찾기  
- 최적화(optimization) 문제, 결정(decision) 문제 해결 가능
- 부분집합 구하기, 순열, 가지치기
---
### 부분집합 popwerset
공집합~자기자신을 포함한 모든 부분집합: powerset, 2**n개  

- 예제 : 원소별로 반복문을 순회, 해당 원소가 포함되는지 아닌지 기록  
  ```python
  # 방법 1: for문의 반복
  bit = [0, 0, 0, 0]
  for i in range(2):
    bit[0] = i                      # 0번째 원소 
    for j in range(2):
      bit[1] = j                    # 1번째 원소
        for k in range(2):
          bit[2] = k                # 2번째 원소
          for l in range(2):
            bit[3] = l              # 3번째 원소
            print(bit)              # 생성된 부분집합 출력

  # 방법 2: 백트래킹 활용
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
  ```
---
#### 가지치기 in 부분집합의 합
부분집합의 합 구하기: 이전의 원소들의 합이 이미 초과 => 다른 원소의 유무 생각할 필요 없음
- 원소별로 포함 여부를 판단  
  1. 해당 원소까지의 합이 찾는 값 => end(더 이상 원소 추가 필요 x)
  2. 모든 원소에 대한 고려가 끝남 => 답이 없음
  3. 이미 합이 더 큼 => 더 이상 고려 x
  4. 아직 합이 더 작음 => 아직 남은 원소에 대해 추가 탐색, 다른 원소 고려

---
### 순열
가능한 모든 경우에서 숫자들을 순서대로 배열  
- 예제 : {1,2,3} 모든 순열 생성
  ```python
  # 방법 1: for문의 반복
  for i1 in range(1, 4):
    for i2 in range(1, 4):
      if i2 != i1:
        for i3 in range(1, 4):
          if i3 != i1 and i3 != i2:   # 앞의 원소가 나오지 않은 경우
            print(i1, i2, i3)

  # 방법 2: 백트래킹 활용
  def construct_candidates(a, k, n, c):
      in_perm = [False] * (NMAX + 1)

      for i in range(k):
          in_perm[a[i]] = True

      ncandidates = 0
      for i in range(1, NMAX + 1):
          if in_perm[i] == False:
              c[ncandidates] = i
              ncandidates += 1
      return ncandidates

  def backtrack(a, k, n):
      c = [0]*MAXCANDIDATES

      if k == n:
          for i in range(0,k):
              print(a[i], end=' ')
          print()
      else:
          ncandidates = construct_candidates(a, k, n, c)
          for i in range(ncandidates):
              a[k] = c[i]
              backtrack(a, k+1, n)

  MAXCANDIDATES = 3
  NMAX = 3
  a = [0]*NMAX
  backtrack(a, 0, 3)
  ```
***