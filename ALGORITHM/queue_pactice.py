# queue 생성 및 연산 연습

# 선형 큐
N = 10
q = [0] * N
front = -1
rear = -1

rear += 1   # enqueue(1)
q[rear] = 1

rear += 1   # enqueue(2)
q[rear] = 2

rear += 1   # enqueue(3)
q[rear] = 3

front += 1  # dequeue(1)
print(q[front])

front += 1  # dequeue(2)
print(q[front])

front += 1  # dequeue(3)
print(q[front])

# 입력한 순서대로 pop
###########################################################
# 선형 큐: 간단한 방법
q2 = list()
q2.append(10)
q2.append(20)
q2.append(30)
print(q2.pop(0))    # 가장 왼쪽 인덱스에 있는 값 pop
print(q2.pop(0))
print(q2.pop(0))

##########################################################
# 원형 큐
print('원형 큐')
Q_SIZE = 4
cQ = [0]*Q_SIZE
front = rear = 0

rear = (rear+1) % Q_SIZE    #enq(1)
cQ[rear] = 1

rear = (rear+1) % Q_SIZE    #enq(2)
cQ[rear] = 2

rear = (rear+1) % Q_SIZE    #enq(3)
cQ[rear] = 3

# print(cQ)   # [0, 1, 2, 3]

front = (front+1) % Q_SIZE    #deq(1)
# print(cQ[front])    # 1

rear = (rear+1) % Q_SIZE    #enq(10)
cQ[rear] = 10
# print(cQ)   # [10, 1, 2, 3] rear의 다음 칸이 front가 아닌 경우는 포화가 아님

rear = (rear+1) % Q_SIZE    #enq(20)
cQ[rear] = 20
# print(cQ)   # [10, 20, 2, 3] 덮어쓰기 발생

##########################################################
# 클래스 이용해 선형 큐 구현
class LinearQueue:
    def __init__(self, size):
        self.size = size  # 큐의 최대 용량 설정
        self.queue = [None] * size  # 큐를 리스트로 초기화
        self.front = self.rear = -1  # front와 rear를 -1로 초기화하여 빈 큐 상태로 설정

    # 공백상태
    def is_empty(self):
        return self.front == -1  # front가 -1이면 큐가 비어있음을 의미

    # 포화 상태
    def is_full(self):
        return self.rear == self.size - 1  #

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        if self.is_empty():
            self.front = self.rear = 0  # 큐가 비어있으면 front와 rear를 0으로 설정, 큐에 아이템이 하나 있으면 front와 rear는 같은 위치를 가리킴
        else:
            self.rear = self.rear + 1 # rear를 다음 위치로 이동
        self.queue[self.rear] = item  # rear 위치에 아이템 저장

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue[self.front]  # front 위치의 아이템 추출
        if self.front == self.rear:
            self.front = self.rear = -1  # 큐에 아이템이 하나 남아있는 경우 front와 rear를 초기화
        else:
            self.front = self.front + 1  # front를 다음 위치로 이동
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.queue[self.front]  # front 위치의 아이템 반환

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        i = self.front
        while i != self.rear:  # front부터 rear까지 반복하면서 아이템 출력
            print(self.queue[i], end=" ")
            i = (i + 1) % self.size  # 다음 위치로 이동
        print(self.queue[i], end=" ")  # rear 위치의 아이템 출력
        print()



# 테스트
queue = LinearQueue(5)
queue.enqueue(1)  # rear = 0
queue.enqueue(2)  # rear = 1
queue.enqueue(3)  # rear = 2
queue.enqueue(4)  # rear = 3
queue.enqueue(5)  # rear = 4
queue.enqueue(6)  # 큐가 가득 차서 에러가 나야 합니다.

queue.display()  # 1 2 3 4 5
print(queue.dequeue())  # 1
print(queue.dequeue())  # 2

queue.display()  # 3 4 5
print(queue.peek())  # 3

queue.dequeue()
queue.display() # 4 5
print(f'큐 포화 상태 체크: {queue.is_full()}') # True
queue.dequeue() # 4
queue.display() # 5
print(f'큐 포화 상태 체크: {queue.is_full()}') # True
queue.enqueue(6)
queue.dequeue() # 5
print(f'큐 포화 상태 체크: {queue.is_full()}') # False
queue.display() # 큐가 비어있음
queue.dequeue()  # 큐가 비어있음
##########################################################
# 내장 라이브러리 이용해 선형 큐 구현
from queue import Queue

queue = Queue(maxsize=3)

queue.put(1)
queue.put(2)
queue.put(3)

while not queue.empty():
    item = queue.get()
    print(item)
##########################################################
# 내장 라이브러리 이용해 덱 구현
from collections import deque

queue = deque(maxlen=3)

queue.append(1)
queue.append(2)
queue.append(3)
queue.d.appendleft(4)

while queue:
    item = queue.popleft()
    print(item)
