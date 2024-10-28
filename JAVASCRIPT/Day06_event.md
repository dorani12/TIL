## JS:Javascript_Event 이벤트 제어
자바스크립트 Day06
***
## Event 신호, 사건
화면 스크롤, 버튼 클릭 -> 팝업 창 출력, 마우스 커서로 드래그 앤 드롭, 키보드 입력 등등
### `event` object
DOM에서 event 발생시 생성되는 객체  
ex) mouse, input, keyboard, touach ...  
=> event 발생시 연결된 event handler로 연결
### event handler `.addEventListener()`
: 특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수 호출  
`EventTarget(DOM요소).addEventListener(type(수신할 이벤트), handler(콜백 함수))`  
* type : 수신할 이벤트 이름, 문자열로 작성
* handler : 발생한 이벤트 객체를 수신하는 콜백 함수(반환값 없음), event 객체를 매개변수로 받아옴

예제
```javascript
// 1. 버튼 선택
const btn = document.querySelector('#btn')
// 2. 콜백 함수
const detectClick = function (event) {
  console.log(event)   // 이벤트가 발생한 버튼의 정보 출력, PointerEvent
  console.log(event.currentTarget)    // <button id="btn">버튼</button> 출력
  console.log(this)                   // <button id="btn">버튼</button> 출력
}
// 3. 버튼에 이벤트 핸들러를 부착
btn.addEventListener('click', detectClick)
```
* handler 내부의 this는 이벤트 리스너에 연결된 `currentTarget` 가리킴
* event 발생시 event 객체가 생성되어 첫번째 인자로 전달

### 버블링 bubbling
자식요소의 이벤트 동작 -> 부모 요소의 핸들러까지 동작
- 가장 최상단 조상 요소, document를 만날 때까지 모든 핸들러 동작
- 요소의 공통 조상에 이벤트 핸들로 1개 할당 -> 여러 버튼 요소에서 발생하는 이벤트를 한번에 다루고, `event.target`을 이용해 실제 이벤트가 발생한 요소 확인
- `this`는 누구?
  * `.currentTarget` : '현재' 요소 = `this`, 항상 이벤트 핸들러가 연결된 요소만을 참조
  * `.target` : 실제 이벤트가 시작된, 가장 안쪽의 요소를 참조, 버블링이 진행되어도 값 변경 X

#### 캡처링 capturing
이벤트가 하위 요소로 전파 <-> 버블링
***
### Evnet Handler 예제
#### 버튼
```javascript
<div>
  <button>버튼1</button>
  <button>버튼2</button>
  <button>버튼3</button>
  <button>버튼4</button>
  <button>버튼5</button>
</div>
<script>
  const divTag = document.querySelector('div')

  const clickHandler = function (event) {
    console.log(event.target)
  }

  divTag.addEventListener('click', clickHandler)
</script>
```
#### 클릭 횟수 표기
```html
<body>
  <button id="btn">버튼</button>
  <p>클릭횟수 : <span id="counter">0</span></p>
```
```javascript
  <script>
    // 1. 초기 값
    let countNumber = 0
    // 2. 버튼 요소 선택
    const btn = document.querySelector('#btn')
    // 3. 이벤트 핸들러의 콜백 함수
    const clickHandler = function(event) {
      countNumber += 1
      const spanTag = document.querySelector('#counter')
      spanTag.textContent = countNumber
    }
    // 4. 선택한 버튼에 이벤트 핸들러 부착
    btn.addEventListener('click', clickHandler)
</script>
</body>
```
#### 입력 값 표기
```javascript
<input type="text" id="text-input">
<p></p>

<script>
  const inputTag = document.querySelector('#text-input') // input 요소 선택 -> 이벤트 발생 지점
  const pTag = document.querySelector('p') // p요소 선택
  const inputHandler = function (event) {
    // console.log(event)  // 콜백 함수 -> 모든 입력 값이 log에 저장됨
    // console.log(event.currentTarget.value)
    const inputData = this.value

    pTag.textContent = inputData  // -> 선택한 p요소의 텍스트 콘텐츠에 할당
  }
  
  inputTag.addEventListener('input', inputHandler) // 선택한 input 요소에 이벤트 핸들러 부착
</script>
```
-> currentTarget은 이벤트가 처리되는 동안에만 사용 가능  
-> `console.log(event.currentTarget)`으로 콘솔에서 값 확인  

