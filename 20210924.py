데이터베이스 CRUD(read/write) 
   읽기 최적화 기술 -> 쓰기 최적화는 NoSQL
   인덱스 추가 -> B트리/해시/전문검색 인덱스 
      인덱스 달아도 느리다면? -> 샤딩 / 파티셔닝 / 복제(다중화)

DBMS의 연결(샤딩/파티셔닝/복제) ->  수 십 대
빅데이터는 만 단위임

빅데이터는 파일시스템 레벨에서 병렬화/복제 지원
DBMS는 파일시스템은 일반 -> 응용프로그램레벨에서 병렬화 복제 지원하는 구조

Infrastructure 측면의 변화

1. MSA(Micro-service Architecture)
   전자정부프레임워크의 기반 스프링 프레임워크 
   Spring Framework 4.x -> 5.x(Spring Cloud)

2. Cloud(AS-IS vShpere)   cf. KISA 클라우드 보안인증제
   TCO(총보유비용) 관점  

3. VMWare vShpere->docker(컨테이너기반 가상화)+kubernetes
   가상화의 이유 -> Utilization 때문
      실제 서버에서 가상화 사용율 99%
   가상화(효율 90%) -> 컨테이너기반 가상화(효율 97%)

빅데이터와 클라우드/MSA

데이터베이스 1USER/5USER/10USER/UNLIMITED

ORACLE xe(무료) / 10억(unlimited)
cf. 키파일 

Lazy loading 

프로그램 -> 접속/쿼리 -> DBMS  
   접속 -> 1s -> 쿼리 

접속하면 실제 커넥션 할당(X)
쿼리가 날라오면 실제 커넥션 할당(O)


전체시스템 효율 재고(스파크에서는 적극적으로 활용)

b = f(a);
c = g(b);
d = h(c);

리니지(Lineage)
  a(최초입력) -> f() -> b -> g() -> c -> h() -> d(최종출력)

변환함수 / 액션함수 / error내성
  액션함수가 최소 하나는 있어야 한다

a,b,c,d => 수정 불가능(금지)

상수/변수 -> 값을 바꿀 수 없는 변수 -> mutable / immutable
cf. RAM/Flash Memory(고속 ROM)/ROM -> volatile/non-volatile
    SSD NVME/SATA

int a = 5;
a = 10;
System.out.println(a);

final int a = 5;
a = 10;

scala(언어) -> 변수(var)/상수(val)

var a => 변수 a / val a => 상수 a

***** 스파크(스칼라로 짠 빅데이터 프레임워크) RDD = 스칼라(언어) val 

javascript arrow function(lambda)

closure(자바스크립트/파이썬)

로컬 변수 / 전역 변수
1. 함수 안에서 변수 정의 -> local(stack)
2. 함수 밖에서 변수 정의 -> global(heap)

변수의 저장위치(heap/stack)

클로저(closure)
  함수의 리턴값을 코드를 리턴 -> 코드 안에 로컬변수의 값을 넣음 
  리턴된 코드를 함수실행(eval) -> 유효함(함수호출 종료이후)

클로저의 활용용도
  전역변수의 대안

docker.com에서 docker desktop 다운로드 & 설치

# powershell에서,
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart


dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

#다음 파일 다운로드 후 설치
https://docs.microsoft.com/ko-kr/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package



wsl --set-default-version 2
wsl --install -d ubuntu
wsl --set-default Ubuntu
wsl --set-version Ubuntu 2
wsl --update
wsl --shutdown 
wsl


kaydash
[원하는암호입력]
[원하는암호입력]
sudo su - root
[원하는암호입력]
passwd
[원하는암호입력]
[원하는암호입력]

윈도우 파일탐색기: \\wsl$



cd /data
wsl -e docker run -it -v /data:/home/jovyan/work -p 8888:8888 jupyter/all-spark-notebook

#[Trouble Shooting]
# 만약 dial unix /var/run/docker.sock: connect: permission denied 오류를 만나는 경우,
ll /var/run/docker.sock=
# srw-rw---- 1 root docker 0 Oct  8 09:16 /var/run/docker.sock=
id
# uid=1000(kaydash) gid=1000(kaydash) groups=1000(kaydash),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),117(netdev)
sudo /usr/sbin/groupadd -f docker
sudo /usr/sbin/usermod -aG docker kaydash
sudo chown root:docker /var/run/docker.sock
exit
wsl --shutdown 
wsl

# [끝]





#웹브라우저에서 접속
http://127.0.0.1:8888/?token=...............


# new-> spylon-kernel(scala)

print("Hello")
print(2+3)

var arr = Array(1, 2, 3, 4, 5)
arr = Array(1,2,3) // error


# new -> python3

print("hello")
pritn(2+3)

# new -> sample.txt
i am a boy.
you are a girl.



