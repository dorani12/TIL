## DB_RDBMS,Query문
DB Day01  
관계형 데이터베이스, 쿼리문 작성
***
## 데이터베이스
데이터를 체계적으로 관리(= 저장, 조작 CRUD)하기 위함  
* 데이터 : 저장이나 처리에 효율적인 형태로 변환된 정보

## RDBMS : 관계형 데이터베이스 시스템
Relational DataBase Management System : 데이터베이스 관리 SW 프로그램  
= DB와 사용자간의 인터페이스 역할, 데이터 저장 및 관리를 용이하도록 함  
ex) SQLite, Oracle, MySQL...    
데이터간에 **관계**가 있는 데이터 항목들의 모음
* 관계 : 여러 테이블 간의 *논리적*인 연결
* 테이블, 행, 열의 정보를 구조화하는 방식
* 서로 관련된 데이터 포인터를 저장, 이에 대해 액세스 할 수 있도록 함

### 구성 요소
* 테이블 : 데이터 기록, relation
* field : 열, column, attribute, 속성
* record : 행, row, tuple, 구체적인 값
* database : 테이블의 집합, schema
* 기본키, pk : Primary Key, 행에서 고유하게 식별 가능한 값, 레코드의 식별자
* **외래키**, fk : Foreign Key, 고유한 식별 값 (동명이인 식별), 다른 테이블의 기본 키 참조 => 서로 다른 테이블간의 관계를 만드는 데 사용
***
## SQL : Structure Query Language
DB에 정보 저장, 처리하기 위한 프로그래밍 언어   
Query -> DB로부터 정보 요청   

1. 대문자 : 대소문자 구분 X, but 대상과 명령어를 구분 편하게 하기 위해 **대문자**로 작성
2. `;` : 세미콜론 ; 필수

### SQL statements
1. DDL(Data Definition Language)   
: 데이터 정의 = 데이터 기본 구조 및 형식 변경  
: CREATE, DROP, ALTER

2. **DQL**(Data Query Language)  
: 데이터 검색  
: SELECT문   

3. DML(Data Manipultaion Language)  
: 데이터 조작 = 추가, 수정, 삭제
: INSERT, UPDATE, DELETE

4. DCL(Data Control Language)  
: 데이터 제어 = 데이터 및 작업에 대한 사용자 권한 제어  
: COMMIT, ROLLBACK, GRANT, REVOKE
***
## Single Table Queries
FROM => SELECT => ORDER BY  
테이블에서, 조회하여, 정렬한 결과 반환
## Querying Data : DQL = Data Query Language  
: 데이터 검색_SELECT   

### SELECT 테이블에서 데이터 조회
```SQL
SELECT
  select_list # 데이터를 선택하려는 필드 (여러개 가능, *는 전체)
FROM
  table_name; # 테이블 명
```
* `AS`  
: `SELECT FirstName AS '이름' FROM employees;`: `AS`라는 키워드로 필드의 데이터를 불러올 때, `FirstName` 대신 `이름`으로 값을 불러옴
* `*` : 전체 데이터 = 모든 필드 선택 by, asterisk
* 연산도 가능 : `SELECT Milliseconds / 60000 AS '재생시간(분) FROM trakcs;'`

### ORDER BY 정렬
```SQL
SELECT
  select_list     # 데이터를 선택하려는 필드
FROM
  table_name      # 테이블 명
ORDER BY
  컬럼 명 ASC,    # 오름차순 정렬
  컬럼 명2,       # 기본 값이 오름차순이라 생략 가능 
  컬럼 명3 DESC;  # 내림차순 정렬
```
* 먼저 기재된 컬럼기준으로 정렬 후, 같은 순위면 다음 컬럼 기준으로 정렬
* NULL 값은 오름차순 정렬시 0순위

### Fitering 필터
* Clause 절
    - DISTINCT : 조회 결과 중 중복된 레코드 제거,!종류 몇가지인지!  
    : `SLECT DISTINCT Country FROM customers ORDER BY Country;`
    - **WHERE** : 검색 조건, `IS NULL`로 빈 값인지 체크   
    WHERE -> ORDER BY 순으로 작성
      ```SQL
      SELECT
        select_list     # 데이터를 선택하려는 필드
      FROM
        table_name      # 테이블 명
      WHERE
        조건;
        # ex) City = 'Prague';
        # Company IS NULL AND Country = 'USA';
        # Bytes BETWEEN 1000 AND 5000;
        # Country IN ('Canada', 'Italy', 'France');
        # LastName LIKE '%son'; 'son'으로 끝나는 경우
        # LastName LIKE '___a'; 'a'으로 끝나면서, 총 4자리
      ```
    - LIMIT : 조회 개수(레코드 수) 제한
      offset 경계선 이후부터 개수 만큼 출력
      ```SQL
      SELECT
        select_list     # 데이터를 선택하려는 필드
      FROM
        table_name      # 테이블 명
      LIMIT
        [offset,] 개수; # 기본 값은 생략 가능, 최대 레코드 수 지정
      ```        
      `LIMIT 3, 4;` = Bytes 기준 내림차순으로 4번째 부터 7번째 데이터만 조회
    
* Operator 연산자
    - BETWEEN : 범위 내에 존재?
    - IN : 특정 목록 안에 존재?
    - LIKE : 특정 패턴과 일치?  
    : `%` 0개 이상의 문자열과 일치?, `_` 단일 문자(자리 수)와 일치?
    - Comparison 비교: `=`,`>=`, `<=`, `!=`, `IS`, `LIKE`, `IN`, `BETWEEN 00 AND`
    - Logical : `AND &&`, `OR ::`, `NOT !`

