## Django_Template & URLs
Django Day02  
***
## DTL : Django Template system 데이터 표현 및 제어
template에서 조건, 반복, 변수 등의 프로그래밍적 기능 제공

* 변수 variables
* 필터 filter | :  변수의 변형
* 태그 tags % : 반복, 논리에 따라 제어 흐름 생성, 시작/종료 태그 필요
* 주석 comments #

### template system 활용 방법
1. views.py 파일 : dictionary 형태로 context 작성
```python
def index(request):
    # dictionary 형태로 context 작성
    context = {
        'name' : 'Alice'
    }
    #요청데이터, 템플릿 이름#
    return render(request, 'index.html', context)
```
2. at. html 파일  
* `{{key}}` 안에 dictionary key 값의 이름 작성
* `{{variable | filter}}` 변수 뒤에 내장된 filter 사용 
  * ex)
  * `{{name|truncatewords:30}}` name이라는 key에 대한 value 값이 길어서 잘라서 출력, : 뒤는 값을 또 받아옴
  * `{{picked| length}}` picked라는 key에 대응하는 value 값의 길이를 출력
* `{% tag %}` : ex)`{% if %} {% endif %}` 출력되지는 않지만 제어의 흐름!
* `{# 주석 #}` or `{% comment %} ... {% endcomment %}`

#### 예제
1. urls.py
`urlpatterns = path('dinner/', views.dinner),]`
2. views.py
```python
def dinner(request):
    foods = ['국밥', '카레', '탕수육', '소주', '']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    
    return render(request, 'dinner.html', context)
```
3. template 파일 ex) `dinners.html`
```html
<h1>Dinner 선택하기</h1>
{% comment %} 새로고침시 랜덤으로 list내의 원소 하나를 선택 {% endcomment %}
<p>{{picked}} 메뉴는 {{picked|length}}글자 입니다.</p>
<p>{{foods}}</p>
{# 반복문을 작성하기! for 입력후 자동완성 지원됨 #}
<ul>
  {% for food in foods %}
  <li>{{food}}</li>
  {% endfor %}
</ul>
{% if picked|length == 0 %}
  <p>메뉴가 소진되었습니다.</p>
{% else %}
  <p>메뉴가 아직 남아있습니다.</p>
{% endif %}
```      
---
## 템플릿 상속
모든 페이지에 bootstrap을 적용하려면?!  
부모 템플릿이 공통 요소(navigation bar, footer 등)를 포함하고 하위 템플릿이 재정의 할 수 있는 공간을 정의 해놓기

* 부모 템플릿_base.html  
`{% block content %}` 로 내용을 추가할 부분을 표기  
`{% endblock content %}`  

* 자녀 템플릿
1. 확장: `{% extends "base.html" %}`로 상속 받겠다고 선언!_최상단에 1개만 선언
2. 적용: `{% block content %}`와 `{% endblock content %}` 사이에 넣고 싶은 내용 추가  
ex) `{% block content %} \n <h1>{{name}} 안녕!</h1> \n {% endblock content %}`
***
## 요청과 응답_HTML form
HTTP 요청을 서버에 보내기  
form element를 이용하여 서버에 요청을 보낼 수 있고, text 입력, submit 등 여러 요소 제공  
- action: 어디로!_입력 데이터가 전송될 URL = ? 기준으로 key와 value의 쌍으로 구성  
- method: 어떤 방식으로!_`GET`
- input의 name 속성을 이용해서 원하는 곳으로 보내기

예제
```html
<h1>Fake Naver</h1>
{#"요청을 보낼 서버의 주소"| ? 이전의 값 #}
<form action="https://search.naver.com/search.naver">
  <input type="text" name="query">
  <input type="submit">
</form>
```
### HTTP request 객체
form으로 전송한 데이터, Django로 들어오는 모든 요청 관련 데이터가 들어오는 `request`  
class형태로 작성되어있고, `request.GET.get('form의 name속성 값')`을 통해 name으로 들어온 값을 얻을 수 있음  

예제
```python
def catch(request):
    # 사용자가 요청한 request에서 query를 추출해서 검색에 사용
    query_in = request.GET.get('query')
    context = {
        'query': query_in
    }
    return render(request, 'catch.html', context)
```
```html
<h1>Throw</h1>
{#"요청을 보낼 서버의 주소"| ? 이전의 값 #}
<form action="/catch/" method='GET'>
  <input type="text" name="query">
  <input type="submit">
</form>
```
```html
<h1>Catch</h1>
<p>당신이 입력한 값은 {{query}}입니다.</p>  
```
***
## URL dispatcher 분배기
url의 일부에 변수를 포함시켜 불필요한 반복 줄이기  
by. variable routing : url 일부에 변수를 포함하여 view함수로 전달
  - `path_converter:varible_name` : ex) `path('articles/<int:num>/', views.detail)`  
  - str, int 등 

ex) 
1. urls.py에 `path('articles/<str: name>/', views.greeting)`  
2. veiws.py에 `def greeting(request, name): \n context = { 'name': name} \n return render(request, 'articles/greeting.html', context)`  
3. greeting.html에 `{{name}}`이 들어가도록 작성!

### App과 URL
application이 여러개일때, urls.py를 구분하여 작성  
project의 urls.py는 `path(articles/, include('articles.urls))`로  
나머지는 articles라는 어플리케이션의 urls.py에 작성하기  
=> 이름 지정하기 `{% url 'app_name:url_name' arg1 arg2 %}`와 같이 tag 이용 가능
어플리케이션이 여러개이니 `app_name = 'articles'`로 쓰고 `{% url 'articles:url name' arg1 arg2 %}`으로 구분하기

#### 참고
* urls -> views -> templates의 경로로 처리
***