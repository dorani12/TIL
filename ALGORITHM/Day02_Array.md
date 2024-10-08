## 알고리즘, 배열  
알고리즘 2일차  
**손으로 적고 그리며 로직 구조, 슈도 함수를 완성시키고 난 뒤에 코드를 적기 시작!**  

---
## Sort 정렬  
:특정 기준으로 오름차순(ascendig), 내림차순(descending)으로 정렬  
- **버블 정렬**
  - 인접한 두 개의 원소를 비교하며 자리를 계속 교환
  - 한 단계 끝 -> 가장 큰 원소가 마지막 자리로 정렬(오름차순 정렬 시)
  - 시간 복잡도: O(n**2)
  - 코딩 간단 but, 시간복잡도가 크다  
  예제
    ```python
    def BubbleSort(arr, N) # 정렬할 배열과 배열의 크기
        for i in range(N-1, 0, -1): #단계가 지날 때마다, 가장 끝부터 정렬됨
            for j in range(0, i): #맨 왼쪽 부터, 인접한 원소와의 크기 비교_-1인건 왼쪽, 오른쪽 비교
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j] #인접한 원소 간 위치 변경_python은 tmp불필요
    ```
## - **카운팅 정렬**
  - 각 항목이 몇 개씩 있는지 세고 항목들의 순서를 결정 -> 선형 시간에 정렬
  - only. 정수로 표현되는 자료형에 적용
  - 시간 복잡도: O(n+k)_(n은 리스트의 길이, k는 정수의 최댓값)
  - 시간 복잡도가 낮지만, n이 비교적 작을 때, 정수 자료형만 가능  
  예제
    ```python
    def CountingSort(Data, Temp, k) # 정렬할 배열 data와 배열의 크기
      # 갯수를 셀 원소의 갯수는 마지막 인덱스+1!
      counts = [0] * (k+1)
      # 1. data 리스트를 순회하며, 각 원소의 갯수를 count하기
      for i in range(0, len(Data)):
        counts[Data[i]] += 1
      # 2. 각 항목 전까지 원소의 갯수를 더해 누적시키기
      for i in range(1, k+1):
        counts[i] += counts[i-1]
      # 3. Temp를 data의 길이로 놓고 마지막 원소부터 시작, count에 해당하는 위치 -1에 해당 원소를 위치시키고 (counts 값 -1) 완성
      for i in range(len(Temp)-1, -1, -1):
        counts[Data[i]] -= 1
        Temp[counts[Data[i]]] = Data[i]
    ```
- 선택 정렬
- 퀵 정렬
- 삽입 정렬 
- 병합 정렬

***

### Baby-gin Game  
0~9 사이의 카드 중 임의의 카드 6장 뽑기  
3장의 카드가 연속 -> run  
3장의 카드가 동일한 번호 -> triplet  

run과 triplet으로만 구성되는 경우 baby-gin  

babt-gin인지를 판별하시오!  

---
1.  
### by. **완전 검색**  
= 문제의 해법으로 생각되는 모든 경우의 수를 나열 후 확인  
= Exaustive Search, brute-force, generate-and-test
  - 경우의 수가 적은 경우 유리
  - 정확도가 매우 높음 -> 우선 완전 탐색을 수행하고 성능 개선을 위해 다른 방법도 고민하자

#### 순열_permutation  
=> 순열 생성 후 모든 경우의 수에서 baby-gin인지 판별  

- 서로 다른 것 중 몇 개를 뽑아서 한 줄로 나열하기
- = nPr = n!

---
2.  
### 탐욕 알고리즘 Greedy  
현 상태에서 최적의 해라고 생각되는 것을 선택함  
1. 현재 상태에서의 부분 문제의 최적의 해 -> 부분해 집합 solution set에 추가
2. 실행 가능성 검사 *=문제의 제약 조건을 위반하지 않는지*
3. 해 검사 =새로운 부분해 집합이 문제의 해가 되는지 확인

ex) 거스름돈 줄이기  
baby-gin 해결법 by. greedy
1. 원소의 갯수가 3개이면 triplet
2. run을 판별? 3개의 연속된 수들(`counts[i-1], counts[i], counts[i+1]`)의 갯수가 `>=1`인경우 판별

---

자릿수 판별 방식  
```python
# 자릿수 판별 
num =  456789
c = [0]*12 #각 자릿수를 추출하여 개수를 누적할 리스트_0~9까지인데, 9로부터 10,11은 빈자리지만 검사시 사용하려고 배정

for i in range(6): #자릿수가 6
  c[num %10] += 1 #num을 10으로 나눈 나머지 => 1의 자릿수
  num //= 10 #10으로 나누어서 num을 갱신 -> 한 자릿수씩 없애기!
```

cf) 부분합    
_문제의 조건을 잘 살펴서 음수가 되는 경우, 예상했던 합의 범위를 벗어나는 경우 고려   

gravity  
회전을 생각하지 말고, 오른쪽으로 판별을 하면서 높이가 높은게 있으면 낙차 판단  

for-else문  
= for 문을 돌면서 break를 만나지 않은 경우 for 문 종료 후 실행됨
