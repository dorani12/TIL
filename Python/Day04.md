## 파이썬 함수 
module, package ~ 제어문: 조건문, 반복문

---
### 모듈  
- 한 파일로 묶인 변수와 함수의 모음<br>특정한 기능을 하는 코드가 작성된 파이썬 파일(`.py`)  
- 주의) 같은 이름의 함수 있으면 마지막 import로 인식 -> `from ~~ import *` 같이 모두 불러오는건 조심
- `from my_math import sqrt as my_sqrt` 같이 as 별칭으로 불러오기도 함
- `from 경로 import 모듈 명`
#### 모듈을 가져오는 방법
- `import` 문 사용

    ```python
    import math
    
    print(math.sqrt(4))
    #math라는 모듈에서 sqrt()함수를 찾아라!
    ```
- `from` 절 사용

    ```python
    from math import sqrt

    print(sqrt(4))
    ```
### 파이썬 표준 라이브러리 `Python Standard Library`  
- 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

> 참고 문서 : https://docs.python.org/ko/3/library/index.html  

모듈들을 모아서 directory에 묶으면 패키지  
패키지들과 여러 모듈 더해서 라이브러리!  

#### `pip` 파이썬 패키지 관리자  
- **외부 패키지**들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템  
- cf) 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치할 수 있음   
    ```bash
    $ pip install SomePackage
    $ pip install SomePackage==1.0.5
    $ pip install SomePackage>=1.0.4
    ```
#### requests 외부 패키지 설치 및 사용 예시
- 외부로 요청을 보내서 패키지가 설치될 수 있도록 함
- global하게 request라고 install
  ```bash
  $ pip install requests
  ```
  ```python
  import requests

  url = 'https://random-data-api.com/api/v2/users'
  response = requests.get(url).json()

  print(response)
  ```
***
### 제어문  
- cotrol Statement
- 코드의 실행 흐름을 제어하는 데 사용되는 구문  
- <span style='color:red;'>조건</span>에 따라 코드 블록을 실행하거나 <span style='color:red;'>반복</span>적으로 코드를 실행  
- 조건문
    - `if`, `elif`, `else`
- 반복문
    - `for` : **종료조건 0**, `while` : **조건이 참**인 동안 반복실행_false가 되면 종료
- 반복문 제어
    - `break`, `continue`, `pass`  

#### 반복 가능한 객체 `iterable`  
- 반복문에서 순회할 수 있는 객체<br>
(시퀀스 객체 뿐만 아니라 **dict, set 등도 포함**)
- 변수명 꿀팁: `for 단수형 in 복수형`
- ex) 리스트, 딕셔너리 같은 시퀀스 items중에 원소 item, 문자 char, 숫자 i
  ```python
  items = ['apple', 'banana', 'coconut']

  for item in items:
      print(item)
  ```
  ```python
  my_dict = {
      'x': 10,
      'y': 20,
      'z': 30,
  }

  for key in my_dict:
      print(key) #일반적으로는 key가 받아짐
      print(my_dict[key]) #값 받는 방법
  ```
#### `enumerate(iterable, start=0) `  
- iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
- enumerate 예시
  ```python
  fruits = ['apple', 'banana', 'cherry']

  for index, fruit in enumerate(fruits):
  print(f'인덱스 {index}: {fruit}')

  """
  인덱스 0: apple
  인덱스 1: banana
  인덱스 2: cherry
  """
  ```

#### 반복 제어  
- for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만<br>
때때로 일부만 실행하는 것이 필요할 때가 있음  

#### 반복문 제어 키워드  
- `break`
  - 반복을 즉시 중지
- `continue`
  - 다음 반복으로 건너뜀
- `pass`
  - 아무런 동작도 수행하지 않고 넘어감
  - pass 예시
    1. 코드 작성 중 미완성 부분
        - 구현해야 할 부분이 나중에 추가될 수 있고, 코드를 컴파일하는 동안 오류가 발생하지 않음
          ```python
          def my_function():
              pass  
          ```
    2. 조건문에서 아무런 동작을 수행하지 않아야 할 때
        ```python
        if condition:
            pass  # 아무런 동작도 수행하지 않음
        else:
            # 다른 동작 수행
        ```
    3. 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법
        ```python
        while True:
            if condition:
                break
            elif condition:
                pass  # 루프 계속 진행
            else:
                print('..')
        ```
***
### List Comprehension
- 간결하고 효율적인 리스트 생성 방법
- 꿀팁) 2차원 리스트 작성
- 구조
  ```python
  [expression for 변수 in iterable] #변수가 딱히 쓸모 없고 횟수만 중요하면 `_`로 표기 `for _ in range(5)`
  list(expression for 변수 in iterable)

  [expression for 변수 in iterable if 조건식]
  list(expression for 변수 in iterable if 조건식)
  ```
