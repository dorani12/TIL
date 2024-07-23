## 파이썬 Data Structure에 따른 Method
data structure와 method_dict, set

---
### 3. dict 딕셔너리  

|            메서드           	|                                                                                설명                                                                              	|
|:---------------------------:	|:----------------------------------------------------------------------------------------------------------------------------------------------------------------:	|
|           D.clear()         	|     딕셔너리 D의   모든 키/값 쌍을 제거                                                                                                                          	|
|           D.get(k)          	|     키 k에   연결된 값을 반환 (키가 없으면 None을 반환)                                                                                                          	|
|         D.get(k,   v)       	|     키 k에   연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환                                                                                             	|
|           D.keys()          	|     딕셔너리 D의   키를 모은 객체를 반환                                                                                                                         	|
|          D.values()         	|     딕셔너리 D의   값을 모은 객체를 반환                                                                                                                         	|
|           D.items()         	|     딕셔너리 D의   키/값 쌍을 모은 객체를 반환                                                                                                                   	|
|           D.pop(k)          	|     딕셔너리 D에서   키 k를 제거하고 연결됐던 값을 반환 (없으면   오류)                                                                                          	|
|         D.pop(k,   v)       	|     딕셔너리 D에서   키 k를 제거하고 연결됐던 값을 반환 (없으면   v를 반환)                                                                                      	|
|        D.setdefault(k)      	|     딕셔너리 D에서   키 k와 연결된 값을 반환                                                                                                                     	|
|     D.setdefault(k,   v)    	|     딕셔너리 D에서   키 k와 연결된 값을 반환     k가   D의 키가 아니면 값 v와   연결한 키 k를 D에   추가하고 v를 반환                                            	|
|        D.update(other)      	|     other 내 각 키에 대해 D에   있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체.     other에 있는 각 키에 대해 D에   없는 키면 키/값 쌍을 D에   추가    	|
```python
# .clear()_딕셔너리의 모든 키, 값 쌍 제거
person = {'name': 'Alice', 'age': 25}
print(person.clear()) #None

# .get(key)_키에 연결된 값 반환(없으면 기본 값, none)/.get(key[,default])
person = {'name': 'Alice', 'age': 25}
print(person.get('name')) #= print(person['name'])
print(person.get('age'))
print(person.get('country')) #None
print(person.get('country', 'Unknown')) #Unknown_키에 해당하는 반환 값 없어서 기본값을 'Unknown'으로 설정

# .keys()_딕셔너리에 있는 key 값들을 반환
person = {'name': 'Alice', 'age': 25}
print(person.keys()) #dict_keys(['name', 'age'])
for item in person.keys():
    print(item)

# .values()_값들을 list형태로 반환
person = {'name': 'Alice', 'age': 25}
print(person.values()) #dict_values(['Alice', 25])

# .items()_dictionary 안의 키와 값의 쌍을 tuple 형태로 반환, k,v로 해서 key와 value 추출 가능
person = {'name': 'Alice', 'age': 25}
print(person.items()) #dict_items([('name', 'Alice'), ('age', 25)])
for item in person.items():
    print(item) #('name', 'Alice') \n ('age', 25) 튜플 채로 반환
    print(*item)# name Alice \n age 25 !*를 통해 언패킹!
for key, value in person.items():
    print(key)
    print(value) 
#name \n Alice \n age \n 25 키와 값들을 각각 반환 가능

# .pop(key[,default])_key 제거하고 연결된 값은 반환
person = {'name': 'Alice', 'age': 25}
print(person.pop('name')) #Alice_name key 값에 연결된 값
print(person)
print(person.pop('country', 'Unknown')) #Unknown으로 디폴트 값 출력

# .setdefault(key[,default])_key가 있으면 해당하는 value 출력/조회되지 않을 경우, default 값으로 value 저장
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('name')) #Alice
print(person.setdefault('country', 'Korea')) #Korea
print(person) #{'name': 'Alice', 'age': 25, 'country': 'Korea'}

# .update([other])_other에 들어있는 키와 값의 쌍으로 딕셔너리 갱신(기존 키가 있으면 value는 덮어쓰기)/없는 key였으면 추가
person = {'name': 'Alice', 'age': 25}
other_person = {'name2': 'Jane', 'gender': 'Female'}

#값 추가하는 방법 1_key = value 형태로 작성된 값들도 가능
person.update(age = 180, country = 'Korea')
print(person) #{'name': 'Alice', 'age': 180, 'country': 'Korea'}
#값 추가하는 방법 2_딕셔너리 형태의 변수 넣기
person.update(other_person)
print(person) #{'name': 'Jane', 'age': 180, 'country': 'Korea', 'gender': 'Female'}
#{'name': 'Alice', 'age': 180, 'country': 'Korea', 'name2': 'Jane', 'gender': 'Female'}
```
***
### 4. set 세트  
set() 안의 항목들은 순서가 없음/중복된 값 저장 불가능
|           메서드          	|                                설명                               	|
|:-------------------------:	|:-----------------------------------------------------------------:	|
|          s.add(x)         	|     세트 s에 항목   x를 추가. 이미   x가 있다면 변화 없음         	|
|          s.clear()        	|     세트 s의   모든 항목을   제거                                 	|
|         s.remove(x)       	|     세트 s에서   항목 x를 제거. 항목   x가 없을 경우 Key error    	|
|           s.pop()         	|     세트 s에서   랜덤하게 항목을 반환하고,   해당 항목을 제거     	|
|        s.discard(x)       	|     세트 s에서   항목 x를 제거                                    	|
|     s.update(iterable)    	|     세트 s에   다른 iterable 요소를   추가                        	|

