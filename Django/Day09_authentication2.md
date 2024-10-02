## Django Authentication System
Django Day09
***
## 회원가입 signup 
UserCreationForm() : 회원가입시 사용자의 입력 데이터 받는 built-in ModelForm
1. 회원가입 페이지 작성 `urls.py`: `path('signup/', views.signup, name='signup'),`
2. `views.py`
   ```python
   from django.contrib.auth.forms import UserCreationForm
    def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                    form.save()
                    return redirect('articles:index')
        else:
            form = UserCreationForm()
        context = {
            'form':form,
        }
        return render(request, 'accounts/signup.html', context)
   ```
3. `signup.html`
    ```html
    <form action='{% url "accounts:signup" %}' method = 'POST'>
        {% csrf_token %}
        {{ form.as_p}}
        <input type='submit' value='회원가입'>
    </form>
    ```    
4. 로직 에러 발생: auth.User <-> accounts.User  
:UserCreationForm에서 사용하는 user모델은 기본 모델이지만, login에서 내가 만든 user model로 바꿨으므로 `class Meta: \n model = User` 수정 필요
   * 이때, 현재 프로젝트에서 활성화된 사용자 모델을 반환하는 `get_user_model()` 활용해 접근 | 직접 참조 안함!!  
   * `forms.py`
   ```python
    from django.contrib.auth import get_user_model
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm 

    class CustomUserCreationForm(UserCreationForm):
        class Meta(UserCreationForm.meta):
            model = get_user_model()

    class CustomUserChangeForm(UserChangeForm):
        class Meta(UserChangeForm.meta):
            model = get_user_model()
   ```
   * `views.py`에서도 `from .forms import CustomUserCreationForm`, `form = CustomUserCreationForm()`으로 수정!!
5. `index.html`에 `<a href = "{% url 'accounts:signup' %}">signup</a>`으로 회원가입 링크 작성  

## 회원 탈퇴 Delete
1. 탈퇴 페이지 작성 `urls.py`: `path('delete/', views.delete, name='delete'),`
2. `views.py`
    ```python
   def delete(request):
        request.user.delete()
        return redirect('articles:index')
   ```
   * request내에 요청 중인 user의 정보를 포함중 -> 새로운 변수에 값을 할당할 필요 없음
3. `delete.html`
    ```html
    <form action='{% url "accounts:delete" %}' method = 'POST'>
        {% csrf_token %}
        <input type='submit' value='회원탈퇴'>
    </form>
    ```    

## 회원정보 수정 Update
UserChangeForm() : built-in ModelForm, 사용자 정보 수정시 값을 입력 받음

1. update 페이지 작성 `urls.py`: `path('update/', views.update, name='update'),`
2. `views.py`
   ```python
   from .forms import CustomUserCreationForm
    def update(request):
        if request.method == 'POST':
            form =  CustomUserChangeForm(request.POST, instance=request.user)    # ModelForm과 Form은 인자로 받는 값의 순서가 다름! 
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form':form,
        }
        return render(request, 'accounts/update.html', context)
   ```
3. `update.html`
    ```html
    <form action='{% url "accounts:update" %}' method = 'POST'>
        {% csrf_token %}
        {{ form.as_p}}
        <input type='submit'>
    </form>
    ```    
4. `index.html`에 `<a href = "{% url 'accounts:update' %}">회원 정보 수정</a>`으로 로그인 링크 작성  

5. 일반 사용자에게도 admin에서 제공하는 정보수정 페이지로 이동 -> 권한 설정 문제 : 출력 필드 재정의
    * `forms.py`
    ```python
    class CustomUserChangeForm(UserChangeForm):
        class Meta(UserChangeForm.meta):
            model = get_user_model()
            fields = ('first_name', 'last_name', 'email',)
    ```

## 비밀번호 변경 PasswordChangeForm()
built-in **form** : 변경 이전의 값을 DB에 저장 X, 새로 입력 받은 값만 저장  
* 비밀번호 변경 페이지(built-in modelform)하단에 비밀번호 변경 주소 별도 표기
1. `urls.py`_app이 아닌 프로젝트의 urls.py에서 접근
   * `from accounts import views`
   * `path('<int: user_pk>/password/', views.change_password, name='change_password'),`

2. `change_password.html`
   ```html
   <form action = "{% url 'change_password' user.pk %}" method="POST">
        {% csrf_token %}
        {% form.as_p %}
        <input type='submit' value='Password_ch'>
    </form>
    ```
3. `views.py`
   ```python
   from django.contrib.auth.forms import PasswordChangeForm
    def change_password(request, user_pk):
        if request.method == 'POST':
            form =  CustomUserChangeForm(request.POST, instance=request.user)    # ModelForm과 Form은 인자로 받는 값의 순서가 다름! 
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = PasswordChangeForm(request.user) # 인자를 받는 함수로 설정되어 있음
        context = {
            'form':form,
        }
        return render(request, 'accounts/change_password.html', context)
   ```
4. 비밀번호 변경시, 기존 세션의 회원정보와 바뀐 DB의 값 => 회원이 아니라고 판단해 로그아웃됨
   * 암호 변경시 세션 무효화를 막아주는 함수_`update_session_auth_hash(request, user)` 이용
   * = 새로운 password 이용한 Session Data로 기존 session 갱신
   * `views.py`에 `from django.contrib.auth import update_session_auth_hash`
   * `user = form(save) \n update_session_auth_hash(request, user)`로 수정
***
## 접근 제한 of 인증된 사용자
1. is_authenticated : 사용자의 인증여부 확인_인증된 사용자면 True
    * 로그인 된 경우만 게시글 작성, 회원정보 수정 등에 접근 가능
    * 로그인이 안된 경우, 회원가입과 로그인만 가능
    ```html
    {% if request.user.is_authenticated %}
        <p>안녕하세요 {{ user.username }}</p>
        <h1>Articles</h1>
        <a href = "{% url 'accounts:update' %}">회원 정보 수정</a>
        <form action="{% url "accounts:logout" %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="LOGOUT">
        </form>
        <form action='{% url "accounts:delete" %}' method = 'POST'>
            {% csrf_token %}
            <input type='submit' value='회원탈퇴'>
        </form>
        
        <a href="{% url "articles:create" %}">CREATE</a>
        {% for article in articles %}
            <p>글 번호: {{ article.pk }}</p>
            <a href="{% url "articles:detail" article.pk %}">
            <p>글 제목: {{ article.title }}</p>
            </a>
            <p>글 내용: {{ article.content }}</p>
            <hr>
        {% endfor %}
    {% else %}
        <a href="{% url "accounts:login" %}">Login</a>
        <a href = "{% url 'accounts:signup' %}">SignUp</a>
    {% endif %}
    ```
    * views.py에서도 login, signup에 `if request.user_is_authenticated: return redirect('arcticles:index')`로 인증된 사용자는 로그인, 회원가입에 접근 안되도록 수정
2. login_required : 인증된 사용자만 view함수 실행 가능, 아닌 경우 login으로 redirect
    * `from django.contrib.auth.decorators import login_required`후 `@login_required`를 인증된 사용자만 실행 가능한 함수 위에 작성(게시글, account create, delete, update)

***
### 참고
* `is_authenticated()`는 method X, 속성 값(property에 해당)
* 회원가입 후 자동 로그인 가능
* 탈퇴 후 로그아웃 순서로 진행 -> 로그아웃 먼저 진행시 세션에 회원정보에 대한 데이터 사라짐
* `PasswordChangeForm(request.user)`는 매개변수를 받는 순서가 다름에 유의!
***
