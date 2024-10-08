## 파이썬 기초문법 1
프로그래밍~Data 타입 중 문자열까지  

---
#### 프로그래밍?  
프로그램은 명령어들의 집합  
- *문장에 있는 표현식들을 평가하여 값을 얻어냄*
---
#### 연산자 

- ** 지수  
- / 나눗셈  
- % 나머지
- // 몫

#### 변수(variable)와 변수 할당
- 값을 저장하기 위한 이름 = 변수  
- 표현식을 통해 변수에 값을 저장 = 할당   
- 참조_변수는 메모리 주소를 가지고 값을 참조함
---
#### 데이터 타입  
`type(변수명) #자료형 종류 출력`
- Numeric Types
    - int (정수), float (실수), complex (복소수)
- Sequence Types
    - list, tuple, range
- Text Sequence Type
    - str (문자열)
- Non-sequence Types
    - set, dict
- 기타
    - None, Boolean, Functions
---
**`decimal` 함수**  
`float` 자료형에서는 0.1이 정확히 0.1이 아닌 **근사한 값**을 표현하게 됨  
이런 문제를 해결하기 위해 decimal 함수를 활용하여 값을 정확한 값으로 나타내도록 함  

---
#### **sequene types**
= str, list, tuple, range  
여러 개의 값들을 순서대로 나열함
1. 순서(Sequence)  
   - 값들이 순서대로 저장 (정렬 X)  
2. 인덱싱(Indexing)  
   - 각 값에 고유한 인덱스(번호)를 가지고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정할 수 있음  
    ***0부터 시작***
3. 슬라이싱(Slicing)  
   - 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음  
    ex) `arr = 'hello' `일 때, `print(arr[1:3])`은 `el`  
    범위에서 **앞쪽은 포함, 뒤쪽은 포함x**, 직전까지의 인덱스를 출력하게됨  
    = *이상, 미만*  
    +step 설정 `[:5:2]` ->0부터 5까지, 6번째 미만을 두칸 간격으로 출력  
    `[::-1]`은 순서 뒤집기  
4. 길이(Length)  
   - len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음 
5. 반복(Iteration)  
   - 반목문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음  
---
#### 문자열
배열로 저장하는 것이 아니라 통째로 저장하는 파이썬 방식  
->**특정 인덱스만 변경 불가능함**  
#### Escape sequence
- 역슬래시(backslash, `/`)뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
- 파이썬의 일반적인 문법 규칙을 잠시 탈출한다는 의미

|     예약   문자    	|      내용(의미)    	|
|:------------------:	|:------------------:	|
|          `\n`        	|      줄   바꿈     	|
|          `\t`        	|          탭        	|
|          `\\`        	|       백슬래시     	|
|          `\’`        	|     작은 따옴표    	|
|          `\"`        	|     큰   따옴표    	|

#### String Interpolation
- 문자열 내에 변수나 표현식을 삽입하는 방법  
##### f-string
- 문자열에 `f` 또는 `F` 접두어를 붙이고 표현식을 `{expression}`로 작성하는 문법  
- 문자열에 파이썬 표현식의 값을 삽입할 수 있음  