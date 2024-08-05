### 알고리즘, 문자열 
알고리즘 5일차

---
### 문자열  
아스키코드: 7bit 인코딩으로 128개의 문자 표현  
*8 bit = 1 byte*  
- 유니코드 인코딩(UTF: Unicode Transformation Format)  
  - UTF-8: Web 8bit~32bit(1 byte * 4)  
  - UTF-16: Windows, Java 16bit~32bit(2 byte * 2)  
  - UTF-32: Unix 32bit~32bit(4 byte * 1)   

CRLF  
CR: 제어 문자_Carriage Return \r  
LF: Line Feed \n  

---
##### C언어 vs 파이썬  
아스키 코드 형태로 저장  
char형태, 마지막에 \0(null문자)이 있어야 함  
strlen(), strcpy(), strcmp()

str형태, immutable 값을 변경 불가(튜플도)  
UTF-8으로 저장  
'+'로 연결, '*'로 반복  
메소드 다양_replace(), split(), isalpha(), find()  

***
### 문자열 뒤집기
1. str[::-1]
2. 임시 변수 할당 후 N//2만큼 교환 진행  

### 문자열 비교
== 연산자(파이썬, 자바에서는 equals())   
: 값이 같은지 확인  
is (파이썬, 자바에서는 ==)  
: 문자열에서는 메모리 참조가 같은지 확인  

### 형변환
C언어: atoi() : 문자열 -> 정수 / itoa() : 정수형 -> 문자열  
Java:  Integer.parseInt(String), toString()  
Python: str(숫자), int('문자로 표현된 숫자'), float('3.14')...  
ord(), chr() 아스키코드 몇번째인지 반환  