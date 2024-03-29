---
categories:
  - computerNetwork
---

# 컴퓨터 네트워크 스터디 1주차

## 컴퓨터 네트워크

네트워크는 Net+Work의 합성어로써 컴퓨터들이 통신 기술을 이용해 그물망처럼 서로 연결된 통신이용 형태이다.

즉 두 대 이상의 컴퓨터를 연결하고 서로 통신할 수 있는 것을 말한다.

과거 ARPANET이 데이터를 패킷단위로 잘라서 취급하는 패킷 교환 네트워킹 방식을 현재까지 사용한다.

또한 다른 환경의 컴퓨터들과의 통신을 위해 여러 프로토콜들이 정의된다.

## 컴퓨터 네트워크에서 데이터를 전송하는 방식

데이터 전송하는 방법에는 2가지가 있다.

### 회선 교환 방식

회선 교환방식은 데이터를 교환하기 위해 일대일의 전송로를 만들고 교환이 종료될 때까지 전송로를 계속해서 유지하는 방식이다.

우리가 통화할때 상대방이 통화종료하기 전까지 수화기를 계속해서 듣고 있는 것과 비슷하다.

회선을 점유하여 사용하기 때문에 안정적인 통신 품질을 유지할 수 있다는 장점이 있으나, 데이터가 흐르지 않을때도 회선이 연결되어 있다는 특징 때문에 회선 이용 효율이 낮다는 단점이 치명적이라 현재는 적합하지 않은 데이터 전송방법이다.

### 패킷 교환 방식

상술한 회선 교환 방식의 단점인 회선 이용 효율을 향상할 목적으로 고안된 데이터 전송 방식이다.

패킷 교환 방식은 데이터를 패킷이라 부르는 작은 단위로 나누어 보냅니다. 패킷은 데이터와 헤더로 이루어지는데, 헤더에 수신 컴퓨터 정보, 데이터 중 몇 번째의 패킷인지등 다양한 정보들을 포함한다.

송신 컴퓨터는 패킷의 헤더 정보를 보고 수신 컴퓨터로 패킷을 배달하고, 수신 컴퓨터는 헤더의 정보를 보고 헤더를 제가하여 데이터를 취한다.

## _프로토콜(Protocol)_

단순히 패킷을 주고 받았다고 해서 통신이 성공적으로 이루어질 수 없다.  
또한 과거에는 통신 규약이 정립되어 있지 않았기 때문에, 다른 회사의 제품을 쓰면 서로 호환이 안되는 문제가 있었다.  
이러한 문제를 해결하기 위해서 패킷을 처리하기 위한 규칙을 만들었고, 이것이 프로토콜이다.

대표적으로는 우리가 자주쓰는 HTTP가 프로토콜의 일종이다.

### 프로토콜의 구성요소

통신 규약인 프로토콜에는 다양한 것들이 포함되어 있는데, 물리적 사양, 송신 상태 특정, 패킷 전송, 신뢰성 확립, 보안 확보 등이 포함되어 통신을 원활하게 한다.

#### 물리적 사양

LAN 케이블 소재, 커넷터 형테, 핀 할당의 하드워어 측면들도 프로토콜에 정의되어 있다. 우리가 매일 쓰는 와이파이의 전파 주파수, 패킷의 전파 변환 방식 또한 프로토콜에 포함된다.

#### 송신 상대 특정

네트워크에서 신호를 보낼 대상을 특정하는 것도 프로토콜에 포함된다.

#### 패킷 전송

상술한 바와 같이 패킷 교환 방식에서는 단순 데이터 뿐만 아니라 메타 데이터들을 헤더에 포함하여 주고 받는다. 이때 몇번째 비트부터 몇번째 비트까지가 헤더인지.. 등의 규칙 또한 프로토콜에 의해 정의된다.

#### 신뢰성 확립

우리는 과연 주고 받은 패킷의 데이터들을 신뢰할 수 있을까?

이를 위해 에러 검출과 같은 과정이 필요하게 되는데, 이 또한 프로토콜에 의해 정의된다.

#### 보안 확보

공공인증서, 개인정보와 같은 민감한 정보들을 주고 받음에 있어서 보안성을 높이기 위해 암호화/복호화 과정이 필요하다. 역시 프로토콜에 의해 정의된다.

