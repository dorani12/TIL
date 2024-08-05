### 알고리즘, 문자열 
알고리즘 6일차

---
## 패턴 매칭
### 1. 고지식한 알고리즘 Brute Force  
- 처음부터 끝까지 차례대로 순회하며 모든 문자 비교  
-> 시간 복잡도 O(MN)

- 예제
  ```python
  text = 'TTTTTABC'  # 전체 패턴, target 패턴을 찾을 대상
  pattern = 'TTA'   # 찾으려는 패턴 
  N = len(text)  # 전체 패턴의 길이
  M = len(pattern)  # 찾으려는 패턴의 길이
  cnt = 0
  
  # 방법 1_찾은 패턴의 시작 idx 반환
  def BruteForce(p,t):
    i = 0  # text의 인덱스
    j = 0  # pattern의 인덱스
    while j < M and i < N:  # 검색하고자 하는 인덱스가 범위 벗어나지 못하도록!
      
      # 틀린 곳을 발견
      if t[i] != p[j]:
        i = i - j  # 지금 위치 - j만큼 -> 틀린 곳부터~ 맞는줄알고 넘어갔던 부분 다시 검색
        j = -1  # idx 초기화(아래에서 +1해주므로 0이 아니라 -1로 초기화 함)

      # 비교한 idx와 일치하는 경우
      i = i + 1  # 한 문자가 일치하는 경우, 다음 문자도 일치하는지 검색하기
      j = j + 1
    
    # 검색 종료 후 결과 반환
    if j == M :  # 패턴의 맨 뒤까지 검색했을 때 
      return i - M  # 검색 성공_찾고자 하는 패턴이 위치하는 시작 idx 반환
    else: 
      return -1  # 검색 실패

  # 방법 2_심플 버전
  def BruteForce2(p,t):
    # len(text) - len(pattern) + 1 : 패턴의 길이 만큼 순회를 할건데 idx 에러 안나도록
    for idx in range(N-M+1):  
      for j in range(M):  # 패턴의 길이만큼 순회
        # 단어 별로 탐색하다가 다른 경우 발생
        if t[idx+j] != p[j]:
          break  #for j, 다음 글자부터 비교 시작
        # 순서대로 같은 경우
      else:     # for j가 중단 없이 반복되면 실행됨
        cnt += 1  # 패턴 개수 1증가
        return idx
    else:  # for-else문은 반복의 처음부터 끝까지 아무런 문제없이 실행되는 경우에 실행할 문장
      return -1

    print(cnt)  # 패턴이 일치한 횟수
  ```
---
### 2. KMP 알고리즘  
- 매칭에 실패하는 경우, 돌아갈 위치 계산 *by. 틀린 위치 이전 일치한 개수*  
-> 시간 복잡도 O(M + N)

- 예제 *업데이트 필요*
  ```python


  ```
---
### 3. 보이어-무어 알고리즘  
- 끝에서 부터 시작_jump할 수 있는 부분이 더 많음  
-> 시간 복잡도: 일반적으로 O(N) 보다 작음, 최악의 경우 O(M + N)  

***
### 문자열 암호화  
cf) XOR(exclusive-or) 둘이 달라야지만 1  
시저암호, 단일key 암호화.... 등등

### 문자열 압축
- run-length encoding: BMP 파일 포맷의 압축  
- 허프만 코딩 알고리즘: 자주 사용하는 형태의 코드 길이는 짧게, 아닌 경우 길게 설정