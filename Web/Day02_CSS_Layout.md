## WEB
웹 Day02
CSS Layout_flexbox

---
## CSS Layout
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


    ```
2. Inner display type   
`display: flex;`  
(나중에 나옴)