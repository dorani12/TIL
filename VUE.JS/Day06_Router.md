## Vue.js_vue router
뷰 Day06
***
## Routing
네트워크에서 경로를 선택하는 프로세스  
: 웹 애플리케이션에서 다른 페이지 간의 전환과 경로 관리
### SSR에서 Routing
서버측에서 수행, 사용자가 방문한 URL경로를 기반으로 응답 전송  
링크 클릭 시, 브라우저는 서버로부터 HTML 응답 수신 & 새 HTML로부터 전체 페이지 다시 로드  
### CSR에서 Routing
클라이언트 측 -> JavaScript가 새 데이터를 동적으로 가져옴, 전체 페이지를 다시 로드하진 않음  
* Routing이 없는 경우 URL을 통한 페이지의 변화 감지 X
* 페이지가 렌더링 중인 것에 대한 상태 알 수 없음 -> URL이 1개, 새로고침은 처음 페이지로 되돌아감
* 뒤로 가기 사용 불가  
=> 페이지 1개이지만 주소에 따라 여러 컴포넌트를 새로 렌더링하여 여러 페이지를 사용하는 것처럼 보이도록 함  
***
## Vue Router
Vue 공식 라우터  
`Add Vue Router for Single Page Application development? » Yes`  
* router 폴더 생성 -> 라우팅에 대한 정보 및 설정 작성, router에 URL과 컴포넌트 매핑
* views 폴더 생성 -> 기존의 components와 기능 같지만, 일반 컴포넌트와 구분을 위해 `~~View.vue` 파일로 작성
* App.vue에서 `RouterLink` 태그 생성 -> 페이지 로드 없이 URL을 변경하여 URL 생성 및 로직 처리  
* App.vue에서 `RouterView` 컴포넌트로 URL에 해당하는 컴포넌트 표시

### Basic Routing
1. `index.js`에서 라우터 설정 작성(주소, 이름, 컴포넌트)  
    ```javascript
    const router = createRouter({
    routes: [
      {
        path: '/',
        name: 'home',
        component: HomeView,
      },
    ```
2. `App.vue`에서 `RouterLick`의 to 속성으로 `index.js`에서 정의한 주소 값 사용  
  `<RouterLink to="/">Home</RouterLink>`  
  `<RouterLink to="/about">About</RouterLink>`
3. URL 클릭시 `<RouterView />`컴포넌트가 렌더링

### Named Routes
라우팅 경로에 이름 지정  
name 속성 값에 경로에 대한 이름을 지정함 by. v-bind의 `to` 속성에 props 객체로 전달  
`<RouterLink :to="{name : 'home'}">Home</RouterLink>`  
`<RouterLink :to="{name : 'about'}">About</RouterLink>`  
* 하드 코딩된 URL 사용 X
* URL 입력 시 오타 방지의 장점

### Dynamic Route Matching
URL 일부를 변수로 사용 -> 동적으로 경로 매칭  
* `UserView.vue`파일 생성
* 매개변수를 `:` 콜론으로 표기 ex) `path: '/user/:id'`
  * import UserView from '@/views/UserView.vue'
  * path, name, component 작성 
* `to` 속성에 params 전달 `params: {'id' : userId}`
* `App.vue`에서 `<RouterLink :to="{name : 'user', params: {'id' : userId} }">User</RouterLink>`
* 매개변수를 활용하기
  * `$route.params.id`를 활용 -> 사용자의 id 출력 가능
  * 대신, UserView.vue의 script에 `import {useRoute} from 'vue-router'`, `const route = useRoute()`, `const userId = ref(route.params.id)`로 작성시 template에서 `{{ userID }}` 바로 접근 가능  

```javascript
//index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/user/:id',
      name: 'user',
      component: UserView,
    },
  ],
})

export default router
```
```javascript
// App.vue
<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { ref } from 'vue' 

const userId = ref(1)

</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink :to="{name : 'home'}">Home</RouterLink>
        <RouterLink :to="{name : 'about'}">About</RouterLink>
        <RouterLink :to="{name : 'user', params: {'id' : userId} }">User</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
```
```javascript
<template>
    <div>
        <h1>UserView</h1>
        <!-- <h2>{{ $route.params.id }}번 User 페이지</h2> -->
        <h2>{{ userId }}번 User 페이지</h2>
    </div>
</template>

<script setup>
import { ref } from 'vue' 
import { useRoute } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)
</script>

<style scoped>

</style>
```
### Nested Routes 중첩된 라우팅
URL 중첩된 컴포넌트의 구조에 따라 변경되도록 함  
* children 옵션 : 배열 형태로 필요한 만큼의 중첩 관계 표현   
    ```javascript
    //index.js
    {
      path: '/user/:id',
      name: 'user',
      component: UserView,
      children: [
        { path: 'profile', name: 'user-profile', component: UserProfile},
        { path: 'posts', name: 'user-posts', component: UserPosts}
      ]
    },
    ```
* 새로 RouterLink, RouterView 작성  
    ```javascript
    <template>
    <div>
        <h1>UserView</h1>
        <RouterLink :to="{name: 'user-profile'}">Profile</RouterLink>
        <RouterLink :to="{name: 'user-posts'}">Posts</RouterLink>
        <!-- <h2>{{ $route.params.id }}번 User 페이지</h2> -->
        <h2>{{ userId }}번 User 페이지</h2>
        <hr>
        <RouterView />
    </div>
    </template>

    <script setup>
    import { ref } from 'vue' 
    import { useRoute, RouterLink, RouterView } from 'vue-router'

    const route = useRoute()
    const userId = ref(route.params.id)
    </script>

    <style scoped>

    </style>
    ```
