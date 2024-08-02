### 알고리즘, 배열  
알고리즘 1일차  
**손으로 적고 그리며 로직 구조, 슈도 함수를 완성시키고 난 뒤에 코드를 적기 시작!**

APS: Algorithm Problem Solving  
:문제를 해결하기 위한 절차나 방법 by. 유한한 단계  
- 입출력 함수 제외 내장함수 사용 금지 
- 내장함수의 동작원리 이해

***
#### 알고리즘의 성능_시간복잡도  
- 실제 걸리는 시간
- 실행되는 명령문의 개수
=> 빅 O오 표기법 (ex. O(n**2), O(n))
*10의 9제곱인 10억번 정도가 1초*_제한시간 있는 경우 주의  

***
### Array 배열  
:하나의 이름으로 일정한 자료형의 변수들을 열거하여 사용  
- 1차원 배열
  - ex) Arr = [0]*10,  Arr = list(), Arr = [1,2,3] 등 
  - cf) append는 시간이 오래걸리는 편..
  - 입력 받은 정수를 1차원 배열에 저장
    ```python
    # 첫 줄에 양수의 개수 N이 주어진다.
    # 다음 줄에 빈칸으로 구분된 N개의 양수 A_i가 주어진다.
    N = int(input())
    arr = list(map(int, input().split()))
    ```
  - 배열 원소 중 min, max 원소 찾기 예제
    ```python
    T = int(input())
    for testcase in range(1, T+1):
        # 입력문
        N = int(input())
        # input으로 받은 입력 값을 빈칸 기준 나누기/나눈 값들에 int() 적용/리스트에 저장
        arr = list(map(int, input().split()))
        
        # 본문
        max_v = arr[0]
        for i in range(N):
            if max_v < arr[i]:
                max_v = arr[i]

        min_v = arr[0]
        for i in range(N):
            if min_v > arr[i]:
                min_v = arr[i]

        # 출력문
        print(f'#{testcase} {max_v-min_v}')
    ```
---
### Sort 정렬  
:특정 기준으로 오름차순(ascendig), 내림차순(descending)으로 정렬  
- 버블 정렬
  - 인접한 두 개의 원소를 비교하며 자리를 계속 교환
  - 한 단계 끝 -> 가장 큰 원소가 마지막 자리로 정렬(오름차순 정렬 시)
  - 시간 복잡도: O(n**2)
  - 예제
    ```python
    def BubbleSort(arr, N) # 정렬할 배열과 배열의 크기
        for i in range(N-1, 0, -1): #단계가 지날 때마다, 가장 끝부터 정렬됨
            for j in range(0, i): #맨 왼쪽 부터, 인접한 원소와의 크기 비교_-1인건 왼쪽, 오른쪽 비교
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j] #위치 변경_python은 tmp불필요
    ```
- 카운팅 정렬
- 선택 정렬
- 퀵 정렬
- 삽입 정렬
- 병합 정렬
