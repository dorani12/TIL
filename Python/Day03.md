## 파이썬 함수 
함수의 정의~패킹,언패킹

---
### 함수
 
 #### 함수의 정의와 호출
- 함수 정의(정의)
    - 함수 정의는 `def` 키워드로 시작
    - def 키워드 이후 함수 이름 작성
    - 괄호안에 매개변수를 정의할 수 있음_*정의할 때 input 값*
    - 매개변수(parameter)는 함수에 전달되는 값을 나타냄
- 함수의 반환 값(return)
    - return 값이 없다면 none
    - `return` 키워드 이후에 반환할 값을 명시
    - `return` 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환
- 함수 호출
    - 함수를 사용하기 위해서는 호출이 필요
    - 함수의 이름과 소괄호를 활용해 호출
    - 필요한 경우 인자(argument)를 전달해야 함_**호출 할 때 전달하는 값**
    - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입됨
---
  ```python 
  def make_sum(pram1, pram2):
      """이것은 두 수를 받아
      두 수의 합을 반환하는 함수입니다.
      >>> make_sum(1, 2)
      3
      """
      return pram1 + pram2
  result = make_sum(100, 30)
  #130값을 출력
  return_value = print(result)
  #return 이 없는 함수이기 때문에 none 반환
  print(return_value)
  ```
  반환값을 받아오는지 아닌지 함수별로 다르다!  

---
#### 다양한 인자 종류
1. 위치 인자_인자의 위치가 중요
2. 기본 인자 값_default 값 할당, 인자 부족해도 ok
3. 키워드 인자
  - 인자의 이름, 값을 같이 전달_순서 x
  - _단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함
4. 임의의 인자 목록_*args로 개수 모르는 여러개 인자를 튜플로 처리
5. 임의의 키워드 인자 목록_**kargs로 딕셔너리로 처리

#### Positional Arguments (위치인자)
- 함수 호출 시 인자의 위치에 따라 전달되는 인자
- <span style='color:crimson;'>위치인자는 함수 호출 시 반드시 값을 전달해야 함</span>  
  
#### Arbitrary Argument Lists (임의의 인자 목록)
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 <span style='color:red;'>`‘*’`</span>를 붙여 사용하며, 여러 개의 인자를 tuple로 처리  
  
#### Arbitrary Keyword Argument Lists (임의의 키워드 인자 목록)  
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자  
- 함수 정의 시 매개변수 앞에 <span style='color:red;'>`‘**’`</span>를 붙여 사용하며, <br>여러 개의 인자를 dictionary로 묶어 처리  

    ```python
    def print_info(**kwargs):
        print(kwargs)

    print_info(name='Eve', age=30) # {'name': 'Eve', 'age': 30}
    ```
---
### 재귀 함수
- 함수 내부에서 자기 자신을 호출하는 함수
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
- base case_종료조건!
- 문제의 자연스러운 표현
  - 복잡한 문제를 간결하고 직관적으로 표현 가능
- 코드 간결성
  - 상황에 따라 반복문보다 알고리즘 코드가 더 간결하고 명확해질 수 있음
- 수학적 문제 해결
  - 수학적 정의가 재귀적으로 표현되는 경우, 직접적인 구현 가능

#### 재귀 함수 활용 시 기억해야 할 것
1. 종료 조건을 명확히
2. 반복되는 호출이 종료 조건을 향하도록

- 예시: 팩토리얼, 피보나치 함수
    ```python
    def factorial(n):
        # 종료 조건: n이 0이면 1을 반환
        if n == 0:
            return 1
        else:
            # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
            return n * factorial(n - 1)
    # 팩토리얼 계산 예시
    print(factorial(5))  # 120
    ```

---
### 내장 함수  
import 없이 사용 가능_기본 제공  
  ```python
  #자주 사용되는 내장 함수 예시
  numbers = [1, 2, 3, 4, 5]

  print(len(numbers))  # 5
  print(max(numbers))  # 5
  print(min(numbers))  # 1
  print(sum(numbers))  # 15
  print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]
  ```
#### `map(function, iterable)`  
- 순회 가능한 데이터구조(iterable)의 **모든 요소에 함수를 적용**하고, 그 결과를 map object로 반환
- SWEA 문제의 input 처럼 문자열 `'1 2 3'`이 입력 되었을 때 활용 예시  
  ```python
  numbers1 = input().split()
  print(numbers1)  # ['1,', '2,', '3']

  numbers2 = list(map(int, input().split()))
  print(numbers2)  # [1, 2, 3]
  ```  
#### `zip(*iterable)`
- 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
- 여러 개의 리스트를 동시에 조회할 때  
    ```python
    kr_scores = [10, 20, 30, 50]
    math_scores = [20, 40, 50, 70]
    en_scores = [40, 20, 30, 50]
    for student_scores in zip(kr_scores, math_scores, en_scores):
        print(student_scores)
    """
    (10, 20, 40)
    (20, 40, 20)
    (30, 50, 30)
    (50, 70, 50)
    """
    ```
- 2차원 리스트의 같은 컬럼(열) 요소를 동시에 조회할 때  
    ```python
    scores = [
        [10, 20, 30],
        [40, 50, 39],
        [20, 40, 50],
    ]
    for score in zip(*scores):
        print(score)
    """
    (10, 40, 20)
    (20, 50, 40)
    (30, 39, 50)
    """
    ```
- 열이 같은 원소들끼리 튜플형태로 묶어줌
#### 람다 표현식 (Lambda expressions)  
- 익명 함수를 만드는 데 사용되는 표현식_**1회성**으로 쓸 때 활용
- 한 줄로 간단한 함수를 정의: `lambda 매개변수: 표현식`
  
### Python의 범위(Scope)  
- 함수는 코드 내부에 `local scope`를 생성하며, 그 외의 공간인 `global scope`로 구분

#### 범위와 변수 관계  
- scope  
    - **global** scope : 코드 어디에서든 참조할 수 있는 공간  
    - local scope : 함수가 만든 scope (**함수 내부에서만** 참조 가능)  
- variable   
    - global variable : global scope에 정의된 변수  
    - local variable : local scope에 정의된 변수  
- 이름 검색 규칙(Name Resolution) = LEGB Rule  
  built-in function인 *`sum`을 변수명으로 작성하지 말자!*

## Packing & Unpacking

#### `*`, `**` 패킹 / 언패킹 연산자 정리
- `‘*’`
    - 패킹 연산자로 사용될 때, 여러 개의 인자를 하나의 튜플로 묶음
    - 언패킹 연산자로 사용될 때, 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달
    
- `‘**’`
    - 언패킹 연산자로 사용될 때, 딕셔너리의 키-값 쌍을 언패킹하여 함수의 키워드 인자로 전달