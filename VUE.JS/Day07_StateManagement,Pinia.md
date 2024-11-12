## Vue.js_State Management, Pinia
뷰 Day07
***
## State Management
상태관리 => 데이터, 반응형 상태  
단방향 데이터 흐름  
* Template => View : 상태를 선언적으로 매핑하여 시각화
* Script => State : 앱 구동에 필요한 기본 데이터, Actions : 기능, 사용자 입력에 대해 반응적으로 상태를 변경할 수 있게 정의된 동작   
* Style

### 문제 발생 
- 여러 컴포넌트가 상태를 공유할 때  
  - 여러 뷰가 동일한 상태에 종속
  - 서로 다른 뷰의 기능이 동일한 상태를 변경시킴  
- 여러 뷰가 동일한 상태에 종속
  - emit & props에서 계층구조가 깊어진 경우 -> 유지보수, 관리의 비효율성
- 서로 다른 뷰의 기능이 동일한 상태를 변경
  - 발신된 이벤트를 통해 상태의 여러 복사본을 변경 및 동기화 -> 패턴이 깨지고 유지 관리 X

### 해결
중앙 저장소 : 각 컴포넌트의 공유 상태 추출, 전역에서 참조할 수 있는 저장소 => `Pinia`
***
## `Pinia` : Vue의 공식 상태 관리 라이브러리
### 설치와 시작
1. `npm create vue@latest`
2. `√ Add Pinia for state management? ... Yes`
3. `cd vue-project` , `npm install`, `npm run dev`
=> `stores` 폴더 신규 생성  
### Pinia 구성 요소
1. Store : 중앙저장소, 모든 컴포넌트가 공유하는 상태와 기능 작성  
    ```javascript
    //stores/counter.js
    import { ref, computed } from 'vue'
    import { defineStore } from 'pinia'

    export const useCounterStore = defineStore('counter', () => {
      const count = ref(0)
      const doubleCount = computed(() => count.value * 2)
      function increment() {
        count.value++
      }

      return { count, doubleCount, increment }
    })
    ```
    defineStore( )  
      * 반환 값의 이름 -> use, store 사용하기  
      `return { count, doubleCount, increment }`로 반환 필요  
      private한 상태 속성 X, 공유 가능 데이터만 취급  
      * 첫번째 인자 -> 애플리케이션에 걸쳐 사용하는 store의 고유 Id
2. State : 데이터, 반응형 상태 = `ref( )`   
`const count = ref(0)`
3. getters : 계산된 값 = `computed( )`  
`const doubleCount = computed(() => count.value * 2)`
4. actions : 메서드 = `function( )`  
`function increment() { count.value++ }`
5. plugin  
  애플리케이션의 상태관리에 필요한 추가 기능을 제공하거나 확장하는 도구, 모듈, 별도의 패키지 설치 필요  
