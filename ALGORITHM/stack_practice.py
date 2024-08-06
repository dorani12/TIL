# 스택 자료구조 만들고 연습하기

stack = []  # array 형태로 stack 선언

stack.append(1)  # append 이용해서 push(1)
stack.append(2)  # push(2)
stack.append(3)  # push(3)

# 스택은 LIFO이르므로 3, 2, 1 순으로 pop
print(stack.pop()) # 3
print(stack.pop()) # 2
print(stack.pop()) # 1

###########################################
stack_size = 10
stack2 = [0] * stack_size
top = -1

top += 1    # push(1)
stack2[top] = 1

top += 1    # push(2)
stack2[top] = 2

top += 1    # push(3)
stack2[top] = 3

top -= 1    # pop()
print(stack2[top+1])  # 3
print(stack2[top])  # 2
top -= 1
print(stack2[top]) # 1
top -= 1

print('###########################################')
# 재귀함수_ **중단 조건**, 진행시 자기자신 호출 
# 팩토리얼 함수
def fact(n):
    global cnt
    cnt += 1
    if n == 1:
        return 1
    return n*fact(n-1)

cnt = 0
print('n 팩토리얼 값:', fact(5), '호출 횟수:', cnt)

# 피보나치 수열
def fibo_arr(n):
    if n < 2:
        return n
    else:
        return fibo_arr(n-1) + fibo_arr(n-2)
    
# 배열의 원소에 접근하기

def f(i, N):  # 현재 인덱스 i, 배열의 크기 N
    if i == N:  # 배열을 벗어나는 경우
        return
    print(arr[i])
    f(i+1, N)

arr = [1, 4, 7]
N = 3
f(0, 3)