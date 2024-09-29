## Django_ORM View
Django Day05  
***
### ORM with view
작성한 게시글 **일부 조회** 연습
1. `urls.py`에 추가
    `path('<int:pk>/', views.detail, name='detail')`
1. `views.py` 파일에서 model 조회
    ```python
    from .models import Article

    def detail(request, pk):
        # url로 부터 받은 pk를 활용해 데이터 조회
        article = Article.objects.get(pk=pk)
        context = {
            'article': article,
        }
        return render(request, 'articles/detail.html', context)

    ```
2. article에서 원하는 내용 접근  
    ```html
        <h1>Detail</h1>
    <p>{{article.pk}}번째 글</p>
    <hr>
    <p>글 제목: {{article.title}} </p>
    <p>글 내용: {{article.content}} </p>
    <p>수정일: {{article.updated_at}} </p>
    <p>작성일: {{article.created_at}} </p>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
    ```
***

### CREATE in View
* `views.py`
    ```python
    def new(request):
        return render(request, 'articles/new.html')

    def create(request):
        # 사용자 요청으로부터 입력 데이터 추출
        title = request.GET.get('title')
        content = request.GET.get('content')

        # 저장
        article = Article(title=title, content=content)
        article.save()

        return render(request, 'articles/create.html')
    ```

* `new.html`
    ```html
    <body>
        <h1>NEW</h1>
        <form action="{% url 'articles:create' %}" method="GET">
            <div>
                <label for='title'>Title: </label>
                <input type="text">
            </div>
            <div>
                <label for='content'>Content: </label>
                <textarea name="content" id="content"></textarea>
            </div>
            <div>
                <input type="submit">
            </div>
        </form>
        <hr>
        <a href="{% url 'articles:index2' %}">[back]</a>
    </body>
    </html>

    ***
    <body>
        <h3>작성 완료.</h3>
    </body>
    ```

***

## HTTP request methods
데이터에 대해 원하는 작업의 종류를 명시
* HTTP : 네트워크 상에서 데이터(리소스)를 주고 받기 위한 약속
* GET : 서버로부터 데이터를 요청하고 받아오는 **조회**에 사용
    * url의 쿼리 문자열로 데이터 전송 *ex) title=제목명&content=내용*
    * 브라우저 히스토리에 남고, 캐싱으로 로딩시간 단축
* POST : 서버에 데이터 제출 후 리소스 변경 = **생성, 수정, 삭제**
    * url이 아닌 body를 통해 데이터 전송
    * 많은 양 전송 가능, 히스토리 X, 캐시 X

### HTTP response status code
* 서버가 클라이언트 요청에 대한 처리 결과를 3자리 숫자로 알려줌
* 404 page not found
* 403 forbidden => 서버에 요청 전달 O, 권한이 없어 거절

#### CSRF 
: cross-site-request-forgery 사이트간 요청 위조  
Token : DTL의 csrf_token태그를 이용해 사용자에 토큰 값 부여  
-> POST 요청 시 토큰 값도 함께 서버로 전송할 수 있도록 함
* `{% csrf_token %}` 을 html 코드에 작성
* Django의 경우 직접 제공한 페이지에서 작송하고 있는지, 위조사이트가 아닌지 방어하기 위함

## Redirect
로그인 후, *로그인이 완료되었습니다.* 보다는 *메인페이지, 마이페이지로 돌아가*는 것이 일반적  
= 클라이언트가 `GET`요청을 한번 더 보내도록 응답  
= redirect() : 클라이언트가 인자에 작성된 주소로 다시 요청을 보내도록 함

* `from django.shortcuts import render, redirect`
* `return redirect('articles:detail', article.pk)` : render 대신 redirect 사용

### DELETE in View
* `urls.py` -> `path(<int:pk>/delete/, views.delete, name='delete'),`
* `views.py`
    ```python
    def delete(request, pk):
        # 어떤 게시글을 삭제할지 조회
        article = Article.objects.get(pk=pk)

        # 조회된 게시글 삭제 후 redirect
        article.delete()
        return redirect('articles:index')
    ```
* `detail.html`
    ```html
    <form action="{% url 'articles:delete' article.pk %}" method='POST'>
        {% csrf_token %}
        <input type='submit' value='삭제'>
    </form>
    ```

### UPDATE in View
* `urls.py` -> `path(<int:pk>/edit/, views.edit, name='edit'),`
* `views.py`
    ```python
    def edit(request, pk):
        # 어떤 게시글을 수정할지 조회
        article = Article.objects.get(pk=pk)
        context = {
            'article': article,
        }
        return render(request, 'articles/edit.html', context)
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        article.title = request.GET.get('title')
        article.content = request.GET.get('content')
        article.save()
        return redirect('articles/detail', articles.pk)
    ```
* `detail.html`
    ```html
    <a href="{% url 'articles:edit' article:pk %}">EDIT</a><br>
    ```
* `edit.html`
    ```html
    <h1>EDIT</h1>
    <form action="{% url 'articles:update' article.pk %}" method='POST'>
        {% csrf_token %}
        <div> 
            <label for="title">Title: </label>
            <input type='text' name="title" id='title' value='{{article.title}}'>
        </div>
        <div> 
            <label for="content">Content: </label>
            <textarea type='content' name="content" id='content' value='{{article.content}}'>
        </div>
        <input type='submit' value='삭제'>
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
    ```
***
### 참고_GET vs POST
* 데이터 전송 방식 : URL의 Query string parameter(캐시) | HTTP body
* 데이터 크기 제한 : URL 최대 길이 | 없음
* 사용 목적 : 데이터 검색 및 조회 | 데이터 제출 및 변경
***