### GROUP BY 그룹화
레코드를 그룹화 -> 요약본 생성 = 집계함수, 종류 count  
- SUM
- AVG
- MAX, MIN
- COUNT
```SQL
SELECT
  select_list, COUNT(*)     # 데이터를 선택하려는 필드
  # ex) Composer, AVG(Bytes) & ORDER BY AVG(Bytes) DESC;
  # ex) Composer, AVG(Bytes) AS '바뀐 이름' & ORDER BY '바뀐 이름' DESC; 해당 필드명으로 정렬해야함
FROM
  table_name      # 테이블 명
GROUP BY
  필드 명;         # 각 그룹에 대해 집계된 값 계산
``` 
* 집계 항목에 대한 조건 => `HAVING 조건식;`  
WHERE에 작성하는 경우 처리 흐름상 에러 발생

#### 참고
FROM => WHERE => GROUP BY => HAVING => SELECT => ORDER BY => LIMIT 
테이블에서, 특정 조건에 맞추어, 그룹화, 그룹화 조건 실행, 조회하여, 정렬한 뒤, 개수제한 한 결과 반환

***
## Managing Tables : DDL = Data Definition Language
데이터의 기본 구조 및 형식 변경_CREATE, ALTER, DROP

### CREATE 테이블 생성
```SQL
CREATE TABLE table_name (
  column_1 data_type constraints,
  column_2 data_type constraints,
)
```
* 컬럼 명, 데이터 타입과 제약 조건 작성  
  * Data type 
    * `INTEGER`
    * `VARCHAR(10)`
    * `TEXT`(문자열)
    * `BLOB`(이미지, 동영상, 문서 등의 바이너리 데이터)
    * `REAL`(부동소수점)
  * Constraints 
    * for. 데이터 무결성, 데이터베이스의 일관성 보장   
    * `NOT NULL`
    * `PRIMARY KEY`(한 테이블에서 무조건 1개 존재해야 함, INTEGER필드에만 적용)
    * `AUTOINCREMENT`(필드의 자동증가, 한 행을 삭제하더라도 다음 cid나 index는 빈공간 두고 +1됨)
    * `FOREIGN KEY`(다른 테이블과의 외래 키 관계 정의)

* `PRAGMA table_info('테이블 명');` : 명령어를 통해 테이블 구조(schema) 확인  

### ALTER TABLE
* ADD COLUMN : 필드 추가  
ex)`ALTER TABLE 테이블 명 ADD COLUMN 컬럼명 data_type constraints, ;`  
`ALTER TABLE Student ADD COLUM Age INEGER NOT NULL DEFAULT 0;`, 여러 개 수정은 바로아래 추가X, Full형태로 써야함
* RENAME COLUMN : 필드 이름 변경, ex) `현재 필드명 TO 새로운 필드명`
* DROP COLUMN : 필드 삭제
* RENAME TO : 테이블 이름 변경  

### DROP TABLE
`DROP TABLE 테이블 명;` 테이블 삭제
***
#### 참고
* Type Affinity(타입 선호도): 유연성, 명시적으로 data type 지정 X 또는 지원 X인 자료형 -> 다른 데이터 타입으로 추론하여 지정해줌
* NOT NULL 제약은 필수적이지 않음
***
## Modifying Data : DML(Data Manipulation Language) 데이터의 수정
데이터 조작 = UPDATE 수정, INSERT 추가, DELETE 삭제 

### 추가 INSERT INTO 000 VALUES 000 
`INSERT INTO` *테이블 명* `(필드 목록) VALUES (값 목록)`
: 테이블 내 특정 필드에, 값 추가

### 수정 UPDATE 000 SET 필드명 = 새 값 [WHERE 조건];
`UPDATE 테이블명 SET 필드명 =  새로운 필드 명 값 WHERE (조건, 수정 대상)id = 1`

### 삭제 DELETE FROM 000 WHERE 조건
`DELETE FROM 테이블명 WHERE 조건;`  
: 조건에 해당하는 레코드 삭제  
* WHERE 안에 쿼리가 들어가는 서브쿼리 형태로 작성 가능  
  EX) articles 테이블에서 작성일이 오래된 순으로 2개 레코드 삭제
  ```SQL
  DELETE FROM 
    articles
  WHERE id IN(
    SELECT id FROM articles
    ORDER BY "createdAt"
    LIMIT 2
  );
  ```
***
## Multiple table queries => Join
여러 테이블 간의 논리적 연결  
분리된 테이블이지만 연관성이 있음 -> 조회시 연관된 데이터를 확인하기 어려음 => Join 사용


  ```SQL
  CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL
  );

  CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(100) NOT NULL,
    userId INTEGER NOT NULL,
    FOREIGN KEY (userId) 
      REFERENCES users(id)
  );
  ```
1. Inner Join : 교집합, 값이 일치하는 레코드에 대해서만 결과 반환
  ```SQL
  SELECT
    select_list
    # *                             # 테이블명.필드명
  FROM
    table_a
    # articles                      # 정보를 얻어올 테이블
  INNER JOIN table_b
    # users                # 일치여부를 확인할 다른 테이블의 필드명 
  ON table_b.fk = table_a.pk;
  # users.id = articles.userID;  # 검색 조건, table명.field명
  [WHERE 조건]
  ```
2. LEFT JOIN  
왼쪽 테이블의 모든 레코드 표기  
but, 오른쪽 테이블과 매칭되는 레코드가 없을 시 NULL 표기
  ```SQL
  SELECT
    *                             # 테이블명.필드명
  FROM
    articles                      # 정보를 얻어올 테이블
  LEFT JOIN users                # 일치여부를 확인할 다른 테이블의 필드명 
  ON users.id = articles.userID;  # 검색 조건, table명.field명
  [WHERE 조건]
  ```
***
