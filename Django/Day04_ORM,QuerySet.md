## Django ORM, QuerySet
Django Day04  
***
## ORM : object-relational-mapping
객체지향프로그래밍 언어를 사용해 호환되지 않는 유형의 시스템 간에 데이터 변환 기술  
: Django와 DB의 언어가 다름 -> 같은 명령어로 소통 불가  
but, Django에 내장된 ORM이 중간에서 해석 및 변환

## QuerySet API
- ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용
- API를 활용 -> SQL이 아닌 python 코드로 데이터 처리 by. *모델 클래스, 인스턴스*
- 구문: `Model class.Manager.Queryset API(메서드)` ex) `Article.objects.all()`
- **Query**는 DB의 특정 데이터를 보여달라는 요청, 받은 응답 데이터는 *QuerySet*
- **CRUD** : Create 저장, Read 조회, Update 갱신, Delete 삭제
---
### QuerySet 실습
1. `$ pip install ipyhton`, `$ pip install django-extentions`명령어를 통해 외부 라이브러리 설치
2. `$ pip freeze > requirements.txt`로 요구사항 텍스트파일 업데이트, `settings.py`파일의 INSTALLED_APPS에 `django_extensions` 추가
3. `$ python manage.py shell_plus` : 한 줄의 명령어로 인한 변화를 바로 확인 가능함
+) Django shell은 장고 내에서 실행되는 python shell 
***
### Create 생성
인스턴스 article을 활용해 instance 변수 활용  

* `article = Article()`, `article.title = 'first'`, `article.content = 'django'`와 같이 인스턴스 내에 field명에 넣고 싶은 자료를 입력   
| `article = Article(title = 'first', content = 'django' )`  
| `Article.objects.create(title = 'first', content = 'django')` : 생성 이후 데이터 반환
* `article.save()` 로 자료 저장 
* `article`이라는 명령어나, `Article.objects.all()`을 통해 DB에 저장된 것 확인 가능

### Read 조회
method
1. all() : 전체 데이터 조회
2. filter() : 매개변수와 일치하는 객체를 가진 QuerySet 반환 = 없어도 빈거 return  
    ex) `Article.objects.filter('first')`
3. get() : 단일 객체 반환, 매개변수 일치할 때만 = 없을 때, 여러개 있으면 오류 발생 => 고유성을 보장하는 조회, primary key

### Update 수정
순서: 조회 -> 내용 수정 -> DB에 저장
1. 조회_뭘 수정할건지 대상 설정
`article = Article.object.get(pk = 1)` 으로 조회
2. `article.content = '수정 내용'`
3. `article.save()`로 DB에 수정내용 전달

### Delete 삭제
조회 후 삭제 `article.delete()`_삭제했던 pk는 재사용 X
***
## ORM with view
작성한 게시글 **전체 조회** 연습
1. `views.py` 파일에서 model 조회
    ```python
    from .models import Article

    def index2(request):
        # 전체 게시글 조회 요청 -> DB에
        articles = Article.objects.all()
        context = {
            'articles': articles,
        }
        return render(request, 'articles/index2.html', context)

    ```
2. article에서 원하는 내용 접근  
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Articles</h1>
        <p>{{articles}}</p>
        {% for article in articles%}
            <p>{{article}} </p>
            <p>글 번호: {{article.pk}} </p>
            <p>글 제목: {{article.title}} </p>
            <p>글 내용: {{article.content}} </p>
            <hr>
        {% endfor %}
    </body>
    </html>
    ```
***
