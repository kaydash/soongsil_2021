SQL on Bigdata
 - Hive 2
 - SparkSQL

+ 쿼리 옵티마이저(Catalyst Optimizer)
+ 코딩 -> 쿼리

RDD -> SparkSQL (성능이 2배까지 차이)

docker ps -a
docker start xxxx
docker logs xxxx
docker exec -it xxxx bash

# wget https://s3-eu-west-1.amazonaws.com/csparkdata/ol_cdump.json   

# gzip ol_cdump.json
# gzip -d ol_cdump.json.gz
# apt update
# apt install bzip2
# bzip2 ol_cdump.json
# bzip2 -d ol_cdump.json.bz2

spark.sql("SELECT count(*) FROM cdump").show()
spark.sql("SELECT * from cdump limit 10").show()
spark.sql("SELECT count(distinct authors) from cdump").show()
spark.sql("SELECT authors,genres,title,type,isbn_10,number_of_pages,languages from cdump  order by title desc limit 10").show()
spark.sql("SELECT authors,genres,title,type,isbn_10,number_of_pages,languages from cdump where genres is not null order by number_of_pages desc limit 10").show()
spark.sql("SELECT authors,genres,title,type,isbn_10,number_of_pages,languages from cdump where title like '%travel%' order by number_of_pages desc limit 20").show()

equi-join(standard) vs. non-equi join

select * from person full join address on person.name = address.name

Inner Join
  null 값이 나오는 것은 삭제 

Full Join
  null 이 나오는 것도 다 출력

Left Join / Right Join
  Full Join은 MySQL/MariaDB에서 지원하지 않음

RDBMS은 
1. 테이블기반 데이터베이스
2. 조인(테이블 합치는 연산)으로 처리 -> 큰 데이터가 생김
      최적화

cf. 오라클은 조인대신 서브쿼리로 해결하는 경우가 많음(MySQL은 서브쿼리최적화가 약함)

- 테이블 하나 DF/DS 하나씩 할당
  테이블 - JSON - 스파크 뷰 - 데이터프레임/데이터셋 - 조인

- JSON의 키(컬럼) 하나가 원자성을 안가지는 경우
     value가 배열이나 오브젝트가 되는 경우 -> JSON 하나가 데이터프레임 여러 개에 대응(***)


ol_cdump의 authors를 explode()로 구현하시오.

sjha72@gmail.com로 제출해 주세요.

type:string

"authors": [{"type": {"key": "/type/author_role"}, "author": {"key": "/authors/OL5360212A"}}]


OS -> 환경변수 영역(Process마다)

부모프로세스 -> fork(create process) -> 자식프로세스
  환경변수 복사가 일어남(***)
 
$ export SAMPLE=hello (SAMPLE = HELLO 는 에러발생)
  관례적으로 환경변수 이름은 대문자 

cf. set SAMPLE=hello (windows)

$ echo $SAMPLE
환경변수의 값 확인

cf. echo %SAMPLE% (windows)

$ env     cf. set (windows)
전체 환경변수 내용 출력






https://wikidocs.net/28556


https://towardsdatascience.com/interactively-analyse-100gb-of-json-data-with-spark-e018f9436e76
# docker exec it bash

wget --continue http://openlibrary.org/data/ol_cdump_latest.txt.gz 

wget https://s3-eu-west-1.amazonaws.com/csparkdata/ol_cdump.json  

gzip ol_cdump.json

bzip2 ol_cdump.json

# apt update

var df=spark.read.json("/data/ol_cdump.json")
df.write.parquet("/data/ol_cdump")
val cdumpDF=spark.read.parquet("/data/ol_cdump")
cdumpDF.select("*").write.saveAsTable("cdump")
cdumpDF.select("authors","genres","title","type","isbn_10","number_of_pages","languages").write.saveAsTable("cdump")
spark.sql("SELECT count(*) FROM cdump").show()

spark.sql("SELECT * from cdump limit 10").show()

spark.sql("SELECT count(distinct authors) from cdump").show()

spark.sql("SELECT authors,genres,title,type,isbn_10,number_of_pages,languages from cdump  order by title desc limit 10").show()

spark.sql("SELECT authors,genres,title,type,isbn_10,number_of_pages,languages from cdump where genres is not null order by number_of_pages desc limit 10").show()

spark.sql("SELECT authors,genres,title,type,isbn_10,number_of_pages,languages from cdump where title like '%travel%' limit 20").show()


val df = spark.read.json("/data/people.json")
df.select("*").write.saveAsTable("people")

sql("select * from people").show()

val personDF=spark.sql("SELECT distinct authors from cdump")
personDF.select("*").write.saveAsTable("person")
sql("select * from person").show()


https://moons08.github.io/programming/spark_melting/
val data = sc.parallelize(Seq(
    """{"userId": 1, "someString": "example1",
        "Date": [20190101, 20190102, 20190103], "val": [1, 2, 9]}""",
    """{"userId": 2, "someString": "example2",
        "Date": [20190101, 20190103, 20190105], "val": [9, null, 6]}"""
))

val df = spark.read.json(data)

df.printSchema

import org.apache.spark.sql.functions.{udf, explode}

val zip = udf((xs: Seq[Long], ys: Seq[Long]) => xs.zip(ys))

