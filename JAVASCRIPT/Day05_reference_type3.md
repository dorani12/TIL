## JS:Javascript_참조 자료형 3_배열
자바스크립트 Day05
***
## Array 배열
object와 같이 key와 value로 값이 구분되지만, **순서**가 있는 자료형!  
`[ ]`이용, `.length` 속성 이용해 배열에 담긴 요소의 개수 확인 가능  

```javascript
const names = ['Alice', 'Bella', 'Cathy']
console.log(names)
console.log(names[0]) // Alice
console.log(names[1]) // Bella
console.log(names[2]) // Cathy

// 길이
console.log(names.length) // 3

// 수정
names[1] = 'Dan'
console.log(names[1])
```

### Array Method
`push`, `pop` : 배열의 끝 요소 추가/제거  
`unshift`, `shift` : 배열의 앞 요소 추가/제거    
```javascript
const names = ['Alice', 'Bella', 'Cathy']

// pop 배열의 맨 끝 요소 제거 후 반환
console.log(names.pop()) // Cathy
console.log(names) // ['Alice', 'Bella']

// push
names.push('Dan')
console.log(names) // ['Alice', 'Bella', 'Dan']

// shift 배열의 맨 앞 요소 제거, 해당 값 반환
console.log(names.shift()) // Alice
console.log(names) // ['Bella', 'Dan']

// unshift 배열 맨 앞에 요소 추가
names.unshift('Eric')
console.log(names) // ['Eric', 'Bella', 'Dan']
```
***
### Array Helper Methods
배열 조작 쉽게 할 수 있도록 하는 특별한 메서드  
: 배열의 각 요소 순회하며 콜백함수 호출  
메서드 호출 시 인자로 콜백함수를 받음

### forEach
배열 내의 모든 요소 각각에 대해 콜백 함수 호출  
* 반환 값 X(= undefined)
* `arr.forEach(callback(item[,index[,array]]))`
  * item => 처리할 배열의 요소
  * index => 처리할 배열 요소의 인덱스(optional)
  * array => forEach를 호출한 배열(optional)
```javascript
const names = ['Alice', 'Bella', 'Cathy']

// 일반 함수 표기
names.forEach(function (name) { 
  console.log(name)
})
// 화살표 함수 표기
names.forEach((name) => {
  console.log(name)
})
// 활용
names.forEach(function (name, index, array) {
  console.log(`${name} / ${index} / ${array}`)
})  // Alice / 0 / Alice,Bella,Cathy
    // Bella / 1 / Alice,Bella,Cathy
    // Cathy / 2 / Alice,Bella,Cathy
```
***
### map
배열 내의 모든 요소 각각에 대해 콜백 함수 호출
* 함수 호출 결과를 모아 **새로운 배열 반환**
* `arr.map(callback(item[,index[,array]]))`
```javascript
// 1. for...of 와 비교
const persons = [
  { name: 'Alice', age: 20 },
  { name: 'Bella', age: 21 }
]

// 1.1 for...of
let result1 = []
for (const person of persons) { 
  result1.push(person.name)
}
console.log(result1) // ['Alice', 'Bella']

// 1.2 map
const result2 = persons.map(function (person) {
  return person.name
})
console.log(result2) // ['Alice', 'Bella']


// 2. 화살표 함수 표기
const names = ['Alice', 'Bella', 'Cathy']
const result3 = names.map(function (name) {
  return name.length
})

const result4 = names.map((name) => {
  return name.length
})
console.log(result3) // [5, 5, 5]
console.log(result4) // [5, 5, 5]

// 3. 커스텀 콜백 함수
const numbers = [1, 2, 3]
const doubleNumber = numbers.map((number) => {
  return number * 2
})
console.log(doubleNumber) // [2, 4, 6]
```
***
### 배열 순회 종합
- `for loop`
  - 배열의 인덱스 활용 -> 각 요소에 접근  
  - break, continue 이용 가능
- `for ... of`
  - 배열 요소에 바로 접근  
  * break, continue 이용 가능
- `forEach` 
  * 간결, 가독성 good  
  * callback 함수 활용해 각 요소 조작 용이  
  * break, continue 이용 X
```javascript
// 배열 순회 종합
const names = ['Alice', 'Bella', 'Cathy']

// for loop
for (let idx = 0; idx < names.length; idx++) {
  console.log(names[idx])
}

// for...of
for (const name of names) {
  console.log(name)
}

// forEach
names.forEach((name) => {
  console.log(name)
})
```
### 기타
* `filter` : 콜백 함수의 반환 값이 참인 요소들을 모아 새로운 배열 반환
* `find` : 콜백 함수의 반환 값이 참이면 해당요소 반환
* `some` : 배열의 요소 중 하나라도 콜백함수 통과 -> true
* `every` : 모든 배열의 요소거 콜백함수 통과 -> true, 아니면 false & 배열 순회 중지
* 배열 with. 전개 구문 = 배열의 복사
```javascript
// 배열 복사 (with 전개 구문)
let parts = ['어깨', '무릎']
let lyrics = ['머리', ...parts, '발']

console.log(lyrics) // [ '머리', '어깨', '무릎', '발' ]
```
***
## Callback Function 콜백 함수
다른 함수에 인자로 전달되는 함수  
```javascript
// 바로 선언
const numbers1 = [1, 2, 3]
numbers1.forEach(function(number){
  console.log(number)
})

// callback함수를 따로 명명 후 호출
const numbers2 = [1, 2, 3]
const callBackFunc = function(number) {
  console.log(number)
}
numbers2.forEach(callBackFunc)
```
***
### 참고_콜백 함수, forEach, 배열의 object속성
#### callback 함수의 목적
1. 함수의 재사용성  
  함수를 호출하는 코드에서 콜백함수의 동작을 자유롭게 변경 가능  
2. 비동기적 처리  
  : `setTimeout()` : 콜백함수를 인자로 받아 일정시간 후에 실행

#### forEach에서 break 사용
`some`, `every`라는 키워드를 활용해 순회를 중단하는 break의 기능 수행해보기
```javascript
const array = [1, 2, 3, 4, 5]
// some
// - 배열의 요소 중 적어도 하나라도 콜백 함수를 통과하는지 테스트
// - 콜백 함수가 배열 요소 적어도 하나라도 참이면 true를 반환하고 순회 중지
// - 그렇지 않으면 false를 반환
const isEvenNumber = array.some(function (element) {
  return element % 2 == 0
})
console.log(isEvenNumber) // true
// every
// - 배열의 모든 요소가 콜백 함수를 통과하는지 테스트
// - 콜백 함수가 모든 배열 요소에 대해 참이면 true를 반환
// - 그렇지 않으면 false를 반환하고 순회 중지
const isAllEvenNumber = array.every(function (element) {
  return element % 2 == 0
})
console.log(isAllEvenNumber) // false

const names = ['Alice', 'Bella', 'Cathy']
// 1. some
// - 콜백 함수가 true를 반환하면 some 메서드는 즉시 중단하고 true를 반환
names.some(function (name) {
  console.log(name) // Alice, Bella
  if (name === 'Bella') {
    return true
  }
  return false
})
// 2. every
// - 콜백 함수가 false를 반환하면 every 메서드는 즉시 중단하고 false를 반환
names.every(function (name) {
  console.log(name) // Alice, Bella
  if (name === 'Bella') {
    return false
  }
  return true
})
```
#### 배열의 objects 속성
배열 역시 key, value를 가지는 참조 타입의 객체
* 배열의 요소를 `[]`이용해 접근 -> 객체와 동일
* 숫자(index)로 접근 -> 순서가 생기게 됨
  
***