#### CSS추가
```javascript
  <style>
    .blue {
      color: blue;
    }
  </style>
</head>

<body>
  <h1></h1>
  <button id="btn">클릭</button>
  <input type="text" id="text-input">

  <script>
    // input 부분 구현 -> input & h1 요소 선택
    const inputTag =  document.querySelector('#text-input')
    const h1Tag = document.querySelector('h1')
    // 콜백 함수 구현
    const inputHandler = function (event) {
      const inputData = event.currentTarget.value  // 사용자 입력 데이터 추출
      h1Tag.textContent = inputData   // h1 요소의 콘텐츠로 할당
    }
    inputTag.addEventListener('input', inputHandler)

    // 2. 버튼 기능 구현
    const btn = document.querySelector('#btn')    // 버튼 요소 선택
    // 콜백 함수
    const clickHandler = function (event) {
      // 방법 1
      h1Tag.classList.add('blue')   // h1요소의 클래스 목록에 blue 요소 추가
      // 방법 2
      // h1Tag.classList.toggle('blue') // 토글 방식
    }
    btn.addEventListener('click', clickHandler) // 버튼에 이벤트 핸들러 부착
  </script>
</body>
```
#### ToDoList 구현
```javascript
<body>
  <input type="text" class="input-text">
  <button id="btn">+</button>
  <ul></ul>

  <script>
    // 1. 필요한 요소 선택
    const inputTag = document.querySelector('.input-text')  // class로 작성됨
    const btn = document.querySelector('#btn')              // id로 작성
    const ulTag = document.querySelector('ul')

    // 2. 콜백 함수
    const addTodo = function (event) {
      // const inputData = event.currentTarget.value
      const inputData = inputTag.value  // 사용자 입력 데이터 저장
      if (inputData.trim()) {
        const liTag = document.createElement('li')  // li 태그 생성
        // li tag의 텍스트 콘텐츠로 사용자 입력 값 저장 
        liTag.textContent = inputData
        // console.log(liTag)
        ulTag.appendChild(liTag)

        // todo를 입력한 후에 input data 초기화
        inputTag.value = ''  
      } else {
        alert('todo를 입력해주세요.')
      }
    }

    // 3. 버튼에 이벤트 핸들러 부착
    btn.addEventListener('click', addTodo)
  </script>
</body>
```
#### 로또 번호 생성기
`lodash` : 모듈화, 성능 및 추가 기능 제공, JavaScript 유틸리티 라이브러리에 해당  
array, object 등의 자료구조 다루기 유용 [lodash 공식 문서](https://lodash.com/)

```javascript
<body>
  <h1>로또 추천 번호</h1>
  <button id="btn">행운 번호 받기</button>
  <div></div>


  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    // 1. 필요한 모든 요소 선택
    const btn = document.querySelector('#btn')
    const divTag = document.querySelector('div')

    // 2. 로또 번호 생성 by. lodash
    const getNumbers = function () {
      const numbers = _.range(1, 46)  // 1부터 45까지의 배열 생성

      const sixNumbers = _.sampleSize(numbers, 6) // 45개의 요소 중 랜덤으로 6개 추출
      return sixNumbers
    }

    // 3. 로또 번호를 화면에 출력 -> 이벤트 핸들러의 콜백 함수
    const getLottery = function (event) {
      const numbers = getNumbers()

      const ulTag = document.createElement('ul')

      numbers.forEach((number)=> {   // 추출한 6개의 숫자를 모두 반복하면서 li 태그 생성
        const liTag = document.createElement('li')
        liTag.textContent = number
        ulTag.appendChild(liTag)  // li 태그를 부모 ul 태그의 자식으로 추가
      })
      divTag.appendChild(ulTag)   // 완성된 ul 태그를 div 태그의 자식으로 추가
    }

    btn.addEventListener('click', getLottery)   // 버튼에 이벤트 핸들러 부착
  </script>
</body>
```
***
### 이벤트 동작 취소
`.preventDefault()` : 기존의 동작 실행 X -> 새로 고침이나 페이지 이동 방지  
```javascript
const h1Tag = document.querySelector('h1')
h1Tag.addEventListener('copy', function (event) {
  console.log(event)
  event.preventDefault()
  alert('복사 할 수 없습니다.')
})
```
***
### 참고_this와 화살표 함수
addEventListener 내에서 화살표 함수는 자신만의 this를 생성 X  
-> 상위 scope의 this를 사용 | 대부분 window를 가리킴
***