## _Protocol 계층 모델_

프로토콜은 무수히 많다.

각 프로토콜이 기능하는 것을 처리에 맞춰 계층 구조로 분류할 수 있는데, 이러한 프로토콜 계층을 OSI 7계층 모델 혹은 TCP/IP 모델로 나타낼 수 있다.

OSI 7계층 모델은 이론적이고, 현실에서 잘 쓰이지 않지만 네트워크 개념들이 이에 파생하였기 때문에 매우 중요한 모델이다.

TCP/IP 모델은 실용성에 초점이 맞추어 개발된 모델이기 때문에 현재 대부분의 프로토콜이 TCP/IP 참조 모델에 대응된다. (많이 쓰인다.)

### OSI 7 Layers

![OSI 7계층](https://velog.velcdn.com/images/pppp0722/post/c3a64a22-e99b-414a-a228-8302ec874542/image.png)

그러면 각 계층이 하는 역할을 알아보자.

우리가 프로그래밍 언어를 나눌때 하드웨어 친화적이면 Low-Level, 사람 친화적이면 High-Level로 구분하는 것과 비슷하다.

#### 물리 계층(L1)

디지털 데이터를 전기 신호, 광 신호, 전파로 변환해 네트워크로 보낸다.
즉 완전히 하드웨어와 가까운 계층이다.

PDU라고 하기엔 부족하지만 비트단위로 데이터를 다룬다고 볼 수 있다.

#### 데이터 링크 계층(L2)

물리 계층의 신뢰성을 확보하고, 같은 네트워크에 있는 단말과의 연결성을 확보한다.

MAC주소를 이용하여 알맞는 수신 단말을 찾는다.

PDU는 프레임이다.

#### 네트워크 계층(L3)

다른 네트워크에 있는 단말과의 연결성을 확보한다.

IP주소를 이용하여 알맞은 네트워크를 찾는다.

PDU는 패킷이다.

#### 전송 계층(L4)

애플리케이션 식별 및 그에 따라 통신을 제어한다.

포트 번호를 이용해 알맞은 애플리 케이션을 식별하는데 예를 들어 HTTP는 80번, HTTPS는 443번으로 정의되어있다.

PDU는 세그먼트(TCP) 혹은 데이터그램(UDP)이다.

#### 세션 계층(L5)

애플리케이션 데이터를 송신하기 위한 논리적 통신로(세션)을 관리한다.

#### 표현 계층(L6)

애플리케이션 데이터를 통신 가능한 방식으로 변환한다.

#### 애플리케이션 계층(L7)

사용자와 가장 가까운 High-Level 계층으로서 사용자에게 애플리케이션을 제공한다.

PDU는 메세지이다.

### _TCP/IP_

![TCP/IP](https://media.geeksforgeeks.org/wp-content/uploads/20230417045622/OSI-vs-TCP-vs-Hybrid-2.webp)

OSI 7계층을 실용성 있게 단순화한 버전이라고도 볼 수 있다. (실제로 두 모델은 아예 상관이 없는 독립적인 모델이긴 하지만)

대부분의 프로토콜이 TCP/IP 프로토콜에 대응하는 형태로 만들어져 있다.

#### 링크 계층

같은 네트워크에 있는 단말과의 연결성을 확보한다.

#### 인터넷 계층

다른 네트워크에 있는 단말과의 연결성을 확보한다.

#### 전송 계층

애플리케이션 식별 및 그에 대한 통신을 제어한다.

#### 애플리케이션 계층

사용자에게 애플리케이션을 제공한다.

## 프로토콜을 계층화하는 이유

OSI 7계층과 TCP/IP는 보면 프로토콜은 계층 구조로 분류되는 것을 확인 할 수 있다. 이렇게 계층화 한 이유는

#### 변경의 용이함

특정 계층에서 변경이 필요할 경우 해당 프로토콜 전체를 완전히 수정하지 않아도, 해당 레이어만 바꾸면 된다.

#### 포괄성

주어진 계층에서 같은 통신 프로토콜만 사용한다면 다른 HW/SW를 사용한다 하더라도 통신이 가능하다.

### 투명성

각 계층의 역할을 명확히 분리함으로써 상위계층은 하위계층의 세부구현에 대해 신경쓰지 않아도 된다.

## 컴퓨터 네트워크에서 캡슐화와 비캡슐화

송신 단말에서 데이터를 보낼 때 상위 계층에서 하위 계층으로 가면서 해당하는 계층에서의 데이터의 복호화를 위한 헤더(트레일러)가 붙는다.

이 과정을 캡슐화라고 한다.

반대로 송신 단말은 이렇게 데이터에 헤더(트레일러)들이 붙은 상태의 신호를 받게 되고, 헤더를 읽고 알맞은 상위 계층으로 올려보냄과 동시에 헤더를 제거한다.

이 과정이 비캡슐화이다.

## NIC, 리피터, 리피터 허브(물리 계층/L1 기기)

NIC는 Network Interface Card의 약어이다. 말그래도 네트워크 인터페이스이다.

우리가 렌선을 꼽는 그 구멍을 포함하는 카드를 칭한다.

모든 네트워크 단말은 애플리케이션과 운영체제가 처리한 패킷을 이 NIC를 이용해 네트워크로 내보낸다.

Repeater는 반복하는 놈, 즉 신호를 증폴하시켜는 기기이다. LAN 케이블의 전류는 거리에 비례하여 감쇠하게 되는데, 이를 리피터가 다시 증폭시킨다.

그러나 요즘은 감쇠가 잘 일어나지 않는 광섬유 케이블을 사용하기에 리피터는 사용하지 않는 추세이다.

리피터 허브는 전달받은 패킷의 복사본은 그대로 다른 모든 포트에 전송하는 기기이다.

이 리피터 허브는 L2스위치(단순히 모두 전달하는 것을 넘어서 특정한 포트에만 줄 수 있음)로 대체되었다.

## 브릿지, L2 스위치(데이터 링크 계층/L2기기)

브릿지는 포트와 포트 사이의 다리역할을 하는 놈이다.

단말에서 처리된 패킷의 MAC주소를 보고 알맞은 MAC주소를 가진 포트로 전송한다. 이 과정을 브리징이라 하고, MAC 주소를 MAC 주소 테이블이라는 테이블로 관리한다.

하지만 L2스위치로 대체 되었다.

L2 스위치는 많은 포트를 가진 브릿지라 할 수 있다.

단말에서 받은 프레임의 MAC주소를 MAC 주소 테이블로 관리하고 전송 처리하는데, 이를 L2 스위칭이라 한다.

브릿지보다 많은 단말에 접속할 수 있어 많이 쓰인다. 집에 있는 와이파이 공유가 이에 해당한다.

## 라우터, L3 스위치(네트워크 계층/L3기기)

네트워크 계층은 IP주소를 이용하여 네트워크와 네트워크를 전송하는 계층이다.

IP 패킷의 헤더에는 IP주소가 들어있는데,

라우터는 단말로부터 받아들인 IP 패킷의 IP주소를 보고 다른 네트워크에 전달하는 역할을 담당한다. 라우터는 라우팅 테이블이라는 테이블에 기반하여 패킷을 전송할 대0상지를 관리한다.

L3 스위치는 L2 스위치에 라우팅 기능을 추가한 것이다. 스위칭 기능(같은 네트워크)에 더불어 라우팅 기능(다른 네트워크) 또한 수행할 수 있다.

## L7 스위치(애플리케이션 계층/L7기기)

부하 분산 방식이라는 방법에 근거하여 뒤쪽에 있는 여러 서버들로 나눔으로써 시스템에 처리 가능한 트래필양을 확정해준다.

## LAN과 WAN

LAN과 WAN은 네트워크의 형태를 나누는 가장 기초적인 방식이다.

### LAN

Local Area Network는 말 그대로 국소적인 네트워크를 말한다. 집에서 와이파이로 연결된 스마트폰, 랜선으로 연결된 스마트 TV, 데스크탑들이 연결된 네트워크가 그것이다.

기업의 경우는 10000대 이상의 단말이 구성 될 수도 있다.

### WAN

Wide Area Network는 거리상 멀리 떨어진 범위의 네트워크를 말한다.
전지구에 연결되어 있는 인터넷이 그 예이다. 인터넷 서비스 제공자(Internet Service Provider)가 가진 라우터에 의해 전 지구가 인터넷으로 연결되어 있다.
