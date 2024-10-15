## DB_Many to many relationships
DB Day04  
다대다관계_프로필&팔로우 기능 구현, Fixtures
***
## 팔로우 기능 구현
### 프로필 페이지 생성
1. **url** : `accounts/urls.py`에  
`path('profile/<username>/', views.profile, name='profile'),`
2. **view** : `accounts/views.py`
```python
from django.contrib.auth import get_user_model

def profile(request, username):
  User = get_user_model()
  person = User.objects.get(username=username)
  context = {
    'person' : person,
  }
  return render(request, 'accounts/profile.html', context)
```
3. **template** :   
- `accounts/profile.html`  
```html
<h1>{{ person.username }}님의 프로필</h1>
<hr>
<h2>{{ person.username }}가 작성한 게시글</h2>
{% for article in person.article_set.all %}
  <div>{{ article.title }}</div>
{% endfor %}
<hr>
<h2>{{ person.username }}가 작성한 댓글</h2>
{% for comment in person.comment_set.all %}
  <div>{{ comment.content }}</div>
{% endfor %}
<hr>
<h2>{{ person.username }}가 좋아요한 게시글</h2>
{% for article in person.like_articles.all %}
  <div>{{ article.content }}</div>
{% endfor %}
```  
- `articles/index.html`  
```html
<a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
<p>작성자 : <a href ="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></p>
```
***
### 팔로우 기능
follow, follower은 대칭 X
1. `accounts/models.py`에 ManyToManyField() 작성   
- 참조 : 내가 팔로우하는 사람들 = followings  
- 역참조 : 상대방 입장에서 나는 팔로워 중 한 명 = followers
```python
class User(AbstractUser):
  followings = models.ManyToManyField('self', symmetrical = False, related_name='followers')
```
2. url 작성 => `articles/url.py`  
`path(<int:user_pk>/follow/, views.follow, name='follow'),`

3. view :  `accounts/view.py` 
```python
@login_required
def follow(request, user_pk):
  User = get_user_model()
  person = User.objects.get(pk=user_pk)
  if person != request.user:
    if request.user in person.followers.all():
      person.followers.remove(request.user)
  else:
    person.followers.add(request.user)
  return redirect('articles:profile', person.username)
```
4. template : `accounts/profile.html`
```html
<div>
  <div>
    팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length}}
  </div>
  {% if request.user != person %}
    <div>
      <form action="{% url 'articles:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in person.followers.all %}
          <input type="submit" value="팔로우 취소">
        {% else %}
          <input type="submit" value="팔로우">
        {% endif %}
      </form>
    </div>
  {% endif %}
</div>
```
***
## 추가 학습
### Fixtures
Django가 DB로 가져오는 방법을 알고있는 데이터 모음, 초기 데이터  
* fixture 파일 기본 경로: `app_name/fixtures/`
* dumpdata : 생성, DB의 모든 데이터 추출  
`$ python manage.py dumpdata [app_name[.ModelName] [app_name[.ModelName]...]] > filename.json`
* loaddata : 데이터 입력  
`$ python manage.py loaddata filename.json filename.json filename.json` : 모델 관계가 이전 모델의 생성 여부가 중요하면 순서 O, 한 줄로 여러개 실행 가능

cf) encoding codec 오류 발생시
* `$ python -Xutf8 manage.py dumpdata [] `
* 메모장에서 json 파일 열고, 다른이름으로 저장에서 인코딩 utf8로 설정

### Improve Query 쿼리 개선
같은 결과를 얻기위해 DB에 보내는 쿼리 수 줄여보기  
- **annotate** : `GROUP BY`의 집계함수 활용  
= 결과 객체에 집계 결과를 가져오는 필드 생성  
ex) 댓글 개수를 게시글 마다 반복해서 불러오는 `{{article.comment_set.count}}` 대신   
`articles = Article.objects.annotate(Count('comment')).order_by('-pk')`와 `{{article.comment__count}}`
- select_related : `INNER JOIN`  
ex) 게시글마다 작성한 유저명 반복 평가 `{{article.user.username}}` 대신 게시글을 조회하며 유저 정보까지 조회  
`articles = Article.objects.select_related('user').order_by('-pk')`
- prefetch_related  
ex) 게시글 조회시 참조된 댓글까지 한번에 조회   
`articles = Article.objects.prefetch_related('comment_set').order_by('-pk')`
- 최종 최적화 : `Articles = Article.objects.prefetch_related(Prefetch('comment_set', queryset=Comment.objects.select_related('user'))).order_by('-pk')`