## Django_models
Django Day03  
***
## Model_DB 관리, 소통
DB의 테이블 정의 및 데이터 조작 -> 테이블의 구조 설계  

Django의 경우 model class를 이용하여 DB에 테이블 구조를 생성

### Model Class
테이블의 구조를 어떻게 설계할지 작성
* `from django.db import models`: application내의 `models.py`작성, `models`를 `import` 
* `class Article(models.Model):` models의 Model을 상속 받아 클래스 선언
* `title = models.CharField()` : field types = 데이터 유형, field options = 제약조건
    * null : 빈 값 허용
    * blank : form 에서 빈 값 허용
    * default : 필드의 기본 값
* 클래스의 변수 명 -> 필드(열)의 이름!  

예시
```python
class Article(models.Model):
    title = models.CharField(max_length=10) # 제한된 길이의 문자열 저장, max_length는 필수 옵션
    cotent = models.TextField() # 길이 제한 x, 대용량 텍스트 저장
    amount = models.IntegerField()
```
이외에도 `File`, `Image`, `DateTime` 등이 있음

## Migrations
model 클래스의 변경사항(필드 생성, 수정 삭제)을 DB에 반영  
1. `python manage.py makemigrations`: 최종 설계도 migration을 작성
2. `python manage.py migrate` : 최종 설계도를 DB에 전달 및 반영  

sql파일을 확인!

### 테이블 수정
1. 필드 추가
- `created_at = models.DateTimeField(auto_now_add=True)`: 데이터가 처음 생성될 때만 현재 날짜, 시간을 저장
- `updated_at = models.DateTimeField(auto_now=True)`: 데이터가 저장될 때마다 자동으로 현재 날짜,시간 저장 
2. migration 작성 by. `python manage.py makemigrations` & 기본값 사용
3. `migrate` 명령어 사용 후 적요되었는지 확인

***
## Admin site
관리자 페이지_계정 필요, 데이터 확인 및 테스트 진행  
Django의 경우 automatic admin interface로 자동으로 관리자 인터페이스 제공  
1. 계정 생성 : `python manage.py createsuperuser`
2. DB의 `auth_user`에 계정 생성 확인_**migrate 필수**
3. `admin.py`에 작성한 모델 클래스 등록
```python
from django.contrib import admin
from .models import Article

admin.site.register(Article)        # 등록!
```
4. admin site에 로그인 후 데이터 수정 테스트 진행
5. DB의 테이블에 추가되었는지 확인

***
## lottos 프로젝트
1. `$ python -m venv venv`, `$ source venv/Scripts/activate`로 가상환경 생성 후 실행
2. `$ pip install django==4.2` or `$ pip install -r requirements.txt`로 django 또는 필요한 파일 저장
3. `$ django-admin startproject lotto_pjt_ex .` lotto_pjt_ex라는 이름으로 project 만들기 | `.` 있으면 따로 폴더 안열고 생성
4. `$ python manage.py runserver` 명령어를 통해 서버가 열리는지 확인_http://127.0.0.1:8000/
5. `$ python manage.py startapp lottos` app생성_이름은 복수형!  
    : app 생성을 완료 했다면, settings.py에 INSTALLED_APPS의 젤 위에 APP 놓기  
6. pjt 내의 urls.py와 lottos app내 urls.py 작성하기
    ```python
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('lottos/', include('lottos.urls')),
    ]
    ```
    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```
7. `templates/lottos`폴더 내에 `index.html`파일을 작성해 어떤 화면이 나오도록 할지 잡기  
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <div>hello django!</div>
        <h1>lottos</h1>
        <p>이번 회차 번호: {{ real_lottos }} </p>
        <p>구매한 번호: {{ lottos }} </p>

        <p> 맞은 숫자: {{ correct_lottos }} </p>
    </body>
    </html>
    ```
8. `views.py`를 통해 lottos 앱 내에서 request에 따라 어떤 함수를 실행할지 `index` 함수 작성  
    ```python
    def index(request):
        print('index 무사 도착')
        lottos = sorted(list(random.sample(range(1, 46), 6)))
        real_lottos = [4, 9, 12, 15, 33, 45]
        correct_lottos = list(set(lottos).intersection(real_lottos))
        context = {
            'lottos': lottos,
            'real_lottos': real_lottos,
            'correct_lottos' : correct_lottos,
        }

        return render(request, 'lottos/index.html', context)    
    ```
***