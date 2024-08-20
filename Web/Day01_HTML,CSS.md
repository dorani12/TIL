## WEB
웹 Day01
HTML, CSS

---
## WEB
web site와 web application을 통해 사용자들이 정보를 검색하거나 상호작용하는 기술  
web site: 여러 개의 web page가 모여 서비스나, 정보를 제공  
Web page: HTML(구조), CSS(꾸미기), javascript(행동)를 이용해 만들어지는 web site를 구성하는 하나의 요소가 웹페이지  

## HTML 
: 웹페이지의 구조와 의미를 구성하는 **문서**
- HyperText(참조, 다른페이지로의 연결, 비선형성)
- Markup(태그 등을 활용한 문서, 데이터의 구조 명시)
- language  
(viewer는 visualStudio의 alt+B 사용| ! + tab 단축키로 기본 양식 만들어줌)  

공백, 줄바꿈 문자 인식 x  
에러 메세지 출력 x  
MDN Web Docs를 참고해서 표준 문서에 맞도록 작성하기

### 구조
태그들 간의 상하관계 o, 들여쓰기는 인식하지 않음(가시성)  
contents(내용)이 있는 경우 `</tag>` 닫는 tag필요  

- `<!DOCTYPE html>` : 이 문서는 html 문서
- `<html></html>` : 전체 페이지의 콘텐츠를 포함
- `<title></title>` : 브라우저 탭, 즐겨찾기 등에서 활용될 페이지 자체의 이름
- `<head></head>` : 문서와 관련된 설명과 설정, 식별용, 사용자에게 보이지 않음
- `<body></body>` : 사용자에게 보여질 부분, 하나의 문서엔 1개의 body 요소
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>My page</title>
    </head>
    <body>
        <p>This is my page</p>

    </body>
    </html>
    ```
---
#### attributes(속성): class  
요소들을 설정, 다양한 방식으로 동작을 조절하기 위함  
1. 속성은 요소의 이름, 속성 사이에 공백 필요
2. 하나 이상의 속성이 있는 경우 속성 사이에 공백으로 구분
3. 속성 값은 열고 닫는 따옴표로 감싸기

- `<a href="*링크의 주소 값*">하이퍼텍스트의 이름</a>` : 하이퍼 링크
- `<img src = "images/sample.png" alt = "대체 텍스트">` : 이미지   
(alt는 필수 아니지만 배리어 프리를 위해 필수적으로 넣기)

---
#### 구조와 의미
- `<h1>Heading</h1>` : 대제목_문서의 최상위 제목
- `<p>paragraphs</p>` : 문단 paragraphs
- 리스트
    - ol : 순서가 있는 리스트
    - ul : 순서가 없는 리스트
    ```html
  <ol>
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹</li>
  </ol>

  <ul>
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹</li>
    ```
- 기울임 em, 강조 strong   
    `<p><strong>this 강조</strong> is <em>empahsis 기울임체</em> </p>`

*** 
## CSS
= cascading style sheet  
웹페이지 디자인, 꾸미기와 레이아웃을 담당

### 구조
선택자(selector) {  
    선언(declare)  
    속성(property): 값(value);  
}  

#### 선언 방법
1. inline : html 요소 내에 작성 `<h1 style = "color: red;">Inline Style </h1>` (일회용)
2. **internal 스타일 시트**: 중요! head 태그 내에 작성, 한 파일 내의 여러 요소에서 사용   
    ```html
    <style>
        h2{  
        color: red;  
        }  
    </style>
    ```
3. external 외부(확장성 좋음): .css 파일 생성 후 link이용해서 불러오기

#### 선택자 selectors
- 기본 선택자
    - `*` : 전체 선택자, html 모든 요소
    - tag : 요소, 태그 선택자, 지정한 태그 전체 
    - `.` class : 클래스 선택자, 해당 클래스 전체
    - `#` id : 아이디 선택자, 주어진 id가진 요소
    - attr : 속성 선택자..

- 결합자(combinators)
    - 자손 결합자 `"공백"` : 첫번째 요소의 자손 요소들 선택  
    `p span`: `<p>안의 모든 <span> 선택`
    - 자식 결합자 `>` :  첫번째 요소의 직계 자속 요소만 선택  
    `ul > li`: `<ul>안의 모든 <li> 선택(한 단계 아래 자식들만)`
