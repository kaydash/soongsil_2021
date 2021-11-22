# centos docker 설치
yum update -y --allowerasing --skip-broken --nobest
yum install yum-utils device-mapper-persistent-data lvm2 -y
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce -y

systemctl start docker
systemctl enable docker
systemctl status docker
docker -v


ssh-keygen -t rsa -P '' -f ~/.ssh/id_dsa
cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys
ssh-keygen -f /etc/ssh/ssh_host_rsa_key -t rsa -N "" -y
ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -t ecdsa -N "" -y
ssh-keygen -f /etc/ssh/ssh_host_ed25519_key -t ed25519 -N "" -y

readlink -f /usr/bin/javac
vim ~/.bashrc
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.302.b08-0.el8_4.x86_64/bin/javac


mkdir /hadoop_home
cd /hadoop_home
wget https://archive.apache.org/dist/hadoop/common/stable/hadoop-3.3.1.tar.gz
tar -xvzf hadoop-3.3.1.tar.gz

vim ~/.bashrc
export HADOOP_HOME=/hadoop_home/hadoop-3.3.1
export HADOOP_CONFIG_HOME=$HADOOP_HOME/etc/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin

/usr/sbin/sshd

source ~/.bashrc


cd $HADOOP_CONFIG_HOME
# cp mapred-site.xml.template mapred-site.xml

# edit files.
vi core-site.xml
<!-- core-site.xml -->
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/hadoop_home/temp</value>
    </property>

    <property>
        <name>fs.default.name</name>
        <value>hdfs://nn:9000</value>
        <final>true</final>
    </property>
</configuration>

vi hdfs-site.xml

<!-- hdfs-site.xml -->
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>2</value>
        <final>true</final>
    </property>

    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/hadoop_home/namenode_dir</value>
        <final>true</final>
    </property>

    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/hadoop_home/datanode_dir</value>
        <final>true</final>
    </property>
</configuration>


mkdir /hadoop_home/temp
mkdir /hadoop_home/namenode_dir
mkdir /hadoop_home/datanode_dir


 

vi mapred-site.xml

<!-- mapred-site.xml -->
<configuration>
    <property>
        <name>mapred.job.tracker</name>
        <value>nn:9001</value>
    </property>
</configuration>





/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.302.b08-0.el8_4.x86_64/bin/javac


export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.302.b08-0.el8_4.x86_64/bin/javac