***
### Pinia 활용
* 컴포넌트의 깊이와 상관 X
* Store 인스턴스로 state, getters에 접근하기, state는 읽고 쓰기 가능  
```javascript
////stores/counter.js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  return { count, doubleCount, increment }
})
```
```javascript
//src/App.vue
<script setup>
//1. 중앙 저장소 가져오기
import { useCounterStore } from './stores/counter';
//2. 중앙 저장소 활용 인스턴스 생성
const store = useCounterStore( )
//3. 중앙 저장소에 상태 참조
console.log(store.count)
</script>
```
=> `template`에서 `<p>state: {{ store.count}} </p>`로 값에 접근 가능  
`<p>getters: {{ store.doubleCount}} </p>` : getters도 접근 가능  
`<button @click="store.increment()">++</button>` 모든 action에 직접 접근 및 호출 가능, state 조작, 비동기, API 호출, 다른 로직 진행 가능  
### todolist 기능 구현 실습
```javascript
//src/App.vue
<script setup>
import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'
//1. 중앙 저장소 가져오기
import { useCounterStore } from '@/stores/counter'
//2. 중앙 저장소 활용 인스턴스 생성
const store = useCounterStore()
</script>

<template>
  <div>
    <h1>Todo Project</h1>
    <h2>완료된 Todo : {{ store.doneTodosCount }}</h2>
    <TodoList />
    <TodoForm />
  </div>
</template>
```
```javascript
//stores/counter.js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  let id = 0
  const todos = ref([
    {id: id++, text: '할 일1', isDone: false},
    {id: id++, text: '할 일2', isDone: false}
  ])
  const addTodo = function(todoText) {
    todos.value.push({
      id: id++,
      text: todoText,
      isDone: false
    })
  }
  const deleteTodo = function(todoId) {
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    todos.value.splice(index, 1)
  }
  const updateTodo = function (todoId) {
    todos.value = todos.value.map((todo) => {
      if (todo.id === todoId) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }
  const doneTodosCount = computed(() => {
    const doneTodos = todos.value.filter((todo) => todo.isDone)
    return doneTodos.length
  })
  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }, {persist:true}
})
```
```javascript
//src/TodoListItem.vue
<template>
    <div>
        TodoListItem
        <span @click="store.updateTodo(todo.id)" :class="{'is-done': todo.isDone}">{{ todo.text }}</span>
        <button @click="store.deleteTodo(todo.id)">Delete</button>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
defineProps({
    todo : Object
})
</script>

<style scoped>
.is-done {
    text-decoration: line-through;
}
</style>
```
```javascript
//src/TodoList.vue
<template>
    <div>
        <TodoListItem 
            v-for="todo in store.todos"
            :key="todo.id"
            :todo="todo"
        />
    </div>
</template>

<script setup>
import TodoListItem from '@/components/TodoListItem.vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>
```
```javascript
//src/TodoForm.vue
<template>
    <div>
        <h2>TodoForm</h2>
        <form @submit.prevent="createTodo(todoText)" ref="formElem">
            <input type="text" v-model="todoText">
            <input type="submit">
        </form>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import { useCounterStore } from '@/stores/counter'
const todoText = ref('')
const store = useCounterStore()

// form 태크 선택
const formElem = ref(null)
// 중앙저장소의 addTodo 액션을 직접 호출 가능 
// but, createTodo 작성 이유는 addTodo 호출 전후로 추가 로직 작성 할 수 있기 때문
const createTodo = function(todoText) {
    store.addTodo(todoText)
    formElem.value.reset() // 초기화!
}
</script>
```
***
### Local Storage
브라우저 내에 key-value 쌍을 저장하는 웹 스토리지 객체  
* 웹 애플리케이션에서 사용자 설정, 상태정보, 캐시 데이터 등을 클라이언트 측에서 보관  
  => 사용자 경험 개선 & 웹사이트 성능 향상
* 페이지 새로고침 & 브라우저 재실행시에도 데이터 유지
* 쿠키와 다르게 네트워크 요청시 서버로 전송 X
* 여러 탭이나 창 간에 데이터 공유 가능  
### Plugin-persistedstate
웹 애플리케이션 상태를 브라우저의 local storage나 session storage에 영구적으로 저장 & 복원  
1. `npm i pinia-plugin-persistedstate` : 설치
2. `main.js`  
    ```javascript
    import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

    const app = createApp(App)
    const pinia = createPinia()

    pinia.use(piniaPluginPersistedstate)
    // app.use(createPinia())
    app.use(pinia)
    ```
3. `stores/counter.js`에서 definStore()의 세번째 인자로 객체 추가  
`return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }, {persist:true} })`
***
### 참고_Pinia 사용
#### Pinia 사용
모든 데이터를 state를 넣어서 사용하지는 않음  
공유된 상태를 관리하는데 유용, but 단순한 애플리케이션에서는 불필요  
중대형 규모 이상부터 SPA 구축시에 Pinia good  
***