## DB_Many to many relationships
DB Day03  
다대다관계_의사,환자 예약시스템, 좋아요 시스템
***
## Many to many relationships
양쪽 모두에서 N:1 관계를 가지는 경우  

ex) 한 환자가 두 명의 의사에게 예약 받도록 하는 상황 -> 예약 테이블 생성
1. model 생성
2. 예약 data 생성
3. 예약 정보 조회
4. 추가 예약 생성
5. 예약 정보 조회 => OK

## Django의 중개모델
`ManyToManyField()` : M:N 관계 설정 모델 필드  
1. 양방향 관계_어느 모델에서든 관련 객체에 접근 가능  
2. 중복 방지_동일한 관계는 한 번만 저장

[옵션]
* related_name : 역참조시 사용하는 manager name 변경
* symmetrical : 관계 설정시 대칭유무 설정, 동일한 모델을 가리키는 정의에서만 사용, 기본 값: True
* through : 사용하고자 하는 중개모델 지정, 추가 데이터 연결

### 추가 정보 기록 = `through`
추가 데이터를 상요해 중개 테이블에 M:N 관계 형성

1. hospitals/models.py  
`symptom = models.TextField()`
`reserved_at = models.DateTimeField(auto_now_add=True)`
2. 예약 생성  
`patient2.doctors.add(doctor1, through_defaults={'symptom':'flu'})`

#### M:N 관계 주요사항
1. 두 테이블에 물리적인 변화 X
2. ManyToManyField -> 중개 테이블 자동 생성
3. ManyToManyField() : 두 모델 중 어디에 위치해도 상관 X_참조, 역참조 방향만 주의

***
## 의사, 환자 진료 예약 모델
1. 환자 모델에 ManyToManyField() 작성  
`hospitals/models.py`  
```python
class Patient(models.Model):
  doctors = models.ManyToManyField(Doctor)
  name = models.TextField()

  def __str__(self):
    return f'{self.pk}번 환자 {self.name}'
```
2. DB 초기화, Migration 진행 & Shell 실행
3. 의사, 환자 생성  
`doctor1 = Doctor.objects.create(name='allie')` \n
`patient1 = Patient.objects.create(name='carol')` \n
`patient2 = Patient.objects.create(name='duke')`
4. 예약 생성_환자가 예약  
```shell
# patient1 -> doctor1
patient1.doctors.add(doctor1)

# patient1 - 자신이 예약한 의사 목록 확인
patient1.doctors.all()
# <QuerySet [<Doctor: 1번 의사 allie>]>

# doctor1 - 자신의 예약된 환자목록 확인
doctor1.patient_set.all()
# <QuerySet [<Patient: 1번 환자 carol>]>
```
5. 예약 생성_의사가 예약  
```shell
# doctor1 -> patient2
doctor1.patient_set.add(patient2)

# doctor1 - 자신이 예약한 환자목록 확인
doctor1.patient_set.all()
# <QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 duke>]>

# patient1,2 - 자신이 예약한 의사 목록 확인
patient1.doctors.all()
# <QuerySet [<Doctor: 1번 의사 allie>]>
patient2.doctors.all()
# <QuerySet [<Doctor: 1번 의사 allie>]>
```
6. 예약 취소하기 (삭제)
```shell
# doctor1 -> patient2 진료예약 취소
doctor1.patient_set.remove(patient2)
# patient1 -> doctor1
patient1.doctors.remove(doctor1)
```
***
## 좋아요 기능 구현
1. articles/models.py Article 클래스에 ManyToManyField 작성   
* ```python
  class Article(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
  ```
* 결과 : 역참조 매니저 충돌  
  * N:1 - `user.article_set.all()` 유저가 작성한 게시글
  * M:N - 유저가 좋아요 한 게시글 모두 동일

* ForeignKey 또는 related_name 작성으로 해결   
  - `like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')`
2. url 작성 => `articles/url.py`  
`path(<int:article_pk>/likes/, views.likes, name='likes'),`
3. view 함수   
```python
@login_required
def likes(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  if request.user in article.like_users.all():
    article.like_users.remove(request.user)
  else:
    article.like_users.add(request.user)
  return redirect('articles:index')
```
4. templates
```html
{% for article in articles %}
  <form action="{% url 'articles:likes' article.pk %}" method="POST">
    {% csrf_token %}
    {% if request.user in article.like_users.all %}
      <input type="submit" value="좋아요 취소">
    {% else %}
      <input type="submit" value="좋아요">
    {% endif %}
  </form>
  <hr>
{% endfor %}
```
***