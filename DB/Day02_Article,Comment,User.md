## DB_다대일 관계
DB Day02  
Many to one relationships
***

## RDBMS : 관계형 데이터베이스 시스템
데이터간에 관계가 있는 데이터 항목들의 모음
### SQLlite  

### SQL : Structure Query Language
대소문자 구분 X, but 대상과 명령어를 구분 편하게 하기 위해 대문자로 작성
세미콜론 ; 필수

### SQL statements
**DQL**(Data Query Language): SELECT문 = 데이터 검색
DML
DCL
***












***
(DB 오프라인 수업 내용)
## Article & User
user 모델 참조 방법(p.80 암기)  
게시글 create -> is_valid에서 문제 발생  
=> article = form.save(commit=False) : save 후 객체만 바로 반환



### CREATE 테이블 생성
```SQL
CREATE TABLE table_name (
  column_1 data_type constraints,
  column_2 data_type constraints,
)
```
* 컬럼 명, 데이터 타입과 제약 조건 작성  
  * Data type 
    * INTEGER
    * VARCHAR(10)
    * TEXT(문자열)
    * BLOB(이미지, 동영상, 문서 등의 바이너리 데이터)
    * REAL(부동소수점)
  * Constraints 
    * for. 데이터 무결성, 데이터베이스의 일관성 보장   
    * NOT NULL
    * PRIMARY KEY(한 테이블에서 무조건 1개 존재해야 함, INTEGER필드에만 적용)
    * AUTOINCREMENT(필드의 자동증가, 한 행을 삭제하더라도 다음 cid나 index는 빈공간 두고 +1됨)
    * FOREIGN KEY(다른 테이블과의 외래 키 관계 정의)

* `PRAGMA table_info('테이블 명');` : 명령어를 통해 테이블 구조(schema) 확인  

### ALTER TABLE
* ADD COLUMN : 필드 추가
* RENAME COLUMN : 필드 이름 변경, ex) `현재 필드명 TO 새로운 필드명`
* DROP COLUMN : 필드 삭제
* RENAME TO : 테이블 이름 변경  
ex)`ALTER TABLE 테이블 명 ADD COLUMN 컬럼명 data_type constraints, ;`

### DROP TABLE
`DROP TABLE 테이블 명;` 테이블 삭제
***
#### 참고
* Type Affinity(타입 선호도): 유연성, 명시적으로 data type 지정 X 또는 지원 X인 자료형 -> 다른 데이터 타입으로 추론하여 지정해줌
* NOT NULL 제약은 필수적이지 않음

## Modifying Data : DML(Data Manipulation Language) 데이터의 수정
데이터 조작 = UPDATE 수정, INSERT 추가, DELETE 삭제 

### INSERT INTO 000 VALUES 000 
`INSERT INTO` *테이블 명* `(필드 목록) VALUES (값 목록)`

### UPDATE 000 SET 필드명 = 새 값 [WHERE 조건];
`UPDATE 테이블명 SET 필드명 =  새로운 필드 명 값 WHERE (조건, 수정 대상)id = 1`

### DELETE FROM 000 WHERE 조건
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

## Multiple table queries => Join
여러 테이블 간의 논리적 연결  
분리된 테이블이지만 연관성이 있음 -> 조회시 연관된 데이터를 확인하기 어려음 => Join 사용

1. Inner Join : 교집합, 값이 일치하는 레코드에 대해서만 결과 반환
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
  ```SQL
  SELECT
    * # 테이블명.필드명
  FROM
    articles # 정보를 얻어올 테이블
  INNER JOIN users # 일치여부를 확인할 다른 테이블의 필드명 
  ON users.id = articles.userID;  # 검색 조건, table명.field명
  [WHERE 조건]
  ```
2. LEFT JOIN  
왼쪽 테이블의 모든 레코드 표기  
but, 오른쪽 테이블과 매칭되는 레코드가 없을 시 NULL 표기

***