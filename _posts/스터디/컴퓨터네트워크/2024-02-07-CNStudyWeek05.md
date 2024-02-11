---
title: "컴퓨터 네트워크 스터디 5주차"
excerpt: "IP address"
categories:
  - computerNetwork
---

# IP Address

**IP 주소란 네트워크 환경에서 단말들이 통신하기 위해 각 노드에 부여된 네트워크 상의 장소**이다.

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/IPv4_address_structure_and_writing_systems-en.svg/440px-IPv4_address_structure_and_writing_systems-en.svg.png)

> IP는 OSI 7 계층중 3계층인 네트워크 계층에서 사용하는 Internet Protocol의 약어이다.
>
> IP는 데이터를 패킷 단위로 나누어 전송, 받는 쪽에서 이들을 다시 조합하여 데이터를 변환한다.
>
> IP주소는 이 프로토콜에서 각 단말들을 구분하는 고유번호이다.

---

# IPv4 vs IPv6

IP는 IPv4, IPv6 두 가지 버전이 있다.

IPv4는 32비트의 IP 주소를 사용한다.

이는 2^32= (약 43억)개의 단말들을 식별할 수 있으나, 현재에는 이마저도 부족해져 더 긴 IP 주소가 필요하게 되었고 그것이 IPv6이다.

![Ipv4, ipv6 차이](https://mblogthumb-phinf.pstatic.net/MjAxODAyMTJfNTEg/MDAxNTE4NDQyNDc5MzI2.dYNUC2wJeWAB3nOv_HfCHk-Nl1jp8SVfgFo62we1YzAg.aAXtMmD1ttmdYkpjzm9caIaVs6bxha7REWbl6CxX7qQg.PNG.wnrjsxo/image.png?type=w800)

> IPv6는 IPv4와 비교하여
>
> 1. 주소 길이 증가
> 2. 헤더 길이, 필드 수 감소
>
> 라는 주요한 차이가 있다.

주소 길이 증가 : 기존 32 비트의 IP주소 -> 128 비트의 IP주소 이용

헤더 길이 감소 : 기존에 거의 사용하지 않는 옵션 필드를 '확장 헤더'라는 다른 헤더로 분리하여 헤더 길이를 고정시킴

필드 수 감소 : 구시대적, 성능 향상에 도움이 되지 않는 필드를 줄여 처리에 대한 부하 줄임

---

# SubNet, SubNet Mask

서브넷은 IP 주소에서 네트워크 영역을 나눈 부분 네트워크를 말한다.

이러한 서브넷을 만들기 위해 사용되는 것이 서브넷 마스크이다.

> 서브넷 마스크는 IP 주소에서 NetWork ID와 Host ID를 구분하는 역할을 한다.

IP주소와 서브넷 마스크를 AND 연산하여 네트워크 주소를 얻는다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fk6zPf%2FbtsqrBVptXn%2FEOXq4NTlqGSsPkEOGSwni0%2Fimg.png)

서브넷팅은 네트워크를 더 작은 단위의 네트워크로 분할하는 것이다.

또한 IP 주소 낭비를 줄이기 위해 원본 네트워크를 여러 개의 서브넷을 분리하는 과정이라 할 수 있다.

---

# Routing

라우팅은 IP 패킷을 미리 정해진 규칙에 의해 최선의 경로를 선택하는 프로세스이다.

라우터는 라우팅 테이블에 기재된 주소 정보를 기반으로 IP패킷을 알맞은 경로에 전송한다.

라우팅 테이블을 만드는 방법은 정적라우팅과 동적라우팅이 있다.

## Static Routing

수동으로 라우팅 테이블을 만드는 방법이다.

이해하기 쉽고 관리도 쉽기 때문에 소규모 네트워크 환경에 적합하나, 모든 라우팅 테이블을 설정해야 하므로 대규모 네트워크 환경에는 적합하지 않는다.

## Dynamic Routing

근접 라우터들이 서로 자신들의 경로 정보를 교환하여 자동으로 라우팅 테이블을 만드는 방법이다.

