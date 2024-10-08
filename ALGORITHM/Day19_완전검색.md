### 알고리즘, 자료구조_완전 검색
알고리즘 19일차  
반복, 재귀, 순열, 완전 탐색
***
## 재귀
n중 반복문 만들기 용이  
: 하나의 큰 문제를 해결할 수 있는 더 작은 문제로 쪼개고 결과들 결합 -> 가독성 증가

<-> 반복문은 코드를 n번 반복 가능

### 재귀함수
매개변수를 통해 주어질 변수는 값만 복사되어 전달_list자료형만 제외  
기저조건(base case): 재귀호출 탈출 조건

## 순열
서로 다른 N개에서 R개를 중복 없이, 순서를 고려하여 나열: nPr

```python
# 1~6까지 중복x, 숫자 3개 출력
def punc(level):
    if level == 4:          # 종료 조건
        print(arr)
        return

    for i in range(1, 7):
        if used[i] != 1:
            used[i] = 1
            arr.append(i)   # 재귀 호출 전
            punc(level+1)   # 다음 재귀 호출 & 매개변수 전달
            arr.pop()       # 재귀함수 돌아온 이후
            used[i] = 0

# 중복 제거 -> visited[]리스트 활용, `not in`연산자의 경우 시간복잡도가 큰 편
used = [0]*(6+1)
arr = list()
punc(1)
```
***
## 완전 탐색
Brute-Force 부르트 포스 알고리즘 = 모든 가능한 경우를 모두 시도  
서로 영향이 없는 독립적인 문제, 규칙이 없는 경우
***
