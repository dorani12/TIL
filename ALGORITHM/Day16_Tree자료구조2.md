### 알고리즘, 자료구조_Tree
알고리즘 16일차  
이진 탐색 트리와 heap  
***
## 이진 탐색 트리 binary search tree, BST
데이터를 **빠르게 검색**할 수 있도록 체계적으로 저장  
최대 O(log_2 n)의 빠른 속도로 값을 검색 할 수 있는 자료구조  

### BST 연산
삽입 규칙: 부모 노드보다 크면 오른쪽, 작으면 왼쪽에 삽입  
탐색 규칙: 중위 순회, in-order  
삭제 연산:   
1. 리프노드 삭제  
2. 자식 노드 1개인 경우, 자식노드를 부모 노드와 연결 후 삭제
3. 자식 노드 2개인 경우, 왼쪽 서브트리의 가장 큰 값 or 오른쪽 서브트리의 가장 작은 값을 연결 후 삭제

연결리스트 활용 예제
```python
'''
7
3 5 1 2 7 4 -5
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)

N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")
```
---
#### 리스트와 시간 복잡도 비교  
list: 삽입, 삭제, 탐색 O(n)  
BST: 삽입, 삭제, 탐색 평균 O(log n)  
- level만큼만 비교, 한단계 지나면 절반씩 비교대상이 줄어들게 됨_시간복잡도 O(h), height
- 완전이진트리가 아닌 경우(이미 정렬된 데이터), 최악 -> 리스트와 동일한 시간복잡도 O(n)

***
## Heap 힙
**완전 이진 트리**에 있는 노드 중, 키 값이 가장 크거나 작은 노드를 찾기 위해 만든 자료구조  
=> **우선 순위 큐** 구현 가능 *내장함수!!*

### 최대 힙(Max heap)
완전 이진트리 구성 for. 가장 큰 값 찾기  
- 루트 노드: 키 값이 가장 큰 노드  
- 부모노드의 키 값 > 자식 노드의 키 값
- 연산
    - 삽입: 부모 노드와 크기 비교, 삽입하려는 값이 더 큰 경우 swap
    - 삭제: 루트 노드만 삭제, 마지막 노드를 우선 루트로 올리고 더 큰 자식 노드와 다시 swap
```python
'''
7
20 15 19 4 13 11 17

7
20 15 19 4 13 11 23
'''
# 최대힙
def enq(n):
    global last
    last += 1                                   # 마지막 노드 추가(완전이진트리 유지)
    h[last] = n                                 # 마지막 노드에 데이터 삽입
    c = last                                    # 부모 > 자식 비교를 위해
    p = c//2                                    # 부모번호 계산
    while p >= 1 and h[p] < h[c]:               # 부모가 있는데, 더 작으면
        h[p], h[c] = h[c], h[p]                 # swap 교환
        c = p
        p = c//2


def deq():
    global last
    tmp = h[1]                                  # 루트의 키 값 보관
    h[1] = h[last]
    last -= 1
    p = 1                                       # 새로 옮긴 루트
    c = p*2
    while c <= last:                            # 자식이 있으면
        if c+1 <= last and h[c] < h[c+1]:       # 오른쪽 자식이 있고 더 크면
            c += 1
        if h[p] < h[c]:                         # swap
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        else:
            break
    return tmp


N = int(input())                                # 필요한 노드 수
arr = list(map(int, input().split()))

h = [0]*(N+1)                                   # 최대 힙, 완전 이진트리로 구성되므로 2**n이 해당 레벨의 첫번째 원소 idx
last = 0                                        # 힙의 마지막 노드 번호

for num in arr:
    enq(num)

print(h)

while last > 0:
    print(deq(), end=' ')
```

### 최소 힙(min heap)
완전 이진트리 구성 for. 가장 작은 값 찾기    
루트 노드: 키 값이 가장 작은 노드  
부모노드의 키 값 < 자식 노드의 키 값
```python
# 최소힙
def enq(n):
    global last
    last += 1   # 마지막 노드 추가(완전이진트리 유지)
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last    # 부모>자식 비교를 위해
    p = c//2    # 부모번호 계산
    while p >= 1 and h[p] > h[c]:   # 부모가 있는데, 더 크면
        h[p], h[c] = h[c], h[p]  # 교환
        c = p
        p = c//2

def deq():
    global last
    tmp = h[1]   # 루트의 키값 보관
    h[1] = h[last]
    last -= 1
    p = 1           # 새로 옮긴 루트
    c = p*2
    while c <= last:  # 자식이 있으면
        if c+1 <= last and h[c] > h[c+1]:  # 오른쪽자식이 있고 더 작으면
            c += 1
        if h[p] > h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        else:
            break
    return tmp


N = int(input())          # 필요한 노드 수
arr = list(map(int, input().split()))

h = [0]*(N+1)   # 최대힙
last = 0        # 힙의 마지막 노드 번호

for num in arr:
    enq(num)

print(h)

while last > 0:
    print(deq(), end=' ')
```
---
### heap 내장함수
default: min heap
```python
from heapq import heappush, heappop

N = int(input())                # 필요한 노드 수
arr = list(map(int, input().split()))

heap = []                       # 최대 힙을 구현하기 위한 리스트

# 최소 힙 ( 기본 )
for num in arr:
    heappush(heap, num)

print([x for x in heap])        # 힙의 내부 상태를 출력

while heap:
    print(heappop(heap), end=' ')

print('\n------------------------------------')

# 최대 힙
# 삽입 시 음수로 곱하여 저장 (제일 큰 수가 제일 작아짐)
# 삭제 후 음수 값을 곱하여 출력 (다시 원래 수로 복구하여 출력)
for num in arr:
    heappush(heap, -num)

print([-x for x in heap])       # 힙의 내부 상태를 출력 (음수로 저장된 상태)

while heap:
    print(-heappop(heap), end=' ')
```
***
