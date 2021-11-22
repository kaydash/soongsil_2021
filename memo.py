#WiFi
woori / w15885000



sharding
replication
OLAP
OLTP
VLDB(very large database) ; 초대형 데이터베이스.  이는 대개 테라바이트 규모의 데이터와 수십 억개의 레코드를 가지고 있는 데이터베이스를 가리킨다. 이런 류의 데이터베이스는 대개 의사결정지원시스템 또는 수많은 사용자들을 지원하는 트랜잭션 처리 프로그램에서 주로 사용된다.
RDBMS
DW
data lake
HDFS
Data Mining
Hadoop:(2011~)



DAS(Direct Attached Stroage  : USB, thunder bolt...
NAS(Network Attached Storage): LAN 연결
SAN(Storage Area Network)    : 광케이블 연결


빅데이터의 3V, 4V, 5V, 6V
3V: 규모(volume), 속도(velocity) , 다양성(variety) ★★★
4V: 규모(volume), 속도(velocity), 다양성(variety), 가치(value)
4V: 규모(volume), 속도(velocity), 다양성(variety), 진실성(veracity)
5V: 규모(volume), 속도(velocity), 다양성(variety), 가치(value), 진실성(veracity)
6V: 규모(volume), 속도(velocity), 다양성(variety), 가치(value), 진실성(veracity), variability(가변성)


빅데이터처리방식: scalable 방식으로 처리
scale-out
HA
중복성(Redundancy), 다중화 
병렬처리방식

 
하나의 HDFS에 하나의 네임스페이스 제공.
HDFS-블럭사이즈 기본값 64 MB, 실사용에는 128 MB 이상
비교:
	메모리-페이지-4K
	디스크-클러스터/섹터-4K

Overlay system
HDFS over [NTFS / exFAT / ext4FS / HPFS(mac)]
SAMBA(SMB) / Paragon NTFS

NameNode:파일의 메타정보를 저장. 데이터가 어디 있는지 알고 있음.-single point of failure(SPOF. 급소)
네임노드와 세컨더리 네임노드가 장애나면 어떻게 할 것인가(하둡 버전1에서 도출된 문제)


(Filenmae, numReplicas, block-ids,...)
	ex) /users/sameERP/data/part-0, r:2, {1,3}, ...

DataNode(파일블록이 저장되는 노드)


10,000대까지 병렬 연결 가능

백업 불요(내부적으로 2 또는 3 copy)



# MapReduce
WordCount Process: Splitting - Mapping - Shuffling - Reducing - Final result

HADOOP=HDFS+MapReduce


#Yarn: Application Manager(AM), Resource Manager(RM)
Job Tracker, TaskTrigger->노드매니저+리소스매니저
시스템리소스활용과 작업 진행관리를 분리.

#ZooKeeper
NameNode가 고가용성이 가능하도록 구성
	Master-Slave(수동)
	Active-StandBy(Hadoop 2)
		- 전환과정에서 지연시간 소요 문제 발생 가능성
	Active-Active(Hadoop 3)
		- 합의문제(Consensus 문제. Master 역할이 하나가 아니라서 Active 간 합의 필요)
		- 홀수로 구성	
		- election(선거)
		- 리소스매니저 이중화
		
		
# Hadoop Echo system(하둡 생태계): https://kr.cloudera.com/products/open-source/apache-hadoop.html
Hive: MapReduce using Query
Sqoop: export, import, query from RDBMS
Flume2: Webserver LogFile insert into Hadoop
HBase: HDFS to NoSQL
and so on..

# RAID
0:stripe
1:mirror
0+1:stripe and mirror 
1+0:mirror and stripe (내결함성에서 더 좋음)
5:parity check를 사용해서 복구. 3개이상의디스크 필요. 디스크 수 -1 만큼의 용량 사용. 쓰기 성능이 낮음
6:2개의 parity사용. 레이드 5 구성에 비해 더 높은 신뢰성 


# Spark
하둡에 비해 메모리 기반 수행을 통하여 110배까지 높은 성능을 낼 수 있음
대용량 데이터 분석에 목적이 있음
스칼라로 만들어짐(JVM 필요)
자바, 파이썬, R을 지원



