####################################
#### spark and scala installation.
####################################

# Ubuntu-20.04: ubuntu
apt-get install -y scala
su - ubuntu


# centOS 7: hdroot
yum -y update
su - hdroot
wget http://downloads.lightbend.com/scala/2.11.8/scala-2.11.8.rpm
yum -y install scala-2.11.8.rpm
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.13.0.8-1.el7_9.x86_64




# common
cd /data

wget https://dlcdn.apache.org/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz
tar xvfz spark-3.2.0-bin-hadoop3.2.tgz
cd spark-3.2.0-bin-hadoop3.2


# editProp
"""
export SCALA_HOME=/usr/bin

export SPARK_HOME=/data/spark-3.2.0-bin-hadoop3.2/
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
"""

cd $SPARK_HOME/conf
cp spark-env.sh.template spark-env.sh

# vi spark-env.sh
"""
export SPARK_HOME=/data/spark-3.2.0-bin-hadoop3.2
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
"""

scala -version
spark-shell

start-dfs.sh
start-yarn.sh
jps

hdfs dfsadmin -safemode forceExit
hdfs dfs -rm -r -f /output/*

hdfs dfs -ls -h /input

spark-shell 
val textFile=sc.textFile("hdfs://127.0.0.1:9000/input/README.txt")
val counts=textFile.flatMap(line=> line.split(" ")).map(word=>(word,1)).reduceByKey(_+_)
counts.saveAsTextFile("hdfs://127.0.0.1:9000/output/scala_README.txt")
val textFile=sc.textFile("hdfs://127.0.0.1:9000/input/2M.ID.CONTENTS")
val counts=textFile.flatMap(line=> line.split(" ")).map(word=>(word,1)).reduceByKey(_+_)
counts.saveAsTextFile("hdfs://127.0.0.1:9000/output/scala_2M.ID.CONTENTS")
:q

hdfs dfs -cat /output/scala_2M.ID.CONTENTS/** | more

# Streaming 
https://wikidocs.net/28982







# cent7  
yum -y install docker
systemctl start docker

systemctl enable docker


# ubuntu
apt-get -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) \
stable"
apt-get update -y
apt-get -y install docker-ce docker-ce-cli containerd.io


# sudo /usr/sbin/groupadd -f docker
# sudo /usr/sbin/usermod -aG docker hdroot 
# sudo chown root:docker /var/run/docker.sock


# common 
docker run -it -v /data:/home/jovyan/work -p 8888:8888 jupyter/all-spark-notebook



spark-shell

"""
import org.apache.spark._
import org.apache.spark.streaming._

val ssc = new StreamingContext(sc, Seconds(5))      // 5????????? ?????? ?????? 
val lines = ssc.socketTextStream("127.0.0.1", 9999) // ???????????? ?????? ?????? IP, port ??????.
// 127.0.0.1 IP??? ?????????(????????? ????????? ???), docker ps -a ??? ??????????????? ?????? ???, 
//d ocker inspect adoring_chaplygin(???????????????) | grep IPAddress ?????? IP ???????????? ???????????? ??????

val words = lines.flatMap(_.split(" "))
val pairs = words.map(word => (word, 1))
val wordCounts = pairs.reduceByKey(_ + _)
wordCounts.print()

ssc.start()             // ????????? ?????? ?????? 
ssc.awaitTermination()      // ????????? ???????????? ?????? ?????? 
"""


# ????????? ????????????.

docker ps -a
docker exec -it ner...  bash
nc -l  9999






# Window Transformation
su - hdroot

start-dfs.sh
start-yarn.sh
hdfs mkdir -p /data/spark_tmp/checkpoint
cd /data/spark_tmp/

spark-shell
"""
import org.apache.spark._
import org.apache.spark.streaming._

val ssc = new StreamingContext(sc, Seconds(5))
val lines = ssc.socketTextStream("192.168.0.118", 9999)
val words = lines.flatMap(_.split(" "))
val pairs = words.map(word => (word, 1))
val wordCounts = pairs.reduceByKey(_ + _)

// ?????? ????????? ?????? 
ssc.checkpoint("/checkpoint")
// ????????? ????????????????????? ?????? 
val wordCountWindow = wordCounts.reduceByKeyAndWindow( 
    {(x, y) => x + y}, // ????????? ???????????? ????????? ???????????? ?????? 
    {(x, y) => x - y}, // ???????????? ???????????? ????????? ?????? ?????? 
    Seconds(30), // ????????? ?????? 
    Seconds(10)  // ???????????? ?????? 
)
wordCountWindow.print()

ssc.start()
ssc.awaitTermination()
"""








