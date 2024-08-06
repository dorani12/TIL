### 알고리즘, 자료구조_Stack 스택
알고리즘 7일차

---
## 스택
물건을 쌓아 올리듯 자료를 쌓아 올림, 선형구조  
**LIFO( Last in First Out)**: 마지막에 삽입한 자료 먼저 꺼내기, 후입 선출  

### 자료구조
= 자료를 선형으로 저장할 저장소
- 배열 사용 가능(`sp`: stack pointer)
- 마지막으로 입력 -> top
- 연산
  - 삽입 `push`
  - 삭제 `pop`
  - top에 위치한 자료 확인 `peek`
- 선형 구조: 자료간의 관계가 1 : 1  
  비선형 구조: 1 : N  
---
### 스택 구현
push = top의 stack pointer 한자리 상승, 해당 자리에 자료 저장  
pop = top에 위치한 자료 꺼내오기, top의 sp 한자리 내리기
- push 예제
  ```python
  # PUSH는 append로 구현
  def push(item):
    stack.append(item)

  # 정석적인 방법
  def push(item, size):
    global top
    top += 1
    if top == size:
      print('overflow!')
    else:
      stack[top] = item
  
  size = 10
  stack = [0] * size
  top = -1

  push(10, size)

  # 간단한 방법
  top += 1          # push(20)
  stack[top] = 20
  ```
- pop 예제
  ```python
  # pop는 pop 메소드로 구현
  def stack_pop():
    if len(stack) == 0:
      # underflow 발생
      return -1
    else:
      return stack.pop()

  # 정석적인 방법
  def stack_pop():
    global top
    if top == -1:
      print('underflow!')
      return 0
    else:
      top -= 1
      return stack[top+1]
  
  print(stack_pop())

  # 간단한 방법
  if top > -1:  # pop()
    top -= 1
    print(stack[top+1])
  ```
---
#### 스택 구현 고려사항
구현은 용이 but, 스택의 크기 변경이 어려움
-> 저장소 동적 할당, 동적 연결리스트

---
### 스택 응용
#### 1. 괄호 검사
- 조건  
  1. 오른쪽, 왼쪽 괄호의 갯수 동일
  2. 같은 괄호에서 왼쪽 -> 오른쪽 순서대로
  3. 괄호 사이에는 포함관계만 존재함
- 구현  
  - 왼쪽 괄호 들어오면 stack에 넣기
  - 오른쪽 괄호 발견시 pop
  - 이때 개수가 맞는지 확인

#### 2. **function call_함수의 호출**  
먼저 호출한 함수가 내부에서 또다른 함수 호출  
return 값은 내부함수 부터 순차적으로 반환  
-> stack 구조로 함수가 호출되고 실행됨  
(함수에서 사용되는 변수에 값 할당도 마찬가지)  

### 3. **재귀 호출**
함수내에 하위 값에서 상위 값을 구하는 작업 반복시 유리  
**중단조건**, 실행시 자기자신 호출
- 예제: 피보나치 수열   
  ```python
  # 피보나치 수열 = 이전의 두 수의 합을 다음 항으로 하는 수열
  def fibo_arr(n):
      if n < 2:
          return n
      else:
          return fibo_arr(n-1) + fibo_arr(n-2)

  # 팩토리얼 함수
  def fact(n):
      global cnt
      cnt += 1
      if n == 1:
          return 1
      return n*fact(n-1)

  # 배열의 원소에 접근하기
  def f(i, N):  # 현재 인덱스 i, 배열의 크기 N
    if i == N:  # 배열을 벗어나는 경우
      return
    print(arr[i])
    f(i+1, N)
  
  arr = [1, 4, 7]
  N = 3
  f(0, 3)
  ```
---