```html
<head>
<style>
    /* 전체 선택자 */
    * {
    color: red;
    }
    /* 태그 선택자 */
    h2 { 
    color: orange;
    }
    h3,
    h4  { 
    color: blue;
    }
    /* 클래스 선택자 */
    .green { 
    color: green;
    }    
    /* 아이디 선택자 */
    #purple { 
    color: purple;
    }
    /* 자식 결합자 */
    .green > span { 
    font-size: 50px;
    }
    /* 자손 결합자 */
    .green li { 
    color: brown;
    }
    /* class는 중첩으로 작성된 경우 맨 아래에 선언된 것으로 실행됨 */
    p {
      color: blue;
    }

    .orange {
      color: orange;
    }

    .green {
      color: green;
    }        
</style>
</head>
<body>
<h1 class="green">Heading</h1>
<h2>선택자</h2>
<h3>연습</h3>
<h4>반가워요</h4>
<p id="purple">과목 목록</p>
<p class="green orange">3</p>
<p class="orange green">4</p>
<ul class="green">
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹
    <ol>
        <li>HTML</li>
        <li>CSS</li>
        <li>PYTHON</li>
    </ol>
    </li>
</ul>
<p class="green">Lorem, <span>ipsum</span> dolor.</p>
</body>
```
### specify 명시도
css selector에 가중치 계산 => 어떤 스타일을 적용할지 계산  
(전체 선택자가 가장 우선순위가 낮음, *class 선택자만을 고려하자*)

1. importance `!important`
2. inline 스타일의 선언
3. 선택자 : id 선택자 >> **class 선택자** >> 요소 선택자 
4. 소스 코드 선언 순서

#### cascade 계단식, 폭포수
if 동일한 가중치: 마지막에 선언된 것으로 결정

---
### 상속
상속 O 속성: text관련 요소(font)  
상속 X 속성: 위치, box model, 구조 관련 요소

### Box model 박스 모델
html의 모든 요소를 감싸는 box모델  
왼쪽 상단부터 시작   

#### Box display type 박스 표시 타입
1. Outer display type  
박스가 문서의 흐름에서 어떻게 동작할지 결정   
- 아래로 가는 block box(가로의 남은 공백 모두 차지) 
    - 새로운 행 차지
    - width, height 속성 사용 가능
    - padding, margin, border로 인해 다른 요소를 상자로부터 밀어냄
    - ex) h1~6, p, div
- 오른쪽으로 가는 inline box(`<a></a>`, `<img src = "">` : 내용에 해당하는 만큼만 차지)  
    - 옆으로 이동(wid, height 없음)
    - 수직 방향 : padding, margin, border O but, 다른 요소를 상자로부터 밀어내기 불가
    - 수평 방향 : padding, margin, border로 인해 다른 요소를 상자로부터 밀어냄    
    - ex) a, img, span, strong, em

    ```html
    <body>
    <h1>Normal flow</h1>
    <p>Lorem, ipsum dolor sit amet consect explicabo</p>
    <div>
        <p>block 요소는 기본적으로 부모 요소의 너비 100%를 차지하며, 자식 콘텐츠의 최대 높이를 취한다.</p>
        <p>block 요소의 총 너비와 총 높이는 content + padding + border width/height다.</p>
    </div>
    <p>block 요소는 서로 margins로 구분된다.</p>
    <p>inline 요소는 <span>이 것처럼</span> 자체 콘텐츠의 너비와 높이만 차지한다.
        그리고 inline 요소는 <a href="#">width나 height 속성을 지정 할 수 없다.</a>
    </p>
    <p>
        물론 이미지도 <img src="#"> 인라인 요소다.
        단, 이미지는 다른 inline 요소와 달리 width나 height로 크기를 조정할 수 있다.
    </p>
    <p>
        만약 inline 요소의 크기를 제어하려면 block 요소로 변경하거나 inline-block 요소로 설정해주어야 한다.
    </p>
    </body>
    ```
2. Inner display type   
`display: flex;`  
(to be continue..)