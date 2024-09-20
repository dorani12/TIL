## Django
Django Day01  
기본: 가상환경, 백엔드 프레임워크, MTV 디자인 패턴

---
## WEB
web site와 web application을 통해 사용자들이 정보를 검색하거나 상호작용하는 기술  
web site: 여러 개의 web page가 모여 서비스나, 정보를 제공  
Web page: HTML(구조), CSS(꾸미기), javascript(행동)를 이용해 만들어지는 web site를 구성하는 하나의 요소가 웹페이지  

### Web application
* client 클라이언트_서비스 요청
* server 서버_응답하는 주체

backend 백엔드 : 서버 측에서 동작, 클라이언트의 요청에 대한 처리, DB와의 상호작용 담당  

### Web Framework
웹 애플리케이션을 빠르게 개발할 수 있도록, 개발에 필요한 기본 구조, 규칙, 라이브러리 제공  


## Django란?
파이썬 기반, 백엔드 웹 프레임워크 -> 대규모 트래픽 서비스에서도 안정적인 서비스 제공  
!서버 구현!

***
### 가상환경 venv
python 애플리케이션과 그에 따른 패키지들을 격리하여 개별 프로젝트를 관리할 수 있는 독립적인 실행 환경

0. `$ python -m venv venv \n $ source venv/Scripts/activate \n (venv)` : 가상 환경 생성 후 활성화 = ON  
1. 가상환경 활성화 후, pip freeze를 통해 해당 가상환경에 설치된 패키지와 버전을 알 수 있음
2. `pip freeze > requirements.txt`를 통해 1의 내용 문서화 가능
3. `pip install -r requirements.txt`로 텍스트 파일에 있는 패키지 설치 가능

- 프로젝트마다 별도의 가상환경 사용
- on/off 개념으로 개발을 위해 사용하는 도구세트  
의존성 패키지 등 협업시 개발에 필요한 패키지 목록을 공유할 수 있게 됨  

- `$ django-admin startproject firstpjt .`      : ` .`의 유무에 따라 현재 작업중인 폴더에서 생성할지, 폴더를 하나 만들고 그 내부에 만들지를 결정하게 됨
- `$ python manage.py runserver` : 서버 실행

***
## 디자인 패턴
소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책  
= 공통 문제 해결 방식, 형식화된 관행  

### MTV 디자인 패턴 vs MVC(model, view, controller)
데이터, 사용자 인터페이스, 비지니스 로직 분리  

Django는 model, template, view  
- Model : 데이터 관련 로직 관리, 응용프로그램의 데이터 구조 정의, DB 기록 관리
- Template : 레이아웃과 화면 처리, 화면상의 사용자 인터페이스 구조와 레이아웃 정리
- View : M, T와 관련된 로직을 처리해 응답 반환, 클라이언트의 요청에 대해 처리 분기
### 앱 application in Project
- Project : 애플리케이션의 집합(DB 설정, URL 연결, 전체 앱 설정 등 관리)  
- Application : 독립적으로 작동하는 기능 단위의 모듈

1. 앱 생성 : `$ python manage.py startapp articles`
2. 앱 등록 at. 프로젝트 `settings.py`의 `INSTALLED_APPS`에 등록

cf) 프로젝트 구조 중  
`asgi.py` : 비동기식 웹서버와의 연결 관련 설정   
`wsgi.py` : 웹서버와의 연결 관련 설정   
`manage.py` : Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티   

앱 구조 중  
`admin.py` : 관리자용 페이지 설정   
`models.py` : DB와 관련된 model 정의, MTV 디자인 패턴 중 M   
`views.py` : HTTP 요청을 처리하고 해당 요청에 대한 응답 반환, MTV 중 V   
`tests.py` : 프로젝트 테스트 코드를 작성  

### 요청과 응답
코드 작성 순서  
Django 는 `URLs` → `Views` → `Templates` 에 따라 요청 → 응답을 구성하므로, 코드도 이에 따라 작성  

1. URLs : `url.py`의 `urlpatterns`에 요청 주소별로 views 모듈의 해당 주소와 관련된 로직이 실행되도록 view 함수에 전달  
2. View : `views.py`의 함수를 찾아 = `page주소명(request)`에서 특정경로에 있는 template과 request 객체를 결합해 응답 개체 반환  
`def index(request): \n
    return render(request, 'articles/index.html')`
3. Template : templates 폴더 생성, 내부에 articles 폴더 생성 후 템플릿 파일 생성

***
#### 참고
Trailing Comma = 후행 쉼표, 마지막 요소 뒤에도 `,`  
[Django의 규칙]
1. `urls.py`에서 각 url의 문자열 경로는 `/`로 끝남
2. `views.py`에서 모든 함수는 첫번째 인자 = request로 요청 객체를 받음
3. Django의 경우 app폴더 내 templates 안에 있는 template 파일만 읽어올 수 있음
***