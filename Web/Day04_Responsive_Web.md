## WEB
웹 Day04 Responsive Web  

---
#### Emmet, 꿀팁
```html
    <!-- emmet 보다 쉽게 작성하기 -->
    div.container
    <div class="container"></div>
    ul>li*3
    <ul>
        <li></li>
        <li></li>
        <li></li>
    </ul>
    ul>li.items$*5
    <ul>
        <li class="items1"></li>
        <li class="items2"></li>
        <li class="items3"></li>
        <li class="items4"></li>
        <li class="items5"></li>
    </ul>
    nav>ul.menu>li*5>a[href='#']{메뉴 $}
    <nav>
        <ul class="menu">
            <li><a href="#">메뉴 1</a></li>
            <li><a href="#">메뉴 2</a></li>
            <li><a href="#">메뉴 3</a></li>
            <li><a href="#">메뉴 4</a></li>
            <li><a href="#">메뉴 5</a></li>
        </ul>
    </nav>
```
+) ctrl + alt로 동시 선택 가능  
ctrl + l 로 라인 전체 선택   
이동시킬 대상 선택 후 alt 누른채로 이동  

---
## Grid System -> 반응형 웹 디자인
12개의 컬럼으로 웹페이지 레이아웃을 조정   
=> 다양한 디바이스 종류, 크기에 상관 없이 일관된 사용자 경험 제공

### Grid system 기본요소
1. container : column을 담는 공간(row 1개당 12개의 column 영역)
2. column : 실제 컨텐츠를 포함하는 부분
3. gutter: 컬럼들 사이의 여백(x축 padding, y축 margin)  
```html
  <h2 class="text-center">Basic</h2>
  <div class="container">
    <div class="row">
      <div class="box col-4">col</div>
      <div class="box col-4">col</div>
      <div class="box col-4">col</div>
    </div>
    <div class="row">
      <div class="box col-4">col-4</div>
      <div class="box col-4">col-4</div>
      <div class="box col-4">col-4</div>
    </div>
    <div class="row">
      <div class="box col-2">col-2</div>
      <div class="box col-8">col-8</div>
      <div class="box col-2">col-2</div>
    </div>
  </div>

  <hr>

  <h2 class="text-center">Nesting 중첩</h2>
  <div class="container">
    <div class="row">
      <div class="box col-4">col-4</div>
      <div class="box col-8">
        <div class="row">
          <div class="box col-6">col-6</div>
          <div class="box col-6">col-6</div>
          <div class="box col-6">col-6</div>
          <div class="box col-6">col-6</div>
        </div>
      </div>
    </div>
  </div>

  <hr>

  <h2 class="text-center">Offset 상쇄</h2>
  <div class="container">
    <div class="row">
      <div class="box col-4">col-4</div>
      <div class="box col-4 offset-4">col-4 offset-4</div>
    </div>
    <br>
    <div class="row">
      <div class="box offset-3 col-3">col-3 offset-3</div>
      <div class="box col-3 offset-3">col-3 offset-3</div>
    </div>
    <br>
    <div class="row">
      <div class="box offset-3 col-6">col-6 offset-3</div>
    </div>
  </div>

  <hr>

  <h2 class="text-center">Gutters(gx-0)</h2>
  <div class="container">
    <div class="row gx-0">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <br>

  <h2 class="text-center">Gutters(gy-5)</h2>
  <div class="container">
    <div class="row gy-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <br>

  <h2 class="text-center">Gutters(g-5)</h2>
  <div class="container g-5">
    <div class="row">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>
```
---
### 반응형 Web
bootstrap의 경우 breakpoints 6개로 구현  
-> 화면 너비에 따라 xs, sm, md, lg, xl, xxl로 분기점 제공  
(~px이상일 때, 적용)  

media Query 이용
```html
  <h2 class="text-center">Breakpoints</h2>
  <div class="container">
    <div class="row">
      <div class="box col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        col
      </div>
      <div class="box col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
        col
      </div>
      <div class="box col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        col
      </div>
      <div class="box col-12 col-sm-6 col-md-12 col-lg-3 col-xl-12">
        col
      </div>
    </div>

    <hr>

    <h2 class="text-center">Breakpoints + offset</h2>
    <div class="row g-4">
      <div class="box col-12 col-sm-4 col-md-6">
        col
      </div>
      <div class="box col-12 col-sm-4 col-md-6">
        col
      </div>
      <div class="box col-12 col-sm-4 col-md-6">
        col
      </div>
      <div class="box col-12 col-sm-4 offset-sm-4 col-md-6 offset-md-0">
        col
      </div>
    </div>
  </div>
```
```html
  <h2 class="text-center">Grid Cards</h2>
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
```
***
### UX/UI
사용자 경험 of 제품, 서비스  
-> 사람들의 마음, 생각을 이해하고 정리해서 제품에 녹여냄

User Interface  
서비스와 사용자 간의 상호작용을 가능케 하는 디자인 요소 개발  
더 쉽고, 편리하게 사용하도록 고려

***
