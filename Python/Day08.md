## 파이썬 OOP, 디버깅
객체지향프로그래밍_상속, 에러와 예외_디버깅

---
## 상속
### 상속 Inheritance  
- 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것
#### 상속이 필요한 이유  
1. 코드 재사용
    - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
    - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며, 중복된 코드를 줄일 수 있음
2. 계층 구조
    - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
    - 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음
3. 유지 보수의 용이성
    - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐 
    - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음

    ![image](https://github.com/ragu6963/TIL/assets/32388270/f259eed5-c629-4a42-b0cc-4896162169c8)  

### 다중 상속
- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 <span style='color:crimson;'>상속 순서에 의해 결정</span>됨

#### 다이아몬드 문제  
![Diamond](https://i.ibb.co/b23YqZT/440px-Diamond-inheritanc.png)

- 두 클래스 B와 C가 A에서 상속되고 클래스 D가 B와 C 모두에서 상속될 때 발생하는 모호함
- B와 C가 재정의한 메서드가 A에 있고 D가 이를 재정의하지 않은 경우라면
- D는 B의 메서드 중 어떤 버전을 상속하는가? 아니면 C의 메서드 버전을 상속하는가?
#### 파이썬에서의 해결책 : MRO
- MRO(Method Resolution Order, 메서드 결정 순서) 알고리즘을 사용하여 클래스 목록을 생성
- 부모 클래스로부터 상속된 속성들의 검색을 깊이 우선으로, 왼쪽에서 오른쪽으로, 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않음
- 그래서, 속성이 D 에서 발견되지 않으면, B 에서 찾고, 거기에서도 발견되지 않으면, C 에서 찾고, 이런 식으로 진행됨

    ```python
    class D(B, C):
        pass
    ```  
##### MRO가 필요한 이유

- 부모 클래스들이 여러 번 액세스 되지 않도록, <br>각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존하고, <br>각 부모를 오직 한 번만 호출하고, <br>부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 단조적인 구조 형성

- 프로그래밍 언어의 신뢰성 있고 확장성 있는 클래스를 설계할 수 있도록 도움
- 클래스 간의 메서드 호출 순서가 예측 가능하게 유지되며, 코드의 재사용성과 유지보수성이 향상  
#### `super()`
- 부모 클래스 객체를 반환하는 내장 함수
- 다중 상속 시 MRO를 기반으로 현재 클래스가 상속하는 모든 부모 클래스 중 다음에 호출될 메서드를 결정하여 자동으로 호출
##### super의 2 가지 사용 사례
1. 단일 상속 구조
    - 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로, 코드를 더 유지 관리하기 쉽게 만들 수 있음
    - 클래스 이름이 변경되거나 부모 클래스가 교체되어도 super()를 사용하면 코드 수정이 더 적게 필요
2. 다중 상속 구조
    - MRO를 따른 메서드 호출
    - 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지
```python
# super 사용 예시 - 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() #부모 클래스 중 먼저 상속받을 ParentA의 __init__()을 상속받아옴
        self.value_c = 'Child'

child_instance = Child() #child클래스의 인스턴스를 변수 child_instance에 할당
print(child_instance.value_a) #ParentA: super.__init__()을 통해 상속 받아짐
print(child_instance.value_c) #Child
# print(child_instance.value_b) #이미 ParentA를 상속받아왔으므로 B는 생성되지 않음 AttributeError: 'Child' object has no attribute 'value_b'
```
***
## 에러와 예외
### 버그 bug
- 소프트웨어에서 발생하는 오류 또는 결함
- 프로그램의 예상된 동작과 실제 동작 사이의 불일치
### 디버깅 Debugging  
- 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정  
- 프로그램의 오작동 원인을 식별하여 수정하는 작업  
  1. print 함수 활용
      - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
  2. 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
      - breakpoint, 변수 조회 등
  3. [Python tutor](https://pythontutor.com/) 활용 (단순 파이썬 코드인 경우) 
  4. 뇌 컴파일, 눈 디버깅 등

### 파이썬의 에러 유형
- 문법 에러 `Syntax Error`
    - 프로그램의 구문이 올바르지 않은 경우 발생 <br>(오타, 괄호 및 콜론 누락 등의 문법적 오류)
- 예외 `Exception`
    - 문법 에러를 제외한 나머지 에러..프로그램 실행 중에 감지되는 에러
    - Invalid syntax (문법 오류)
        
        ```py
        while # SyntaxError: invalid syntax
        ```

    - assign to literal (잘못된 할당)
        
        ```py
        5=3 # SyntaxError: cannot assign to literal
        ```

    - EOL (End of Line)
        
        ```py
        print('hello   
        # SyntaxError: EOL while scanning string literal
        ```

    - EOF (End of File)
        
        ```py
        print(
        #SyntaxError: unexpected EOF while parsing
        ```
### 예외 `Exception`
- 프로그램 실행 중에 감지되는 에러
- 내장 예외 Built-in Exceptions _클래스로 구현되어있음
  - `ZeroDivisionError`
      - 나누기 또는 모듈로 연산의 두 번째 인자가 0일 때 발생
  - `NameError`
      - 지역 또는 전역 이름을 찾을 수 없을 때 발생
  - `TypeError` 
      - 타입 불일치
          ```py
          '2' + 2  # TypeError: can only concatenate str (not "int") to str
          ```
      - 인자 누락
          ```py
          sum()  # TypeError: sum() takes at least 1 positional argument (0 given)
          ```
      - 인자 초과
          ```py
          sum(1, 2, 3)  # TypeError: sum() takes at most 2 arguments (3 given)
          ```
      - 인자 타입 불일치
          ```py
          import random
          random.sample(1, 2)
          # TypeError: Population must be a sequence.  For dicts or sets, use sorted(d).
          ```
  - `ValueError` 
      - 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받았고, 상황이 IndexError 처럼 더 구체적인 예외로 설명되지 않는 경우 발생

          ```py
          int('1.5') # ValueError: invalid literal for int() with base 10: '3.5'

          range(3).index(6) # ValueError: 6 is not in range
          ```
  - `IndexError`
      - 시퀀스 인덱스가 범위를 벗어날 때 발생
          ```py
          empty_list = []
          empty_list[2]
          # IndexError: list index out of range
          ```
  - `KeyError`
      - 딕셔너리에 해당 키가 존재하지 않는 경우
  - `ModuleNotFoundError`
      - 모듈을 찾을 수 없을 때 발생
  - `ImportError`
      - 임포트 하려는 이름을 찾을 수 없을 때 발생
  - `KeyboardInterrupt`
      - 사용자가 Control-C 또는 Delete를 누를 때 발생
      - 무한루프 시 강제 종료
  - `IndentationError`
      - 잘못된 들여쓰기와 관련된 문법 오류
          ```py
          for i in range(10):
              print(i) # IndentationError: expected an indented block
          ```
### 예외 처리
- 예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리할 수 있도록 하는 방법
  - `try`
    - 예외가 발생할 수 있는 코드 작성
  - `except`
    - 예외가 발생했을 때 실행할 코드 작성
  - `else`
    - 예외가 발생하지 않았을 때 실행할 코드 작성
  - `finally`
    - 예외 발생 여부와 상관없이 항상 실행할 코드 작성
    예시)
    ```python
    try:
        x = int(input('숫자를 입력하세요: '))
        y = 10 / x
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except ValueError:
        print('유효한 숫자가 아닙니다.')
    else:
        print(f'결과: {y}')
    finally:
        print('프로그램이 종료되었습니다.')
    ```
#### 예외 처리 주의사항
`except BaseException:`은 최상위 예외클래스이므로 하위의 예외클래스는 실행 안됨  
->죽은코드 발생
- 내장 예외 클래스는 상속 계층구조를 가지기 때문에 <br>except 절로 분기 시 반드시 하위 클래스를 먼저 확인 할 수 있도록 작성해야 함  
#### 예외 객체 다루기  
##### `as` 키워드  
- 예외객체
    - 예외가 발생했을 때 예외에 대한 정보를 담고 있는 객체
- `except` 블록에서 예외 객체를 받아 상세한 예외 정보를 활용 가능

    ```py
    my_list = []

    try:
        number = my_list[1]
    except IndexError as error:
        print(f'{error}가 발생했습니다.')

    # list index out of range가 발생했습니다.
    ```
##### try-except와 if-else  
- `try-except`와 `if-else`를 함께 사용할 수 있음
  ```python
  try:
      x = int(input('숫자를 입력하세요: '))
      if x < 0:
          print('음수는 허용되지 않습니다.')
      else:
          print('입력한 숫자:', x)
  except ValueError:
      print('오류 발생')
  ```

#### 예외처리의 접근방식의 차이  
```python
my_dict = {'key': 'value'}
#EAFP (Easier to Ask for Forgiveness than Permission)_예외처리 중심, try-except_일단 해보고 안되면 에러
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')
#LBYL (Look Before You Leap)_값 검사 중심, if-else_에러가 발생하지 않아야 실행
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
```
