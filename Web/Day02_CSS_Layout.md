## WEB
웹 Day02
CSS Layout_flexbox

---
## CSS Layout
## Box model 박스 모델
html의 모든 요소를 감싸는 box모델  
왼쪽 상단부터 시작   

### Box 속성 : 요소의 크기와 위치를 지정
top, bottom, left, right로 방향 존재  
1. 내용 : content box = 실제 콘텐츠가 표시되는 영역, width * height로 크기 조정
2. 안쪽 여백 : padding box = 콘텐츠 주위의 공백
3. 테두리 : border = 콘텐츠와 패딩을 래핑
4. 외부 간격 : margin = 테두리 외부의 공간, 콘텐츠, 패딩 및 테두리를 래핑, 박스와 다른 요소 사이의 공백  

- shorthand 속성
    - border: 색상, 테두리, 테두리 굵기를 순서 상관없이 나열
    - margin, padding : 공통 | 4개 = 상우좌하, 3개 =  상/좌우/하, 2개 = 상하/좌우

- standard css box model: margin과 상관없이 content 기준으로 box의 사이즈를 정함
- alternative에서는 `box-sizing: border-box;` 설정을 통해 테두리를 고려한 박스 사이즈로 속성 값 설정 가능

### Box display type 박스 표시 타입
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
    
    - `display : inline-block;`  
        - width, height 속성을 가지고 padding, margin, border로 인해 다른 요소를 상자가 밀려남  
        - but, 줄바꿈은 되지 않음 => 너비와 높이를 정하면서 줄바꿈 x  

    - none  
    우선 사용자에게 보이지 않음, 특정 조건에서 보이거나 사라지도록 하려고 사용

2. Inner display type   
FlexBox (아래에서 계속..) 

---
## Position 특정 요소의 위치 조정
: **Normal flow에서 요소를 제거**하여 다른 위치로 배치 가능  
ex) 다른 요소 위에(Z축) 위치, 특정 위치(top, bottom, left, right)에 고정시키기
- static 기본
    - 기본 값, normal flow에 따라 배치
    - ~~top, bottom, left, right~~
- relative 상대 위치
    - normal flow에 따라 배치, static 기준으로 이동
    - top, bottom, left, right 속성으로 위치 조정 가능
- **absolute 절대 위치**
    - normal flow에서 요소 제거 -> 다른 요소도 위치 변화(해당 요소가 차지하는 공간 x)
    - 가장 가까운 relative 부모 요소를 기준으로 이동(없으면 body tag 기준)
- fixed 고정
    - normal flow에서 요소 제거 -> 다른 요소도 위치 변화
    - 현재의 화면 영역(Viewport) 기준으로 이동, 스크롤해도 위치 변화 X
    - top, bottom, left, right 속성
- sticky
    - relative & fixed의 중간 성격
    - relative => 임계점에 닿는 순간 고정(fixed) & 다음 sticky 만날 시 대체
- z-index
    - 요소의 쌓임 순서(stack order) 정의
    - static이 아닌 요소에만 적용
    - 같은 부모 내에서만 z-index 값을 비교

    ```html
    <style>
        * {
        box-sizing: border-box;
        }

        body {
        height: 1500px;
        }

        .container {
        position: relative;
        height: 300px;
        width: 300px;
        border: 1px solid black;
        }

        .box {
        height: 100px;
        width: 100px;
        border: 1px solid black;
        }

        .static {
        position: static;
        background-color: lightcoral;
        }

        .absolute {
        /*normal flow에서 제거 => 다른 요소가 올라오게 됨
        but, 부모 속성을 relative로 하면 기준점이 설정된다*/
        position: absolute;
        background-color: lightgreen;
        /*기준 점은 가장 가까운 relative 부모 요소*/
        top: 50px;
        left: 100px;
        }

        .relative {
        /*position: relative;*/
        background-color: lightblue;
        top: 100px;
        left: 100px;
        }

        .fixed {
        /* position: fixed; */
        background-color: gray;
        top: 0;
        right: 0;
        }
    </style>
    </head>

    <body>
    <div class="container">
        <div class="box static">Static</div>
        <div class="box absolute">Absolute</div>
        <div class="box relative">Relative</div>
        <div class="box fixed">Fixed</div>
    </div>
    </body>
    ```
---
## FlexBox
: 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식  
1. 선언   
부모 요소 `display: flex;`(배치의 주체) -> 자식 요소들이 flex item이 됨
2. 배치  
main축을 기준으로 start -> end(왼 -> 오 || 위 -> 아래)
`flex-direction: column;`, row, column, row-reverse(시작, 끝점 반대) 가능
3. 행 변화  
`flex-wrap: wrap;` 한 행을 넘어가면 크기 변화주어 행 변화
4. justify 정렬(main 축)  
`justify-content: center;` flex item 정렬_flex-start, end, center
5. align 정렬(교차 축)  
cross axis 교차 축 기준 정렬  
`align-content: center;` 교차축 기준 정렬

+) align-self는 개별 요소 item에 특정한 정렬하도록 줄 수 있음
`flex-grow`, `flex-shrink` => 남은 여백을 어떻게 나눌지(남은 여백을 기준으로 해당비율로 나누어줌)
`flex-basis` : flex-item의 기본적인 크기를 지정 (width보다 우선)

#### 반응형 레이아웃
`flex-wrap: wrap;`, `flex-grow`, `flex-basis` 를 활용해 다른 디바이스, 화면에서도 사이즈 조절이 되도록 화면 구성  
(to be continue..)

***
