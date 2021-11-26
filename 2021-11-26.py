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
\cp /usr/share/java/mysql-connector-java.jar $SQOOP_HOME/tools/lib/
\cp -r $HADOOP_HOME/share/hadoop/mapreduce/* $SQOOP_HOME/tools/lib/
\cp /usr/share/java/mysql-connector-java.jar $SQOOP_HOME/server/lib/

#동작확인(MySQL 테스트 DB world가 있어야 함)
sqoop import --connect jdbc:mysql://127.0.0.1/mysql?useSSL=false \
--username root --table user --password 'hihi@2021'



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

cd /data
wget --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" https://download.oracle.com/otn-pub/java/jdk/8u191-b12/2787e4a523244c269598db4e85c51e0c/jdk-8u191-linux-x64.tar.gz


alternatives --install /usr/bin/java java /usr/local/java/jdk1.8.0_191/bin/java 1

alternatives --install /usr/bin/java javac /usr/local/java/jdk1.8.0_191/bin/javac 1

alternatives --install /usr/bin/java javaws /usr/local/java/jdk1.8.0_191/bin/javaws 1



alternatives --set java /usr/local/java/jdk1.8.0_191/bin/java

alternatives --set javac /usr/local/java/jdk1.8.0_191/bin/javac

alternatives --set javaws /usr/local/java/jdk1.8.0_191/bin/javaws


JAVA_HOME=/usr/local/java/jdk1.8.0_191

JRE_HOME=/usr/local/java/jdk1.8.0_191/jre

export PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin

sqoop2-server stop
sqoop2-server start

sqoop2-shell
show connector
