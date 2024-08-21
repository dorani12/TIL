## WEB
웹 Day03 Bootstrap  
*[bootstrap 공식문서](https://getbootstrap.com/docs/5.3/components/card/)를 늘 참고하며 작성*

---
## Bootstrap
CSS Toolkit : 프론트엔드 프레임워크  
: 반응형 웹 디자인 구현, 커스터마이징, 크로스 브라우징 이슈 지원

### CDN : content delievery network  
지리적 제약 없이 콘텐츠 전송 기술(중간 기지) => 콘텐츠 로딩 속도 감소, 웹페이지 로딩 쉽도록 함  
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
```
### 기본 사용법
class명으로 활용(이미 규칙이 적용됨 => 스타일, 레이아웃 정해짐)  
ex) `mt-5` = margin-top, 5 size(= 3 rem, 48px)  

{property}{sides}-{size}  
- | m | margin |
    |---|---|
    | p | padding |


-    |t |  b | s | e | y | x | ' '(blank) |
     |---|---|---|---|---|---|---|
     | top | bottom | left | right |  top, bottom |  left, right |  모두 다 | 

- |0 |  1 | 2 | 3 | 4 | 5 | auto |
     |---|---|---|---|---|---|---|
     | 0 rem | 0.25rem | 0.5rem | 1rem | 1.5rem | 3rem | auto |
     | 0 px | 4px | 8px | 16px | 24px | 48px | auto |

cf) .5rem = 0.5rem

---
### Reset CSS
모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트  
user agent stylesheet: 브라우저 별로 각자의 기본 스타일 양식이 있음  
-> 모든 브라우저에 맞춰 개발하기 힘들기 때문에 reset css가 필요함  

대표적인 방법  
Normalize CSS : 웹 표준 기준으로 차이가 나는 브라우저를 수정  
-> bootstrap에서는 `bootstrap-reboot.css`파일로 하고 있음

---
### Typography 
[bootstrap 공식문서](https://getbootstrap.com/docs/5.3/content/typography/)  
제목, 본문 텍스트, 목록..
```html
<!-- h1~6 : 기본 속성과 동일  -->
<p class="h1">h1. Bootstrap heading</p>
<!-- display-# : h보다 더 크게 보이는 속성 -->
<h1 class="display-1">Display 1</h1>
<!-- <mark> 하이라이트, <del> 취소선, <u> 밑줄, <small> 작은글자,<strong>강조, <em> 기울임체  -->
<p>You can use the mark tag to <mark>highlight</mark> text.</p>
<p><del>This line of text is meant to be treated as deleted text.</del></p>
<p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
```
---
### Colors
[bootstrap utilities/colors](https://getbootstrap.com/docs/5.3/utilities/colors/)  

ex) `class="box border border-5 border-dark bg-info"`만으로 색상, 테두리의 굵기, 박스의 크기 등을 지정 가능
```html
<!-- primary 파랑, success 초록, danger 빨강....  -->
<p class="text-primary">.text-primary</p>
<p class="text-success">.text-success</p>
<p class="text-danger">.text-danger</p>
<!-- 해당요소의 특성 뒤에 -하고 색상이름, 배경색은 bg- -->
<p class="text-warning bg-dark">.text-warning</p>
<!-- -opacity-50 투명도 조절 -->
<div class="text-primary text-opacity-50">This is 50% opacity primary text</div>
```
---
### Component
[bootstrap component](https://getbootstrap.com/docs/5.3/components/card/)  
UI관련 요소: navigation 바, button, badge, card, alert....  
-> 일관된 디자인을 활용해 웹사이트 구성요소 구축에 유용  

```html
<!-- alert -->
<div class="alert alert-primary" role="alert">
A simple primary alert—check it out!
</div>
<!-- badge -->
<span class="badge text-bg-light">Light</span>
<!-- button -->
<button type="button" class="btn btn-info">Info</button>
```

- nav bar: 네비게이션 바
    ```html
  <!-- navbar -->
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Dropdown
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" aria-disabled="true">Disabled</a>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
    ```
- **card**
    ```html
    <!-- Cards -->
    <div class="card" style="width: 18rem;">
        <img src="images/01.jpg" class="card-img-top" alt="...">
        <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
    </div>
    ```
- carousel(회전목마, 사진 여러 슬라이드로 보기)  
    :js코드의 버튼 부분이 같은 이름 -> carousel이 여러개일때, 하나에만 적용 -> 변수명(id) 변경 필요
    ```html
        <!-- carousel 2 -->
    <!-- carousel 속성 값과 data-bs-target이 일치하는지 확인 -->
    <div id="carouselExampleIndicators2" class="carousel slide">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="images/04.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="images/05.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="images/06.jpg" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators2" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators2" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
  ```
- modal(팝업 알림창)  
  : modal의 동작부분(버튼)과 작동하는 부분(모달의 내용)이 붙어있을 필요는 없음, modal은 modal끼리 묶어놓기(배경에 위치하지 않도록)
  ```html
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
    Launch demo modal
    </button>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            ...
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Save changes</button>
        </div>
        </div>
    </div>
    </div>
  ```

***
## 코드 작성 TIP
### Semantic Web
: 시각적인 것에 더해 요소가 가진 목적과 역할, 의미가 담기도록!  
: 의미론적으로 구조화시키기 (검색엔진, 개발자의 이해도 상승)  
ex) header, nav, main, article, section, aside, footer = 사실상 div와 기능은 같지만 시각화, 구조화  

### CSS 방법론
for. 효율성, 유지보수 용이  
**OOCSS**(object oriented): 객체지향적  
- 구조와 스킨 분리  
ex) 버튼의 공통 구조 정의 + 배경색, 폰트는 개별 요소별로 입히기

- 컨테이너와 콘텐츠 분리  
: 객체를 둘러싸는 컨테이너에 스타일 적용  
ex) 폰트 크기를 담당하는 컨테이너, 색이나 다른걸 담당하는 다른 요소 콘텐츠  

***
