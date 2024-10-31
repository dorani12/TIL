## Vue.js_frontend framework, vue 기본
뷰 Day01
***
### Frontend Development
웹사이트, 웹어플리케이션 등의 UI(사용자 인터페이스), UX(사용자 경험)를 만들고 디자인 하는것  
by. HTML, CSS, Javascript 활용 -> 사용자가 직접 상호작용 하는 부분 개발
***
### client-side framework
ex) Vue.js, React, Angular  
클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용, JS기반 프레임워크
- 단순 정보를 제공하는 웹페이지 -> 대화형 어플리케이션(음악 스트리밍, 채팅, 영상 시청 등)  
  = '웹 어플리케이션' 형태로 웹사이트가 변화함 => 동적인 대화형 어플리케이션을 개발할 필요성
- text 데이터만 처리하는게 아닌, 이미지, 영상 등 다양한 데이터를 다룸
- 동적, 반응형 : 기본 데이터를 제공, 추가적으로 업데이트(렌더링, 추가, 삭제)를 하는 도구의 필요성
- 코드 재사용성 증가 by. 모듈, 컴포넌트   

cf) 다른 프레임워크 없이 프론트엔드 개발 -> Vanilla JS

## SPA : Single Page Application
단일 페이지에서 동작하는 웹 어플리케이션
* 최초 로드시 필요한 모든 리소스 다운로드
* 페이지 갱신에 필요한 데이터만을 비동기적으로 전달 받음 -> 해당 부분 동적으로 갱신
    * AJAX 같은 기술로 비동기적으로 로드
    * 페이지 전체를 로드 X, 서버로부터 필요한 데이터를 받아와 화면에 보여주게 됨
* Javascript를 활용하여 클라이언트 측에서 동적으로 콘텐츠 생성 & 업데이트 -> CSR 방식

## CSR : Client-Side Rendering
클라이언트에서 콘텐츠를 렌더링하는 방식  
### CSR 작동 원리
1. 사용자 -> 웹사이트로 요청
2. 서버에서 최소한의 HTML과 JS파일을 클라이언트로 전송
3. 클라이언트에서 HTML과 JS파일 다운로드, DOM 업데이트 후 페이지 렌더링
4. 브라우저가 Javascript를 실행하여 동적으로 페이지 콘텐츠 생성
5. 필요한 데이터는 API를 통해 서버로부터 비동기적으로 가져옴

=> 이후 서버에서는 HTML 제공 X, 필요한 데이터만 응답

### SPA, CSR의 장단점
[장점]
1. 빠른 페이지 전환 : 전체 페이지 새로고침 없이 페이지의 일부를 다시 렌더링, 서버로 전송되는 데이터 양 최소화 -> 서버 부하 방지
2. 사용자 경험 good -> 새로고침 필요 없어 native app과 유사
3. FE와 BE의 명확한 분리 -> 대규모 애플리케이션 개발, 유지 관리 가능
    * FE : UI렌더링 및 사용자 상호 작용 처리
    * BE : 데이터 및 API 제공 담당

[단점]
1. 느린 초기 로드 속도
    * 전체 페이지를 보기 전 약간의 지연
    * JS가 다운로드, 구문 분석 전 페이지가 완전히 렌더링되진 않음
2. SEO(검색 엔진 최적화) 문제
    * 페이지를 나중에 그려나감 -> 검색에 노출되지 않을 수 있음 (아직 콘텐츠가 모두 존재하지 않음)

### SPA VS MPA, CSR VS SSR
MPA : Multi Page Application  
* 여러 개의 HTML 파일이 서버로부터 로드
* 사용자가 다른 페이지로 이동시 새로운 HTML 파일이 로드됨  

SSR : Server-side Rendering  
* 서버에서 화면 렌더링
* 모든 데이터가 담긴 HTML을 서버에서 완성 후 클라이언트에 전달
***
## Vue.js
사용자 인터페이스를 구축하기 위한 JavaScript 프레임워크  
최신 버전 = Vue 3  
[장점]  
1. 낮은 학습 곡선 : 간결, 직관적인 문법, 잘 정리된 문서
2. 확장성, 생태계 :  다양한 플러그인, 라이브러리 제공, 활성화된 커뮤니티
3. 유연성 및 성능 : 작은 규모 ~ 대규모

### Vue의 핵심기능
1. 선언적 렌더링 (Declarative Rendering)  
    - 표준 HTML을 확장하는 Vue의 템플릿 구문을 활용해 JS상태(데이터)를 기반으로 화면에 출력될 HTML을 선언적으로 작성

2. 반응성 (Reactivity)  
    - JS의 상태 변경 추적 & 변경사항 발생시 자동으로 DOM 업데이트
3. 반응형 데이터 바인딩 : 데이터 변경 시 자동 UI 업데이트
4. 컴포넌트 기반 아키텍쳐 : 재사용 가능한 UI 조각

