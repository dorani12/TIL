## Vue.js_vue 문법 1
뷰 Day02
***
### Template Syntax
DOM을 기본 구성 요소 인스턴스 데이터에 선언적으로 바인딩(vue instance와 DOM연결) 할 수 있는 HTML기반 템플릿 구문(-> 확장된 문법 제공) 사용

1. Text Interpolation  
`<h1>{{message}}</h1> `  
- 데이터 바인딩의 기본적인 형태
- 콧수염 구문 `{{}}`
- 해당 구성 요소 인스턴스의 msg 속성 값으로 대체, 변경시 업데이트  

2. Raw HTML  
`<div v-html>='rawHTML'></div>`  
`const rawHTML = ref('<span style="color:red">color = red</span>)`
3. Attribute Bindings  
`<div v-bind:id="dynamicId">attribute bindings</div>`  
`const dynamicId = ref('my-id')`  
-> 콧수염 구문의 경우 HTML에서 사용 불가 -> v-bind 사용  
HTML의 id 속성 값을 vue의 dynamicId 속성과 동기화 되도록 함
4. JavaScript Expressions
- vue는 모든 데이터 바인딩 내에서 JS 표현식 기능 지원
- 콧수염 구문 내부, directive 속성 값 내에서!
- 조건문은 삼항연산자로 나타냄, 선언식은 불가능  
    ```javascript
    <p>{{ number + 1 }}</p>
    <p>{{ ok ? 'YES' : 'NO' }}</p>
    <p>{{ msg.split('').reverse().join('') }}</p>
    <div v-bind:id="`list-${id}`"></div>
    ```
***
## Directive `v-`
* `v-for`, `v-on`을 제외하고, directive의 속성 값은 단일 javascript 표현식이여야 함  
  * ex) `<p v-if='seen'>Hi there</p>` 에서 'seen'이 속성 값  
* 표현식의 값 변경 -> DOM에 반응적으로 업데이트 적용
### Directive 구조
`v-on:submit.prevent='onSubmit'`  
이름, argument, modifiers, value  
1. Directive arguments : `:`뒤에 표시되는 인자  
  ex) `<a v-bind:href="myUrl">Link</a>`  
  : `<a>`의 href 속성 값을 myURL 값에 바인딩 하도록 함    
    `<button v-on:click="doSomething">button</button>` : 수신할 이벤트의 이름을 작성  
2. Directive modifiers  
  : directive가 특별한 방식으로 바인딩 되어야 함을 나타냄  
  ex) .prevent는 발생한 이벤트에서 event.preventDefault()를 호출하도록 v-on에 지시함  
```javascript
<div id="app">
  <p>Hi there</p>

  <a v-bind:href="myUrl">Link</a>

  <button v-on:click="doSomething">button</button>

  <form v-on:submit.prevent="onSubmit">
    <input type="submit">
  </form>
</div>

<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  const { createApp, ref } = Vue

  const app = createApp({
    setup() {
      const seen = ref(true)
      const myUrl = 'https://www.google.co.kr/'
      const doSomething = function () {
        console.log('button clicked')
      }
      const onSubmit = function () {
        console.log('form submitted')
      }
      return {
        seen,
        myUrl,
        doSomething,
        onSubmit
      }
    }
  })

  app.mount('#app')
</script>
```
## Dynamically Data binding => v-bind
하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩  
### Attribute bindings 속성 바인딩
HTML의 속성 값을 Vue의 상태 속성 값과 동기화 되도록 함   
`v-bind` 를 `:`로 표현하기도 함  
### Dynamic attribute name 동적 인자 이름
`[ ]`로 감싸서 directive argument에 javascript 표현식 사용  
* 표현식에 따라 동적으로 평가된 값이 최종 argument  
* 대괄호 내의 이름 -> 무조건 소문자!! : 브라우저가 속성 값을 소문자로 강제 변환함

```javascript
  <div id="app">
    <img v-bind:src="imageSrc">
    <a v-bind:href="myUrl">Move to url</a>
    <p :[dynamicattr]='dynamicvalue'>Dynamic Attr</p>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const imageSrc = ref('https://picsum.photos/200')
        const myUrl = ref('https://www.google.co.kr/')
        const dynamicattr = ref('title')
        const dynamicValue = ref('Hello Vue.js')
        return {
          imageSrc,
          myUrl,
          dynamicattr,
          dynamicValue
        }
      }
    })

    app.mount('#app')
  </script>
```
***
### Class, Style Bindings
html의 속성에 해당하므로 v-bind를 사용하여 동적으로 문자열 값 할당 가능  
* vue에서는 class, style을 객체, 배열을 활용하여 작성하도록 함
* 객체(배열로 선언도 가능)를 :class에 전달하여 클래스를 동적으로 전환

```javascript
  <style>
    .active {
      color: crimson;
    }

    .text-primary {
      color: blue;
    }
  </style>
</head>

<body>
  <div id="app">

    <!-- Binding to Objects -->
    <div>Text</div>
    <div class="static">Text</div>
    <div :class="{active:isActive}">Text</div>
    <div class="static" :class="{active:isActive, 'text-primary':hasInfo}">Text</div>
    <div class="static" :class="classObj">Text</div>

    <!-- Binding to Arrays -->
    <div :class="[activeClass, infoClass]">Text</div>
    <div :class="[{active:isActive}, infoClass]">Text</div>

  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const isActive = ref(true)
        const hasInfo = ref(true)
        const classObj = ref({
          active : isActive,
          'text-primary' : hasInfo
        })
        const activeClass = ref('active')
        const infoClass = ref('text-primary')
        return { isActive, hasInfo, classObj, activeClass, infoClass }
      }
    })

    app.mount('#app')
  </script>
</body>
```

