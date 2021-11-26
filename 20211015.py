[하둡 PDF 한글판 PC용 대용량 PDF]
https://drive.google.com/drive/folders/120HGGvykpcvCnrlBymu7MPSQbpNNuhjy?usp=sharing

[SecureCRT with Crack]
https://drive.google.com/file/d/1Qxp1HP2-6UREJJ1v328muMb12AfguaWO/view?usp=sharing

[VMwareWorkStation15_with_SerialKey]
https://drive.google.com/file/d/1E28QJ0GCvZKX4hBlykLrfk6o60fXm4B7/view?usp=sharing


# https://hadoop.apache.org/

# vm설정: CPU 2 core(1 thread per 1 core)  / RAM 10 GB 

# centos는 hdroot로 하둡을 실행하고, ubuntu는 ubuntu계정으로 하둡을 실행함.
##########################################################################
# centos #################################################################
##########################################################################
yum -y upgrade
yum -y install java-11-openjdk.x86_64
yum -y install java*jdk-devel
alternatives --config java





sestatus 
vi /etc/sysconfig/selinux
"""
SELINUX=disabled
"""
# reboot -f


vi ~/.bash_profile
"""
# add under all

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.13.0.8-1.el7_9.x86_64
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=$CLASSPATH:$JAVA_HOME/lib/*
CLASSPATH=.:$JAVA_HOME/jre/lib/ext:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/

export TMOUT=00

alias ll='ls -al'
alias showProp='cat ~/.bash_profile'
alias setProp='. ~/.bash_profile'
alias editProp='vi ~/.bash_profile'
alias ms='mysql -u root -poracle'

"""
. ~/.bash_profile




##########################################################################
# ubuntu #################################################################
##########################################################################

apt install -y galternatives
apt install -y openjdk-11-jdk
apt install -y openjdk-11-jre-headless 
apt install -y default-jre             
apt install -y openjdk-13-jre-headless 
apt install -y openjdk-16-jre-headless 
apt install -y openjdk-17-jre-headless 
apt install -y openjdk-8-jre-headless  
apt install -y openjdk-11-jdk-headless


vi ~/.bashrc
"""


export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=$CLASSPATH:$JAVA_HOME/lib/*
CLASSPATH=.:$JAVA_HOME/jre/lib/ext:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/

export TMOUT=00

alias ll='ls -al'
alias showProp='cat ~/.bashrc'
alias setProp='. ~/.bashrc'
alias editProp='vi ~/.bashrc'
alias ms='mysql -u root -poracle'

"""
. ~/.bashrc


# note: java place=> which java;file java; 
# (i.g.) /usr/lib/jvm/java-11-openjdk-amd64/bin/java

#common 

mkdir /data
cd /data
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
tar xvfz hadoop-3.3.1.tar.gz

#if wget error: echo "check_certificate = off" >> ~/.wgetrc



cd /data/hadoop-3.3.1/etc/hadoop/



vi /data/hadoop-3.3.1/etc/hadoop/hadoop-env.sh
"""
# edit vars
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# CentOS의 경우,
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.13.0.8-1.el7_9.x86_64

export HADOOP_HOME=/data/hadoop-3.3.1

"""

# config
# https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#Pseudo-Distributed_Operation


vi /data/hadoop-3.3.1/etc/hadoop/core-site.xml
vi /data/hadoop-3.3.1/etc/hadoop/hdfs-site.xml
vi /data/hadoop-3.3.1/etc/hadoop/mapred-site.xml
vi /data/hadoop-3.3.1/etc/hadoop/yarn-site.xml

mkdir /data/hdfs_dir
vi /data/hadoop-3.3.1/etc/hadoop/core-site.xml
"""
# append this property
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/data/hdfs_dir</value>
    </property>
"""


ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys

ssh localhost
yes
exit

# centos ( ubuntu는 hdroot를 ubuntu로, bash_profile을 bashrc로 바꿔어서 수행
useradd -m hdroot
passwd hdroot
# mkdir /home/hdroot

chown -R hdroot:hdroot /home/hdroot
chown -R hdroot:hdroot /data 

su - hdroot

vi ~/.bash_profile
"""

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.13.0.8-1.el7_9.x86_64
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=$CLASSPATH:$JAVA_HOME/lib/*
export CLASSPATH=.:$JAVA_HOME/jre/lib/ext:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/

export TMOUT=00

alias ll='ls -al'
alias showProp='cat ~/.bash_profile'
alias setProp='. ~/.bash_profile'
alias editProp='vi ~/.bash_profile'
alias ms='mysql -u root -poracle'

export HADOOP_HOME=/data/hadoop-3.3.1
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
export HADOOP_CONF_DIR=/data/hadoop-3.3.1/etc/hadoop


"""


