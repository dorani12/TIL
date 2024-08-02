### 알고리즘, 검색  
알고리즘 4일차

---
### 검색
저장된 자료 중 원하는 자료(키 값) 찾기  

### 순차 검색
배열, 연결 리스트 등 순차구조로 표현된 자료에서 순서대로 검색  
- 정렬되지 않은 경우  
  - 첫번째 원소 ~ 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교
  - 키 값이 동일한 원소 발견시 해당 인덱스 반환
  - 시간복잡도 = O(n)
    ```python
    def sequential_search(a,n,key)
      i = 0
      while i < n and a[i] != key:
          i = i+1
      if i < n:
        return i
      else
        return -1
    ```
- 정렬된 경우
  - 오름차순 정렬이라 가정
  - 순차적으로 검색, 원소의 키 값이 검색 대상의 키 값보다 크면 검색 종료
***
### 이진 검색 binary search 
자료의 가운데에 있는 항목의 키 값가 비교하여 다음 검색의 위치 결정, 검색을 진행  
자료가 정렬되어 있어야 함  
```python
def binarySearch(a, N, key):
  start = 0
  end  = N - 1
  while start <= end:
    middle = (start + end)//2
    if a[middle] == key: # 검색 성공
      return True
    elif a[middle] > key:
      end = middle -1
    else:
      start = middle + 1
  return False # 검색 실패
```
#### 인덱스
DB의 인덱스 -> 이진 탐색 트리 구조
***
### 선택 정렬
가장 작은 값의 원소부터 차례대로 선택하여 위치 교환  
시간복잡도 O(n**2)
1. 최솟값 찾기
2. 리스트의 맨 앞에 위치한 값과 교환
3. 맨 앞의 원소 제외 나머지 대상으로 반복
```python
def selectionSort(a, N):
  for i in range(N -1):
    min_idx = i
    for j in range(i+1, N):
      if a[min_idx] > a[j]:
        min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]
```

### 셀렉션 알고리즘  
저장된 자료로부터 k번째로 작거나 큰 원소를 찾는 방법
```python
def select(arr, k):
  for i in range(0,k):
    min_index = i
    for j in range(i+1, len(arr)): #정렬
      if arr[min_index] > arr[j]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr[k-1] #정렬 후 k번째 원소 반환
```