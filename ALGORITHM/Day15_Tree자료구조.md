### 알고리즘, 자료구조_Tree
알고리즘 15일차  
Tree 자료구조, 이진 트리와 순회  
***
## 트리
- 비선형 구조, 원소들 간에 1:n의 관계를 가짐  
- 원소들 간의 계층관계 O <-> 그래프와 다르게, 자손노드끼리 연결될 일이 없음(사이클 x)
- 최상위 노드(정점) = 루트 root
- 노드는 트리의 원소들, 간선은 부모 노드와 자식 노드를 연결
- 차수 degree
  - 노드의 차수 = 노드에 연결된 자식 노드의 수
  - 트리의 차수 = 트리에 있는 노드의 차수 중에 가장 큰 값
  - 단말 노드(리프 노드) = 차수가 0인 노드, 자식 노드가 없는 노드
- 높이: 루트에서 노드에 이르는 간선의 수 | 최댓값이 트리의 높이

### 자료구조
- 선형 구조: 자료간의 관계가 1 : 1  
: idx로 자료들에 접근 용이, stack, queue, deq, 연결리스트
- 비선형 구조: 1 : N  
: 순서가 없어 idx로 접근하기 어려움, dictionary, set, hash, graph  
  - 노드(N, node, 정점(vertex): 위치라는 개념)
  - 간선(E, edge, 간선: 위치 간의 관계) = 노드를 연결 
---
### 이진 트리 binary tree
모든 노드들이 최대 2개의 서브트리를 가지는 특별한 형태의 트리
- 레벨 i일 때, 노드의 최대 개수는 (2**i)개
- 높이가 h : 노드의 최소개수 h+1, 최대 (2**(h+1)-1)개
- 노드의 번호는 부모 노드가 `n`번 일 때, 왼쪽 자식 노드 `2*n`, 오른쪽 자식 노드 `2*n + 1`
- 레벨 k일 때, 시작 노드의 번호는 `2**k`

#### 포화 이진 트리 full
모든 레벨의 노드가 포화상태
#### 완전 이진 트리 complete
빈자리 x (노드 번호 1 ~ n까지)  
: 높이가 h, 노드 수 n개 일 때 : `2**h <= n <= 2**(h+1)-1`
#### 편향 이진 트리 skewed
자식 노드가 한 개씩 있으면서, 한쪽 방향으로만 자식노드를 가짐

---
### 순회 traversal
: 트리의 노드들을 체계적으로 방문  

- 전위 순회 preorder: 부모 노드 -> 왼쪽 자식 노드 -> 오른쪽 자식 노드(DFS)  
- 중위 순회 inorder: 왼쪽 자식 노드 -> 부모 노드 -> 오른쪽 자식 노드  
  (왼쪽 서브트리에서 모든 왼쪽의 자손 요소 확인 후 중간 값 확인, 오른쪽 서브트리로 이동)  
- 후위 순회 postorder: 왼쪽 자식 노드 -> 오른쪽 자식 노드 -> 부모 노드  

---
### 이진 트리의 저장 : 구현
클래스 선언, 연결 리스트 구현 | 인접 리스트(그래프로 접근)  
+) 수식

기본 방식
```python
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def pre_order(T):
    if T:
        print(T, end = ' ') # 출력 순서로 전위, 중위, 후위 순회 모두 표현 가능
        pre_order(left[T])
        pre_order(right[T])

N = int(input())        # 1번부터 N번까지인 정점
E = N-1
arr = list(map(int, input().split()))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽 자식 번호 저장
right = [0]*(N+1)       # 1부터 시작 -> N +1 
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
# for i in range(0,E*2, 2):
#         p, c = arr[i], arr[i + 1]
    if left[p]==0:          # 왼쪽자식이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c]!=0:        # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root
print(root)
pre_order(root)
```

인접리스트 활용
```python
def dfs(node):
    if node == -1:
        return

    preorder.append(node)
    dfs(graph[node][0])
    inorder.append(node)
    dfs(graph[node][1])
    postorder.append(node)

N = int(input())
E = N - 1
arr = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
# append 를 통해 갈 수 있는 경로를 추가하기
for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    graph[p].append(c)

# 없는 경우 -1로 데이터를 저장하기 위한 코드("좌우 경로가 있는가 ?")
# 탐색 시 index 오류를 방지하기 위해 없는 경로를 -1로 저장하였습니다.
for i in range(N + 1):
    while len(graph[i]) < 2:
        graph[i].append(-1)


preorder = []
inorder = []
postorder = []

dfs(1)

print(*inorder)
print(*preorder)
print(*postorder)
```

연결리스트 활용
```python
from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key  # 노드의 값
        self.left = None  # 왼쪽 자식 노드를 가리킴
        self.right = None  # 오른쪽 자식 노드를 가리킴

class BinaryTree:
    def __init__(self):
        self.root = None  # 트리의 루트 노드

    # 새로운 노드를 삽입하는 함수 (레벨 순서 삽입)
    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
            return

        # 레벨 순서로 트리를 탐색하기 위해 큐를 사용
        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            # 왼쪽 자식이 비어있으면 삽입
            if node.left is None:
                node.left = new_node
                break
            else:
                queue.append(node.left)

            # 오른쪽 자식이 비어있으면 삽입
            if node.right is None:
                node.right = new_node
                break
            else:
                queue.append(node.right)

    def inorder_traversal(self):
        # 중위 순회를 통해 트리의 노드들을 출력하는 함수
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)
        return result

# 예제 사용법
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    print("Inorder Traversal:", tree.inorder_traversal())
    tree.insert(30)
    print("Inorder Traversal:", tree.inorder_traversal())
    tree.insert(20)
    print("Inorder Traversal:", tree.inorder_traversal())
    tree.insert(40)
    print("Inorder Traversal:", tree.inorder_traversal())
    tree.insert(70)
    print("Inorder Traversal:", tree.inorder_traversal())
    tree.insert(60)
    print("Inorder Traversal:", tree.inorder_traversal())
    tree.insert(80)

    print("Inorder Traversal:", tree.inorder_traversal())
```
***