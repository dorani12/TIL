## Django DRF ModelSerializer, REST API
Django Day11
***
### ModelSerializer 댓글 CRUD
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