규모가 큰 환경에 적합하다. 또한 네트워크에 장애가 발생할 시 자동으로 라우팅 테이블을 업데이트 하고 변경을 알림으로써 새로운 경로를 확보할 수 있다는 장점 또한 가지고 있다.

동적 라우티에서 라우터들이 정보를 교환하기 위한 프로토콜을 **라우팅 프로토콜**이라 한다.

### Routing Protocol

라우팅 프로토콜은 제어 범위에 따라 IGP, EGP로 나뉜다.

AS 내부를 제어하는 것이 Interior Gateway Protocol이고

AS 사이를 제어하는 것이 Exterior Gateway Protocol이다.

#### IGP

> 라우팅 알고리즘
>
>  디스턴스 벡터 타입: 거리와 방향에 기반해 경로를 계산하는 라우팅 프로토콜
>
>  링크 스테이트 타입: 링크 상태에 기반해 최적 경로를 계산하는 라우팅 프로토콜
>
> 매트릭 : 네트워크 사이의 거리



#### EGP

> AS 번호 : 인터넷 상에서 유일한 AS번호
>
> 라우팅 알고리즘
>
>  경로 벡터 타입 : 경로와 방향에 기반해 경로 계산
>
> 최선 경로 선택 알고리즘

---

# Public IP vs Private IP

Public IP는 단말이 인터넷과 통신할 수 있게 하는 외부 IP주소이다.

외부에 공개되어 있기 때문에 외부로부터의 연결이 가능하며, 보안을 위해 방화벽등의 보안 프로그램을 설치하는 게 좋다.

Private IP는 로컬 네트워크의 장치를 구별하는 내부 IP 주소이다.

IPv4 주소 부족 문제를 해결하고자 하나의 PublicIP에 사설 망을 구성해 다른 주소로 할당 할 수 있게 만들어졌다.

외부에서 직접 접근할 수 없기에 보안에 용이하다는 장점이 있다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbhlfyg%2FbtrNdsojbeY%2FpFpQggkIqcL1mE4fFKXoj1%2Fimg.png)

위 그림에서 알 수 있듯이 공인 IP로 사설망을 구분하고 나면, 그 각각의 사설망에서는 private IP가 겹쳐도 상관없기에 IPv4 주소 부족 문제를 해결 할 수 있다.

---

# How IP is allocated

IP 할당 방식에는 정적 할당과 동적할당 방식이 있다.

## Static allocation

정적 할당은 단말 별로 수동으로 IP 주소를 설정하는 방법이다.

관리하기 쉬우나 수동으로 주소를 설정해주어야 하기에 소규모 환경에 적합하다.

## Dynamic allocation

자동으로 IP 주소를 할당하는 방식을 말한다.

이때 DHCP라는 프로토콜을 사용하여 단말을 DHCP 서버와 UDP로 통신하며 IP 주소를 할당받는다.

---

# NAT

프라이빗 IPv4 주소를 글로벌 IPv4 주소로 변환하는 기능을 Nerwork Address Translation이라한다.