```javascript
<body>
  <div id="app">
    <!-- Binding to Objects -->
    <div style="color: crimson; font-size: 50px;" >Text</div>
    <div :style = "{color : activeColor, fontSize : fontSize + 'px'}">Text</div>
    <div :style = "{'font-size':fontSize+'px', 'color' : activeColor}">Text</div>

    <!-- Binding to Arrays -->
    <div :style="styleObj">Text</div>
    <div :style="[styleObj, styleObj2]">Text</div>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const activeColor = ref('crimson')
        const fontSize = ref(50)
        const styleObj = ref({
          color: activeColor,
          fontSize : fontSize.value + 'px'  // .value 객체의 값에 접근!!
        })
        const styleObj2 = ref({
          color : 'blue',
          border: '1px solid black'
        })
        return { activeColor, fontSize, styleObj, styleObj2 }
      }
    })

    app.mount('#app')
  </script>
</body>
```
***
## Evnet-Handling : v-on
DOM 요소에 이벤트 리스너를 연결 및 수신  
* `v-on:submit.prevent='onSubmit'`  
  이름, argument, modifiers, value   
* ex) `v-on:event='handler'` -> inline handler, method handler  
* `@event='handler'`도 같은 의미
* `$event` 변수와 같이 global 변수 사용 가능
```javascript
<div id="app">
  <!-- Inline Handlers -->
  <button @click="count++">Add 1</button>  
  <p>Count: {{ count}}</p>

  <!-- Method Handlers (권장 방식, 유지보수 용이)-->
  <button @click="increase">Add 2</button>
  
  <!-- Calling Methods in Inline Handlers -->
  <button @click="greeting('hello')">Say hello</button>
  <button @click="greeting('bye')">Say bye</button>
  
  <!-- Accessing Event Argument in Inline Handlers -->
  <button @click="warning('경고입니다', $event)">Submit</button>
  
  <!-- event modifiers -->
  <button @click="myFunc">Hello</button>
</div>
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  const { createApp, ref } = Vue

  const app = createApp({
    setup() {
      const count = ref(0)
      const increase = function() {
        count.value += 1
      }
      const greeting = function(message) {    // message라는 인자를 받는 method
        console.log(message)
      }
      const warning = function(message, event) {
        console.log(message)
        console.log(event)                // $event라는 값으로 받아올 수 있음
      }
      const name = ref('Alice')
      const myFunc = function(event) {
        console.log(event)
        console.log(event.currentTarget)
        console.log(`Hello ${name.value}!`) // back tic `으로 작성!
      }
      return { count, increase, greeting, warning, name, myFunc }
    }
  })

  app.mount('#app')
</script>
```
***
## Evnet-Handling : Modifiers
`.stop`, `.prevent`, `.self`와 같이 이벤트 실행시 자동으로 동작하는 무언가를 멈추거나 방지하는 등의 역할  
```javascript
<!-- 제출 버튼 클릭시 새로고침 되지 않은 채로, onSubmit 메소드 실행 -->
<form @submit.prevent="onSubmit">       
  <input type='submit'>
</form>
  const onSubmit = function() {
  console.log('onSubmit')
}
```
### key modifiers
키보드 이벤트 수신 시 특정 키에 대한 modifiers  
ex) `<input @keyup.enter = 'onSubmit'>`  
    = key가 엔터인 경우에만 onSubmit 이벤트 호출  
***
## Form Input Bindings
양방향 바인딩 : form 처리 시 사용자가 input을 입력하는 값을 실시간으로 javascript가 동기화  
* 비밀번호 입력 조건이 맞는지 확인, 영어인지 한글인지 검거 등등
* v-bind, v-on 함께 사용
* v-model 사용
### 양방향 바인딩 by. v-bind, v-on
```javascript
<p>{{ inputText1 }}</p>
<input :value="inputText1" @input="onInput">
const inputText1 = ref('')
const onInput = function (event) {
  inputText1.value = event.currentTarget.value
}
```
### 양방향 바인딩 by. v-model
`<input v-model="inputText2">`로 사용자 입력데이터와 반응형 변수를 실시간 동기화 가능 
* 영어 기준 -> IME가 필요한 한국어, 중국어, 일본어의 경우 업데이트 잘안됨
### v-model 활용 input 방식
1. CheckBox : 체크 여부를 boolean으로 저장
2. Radio : 선택된 요소의 원이 채워짐
3. Select : 목록 중 선택한 값을 반환
```javascript
<body>
  <div id="app">
    <!-- single checkbox -->
    <input type="checkbox" id="checkbox" v-model="checked">
    <label for="checkbox">{{ checked }}</label>

    <!-- multiple checkbox -->
    <div>Checked names: {{ checkedNames }}</div>

    <input type="checkbox" id="alice" value="Alice" v-model="checkedNames">
    <label for="alice">Alice</label>

    <input type="checkbox" id="bella" value="Bella" v-model="checkedNames">
    <label for="bella">Bella</label>

    <!-- single select -->
    <div>Selected: {{ selected }}</div>

    <select v-model="selected">
      <option disabled value="">Please select one</option>
      <option>Alice</option>
      <option>Bella</option>
      <option>Cathy</option>
    </select>
  </div>
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const checked = ref(false)
        const checkedNames = ref([])
        const selected = ref('')
        return { checked, checkedNames, selected }
      }
    })

    app.mount('#app')
  </script>
</body>
```
***
### 참고_`$`변수, IME
#### `$`변수
* vue 인스턴스 내에서 제공되는 내부 변수  
* 사용자가 지정한 반응형 변수, 메서드와 구분하기 위함
* 주로 vue 인스턴스 내부 상태를 다룰 때 사용
#### IME : input method editor
: 비영어권 언어를 입력할 수 있도록 하는 운영체제 구성 프로그램
***