# sqoop
cd /data
wget http://archive.apache.org/dist/sqoop/1.99.7/sqoop-1.99.7-bin-hadoop200.tar.gz
tar xvfz sqoop-1.99.7-bin-hadoop200.tar.gz

# mysql
cd /data
yum install -y https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
yum install -y mysql-server
mysqld -V
systemctl enable mysqld && systemctl start mysqld && systemctl status mysqld
grep 'temporary password' /var/log/mysqld.log
mysql -u root -p
ALTER USER 'root'@'localhost' IDENTIFIED BY 'Apple123!Apple123!';
set global validate_password.policy='LOW';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'anjsep2!';
flush privileges;
exit;

# MySQL JDBC 드라이버 설치
cd /data
wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.27-1.el7.noarch.rpm
yum -y install mysql-connector-java-8.0.27-1.el7.noarch.rpm

chown -R hdroot:hdroot 

#다음 게시물을 따라함.: https://abc2080.tistory.com/entry/sqoop-%EC%84%A4%EC%B9%98


#드라이버,하둡파일 복사
cp /usr/share/java/mysql-connector-java.jar $SQOOP_HOME/tools/lib/
\cp -r $HADOOP_HOME/share/hadoop/mapreduce/* $SQOOP_HOME/tools/lib/


#동작확인(MySQL 테스트 DB world가 있어야 함)
sqoop import --connect jdbc:mysql://127.0.0.1/mysql?useSSL=false \
--username root --table users -P anjsep2!



mkdir /var/lib/sqoop2
#\cp -R $HADOOP_HOME/*.jar /var/lib/sqoop2/
#\cp -R $HADOOP_HOME/lib/*.jar /var/lib/sqoop2/
\cp -R $HADOOP_HOME/share/hadoop/common/*.jar /var/lib/sqoop2/
\cp -R $HADOOP_HOME/share/hadoop/common/lib/*.jar /var/lib/sqoop2/
\cp -R $HADOOP_HOME/share/hadoop/hdfs/*.jar /var/lib/sqoop2/
\cp -R $HADOOP_HOME/share/hadoop/hdfs/lib/*.jar /var/lib/sqoop2/
\cp -R $HADOOP_HOME/share/hadoop/mapreduce/*.jar /var/lib/sqoop2/
\cp -R $HADOOP_HOME/share/hadoop/mapreduce/lib-examples/*.jar /var/lib/sqoop2/
\cp -R $HADOOP_HOME/share/hadoop/yarn/*.jar /var/lib/sqoop2/
\cp -R $HADOOP_HOME/share/hadoop/yarn/lib/*.jar /var/lib/sqoop2/
chown -R hadoop:hadoop /var/lib/sqoop2