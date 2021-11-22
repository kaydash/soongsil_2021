해시 -> 검색최적화(인덱스)
  해시함수의 예
  cf. 짝수/홀수, 5부제, 10부제
  -> 복잡한 해시함수 만들면 충돌확률 낮추는 것이 가능 secure hash
  -> 계산이 느려짐 -> GPGPU(CUDA)

SECURE HASH -> 검색, 조작방지(원본확인)
  MD5/MD6 -> SHA-1
  cf. DBMS 암호화

한 번에 검색가능 
   충돌 날 경우 

$ docker ps -a
$ docker exec -it 컨테이너명 bash

# wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1oaq1XvmPSyLBrtZkpncuC7YpG10tQi8U' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1oaq1XvmPSyLBrtZkpncuC7YpG10tQi8U" -O data.tar.gz && rm -rf /tmp/cookies.txt

# tar xvfz data.tar.gz
# cd data
# ls
# pwd
# head 2M.ID.CONTENTS

*** 무슨 단어가 몇 번 나왔나?
# grep sample part-000??

sample / samples / sample" / sample?

1. 특수문자 처리(숫자포함여부)
!@#$%^&*()-_=+[]{};:'"<>,.?/~`
123467890
2. 대소문자 처리
3. 단복수처리
4. 복합단어처리, Be/have/...
...
5. 띄어쓰기, 문법 
...

*****무슨 단어가 가장 많이 나왔나(Top10)
-> order by xxxx desc 

빅데이터를 처리하니 결과가 다시 빅데이터(820만 줄)
   다른 기술에 의존하기 애매함 -> 결국 다시 스파크/하둡 프로그램 작성

빅데이터를 전체 다 정렬하는 것은 비효율적임
   퀵/힙정렬 O(NlogN)

하지만 TopN(상위 N)를 찾는 것은 O(N) 시간안에 처리가능 


Hive(HiveQL)->compile(변환) -> 하둡(MapReduce) -> compile & 실행

SparkSQL(DataFrame & Dataset) -> Spark RDD 변환 -> 실행

Hive < 하둡(MapReduce)  vs.  Spark SQL > Spark RDD

SparkSQL -> 변환 & Catalyst optimizer -> 실행
  DBMS Optimizer와 유사한 Catalyst Optimizer 

explain SQL ...

오라클 > MySQL 보다 훨씬 비쌈

오라클이 MySQL 보다 빠른가?
   급나누기 "옵티마이저"
   서브쿼리 최적화(SQL in SQL, ...)
      cf. 조인 vs. 서브쿼리(MySQL은 약함)

   SQL hint의 중요성이 큰가? 작은가?
   
자동차 네비 -> 길안내 수준 
  거리, 비용, 시간  -> 목적지 길 안내

CBO(cost)/RBO(rule)
  CBO가 주류

구글에서 '스파크 wikidocs'로 검색
https://wikidocs.net/book/2350

XML -> JSON(빠르면서 간단, 충분히 복잡)+
DTD/XMLschema - 쓰기가 까다롭고 느리다 

JSON/YAML이 공존
  yaml(세팅,설정에서 많이 사요)
  데이터표현-json

[ ] - JSON array
{ } - JSON object
a:b - key : value

select name from people where age > 20;

filter() -> where
select() -> projection  


DBMS의역사

1. RDBMS가 시장장악
2. 객체지향+데이터베이스 -> 객체관계형(OR DBMS)
    XML->RDBMS 저장

3. NoSQL(쓰기속도, JSON)
-> NoSQL+ORDBMS
    컬럼기반 테이블(쓰기속도개선)+JSON

3-1. 검색엔진-> 전문검색 인덱스
    
4. 블럭체인과의 통합(테이블)
 

# wsl 에서 수행
cd /
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1oaq1XvmPSyLBrtZkpncuC7YpG10tQi8U' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1oaq1XvmPSyLBrtZkpncuC7YpG10tQi8U" -O data.tar.gz && rm -rf /tmp/cookies.txt

tar xvfz data.tar.gz
cd /data
docker run -it -v `pwd`:/home/jovyan/work -p 8888:8888 jupyter/all-spark-notebook

https://wikidocs.net/28555