#### Component 
재사용 가능한 코드 블록, UI 조각  
- UI를 독립적이고 재사용 가능한 일부분으로 분할, 개별적으로 다룸
- 애플리케이션은 중첩된 component 트리 형태로 구성됨
***
#### Vue 예시
```javascript
  <div id="app">
    <h1>{{message}}</h1> 
    <button v-on:click="countNumber++">
      Count is : {{ countNumber }}
    </button>
  </div>
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const message = ref('Hello vue!')
        const countNumber = ref(0)
        return {
          message,
          countNumber
        }
      }
    })

    app.mount('#app')
  </script>
```
***
## Vue Application
1. `CDN`방식 : `<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>`  
2. `NPM`설치 방식
```javascript
const { createApp } = Vue 
// 전역 Vue 객체를 불러온 뒤, 구조분해 할당 문법으로 vue객체의 createApp 함수 할당//

const app = createApp({ })
// - 새로운 Application instance 생성
// 새로운 객체(컴포넌트) 전달 -> 루트(최상위) 컴포넌트 `{}`필요
app.mount('#app')
// HTML 요소에 Vue Applicaton instance 객체를 탑재, 연결
```
- createApp()에 Vue컴포넌트가 전달됨, 컴포넌트의 상태는 setup()함수 내에서 선언 & 객체 반환!
- 반환된 객체를 템플릿에서 사용 가능 by. `{{ 값 }}`
```javascript
const app = createApp({
    setup() {
        return {
            리턴 값
        }
    }
})
```
### ref( ) : 반응형 상태 선언
- `.value`속성이 있는 ref 객체로 wrapping하여 반환하는 함수
- `ref`로 선언된 변수의 값이 변경 -> 해당 값을 사용하는 템플릿에서 자동 업데이트  
    ```javascript
    const { createApp, ref } = Vue
    const app = createApp({
        setup() {
        const message = ref('Hello vue!')
        console.log(message)  // ref 객체
        console.log(message.value) // Hello vue!
    ```
    - `.value`로 래핑된 값 확인
- template부분에서는 자동으로 언래핑됨  
    ```javascript
    <div id="app">
    <h1>{{message}}</h1> 
    ```
### Event Listeners
`v-on` directive 이용해 DOM 이벤트 수신  
-> 함수 내에서 반응형 변수를 변경 -> 구성 요소의 상태 업데이트  
```javascript
<body>
  <div id="app">
    <button v-on:click="increment">{{count}}</button>
  </div>
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const count = ref(0)
        const increment = function () {
          count.value++
        }
        return {
          count,
          increment
        }
      }
    })

    app.mount('#app')
  </script>
</body>
```
***
## Template Syntax
DOM을 기본 구성 요소 인스턴스 데이터에 선언적으로 바인딩(vue instance와 DOM연결) 할 수 있는 HTML기반 템플릿 구문(-> 확장된 문법 제공) 사용

### Text Interpolation
`<h1>{{message}}</h1> `  
- 데이터 바인딩의 기본적인 형태
- 콧수염 구문 `{{}}`
- 해당 구성 요소 인스턴스의 msg 속성 값으로 대체, 변경시 업데이트  

### Raw HTML
`<div v-html>='rawHTML'></div>`  
`const rawHTML = ref('<span style="color:red">color = red</span>)`
### Attribute Bindings
`<div v-bind:id="dynamicId">attribute bindings</div>`  
`const dynamicId = ref('my-id')`  
-> 콧수염 구문의 경우 HTML에서 사용 불가 -> v-bind 사용  
HTML의 id 속성 값을 vue의 dynamicId 속성과 동기화 되도록 함
### JavaScript Expressions
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
### 참고_ref 객체, unwrap, SEO, SSR
#### ref
의존성 추적 기반의 반응형 시스템  
vue는 렌더링 중에 사용된 모든 ref 추적 & 변경시 추적하는 구성 요소 다시 렌더링  
-> 일반 변수가 아닌 참조 자료형의 객체 타입으로 구현
#### ref 객체 unwrap
템플릿에서 unwrap은 ref가 최상위 속성인 경우에만 적용 가능
```javascript  
  <div id="app">
    <!-- unwrap 문제 상황 -->
    <p>{{ object.id + 1}}</p>

    <!-- 해결책 : ref가 최상위 속성이 되어야 함 
    const { id } = object -->
    <p>{{ id + 1 }}</p>

    <!-- 단, ref가 {{}}의 최종 평가 값인 경우는 unwrap 가능 -->
    <p>{{ object.id }}</p>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const object = {
          id: ref(0)
        }
        const { id } = object
        return {
          object,
          id
        }
      }
    })

    app.mount('#app')
  </script>
```
#### SEO : Search Engine Optimization
검색 엔진에 서비스나 제품이 효율적으로 노출되도록 개선하는 과정  
HTML에 작성된 내용이 정보의 대상
#### SSR
애플리케이션의 목적, 규모, 성능 및 SEO 요구사항에 따라 CSR, SSR을 적절히 사용  
***