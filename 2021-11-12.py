vi $HOME/docker-compose.yaml
# from https://victorydntmd.tistory.com/347
#      https://raw.githubusercontent.com/wurstmeister/kafka-docker/master/docker-compose.yml
"""
version: '2'
services:
  zookeeper:
    image: wurstmeister/zookeeper
    container_name: zookeeper
    ports:
      - "2181:2181"
  kafka:
    image: wurstmeister/kafka:2.12-2.5.0
    container_name: kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: 127.0.0.1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
"""

# docker-compose 설치
# CentOS의 경우
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

#ubuntu의 경우
apt install docker-compose -y



# docker-compose 실행 권한 부여
 sudo chmod +x /usr/local/bin/docker-compose

# 설치된 docker-compose 실행 확인
docker-compose --version


sudo chmod +x /var/run/docker.sock


#Kafka+Zookeeper 실행
docker-compose -f $HOME/docker-compose.yaml up -d

#실행확인(kafka, zookeeper이 모두 up인지 확인)
 sudo docker ps -a

# exit가 발생한다면(예를 들어 kafka), 다음과 같이 확인
docker logs kafka


# docker 종료
docker-compose -f $HOME/docker-compose.yaml down 


#주키퍼(컨테이너) IP주소 확인
sudo docker inspect zookeeper | grep IPAddress
# "IPAddress": "172.18.0.3"

#카프카(컨테이너) 접속
sudo docker exec -it kafka bash


# 토픽 생성
kafka-topics.sh --create --zookeeper 172.18.0.3 --replication-factor 1 --partitions 1 --topic test-Topic

# 토픽 리스트 확인
kafka-topics.sh --list --bootstrap-server localhost:9092

# 토픽 삭제
kafka-topics.sh --delete --zookeeper 172.18.0.3:2181 --topic test-Topic


# 토픽 재생성
kafka-topics.sh --create --zookeeper 172.18.0.3 --replication-factor 1 --partitions 1 --topic test-Topic


#producer
kafka-console-producer.sh --broker-list localhost:9092 -topic test-Topic
Hello
World


#consumer1
kafka-console-consumer.sh --bootstrap-server localhost:9092 -topic test-Topic --from-beginning

#consumer2
kafka-console-consumer.sh --bootstrap-server localhost:9092 -topic test-Topic --from-beginning


#consumer3
kafka-console-consumer.sh --bootstrap-server localhost:9092 -topic test-Topic


















