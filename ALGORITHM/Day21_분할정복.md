### 알고리즘, 자료구조_분할 정복
알고리즘 21일차  
분할정복_퀵 정렬, 병합정렬, 이진검색
***
## 분할 정복
Divide and Conquer : o(log_2 n)  
Top-down: 하나의 문제를 부분문제로 분할

### 병합 정렬 Merge Sort
여러 개의 정렬된 자료의 집합을 병합해 한 개의 정렬된 집합으로 만드는 방식: O(n log n)  
1. 분할: 최소 크기의 부분집합이 될 때까지 분할 -> log n
2. 2개의 부분집합을 정렬하면서 하나의 집합으로 병합_더 작은 수가 앞에 위치하도록 -> n

외부정렬의 기본 방식 | 멀티코어 CPU, 다수의 프로세서에서 병렬화 하기 위한 방법  
```python
# 분할
def merge_sort(m):
    # 리스트의 길이가 1이면 이미 정렬된 상태이므로 그대로 반환
    if len(m) == 1:
        return m

    # 리스트를 절반으로 나누기 위해 중간 인덱스를 계산
    mid = len(m) // 2
    left = m[:mid]  # 리스트의 앞쪽 절반
    right = m[mid:]  # 리스트의 뒤쪽 절반

    # 재귀적으로 왼쪽 부분과 오른쪽 부분을 정렬
    left = merge_sort(left)
    right = merge_sort(right)

    # 두 개의 정렬된 리스트를 병합하여 반환
    return merge(left, right)

# 병합
def merge(left, right):
    # 두 리스트를 병합할 결과 리스트를 초기화
    result = [0] * (len(left) + len(right))
    l = r = 0  # 왼쪽 리스트와 오른쪽 리스트의 인덱스

    # 두 리스트를 순차적으로 비교하여 작은 값을 결과 리스트에 추가
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]     # 왼쪽 리스트의 첫번째 값이 더 작음 -> result에 추가
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 요소들을 결과 리스트에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    # 오른쪽 리스트에 남은 요소들을 결과 리스트에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    # 병합된 결과 리스트를 반환
    return result


arr = [69, 10, 30, 2, 16, 8, 31, 22]
arr = merge_sort(arr)
print(arr)
```
***
### 퀵 정렬
분할: pivot item, 기준 아이템 중심 분할  
병합 과정 불필요  

### 퀵 정렬 partitioning 
partitioning 과정 반복 : O(n log n)  
1. 작업 영역 산정
2. 가장 왼쪽의 수 = pivot(기준)
3. pivot을 기준으로 작은 수는 왼쪽, 큰 수는 오른쪽에 위치시키기(각각의 왼쪽, 오른쪽은 정렬되지 않은 상태)
4. pivot의 위치는 고정 & 왼쪽 영역, 오른쪽 영역을 다시 partitioning

데이터 수가 많은 경우 유리  
cf) 최악의 경우_왼쪽 원소 pivot, 역순 정렬된 경우  
#### Hoare-partition 알고리즘  
교차  
1. pivot을 기준으로 작은 값과 큰 값을 찾아 swap
2. swap한 작은 값과 pivot swap ( [작은 값들] | pivot | [큰 값들] 이 되도록)
```python
arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# arr = [11, 45, 23, 81, 28, 34]
# arr = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
# arr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]


# 피벗: 제일 왼쪽 요소
# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음
def hoare_partition1(left, right):
    pivot = arr[left]  # 피벗을 제일 왼쪽 요소로 설정
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j


# 피벗: 제일 오른쪽 요소
# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음
def hoare_partition2(left, right):
    pivot = arr[right]  # 피벗을 제일 오른쪽 요소로 설정
    i = left
    j = right - 1

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[right] = arr[right], arr[i]
    return i


# 피벗: 중간 요소로 설정
# 일반적으로 더 균형 잡힌 분할이 가능하며, 퀵 정렬의 성능을 최적화할 수 있습니다.
def hoare_partition3(left, right):
    mid = (left + right) // 2
    pivot = arr[mid]  # 피벗을 중간 요소로 설정
    arr[left], arr[mid] = arr[mid], arr[left]  # 중간 요소를 왼쪽으로 이동 (필요 시)
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j


def quick_sort(left, right):
    if left < right:
        pivot = hoare_partition1(left, right)
        # pivot = hoare_partition2(left, right)
        # pivot = hoare_partition3(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


quick_sort(0, len(arr) - 1)
print(arr)
```
#### Lomuto-partition 알고리즘
속도 느림, 가장 오른쪽 원소 pivot     
왼쪽부터 순회하며 pivot보다 큰 원소 i, 작은 원소 j를 swap하는 과정 반복  
```python
arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]


def lomuto_partition(left, right):
    pivot = arr[right]                          # pivot은 오른쪽 원소로!

    i = left - 1                                    
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(left, right):
    if left < right:
        pivot = lomuto_partition(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


quick_sort(0, len(arr) - 1)
print(arr)
```
***
### 이진 검색  
정렬된 데이터들에서만 가능, 특정 값이나 범위를 검색하기 위해 사용  
1. 자료의 중앙에 있는 원소 선택
2. 중앙 원소의 값과 목표 값을 비교
3. 작은 경우 왼쪽 데이터들, 큰 경우 오른쪽 데이터들에서 새로 검색 수행
4. 1~3 반복

O(log n) : 각 단계별로 검색 범위가 1/2로 줄어듦, 정렬 시간 제외
lower bound, upper bound와 같이 범위를 찾기 위해 사용하기도 함  
```python
# 반복문 사용
def binary_search(target):
    low = 0
    high = len(arr) - 1
    # 탐색 횟수 카운팅
    cnt = 0

    while low <= high:
        mid = (low + high) // 2
        cnt += 1                    # 2진탐색 실행 횟수

        if arr[mid] == target:
            return mid, cnt
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1, cnt

# 재귀함수 사용
def binary_search(low, high, target):
    # 기저조건
    # target 을 발견하지 못하면 종료
    if low > high:
        return -1

    mid = (low + high) // 2

    # 발견했다면
    if target == arr[mid]:
        return mid

    # target 이 mid 보다 작다 == target 이 mid 의 왼쪽에 존재한다 == high 를 mid - 1로
    elif target < arr[mid]:
        return binary_search(low, mid - 1, target)
    else:
        return binary_search(mid + 1, high, target)

arr = [2, 4, 7, 9, 11, 19, 23]

print(f'9 = {binary_search(9)}')
print(f'2 = {binary_search(2)}')
print(f'20 = {binary_search(20)}')
```
***
