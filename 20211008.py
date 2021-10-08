
https://wikidocs.net/28556


https://towardsdatascience.com/interactively-analyse-100gb-of-json-data-with-spark-e018f9436e76
# docker exec it bash

wget --continue http://openlibrary.org/data/ol_cdump_latest.txt.gz 

wget https://s3-eu-west-1.amazonaws.com/csparkdata/ol_cdump.json  

gzip ol_cdump.json

bzip2 ol_cdump.json

# apt update


spark.sql("SELECT count(*) FROM cdump").show()

spark.sql("SELECT * from cdump limit 10").show()

spark.sql("SELECT count(distinct authors) from cdump").show()

spark.sql("SELECT authors,genres,title,type,isbn_10,number_of_pages,languages from cdump  order by title desc limit 10").show()

spark.sql("SELECT authors,genres,title,type,isbn_10,number_of_pages,languages from cdump where genres is not null order by number_of_pages desc limit 10").show()

spark.sql("SELECT authors,genres,title,type,isbn_10,number_of_pages,languages from cdump where title like '%travel%' limit 20").show()
