## Django DRF ModelSerializer, REST API
Django Day10
***
## REST API
[AWS 공식 문서](https://aws.amazon.com/ko/what-is/restful-api/) | [Postman 설치](https://www.postman.com/downloads/)  
* Application Programming Interface : 두 SW가 서로 통신할 수 있도록하는 메커니즘_클라이언트 & 서버  
* Representational State Transfer : API server를 개발하기 위한 SW 설계 방법론  
REST 원리를 따르는 RESTful API : 자원을 정의하고 자원에 대한 주소를 지정하는 방식    
  1. 자원의 식별 = URI
  2. 자원의 행위 = HTTP Methods
  3. 자원의 표현 = JSON 데이터  

### 1. URI 식별
Uniform Resource Idenfier : 통합 자원 식별자, 인터넷에서 리소스(자원)을 식별하는 문자열    
### URL 
: Uniform Resource Locator : 통합 자원 위치, 웹에서 주어진 리소스의 주소
1. Schema(Protocol) : 브라우저가 리소스 요청시 사용하는 규약  
ex) http, `https`, mailto(메일 열기), ftp(파일 전송)
2. Domain Name : 요청중인 웹 서버, IP주소 -> 도메인 네임 생성  
ex) 142.251.42.142 => `www.google.com`
3. Port : 기술적인 문  
http 프로토콜의 표준 포트(생략 가능)_HTTP = 80, HTTPS = 443
4. Path : 웹서버의 리소스 경로, 물리적 위치 대신 추상화된 형태의 구조  
ex) /articles/create/
5. Parameters : 웹서버에 제공하는 추가적인 데이터, `&`기호로 key-value 쌍 목록 구분  
ex) `?key1=value1&key2=value2`
6. Anchor : `#` 북마크, 브라우저의 해당 지점으로 바로 이동  
ex) `#TITLE2`

### 2. HTTP Methods 행위
* HTTP `Request Methods` = HTTP verbs 동사, 리소스에 대한 행위, 수행하고자 하는 동작  
  1. `GET` : 검색, 서버에 리소스 표현 요청
  2. `POST` : 제출, 서버의 상태 변경, 데이터를 지정된 리소스에 제출
  3. `PUT` : 요청한 주소의 리소스 수정
  4. `DELETE` : 지정된 리소스 삭제
* HTTP response `status codes` : 특정 HTTP 요청이 완료되었는지, 오류인지 코드로 표현
  * 1nn : informational responses
  * 2nn : successful response
  * 3nn : redirection messages
  * 4nn : client error
  * 5nn : server error

### JSON 데이터 표현
`html`파일(**Template**) 대신 화면 구성에 필요한 리소스를 `json`형태로 제공
1. 가상 환경 생성, 활성화 및 requirements.txt 패키지 설치
2. migrate : `python manage.py migrate`
3. fixture 파일 load : `python manage.py loaddata articles.json` 
4. `python-request-sample.py` 파일을 통해 json 데이터 처리

***
## DRF Django REST framework
Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리  
: `POSTMAN` : API 개발 및 테스트를 위한 서비스, 요청 데이터 구성, 응답 확인, 환경 설정, 자동화 테스트 등의 기능  
: [DRF 공식문서](https://www.django-rest-framework.org/#installation)에서 설치

### Serialization 직렬화
데이터의 구조, 객체 상태를 **재구성 가능 포맷**으로 변환 for. 여러 시스템에서 활용  
* Serializer : serialization을 진행해 Serialized data를 반환해주는 클래스  

## ModelSerializer : Django 모델과 연결된 Serializer 클래스  
사용자 입력 데이터를 받고 자동으로 모델필드에 맞추어 직렬화 진행  
ModelForm의 방식과 비슷, `articles/serializers.py`에 클래스 작성  
```python 
from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serailizers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
```
***
### ModelSerializer CRUD
### GET - 게시글 조회
1. 게시글 데이터 목록을 제공하는 ModelSerializer 정의
```python 
from rest_framework import serializers
from .models import Article
# 게시글 목록 조회
class ArticleListSerializer(serailizers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
# 게시글 상세정보 제공
class ArticleSerializer(serailizers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
```
2. url, view 함수 작성  
* `urls.py`: `path('articles/', views.article_list),`, `path('articles/<int: article_pk>', views.article_detail),`     
* `views.py` : 
   ```python
   from rest_framework.response import Response
   from rest_framework.decorators import api_view

   from .models import Article
   from .serializers import ArticleListSerializer, ArticleSerializer

   @api_view(['GET'])
   def article_list(request):
    articles = Article.objects.all()
    serializer = AritcleListSerializer(articles, many = True)
    return Response(serializer.data)
   
   def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk_)
    serializer = AritcleSerializer(article)
    return Response(serializer.data)
   ```
   1. `many=True` : QuerySet을 Serialize하는 경우  
   2. `serializer.data` : data객체에서 실제 데이터 추출  
   3. `@api_view(['GET'])` : decorator 필수, GET만 적용되며 POST와 같은 다른 메서드 요청시 405 error 발생

### POST - 게시글 데이터 생성
응답 : 성공 -> 201 Created | 실패 -> 400 Bad request  
`view` 함수 작성  
```python
from rest_framework import status

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = AritcleListSerializer(articles, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
### DELETE - 게시글 데이터 삭제
삭제 성공 => 204 No Content 응답
```python
@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk_)
    if request.method == 'GET':
        serializer = AritcleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
### PUT - 게시글 수정
수정 성공 => 200 OK 응답
```python
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk_)
    if request.method == 'GET':
        serializer = AritcleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
`partial` : 부분 업데이트 허용, 수정이 필요한 데이터만 받아오고 수정!  

***
#### 참고_ raise_exception
`if serializer.is_valid(raise_exception=True):`를 통해 유효성 검사를 통과 못하는 경우 400_BAD_REQUEST 자동 처리 -> return 부분 생략 가능
***