## Django Form
Django Day06
***
## HTML 'form'
사용자로 부터 데이터를 제출 받기 위해 활용한 방법_검색, 로그인
* data를 DB에 저장 X
* 유효성 검사 필요
* Django의 경우 단순화하고 자동화 할 수 있는 기능 제공

### form 실습
1. `forms.py`파일 생성 후 form class 정의(application)
    ```python
    from django import forms

    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=10)
        content = forms.CharField()
    ```
    * form 클래스에는 TextField()가 없다!

2. `views.py`에서 함수 변경
    ```python
    from .forms import ArticleForm

    def new(request):
        form = ArticleForm()
        context = {
            'form' : form,
        }
        return render(request, 'articles/new.html', context)
    ```
3. `new.html`에서 `{{form}}`
* `{{form.as_p}}`로 줄바꿈 구현

### Widgets
HTML `input` element 표현 담당
* CharField로만 표현되는 input 요소의 속성 및 출력되는 부분 변경
= `content = forms.CharField(widget = forms.Textarea)`

---
## HTML 'ModelForm'
사용자로 부터 받은 데이터를 DB에 저장_게시글 작성, 회원가입
* data를 DB에 저장 O
* HTML form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 함

### ModelForm 실습
1. ModelForm class 정의(application내의 `forms.py`)
    ```python
    from django import forms
    from .models import Article

    class ArticleForm(forms.ModelForm):
        class Meta:
            model = Article
            fields = '__all__'
            # exclude = ('title',) 과 같이 모델에서 포함X 필드 지정
    ```
    * meta는 세부데이터 = ModelForm의 정보 작성
2. `views.py`
    ```python
    def create(request):
        # modelform 인스턴스 생성
        form = ArticleForm(request.POST)

        # 유효성 검사
        if form.is_valid()
            article = form.save()
            return redirect('articles:detail', article.pk)
        context = {
            'form':form,
        }
        return render(request, 'articles/new.html', context)
        # 유효성 검사 실패시 new페이지로 이동 with 유효성 검사가 실패한 이유
    ```
3. edit 수정
* `views.py`
    ```python
    def edit(request, pk):
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
    return render(request, 'articles/edit.html', context)

     def update(request, pk):
        # 모델폼 인스턴스 생성
        article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article)
        # 유효성 검사
        if form.is_valid()
            form.save()
            return redirect('articles:detail', article.pk)
        context = {
            'article':article,
            'form':form,
        }
        return render(request, 'articles/edit.html', context)
        # 유효성 검사 실패시 new페이지로 이동 with 유효성 검사가 실패한 이유
    ```
* `create.html`에서 `{{form.as_p}}`
***
## New + Create 생성
`POST` method의 필요 유무가 차이
* GET : 게시글 생성 페이지를 줘!
* POST : 게시글 생성 요청!
```python
def create(request):
    # 요청 메서드가 POST라면
    if request.method == `POST`:
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid()
            article = form.save()
            return redirect('articles:detail', article.pk)
    # 요청 메서드가 POST가 아닐 때,(GET, PUT, DELETE 등)
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/create.html', context)
```
## Edit + Update 생성
`POST` method의 필요 유무가 차이
* GET : 게시글 수정 페이지를 줘!
* POST : 게시글 수정된걸 저장 요청!
    ```python
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        if request.method == 'POST':
            form = AritcleForm(request.POST, instance = article)
            if form.is_valid():
                form.save()
                return redirect('articles/detail', articles.pk)
        else:
            form = AritcleForm(instance = article)
        context = {
            'article': article,
            'form':form,
        }
        return render(request, 'articles/update.html', context)
    ```
* edit 페이지 사용 X, 함수도 삭제

***
### 참고_Widgets
`forms.py`
```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder':'Enter the title',
                'max_length' : 10,
            }
        ),
        error_messages={'required':'내용을 입력해주세요.'},
    )
    class Meta:
        model = Article
        fields = '__all__'
```
***