df.withColumn("result", explode(zip('Date, 'val))).select('userId, 'someString,$"result._1".alias("date"), $"result._2".alias("value")).show
val cdumpDF=spark.read.parquet("/data/ol_cdump")


df.withColumn("result", explode(arrays_zip($"date", $"val"))).select($"userId", $"someString", $"result.date", $"result.val").show

cdumpDF.printSchema
root
 |-- authors: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- author: struct (nullable = true)
 |    |    |    |-- key: string (nullable = true)
 |    |    |-- key: string (nullable = true)
 |    |    |-- type: string (nullable = true)
 
df.printSchema
root
 |-- Date: array (nullable = true)
 |    |-- element: long (containsNull = true)
 |-- someString: string (nullable = true)
 |-- userId: long (nullable = true)
 |-- val: array (nullable = true)
 |    |-- element: long (containsNull = true)
df.withColumn("result", explode(arrays_zip($"date", $"val"))).select($"userId", $"someString", $"result.date", $"result.val").show

 
val authorsDF=cdumpDF.select("authors")

authorsDF.withColumn("authors", explode(arrays_zip($"element",$"author"))).select( $"element.key", $"element.type").show

cdumpDF.withColumn("authors", explode(arrays_zip($"element",$"author"))).select( $"element.key", $"element.type").show

cdumpDF.withColumn("result", explode(arrays_zip($"authors"))).select( $"result").printSchema

cdumpDF.withColumn("result", explode(arrays_zip($"authors"))).select( $"result").printSchema
root
 |-- result: struct (nullable = false)
 |    |-- authors: struct (nullable = true)
 |    |    |-- author: struct (nullable = true)
 |    |    |    |-- key: string (nullable = true)
 |    |    |-- key: string (nullable = true)
 |    |    |-- type: string (nullable = true)
 
 cdumpDF.withColumn("result", explode(arrays_zip($"authors"))).select( $"result")
 cdumpDF.withColumn("authors", explode(arrays_zip($"author"))).select( $"authors.key")
 
 cdumpDF.select($"author",explode($"author")).printSchema
  
 cdumpDF.select($"author",explode($"authors")).printSchema
 
 cdumpDF.withColumn("result", explode(arrays_zip($"authors"))).select($"authors",  $"result.author").show


cdumpDF.withColumn("authors", explode(arrays_zip($"authors"))).printSchema
authors


cdumpDF.select($"authors",explode($"authors")).printSchema


authorsDF.select("*").show

authorsDF.select("*").write.saveAsTable("authors")


sql("select * ,cols from authors LATERAL VIEW explode(authors) as cols").show()


df2.withColumn("cols",explode($"authors")).select($"author",$"cols.key",$"cols.type").show


authorsDF.withColumn("cols",explode($"authors")).select($"element").show


authorsDF.select(explode($"authors")).show(false)



authorsDF.select(explode($"authors")).select($"col.author").show

authorsDF.select(explode($"authors")).printSchema



val df2=df.select($"authors")
authorsDF.select(explode($"authors")).select($"col.author",$"col.key",$"col.type").show

val df = spark.read.json("/data/ol_cdump.json")
val df2=df.select($"authors")

val df3=df.select(regexp_replace($"authors","/authors/",""))




df2.select(explode($"authors")).select($"col.author",$"col.key",$"col.type").show


authorsDF.printSchema

df2.select(explode($"authors")).select(replace($"col.author","null",""),$"col.key",$"col.type".alias("11")).show

df2.select(explode($"authors")).select($"col.author",$"col.key",$"col.type".alias("11")).show

df2.select(explode($"authors")).select(regexp_replace($"col.author","null",""),regexp_replace($"col.key","/authors/",""),$"col.type").show(false)


val df3=df.select(regexp_replace($"authors","/authors/",""))

df2.select(explode($"authors")).select(regexp_replace($"col.author","null",""),regexp_replace($"col.key","/authors/",""),$"col.type").show(false)


df2.select(explode($"authors")).select(regexp_replace($"col.author","null"," "),regexp_replace($"col.key","/authors/",""),$"col.type").show(false)


df2.select(explode($"authors")).select(regexp_replace($"col.author","null",""),regexp_replace($"col.key","/authors/",""),split($"col.type","/",-1)).show(false)


df2.select(explode($"authors")).select(regexp_replace($"col.author","null",""),regexp_replace($"col.key","/authors/",""),regex_extract(split($"col.type",":",-1)).show(false)


val df = spark.read.json("/data/ol_cdump.json")
val df2=df.select($"authors")

df2.select(explode($"authors")).select(regexp_replace(concat(regexp_replace($"col.author","null",""),regexp_replace($"col.key","/authors/","")),"null","").alias("author"),split($"col.type",":",-1)).show(false)

df2.select(explode($"authors")).select(regexp_replace(regexp_replace(concat($"col.author",$"col.key"),"/authors/",""),"null",""),split($"col.type",":",-1)).show(false)

val df = spark.read.json("/data/ol_cdump.json")
val df2=df.select($"authors")
df2.select(explode($"authors")).select(regexp_replace($"col.key","/authors/","").alias("autor"),regexp_replace($"col.author","null","").alias("sub_author"),split($"col.type",":",-1).alias("type_info")).show(false)


# ova

https://drive.google.com/u/0/uc?id=1fhb-Q-NL7DEoO_P6ZaALAdYRIzvfbZbK&export=download