##########################################################
# 내장 라이브러리 이용해 원형 큐 구현
class CircleQueue:

    def __init__(self, n):
        self.size = n  # 전체 크기
        self.items = [None] * n  # 각 아이템
        self.rear = 0  # rear
        self.front = 0  # front

    def is_empty(self):
        if self.rear == self.front:
            return True

        return False

    def is_full(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        return False
    """
     큐의 끝과 처음이 연결되어 있다. 
     따라서, 큐가 꽉 찼는지 여부를 확인하기 위해서는
     "마지막 요소의 다음 위치가 처음 요소의 위치와 같은지"를 확인
        self.rear + 1: 현재 rear 위치의 다음 위치를 나타냅니다.
        (self.rear + 1) % self.size: 위의 값을 큐의 크기(self.size)로 나눈 나머지를 구합니다. 
    이것은 rear가 큐를 한 바퀴 돌았을 때 처음 요소의 위치와 동일한 위치를 나타냅니다.
    front == (self.rear + 1) % self.size: 만약 front의 위치가 위에서 계산한 값과 같다면, 큐는 가득 찬 상태를 나타냅니다.
    """

    def enqueue(self, item):
        if self.is_full():
            raise Exception('Queue is full')
        self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        self.front = (self.front + 1) % self.size
        return self.items[self.front]
##########################################################
# 오래된 자료 덮어씌우기    
class CircularQueue:
    def __init__(self, size):
        self.cQsize = size + 1  # 실제 큐 크기를 size+1로 설정하여, 포화 상태와 빈 상태를 구분합니다.
        self.cQ = [None] * self.cQsize
        self.front = 0
        self.rear = 0

    def enq(self, data):
        if (self.rear + 1) % self.cQsize == self.front:  # 큐가 가득 찼을 때
            self.front = (self.front + 1) % self.cQsize  # 오래된 데이터를 덮어쓰기 위해 front를 이동
        self.rear = (self.rear + 1) % self.cQsize
        self.cQ[self.rear] = data

    def deq(self):
        if self.front == self.rear:
            raise Exception("Queue is empty")  # 큐가 비어있을 때 예외 처리
        self.front = (self.front + 1) % self.cQsize
        return self.cQ[self.front]

    def display(self):
        if self.front == self.rear:
            print("Queue is empty.")
            return
        i = (self.front + 1) % self.cQsize
        while i != (self.rear + 1) % self.cQsize:
            print(self.cQ[i], end=" ")
            i = (i + 1) % self.cQsize
        print()

# 테스트
cq = CircularQueue(4)  # 큐의 크기를 3으로 설정 (실제 크기는 4)
cq.enq(1)
cq.enq(2)
cq.enq(3)
cq.enq(4)  # 큐가 가득 차서 1을 덮어씀
cq.enq(5)  # 큐가 가득 차서 2를 덮어씀


print(cq.deq())  # 2
print(cq.deq())  # 3
print(cq.deq())  # 4
print(cq.deq())  # 5
cq.display()  # 큐가 비어있음

##########################################################
# 우선순위 큐   
import heapq
# heap => 정렬도 같이 해주는 queue
class PriorityQueue:
    def __init__(self):
        # 우선순위 큐를 빈 리스트로 초기화
        # 이 리스트는 내부적으로 힙(Heap) 자료구조를 이용해 관리됨
        self.queue = []

    def push(self, item, priority):
        # item과 priority(우선순위)를 튜플로 묶어 힙에 추가
        # heapq.heappush 함수는 새로운 요소를 힙 구조를 유지하면서 리스트에 추가
        # 기본적으로 파이썬의 heapq는 최소 힙(min-heap)을 제공
        # 따라서, 우선순위 값이 낮을수록 먼저 꺼내짐
        heapq.heappush(self.queue, (priority, item))

    def pop(self):
        # 큐에서 가장 높은 우선순위(가장 낮은 priority 값을 가진) 항목을 제거하고 반환
        # heapq.heappop 함수는 가장 작은 요소(최소 힙의 루트)를 제거하면서 힙을 유지
        if self.queue:
            priority, item = heapq.heappop(self.queue)
            return item
        else:
            # 큐가 비어있는 경우 예외를 발생시킴
            raise IndexError("pop from an empty priority queue")

    def __len__(self):
        # 큐에 남아있는 항목의 개수를 반환
        return len(self.queue)

# 우선순위 큐 인스턴스 생성
pq = PriorityQueue()

# 우선순위 큐에 항목 추가
pq.push("task1", 3)  # "task1"을 우선순위 3으로 추가
pq.push("task2", 1)  # "task2"를 우선순위 1로 추가 (가장 높은 우선순위)
pq.push("task3", 2)  # "task3"을 우선순위 2로 추가

# 우선순위가 가장 높은 항목부터 pop하여 출력
print(pq.pop())  # Output: "task2"
# "task2"가 우선순위 1로 가장 낮은 값을 가져 가장 먼저 출력됨

print(pq.pop())  # Output: "task3"
# "task3"이 우선순위 2로 두 번째로 낮은 값을 가져 두 번째로 출력됨

print(pq.pop())  # Output: "task1"
# "task1"이 우선순위 3으로 가장 높은 값을 가져 마지막으로 출력됨