# ubuntu 
vi ~/.bashrc




""""""

ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys


ssh localhost
yes
exit


hdfs namenode -format
ls -al /home/hdroot/data/hdfs_dir
start-dfs.sh
start-yarn.sh
jps

hdfs dfs -mkdir /input
hdfs dfs -put $HADOOP_HOME/README.txt /input
hdfs dfs -ls /input

hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar wordcount /input/README.txt /output

hdfs dfs -ls /output

cd /data/hadoop-3.3.1/share/hadoop/mapreduce/sources
jar xvf hadoop-mapreduce-examples-3.3.1-sources.jar

cd /data/hadoop-3.3.1/share/hadoop/mapreduce/sources/org/apache/hadoop/examples
cat WordCount.java | wc -l


cd /data

wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1oaq1XvmPSyLBrtZkpncuC7YpG10tQi8U' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1oaq1XvmPSyLBrtZkpncuC7YpG10tQi8U" -O data.tar.gz && rm -rf /tmp/cookies.txt

tar xvfz data.tar.gz
cd /data/data
ls
pwd
head 2M.ID.CONTENTS

hdfs dfs -put 2M.ID.CONTENTS /input
hdfs dfs -ls -h /input | grep "2M"
date;
time hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar wordcount /input/2M.ID.CONTENTS /output_wiki
date;
hdfs dfs -ls /output_wiki


# hdfs dfs -rmr [hdfs_dir]


"""
2021-10-15 03:56:28,615 INFO mapreduce.Job: Job job_1634283465389_0001 completed successfully
2021-10-15 03:56:28,790 INFO mapreduce.Job: Counters: 55
        File System Counters
                FILE: Number of bytes read=1197513246
                FILE: Number of bytes written=1685041483
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=2507067838
                HDFS: Number of bytes written=212595228
                HDFS: Number of read operations=62
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Killed map tasks=3
                Launched map tasks=22
                Launched reduce tasks=1
                Data-local map tasks=22
                Total time spent by all maps in occupied slots (ms)=3776861
                Total time spent by all reduces in occupied slots (ms)=489519
                Total time spent by all map tasks (ms)=3776861
                Total time spent by all reduce tasks (ms)=489519
                Total vcore-milliseconds taken by all map tasks=3776861
                Total vcore-milliseconds taken by all reduce tasks=489519
                Total megabyte-milliseconds taken by all map tasks=3867505664
                Total megabyte-milliseconds taken by all reduce tasks=501267456
        Map-Reduce Framework
                Map input records=2099659
                Map output records=395115094
                Map output bytes=4084548252
                Map output materialized bytes=482076923
                Input split bytes=2033
                Combine input records=439307343
                Combine output records=72679098
                Reduce input groups=15113862
                Reduce shuffle bytes=482076923
                Reduce input records=28486849
                Reduce output records=15113862
                Spilled Records=101165947
                Shuffled Maps =19
                Failed Shuffles=0
                Merged Map outputs=19
                GC time elapsed (ms)=70396
                CPU time spent (ms)=999900
                Physical memory (bytes) snapshot=9346387968
                Virtual memory (bytes) snapshot=60240384000
                Total committed heap usage (bytes)=7324303360
                Peak Map Physical memory (bytes)=674742272
                Peak Map Virtual memory (bytes)=3028856832
                Peak Reduce Physical memory (bytes)=585920512
                Peak Reduce Virtual memory (bytes)=3017596928
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=2507065805
        File Output Format Counters
                Bytes Written=212595228

real    13m3.087s
user    0m17.745s
sys     0m3.256s
[hdroot@centos7 ~]$

"""

hdfs dfs -ls -h /output_wiki/

"""
Found 2 items
-rw-r--r--   1 hdroot supergroup          0 2021-10-15 03:56 /output_wiki/_SUCCESS
-rw-r--r--   1 hdroot supergroup    202.7 M 2021-10-15 03:56 /output_wiki/part-r-00000

"""


hdfs dfs -cat /output_wiki/part-r-00000 | grep "world" | awk '{sum += $2} END {print sum}' 

# cat sample.lst | awk '{sum += $2} END {print sum}' 

time hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar wordcount /input/2M.ID.CONTENTS /output_wiki2 > wordCount_wiki.log 2>&1 &