```python

# .add(x)_x를 세트 안에 저장
my_set = {'a', 'b', 'c', 1, 2, 3}
print(my_set)
my_set.add(4)
print(my_set)

# .clear()_세트 안의 모든 값 지우기
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set) #set(): 비어있는 세트 자료형

# .remove(x)_세트 안의 x 값 제거/x가 세트에 저장 안되어 있는 경우 key error
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove('a')
# my_set.remove('e') #KeyError: 'e'_제거할 'e'가 존재하지 않음으로 error
print(my_set) #{1, 2, 3, 'c', 'b'}

# .pop()_세트에서 **임의의 요소를 제거 후 반환**(매번 다른 값이 빠져나감.....ㅎ)
# 해시 테이블에 나타나는 순서대로 값을 반환함
my_set = {'a', 'b', 'c', 1, 2, 3}
print(my_set.pop()) #1_빠져나가는 요소 출력

# .discard(x)_x 값 제거, but 없는 값을 넣어도 keyError 발생x
my_set = {'a', 'b', 'c', 1, 2, 3}
print(my_set.discard('a')) #None_반환 값은 없음
my_set.discard('z')
print(my_set) #{1, 3, 2, 'b', 'c'}

# .update(iterable)_iterable 한 요소를 set 안에 추가
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, '4', '5']) #없는 값 빼고 추가
print(my_set) #{1, 2, 3, '1', '5', '4', 'c', 'b', 'a'}
```
#### 집합연산 메서드
|              메서드            	|                                         설명                                       	|         연산자        	|
|:------------------------------:	|:----------------------------------------------------------------------------------:	|:---------------------:	|
|      set1.difference(set2)     	|        set1에는 들어있지만 set2에는      없는   항목으로 세트를 생성 후 반환       	|      set1   – set2    	|
|     set1.intersection(set2)    	|           set1과 set2 모두   들어있는 항목으로      세트를   생성 후 반환          	|     set1   & set 2    	|
|       set1.issubset(set2)      	|               set1의 항목이 모두 set2에 들어있으면      True를   반환              	|     set1   <= set2    	|
|      set1.issuperset(set2)     	|               set1가 set2의   항목을 모두 포함하면      True를   반환              	|     set1   >= set2    	|
|         set1.union(set2)       	|     set1 또는 set2에(혹은   둘 다) 들어있는      항목으로   세트를 생성 후 반환    	|     set1   \| set2    	|

```python
# 집합 메서드_합,차,교,부분집합
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) #{0, 2, 4}_차집합 set1-set2
print(set1.intersection(set2)) #{1, 3}_교집합 set1&set2
print(set1.issubset(set2)) #False
print(set3.issubset(set1)) #True_set3가 set1의 부분원소인지!set3 <= set2
print(set1.issuperset(set2)) #False set1이 set2의 모든 항목 포함 
print(set1.union(set2)) #{0, 1, 2, 3, 4, 5, 7, 9}_합집합 set1|set2
```
***
참고  
### 해시 테이블 hash table
in. set(), dict() 자료구조_거의 불변한 자료형에서 사용!!!!  
key를 해시 함수를 통해 해시 값으로 변환, 해시 값을 인덱스로 사용하여 데이터를 저장, 검색  
for. **data 빠른 검색**, 효율적인 저장, 접근  
_가변형 객체는 해시테이블의 무결성 유지 불가  
- print(hash(값)) 을 통해 hash 값을 확인 할 수 있음
  - 정수의 경우 항상 같은 해시 값_계산을 다시하진 않음
  - 문자열은 해시 값이 항상 랜덤
- set.pop() 에서 임의의 순서대로 요소가 빠져나감
  - = 해시 테이블에 나타나는 순서대로 값을 반환함
***
### 파이썬 문서규격  
확장된 BNF_문서상의 표기법에 해당  
[] : 생략가능  
{} : 0변 이상 반복  
() : 그룹화  
