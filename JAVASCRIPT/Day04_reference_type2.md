## JS:Javascript_참조 자료형 2_Object, this
자바스크립트 Day04
***
## Object 객체
key로 구분된 데이터 집합(data collection)을 저장
### 객체 구조
- `{ }` 중괄호 이용
- key : value 쌍으로 구성된 property를 작성
- key는 string만, value는 모든 자료형 가능
- 객체 요소에 접근 방법  
  1. `객체명.key 값` 
  2. `객체명['key']`(key 값에 띄어쓰기가 있는 경우)
- `in`연산자 -> 해당 key 값이 객체 내에 존재?! true | false
```javascript
const user = {
  name: 'Alice',
  'key with space' : true,
  greeting : function () {
    return 'hello'
  }
}

# 조회
console.log(user.name) // Alice
console.log(user['key with space']) // true

# 추가 및 수정
user.address = 'korea'
console.log(user) // {...... address: 'korea', greeting : f}
user.name = 'Bella'

# 삭제
delete user.name

console.log('greeting' in user) // true
console.log('country' in user) // false
```

### Method
`object.method()`형식 -> 객체 내에서 '행동'을 정의  
`this`라는 키워드를 통해(객체 자체를 가리킴), 객체 내의 값에 접근 가능  
```javascript
console.log(user.greeting()) // hello

const person = {
  name: 'Alice',
  greeting: function() {
    return `Hello my name is ${this.name}`
  },
}

console.log(person.greeting()) // Hello my name is Alice
```
***
### `this` key word
단순 호출 -> 전역 객체를 가리킴(`window`)  
메서드 호출 -> 메서드를 호출한 객체를 가리킴
```javascript
const myFunc = function () {
  return this
}
cosole.log(myFunc()) // window

const myObj = {
  data: 1,
  myFunc: function () {
    return this
  }
}
console.log(myObj.myFunc()) // myObj
```

### 중첩된 함수 내에서의 `this`  
```javascript
const myObj2 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach(function (number) {
      console.log(this) // window
    })
  }
}
console.log(myObj2.myFunc()) 

const myObj3 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach((number) => {
      console.log(this) // myObj3
    })
  }
}
console.log(myObj3.myFunc()) 
```
- 화살표 함수 `=>`를 활용하는 경우
  - 자신만의 this를 가지지 않음   
  - 외부함수인 myFunc의 this 값을 가져오게 됨

- callback함수

=> javascript의 경우 !동적 할당!  
1. 함수가 호출되기 전까지 값 할당 X
2. 함수 호출 시 this를 암묵적으로 전달받음
3. 장점 : method 한개로 여러 객체에서 재사용 가능

cf) python, java의 경우 선언 시 값이 정해짐
***
### 추가 object 문법
1. 단축 속성  
: key 이름과 값으로 쓰이는 변수의 이름이 같은 경우  
```javascript
<script>
  const name = 'Alice'
  const age = 30

  const user1 = {
    name: name,
    age: age,
  }

  const user2 = {
    name,
    age,
  }
</script>
```
2. 단축 메서드 -> function 생략, method 선언 시  
```javascript
const myObj1 = {
  myFunc: function () {
    return 'Hello'
  }
}

const myObj2 = {
  myFunc() {
    return 'Hello'
  }
}
```
3. 계산된 속성_computed property name  
key가 `[]`에 둘러싸여 있음 => 변수 값 사용 가능  
```javascript
const product = prompt('물건 이름을 입력해주세요')
const prefix = 'my'
const suffix = 'property'

const bag = {
  [product]: 5,
  [prefix+suffix]: 'value',
}

console.log(bag) // {연필: 5, myproperty: 'value'}
```
4. **구조 분해 할당** destructing assignment    
: 배열 또는 객체를 분해 -> 객체 속성을 변수에 쉽게 할당 가능  

```javascript
const userInfo = {
  firstName: 'Alice',
  userId: 'alice123',
  email: 'alice123@gmail.com'
}


// 구조 분해 할당 활용 - "함수 매개변수"
function printInfo({ name, age, city }) {
  console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
}

const person = {
  name: 'Bob',
  age: 35,
  city: 'London',
}

// 함수 호출 시 객체를 구조 분해하여 함수의 매개변수로 전달
function printInfo({name, age, city}) {
  console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
}
printInfo(person) // 이름: Bob, 나이: 35, 도시: London
```
5. 전개 구문 - "객체 복사"  
객체 내부에서 객체 전개 -> 얕은 복사  
```javascript
const obj = { b: 2, c: 3, d: 4 }
const newObj = {a: 1, ...obj, e: 5}
console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}
```
6. 유용한 객체 메서드  
- Object.keys()
- Object.values()
```javascript
const profile = {
  name: 'Alice',
  age: 30
}

console.log(Object.keys(profile)) // ['name', 'age']
console.log(Object.values(profile)) // ['Alice', 30]
```
7. Optional chaining (`?.`)  
속성이 없는 중첩 객체를 에러 없이 접근  
= 참조 대상이 null | undefined라면 평가 대신 undefined 반환  
```javascript
  <script>
    const user = {
      name: 'Alice',
      greeting: function () {
        return 'hello'
      }
    }

    console.log(user.address.street) // Uncaught TypeError: Cannot read properties of undefined (reading 'street')
    console.log(user.address?.street) // undefined

    console.log(user.nonMethod()) // Uncaught TypeError: user.nonMethod is not a function
    console.log(user.nonMethod?.()) // undefined

    // 아래 예시 코드 논리상 user는 반드시 있어야 하지만 address는 필수 값이 아님
    // user에 값을 할당하지 않은 문제가 있을 때 바로 알아낼 수 있어야 하기 때문
    console.log(user.address && user.address.street) // undefined
    console.log()

    // Bad
    user?.address?.street // 존재하지 않아도 괜찮은 대상에만 사용

    // Good
    user.address?.street
  </script>
```  
cf(optional chaining 사용 대신 `user.address && user.address.street`와 같이 `&&`연산자 사용)  
-> 참조가 누락될 가능성이 있는 경우, 어떤 속성이 필요한지 보증이 확실하지 않은 경우 편리

***
### Json
- JavaScript Object Notation
- key-value 형태로 이루어진 자료 표기법  
- Json은 형식이 있는 문자열 -> javascript에서 사용하기 위해 Object 자료형으로 변경 필요
```javascript
const jsObject = {
  coffee: 'Americano',
  iceCream: 'Cookie and cream'
}

// Object -> JSON
const objToJson = JSON.stringify(jsObject)
console.log(objToJson)  // {"coffee":"Americano","iceCream":"Cookie and cream"}
console.log(typeof objToJson)  // string

// JSON -> Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and cream' }
console.log(typeof jsonToObj)  // object
```
***
### 참고_Class
Class : 객체를 생성하기 위한 템플릿 -> 객체의 속성, 메서드를 정의할 수 있도록 함
```javascript
class MyClass { // 클래스 선언 keyword
  constructor() { ... } // 생성자에 해당
  method1() { ... }
  ...
}
```
- `new`연산자 : 클래스나 생성자 함수를 활용 -> 새로운 객체 생성  
  - `const instance = new ClassName(arg1, arg2)` 
  - => `new`연산자에 의해 클래스의 생성자함수는 자동 호출
- `new` 없이 클래스 호출 시 TypeError 발생
***