> NAT(Network Address Translation)는 컴퓨터 네트워크에서 주로 사용되는 기술 중 하나로, 사설 네트워크(Private Network)와 공인 네트워크(Public Network) 사이에서 IP 주소를 변환하는 프로세스를 말합니다. 이는 인터넷 접속을 위해 사설 IP 주소를 공인 IP 주소로 변환하거나, 반대로 공인 IP 주소로부터 들어오는 요청을 사설 IP 주소로 변환하여 내부 네트워크에 전달하는 등의 역할을 합니다.
>
> NAT는 다음과 같은 몇 가지 주요한 유형이 있습니다:
>
> 1. **Static NAT (정적 NAT)**:
>
>    - 하나의 사설 IP 주소가 하나의 공인 IP 주소와 일대일로 매핑됩니다. 특정 사설 IP 주소가 항상 같은 공인 IP 주소와 매핑되어 있습니다.
>
> 2. **Dynamic NAT (동적 NAT)**:
>
>    - 여러 개의 사설 IP 주소가 한정된 수의 공인 IP 주소와 공유됩니다. 사설 IP 주소가 사용될 때마다 동적으로 공인 IP 주소와 매핑됩니다.
>
> 3. **NAT Overload (NAT 포트 포워딩 또는 PAT, Port Address Translation)**:
>    - 여러 개의 사설 IP 주소가 하나의 공인 IP 주소에 매핑되며, 추가로 포트 번호가 사용되어 구별됩니다. 이를 통해 하나의 공인 IP 주소로 여러 개의 사설 IP 주소와 통신할 수 있습니다.
>
> NAT의 주요 장점은 다음과 같습니다:
>
> - **IP 주소 절약**: 사설 IP 주소를 사용하여 내부 네트워크의 호스트들을 식별할 수 있으므로, 공인 IP 주소를 더 효율적으로 사용할 수 있습니다.
> - **보안 향상**: 내부 네트워크의 호스트들이 직접 인터넷에 노출되지 않고 NAT 장치를 통해 통신하기 때문에 보안을 향상시킬 수 있습니다.
> - **IPv4 주소 고갈 대응**: IPv4 주소의 한정된 보유량을 극복하기 위한 임시적인 해결책으로 사용됩니다.
>
> NAT는 네트워크에서 중요한 역할을 하며, 인터넷 연결 및 네트워크 보안에 필수적인 기술 중 하나입니다.

---

# ICMP

> ICMP(Internet Control Message Protocol)는 TCP/IP 네트워크에서 사용되는 프로토콜 중 하나로, 주로 네트워크 상태 및 통신 문제를 감지하고 진단하는 데 사용됩니다. ICMP 메시지는 IP 패킷의 일부로 전송되며, 네트워크 장치 간의 통신 오류를 보고하거나 제어 메시지를 전달하는 데 사용됩니다.
>
> ICMP의 주요 기능은 다음과 같습니다:
>
> 1. **에러 보고**: ICMP는 네트워크에서 발생하는 다양한 에러를 보고합니다. 예를 들어, 목적지 호스트 또는 네트워크가 접속 불가능한 경우 호스트 또는 라우터에서 ICMP 메시지가 생성되어 송신자에게 이를 알려줍니다.
>
> 2. **Echo 요청 및 응답 (Ping)**: ICMP Echo 요청 및 응답 메시지를 사용하여 호스트 또는 네트워크 장치의 동작 상태를 확인할 수 있습니다. 주로 "Ping" 명령어로 알려진 이 동작은 특정 호스트에 Echo 요청을 보내고 그에 대한 응답을 받아 확인합니다.
>
> 3. **경로 발견 및 MTU(Path MTU Discovery)**: ICMP 메시지는 패킷이 최종 목적지까지 도달할 때까지 이동하는 동안 발생하는 중간 라우터의 MTU(Maximum Transmission Unit)를 탐지하는 데 사용됩니다. 이를 통해 최적의 전송 경로를 결정하고, 큰 데이터 패킷이 분할되지 않고 전송될 수 있습니다.
>
> 4. **라우터 간 통신**: ICMP 메시지는 라우터 간 통신을 위한 제어 메시지를 전달하는 데 사용됩니다. 라우터 간의 연결 상태를 확인하고, 라우팅 테이블을 업데이트하고, 네트워크 상태를 관리하는 데 필요한 정보를 전달합니다.
>
> 5. **MTU 바로가기 (Fragmentation Needed)**: 호스트가 보내는 패킷이 네트워크를 통과할 수 없는 경우, ICMP 메시지는 MTU 재조정이 필요하다는 신호를 보냅니다. 이를 통해 패킷의 크기를 조절하여 효율적인 통신을 유지할 수 있습니다.
>
> ICMP는 네트워크에서 중요한 역할을 하며, 네트워크 관리자 및 운영자가 네트워크의 상태를 모니터링하고 문제를 진단하는 데 필수적인 도구로 사용됩니다.

---
