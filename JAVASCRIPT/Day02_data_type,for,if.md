## JS:Javascript_자료형, 조건문, 반복문
자바스크립트 Day02
***
## DataType
### 원시 자료형  vs 참조 자료형
1. 원시 Primitive : 변수에 값이 저장, 불변, 값을 복사해서 저장    
  => Number, String, Boolean, null, undefined  
2. 참조 Reference : 객체의 주소가 저장, 가변적(1개 변경시 같은 주소의 다른 변수도 변경됨)   
  => Objects(Object, Array, Function)

## 원시 자료형
### Number 정수, 실수형 숫자 표현
```javascript
const a = 12
const a = -12
const a = 3.14
const a = Infinity
const a = 2.98e8      #(e8 = 10**8)
const a = NaN         # not a number -> 결과 값이 숫자가 아닐 때 반환
```
### String 문자형 : text data
- `+`연산자만 사용 가능!!
- Template literals : 내장된 표현식을 허용하는 문자열 작성 방식
  - Backtick "`" 을 이용 -> 여러 줄에 걸쳐 문자열 정의 가능, 변수를 문자열 내에 연결 가능(fstring 처럼)
  - 표현식 -> `$`, `{ 표현식 내용 }`
```javascript
const age = 100
const message = `홍길동은 ${age}세 입니다.`
console.log(message)
```
### Null vs Undefined
값이 없음 (개발자, 의도적) vs 값이 할당되지 않음(시스템)

### Boolean
`true`, `false`
***
## 연산자
- 할당 연산자 `=`  
  단축 연산자도 지원 `let a = 0 \n a += 10`
- 증감 연산자 `++`, `--`  
  - ++a : 전위 연산, +1연산 수행 후 그 값을 a에 할당
  - a-- : 후위 연산, 값을 변수에 할당한 뒤 해당 변수의 값 -1
- 비교 연산자 `>`, `<`  
  문자형도 ASCII코드 기준으로 비교 가능
- 동등 연산자 `==`, 일치 연산자 `===`
  - `==` : 암묵적인 형변환 후 값 비교  
    `console.log('1' == 1) // true`, `console.log(0 == false) // true`
  - `===` : 값, 형 type 둘다 일치해야 함  
    `console.log('1' === 1) // false`, `console.log(0 === false) // false`
- 논리 연산자
  - AND `&&` : `true && false // false`
  - OR `||`
  - NOT `!` : `!false  // true`
***
## 조건문
### if
```javascript
const name = 'admin'
if (name == 'admin') { 
  console.log('관리자님 환영해요!')
} else if (name == 'customer') { 
  console.log('고객님 환영해요')
} else {
  console.log(`반갑습니다. ${name}님`)
}
```
### 삼항 연산자 
명시적인 조건문 -> 간결하게 작성  
`조건 ? true일 때 표현식 : false일 때 표현식`  
ex) `const age = 20` /n `const message = (age >= 18) ? '성인' : '미성년자'`

***
## 반복문
### While
조건문이 참인 동안 실행 
```javascript
let i = 0   // 재할당될 예정 => const가 아닌 let을 이용해 선언
while (i < 6) {
  console.log(i)
  i += 1
}
```
### For
특정 조건이 거짓일 때까지 반복
```javascript
for ( [초기문]; [조건문]; [증감문] ){
  실행 될 문장
}

for ( let i = 0; i < 6; i++){
  console.log(i)
}
```
### For ... in 
객체의 열거 가능한 속성, property에 대해 반복  
객체 ex) dictionary는 key, list의 경우에는 index지만, 순서를 보장하지 않음! 
```javascript
for ( variable in object){
  statement 실행문
}

const object = {
  a : `apple`,
  b : `banana`
}

for (const property in object){
  console.log(property) // a, b
  console.log(object[property]) // apple, banana
}
```
### For ... of
반복 가능, iterable한 객체에 대해 반복  
배열!
```javascript
for (variable of iterable){
  실행문
}

const numbers = [0, 1, 2, 3]
for (const number of numbers){
  console.log(number)
}

```
### for in vs for of
```javascript
const arr = ['a', 'b', 'c']
for (const i in arr) {  
  console.log(i) // 0, 1, 2 # in으로 접근시 속성에 해당하는 index 반환
}

for (const i of arr) {
  console.log(i) // a, b, c # of로 접근시 순서에 맞게 value을 반환
}

```
#### 반복문 내부에서 let, const 변수 할당
i = 0 -> i++는 i 값을 재할당  
=> `let`  
for .. of, for .. in은 재할당이 아닌 다른 속성 이름을 변수에 지정   
=> `const`로도 에러 발생 X

***
### 참고_NaN, Undefined
#### NaN
허수를 포함, 피연산자에 NaN이 존재, 정의불가 계산식, 문자열 포함 계산식.... 등등
### Null vs Undefined
값이 없음, 객체가 없음 (개발자, 의도적) vs 값이 할당되지 않음(시스템)
```javascript
typeof null       // 'object'
typeof undefined  // 'undefined'
```
***