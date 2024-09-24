## Django Authentication System
Django Day08
***
## HTTP 특징
html 문서 같은 리소스를 가져올 수 있도록 하는 규약_웹에서 이뤄지는 데이터 교환의 기초
* 비연결 지향
  * 서버는 요청에 대한 응답을 보낸 후 연결을 끊음 
* 무상태
  * 연결을 끊는 순간 클라이언트와 서버와의 통신 종료
  * 상태 정보 유지 X
  * = 로그인, 장바구니 유지 X

## cookie 쿠키
서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
* 클라이언트 측에 저장_속성: 만료 시간, 도메인, 주소 등
* 사용자의 인증, 추적, 상태 유지 등에 사용
* 동일한 브라우저인지 아닌지 판단, 상태정보 기억
    * key-value의 데이터 형식으로 저장
    * 서버: HTTP 응답 헤더의 set-cookie 필드를 통해 클라이언트에 쿠키 전송
    * 브라우저: 받은 쿠키 저장, 동일한 서버에 재요청 시 HTTP 요청 헤더의 cookie 필드에 저장된 쿠키를 함께 전송

### 쿠키 사용 목적
1. 세션관리 : 로그인, 아이디 자동완성, 팝업 체크, 장바구니 등 정보 관리
2. 개인화 : 언어 설정, 테마 등 사용자의 설정 값 저장
3. 트래킹 : 사용자 행동 기록, 분석

### 세션 session
* 서버 측에 생성, 클라이언트와 서버간의 상태 유지
* 상태 정보를 저장하는 데이터 저장 방식  
* 쿠키에 세션 데이터 저장, 매 요청시마다 세션 데이터에 접근할 수 있는 세션ID 같이 전송

## Django Authentication System
사용자 인증 = 신원 확인

### authentication 실습_로그인, 로그아웃
DB 생성시, 프로젝트 시작시 ~ migrate 1회 실행 전!필수
1. `accounts`라는 이름의 두번째 app 생성, settings에 등록
2. 기존 user model에 해당하는 AbstractUser 상속 받기: 추가 사용자 정보관련 수정이 어려움  
    `models.py` 작성
    ```python
    from django.contrib.auth.models import AbstractUser
    from django.db import models

    class User(AbstractUser):
        pass
    ```
3. `django.contrib.auth`  
   `settings.py`의 `AUTH_USER_MODEL = 'accounts.User'`로 내가 만든 class user로 사용하겠다!

4. admin site에 등록_`admin.py`
    ```python
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from .models import User

    amdin.site.register(User, UserAdmin)
    ```
## Login 로그인
Create of Session  
: AuthenticationForm() 로그인 인증에 사용할 데이터를 받는 built-in form

1. login 페이지 작성 `urls.py`: `path('login/', views.login, name='login'),`
2. `views.py`
   ```python
   from django.contrib.auth import login as auth_login
    def login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)    # ModelForm과 Form은 인자로 받는 값의 순서가 다름! 
            if form.is_valid():
                # 만약 인증된 사용자라면, 로그인 진행_세션 데이터 생성
                auth_login(request, form.get_user())    # built-in method 이용, 유효성 검사를 통과하고, 인증된 로그인 한 사용자 객체 반환
                return redirect('articles:index')
        else:
            form = AuthenticationForm()
        context = {
            'form':form,
        }
        return render(request, 'accounts/login.html', context)
   ```
3. `login.html`
    ```html
    <form action='{% url "accounts:login" %}' method = 'POST'>
        {% csrf_token %}
        {{ form.as_p}}
        <input type='submit'>
    </form>
    ```    
4. `index.html`에 `<a href = "{% url 'accounts:login' %}">Login</a>`으로 로그인 링크 작성  

로그인 이후 개발자 도구를 통해 cookie 확인 : `sessionid` 값이 전달되었는지 확인!!

## Logout 로그아웃
logout(request): DB에 현대 요청에 대한 session data 삭제 & 클라이언트 쿠키에서도 session id 삭제
1. `urls.py`: `path('logout/', views.logout, name='logout'),`
2. `index.html`
   ```html
   <form action = "{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type='submit' value='Logout'>
    </form>
    ```
3. `views.py`
   ```python
   from django.contrib.auth import logout as auth_logout
    def logout(request):
        auth_logout(request) 
        return redirect('articles:index')
   ```

## Template with Authentication data_built-in
context_processors로 built-in 해둠
- template에서 바로 사용 가능한 `user`라는 context data가 존재
- `{{user.username}}`을 통해 바로 user 이름 정보 받아올 수 있음

***
### 참고_쿠키
보안장치
* 제한된 정보만 쿠키에 저장
* 중요한 정보는 암호화
* 만료시간 지날 경우 자동 삭제
* 도메인 제한으로 특정 웹사이트에서만 사용 가능  

Django
* DB의 session으로 다룸
***