* 컴포넌트 간 부모-자식 관계 관점이 아닌, URL내에서의 중첩된 관계를 포함하는 관점!

### Programmatic Navigation
RouterLink 대신 Javascript를 사용해 페이지 이동 : 프로그래밍 방식  
1. `router.push( )` : 다른 위치로 이동  
  * 새 항목을 history stack에 push : 사용자가 브라우저 뒤로 가기 버튼 클릭을 통해 이전 URL 이동 가능
  * RouterLink 클릭시 호출되는 내부 메서드이므로 같은 결과!

2. `router.replace( )` : 현 위치 바꾸기, history stack에 새로운 항목 push X로 다른 URL로 이동  
```javasript
//src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import UserPosts from '@/components/UserPosts.vue'
import UserProfile from '@/components/UserProfile.vue'
import LoginView from '@/views/LoginView.vue'

const isAuthenticated = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/user/:id',
      // name: 'user',
      component: UserView,
      children: [
        { path: '', name: 'user', component: UserProfile },
        { path: 'profile', name: 'user-profile', component: UserProfile},
        { path: 'posts', name: 'user-posts', component: UserPosts}
      ],
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        if (isAuthenticated === true) {
          console.log('이미 로그인 상태입니다.')
          return { name: 'home' }
        }
      }
    }
  ],
})

// router.beforeEach((to, from) => {
//   const isAuthenticated  = false

//   // 로그인이 되어있지 않고, 이동하고자하는 페이지가 login이 아니라면
//   if (!isAuthenticated && to.name !== 'login') {
//     console.log('로그인이 필요합니다.')
//     return { name: 'login' }
//   }
// })

export default router
```
```javascript
// App.vue
<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'
import HelloWorld from './components/HelloWorld.vue'

const userId = ref(1)
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink :to="{ name: 'home' }">Home</RouterLink>
        <RouterLink :to="{ name: 'about' }">About</RouterLink>
        <RouterLink :to="{ name: 'user', params: { id: userId } }">User</RouterLink>
        <RouterLink :to="{ name: 'login' }">Login</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>
```
```javascript
// UserView.vue
<template>
  <div>
    <h1>UserView</h1>
    <RouterLink :to="{ name: 'user-profile' }">Profile</RouterLink>
    <RouterLink :to="{ name: 'user-posts' }">Posts</RouterLink>
    <h2>{{ $route.params }}번 유저 프로필 페이지</h2>
    <h2>{{ $route.params.id }}번 유저 프로필 페이지</h2>
    <h2>{{ userId }}번 유저 프로필 페이지</h2>
    <button @click="goHome">홈으로!</button>
    <button @click="routeUpdate">100번 유저 페이지로!</button>

    <hr>
    <RouterView />
  </div>
</template>

<script setup>
import { useRoute, RouterLink, RouterView, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'
import { ref } from 'vue'

const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()

const goHome = function () {
  // router.push({ name: 'home' })
  router.replace({ name: 'home' })
}

onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false
  }
})

const routeUpdate = function () {
  router.push({ name: 'user', params: { id: 100 } }) 
}

onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})
</script>
```
***
## Navigation Guard
Vue router를 통해 특정 URL에 접근시, 다른 URL로 redirect하거나 취소, 내비게이션 보호  
라우트 전환 전/후 자동 실행되는 Hook  
* 종류
* Globally
  * 전역 가드, `index.js`
  * 애플리케이션 전역에서 모든 라우트 전환에 적용
  * `router.beforeEach((to, from) => { .... } return false 또는 return { name: 'About' })` : 다른 URL로 이동하기 직전에 실행  
  to : 이동할 URL정보가 담긴 Route 객체, from : 현재 URL정보가 담긴 Route 객체  
  return의 경우 현재 내비게이션 취소 & from경로로 이동 to 위치 or to 경로로 push  
* Per-route
  * 라우터 가드, 특정 라우트에만 적용, index.js의 각 routes에 작성  
  * 특정 route에 진입했을 때만 실행, 다른 URL에서 탐색해 오는 경우에만 실행  
  * `router.beforeEnter : (to, from) => { .... } return false`
* In-component 
  * 컴포넌트 가드, 컴포넌트 내에서만 적용, 각 컴포넌트의 `<script>`내부에 작성
  * `onBeforeRouteLeave( )` : 현재 라우트에서 다른 라우트로 이동 전 실행
  * `onBeforeRouteUpdate( )` : 이미 렌더링 된 컴포넌트가 같은 라우트 내에서 업데이트 전 실행, 라우트 업데이트 시 추가적인 로직 처리  
    ```javascript
    //UserView.vue
    import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'
    import { ref } from 'vue'

    export default {
      setup() {
        // `this` 업이도 beforeRouteLeave 옵션을 사용할수 있습니다.
        onBeforeRouteLeave((to, from) => {
          const answer = window.confirm(
            'Do you really want to leave? you have unsaved changes!'
          )
          // 네비게이션을 취소하고 현재 페이지에 머무를수 있습니다.
          if (!answer) return false
        })

        const userData = ref()

        // `this` 없이도 onBeforeRouteUpdate 옵션을 지정할수 있습니다.
        onBeforeRouteUpdate(async (to, from) => {
          //URL상의 쿼리나 해시가 변경되어 사용자 ID가 변경되었을때만 가져오게 한다.
          if (to.params.id !== from.params.id) {
            userData.value = await fetchUser(to.params.id)
          }
        })
      },
    }
    ```
***
### 참고_Lazy Loading Routes
#### Lazy Loading Routes
`component: ( ) => import('../views/aboutView.vue')`  
vue의 애플리케이션 첫 빌드 시 해당 컴포넌트 로드 X, 해당 경로를 처음 방문 시 컴포넌트 로드
***